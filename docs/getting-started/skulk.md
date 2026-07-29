---
title: Skulk Quick Start
description: Ingest and query time-series data with Alopex Skulk in a few minutes
---

# Skulk Quick Start

Get a durable time-series store running inside your process. No server, no
daemon, no sidecar — Skulk is a library you link in.

## Install

```bash
cargo add alopex-skulk
```

Rust 1.82 or later. Production dependencies are pure Rust — there is no `cc`
step and no `*-sys` crate, so a plain `cargo build` is all you need on any
target you can already build for.

## Write Your First Points

Open a data root, hand it a batch, and flush. That is the whole write path.

```rust
use alopex_skulk::ingest::line_protocol::LineProtocolDecoder;
use alopex_skulk::ingest::{IngestLimits, Ingestor};
use alopex_skulk::store::recovery::{RecoveryConfig, RecoveryStore};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let limits = IngestLimits::default();
    let store = RecoveryStore::open("./skulk-data", RecoveryConfig::default())?;
    let mut ingestor = Ingestor::new(store, limits);

    // now: the timestamp applied to points that don't carry one
    let now = 1_609_459_200_000_000_000;

    let batch = LineProtocolDecoder::new(limits).decode(
        b"weather,host=edge temperature=21.5,status=\"ready\" 1609459200000000000",
        now,
    )?;

    let outcome = ingestor.ingest(batch, now)?;
    println!("accepted {}", outcome.accepted_count());

    // Points are durable at ingest (WAL). flush_all() publishes Parquet files.
    ingestor.sink_mut().flush_all()?;
    Ok(())
}
```

Note the shape of that line: one measurement, one tag set, and **two fields of
different types** — a float and a string. That is the wide row model. Adding a
third field later does not create a new series.

## Read It Back

```rust
let store = RecoveryStore::open("./skulk-data", RecoveryConfig::default())?;
let rows = store.read_measurement("weather")?;

for row in &rows {
    println!(
        "{} temperature={:?} host={:?}",
        row.row().timestamp(),
        row.row().field("temperature"),
        row.row().series().tags().get("host"),
    );
}
```

!!! note "v0.3 read scope"

    `read_measurement` returns every row for a measurement. Predicate pushdown,
    column projection, and a query language arrive in
    [v0.4](../roadmap.md#skulk) — the v0.3 reader exists to verify writes, not
    to serve queries.

## Ingest From Existing Tooling

Skulk decodes three wire formats, so you can point existing agents at it
without changing what they emit.

=== "Line Protocol"

    ```rust
    use alopex_skulk::ingest::line_protocol::LineProtocolDecoder;

    let batch = LineProtocolDecoder::new(limits)
        .decode(b"cpu,host=edge usage=23.5 1609459200000000000", now)?;
    ```

    Telegraf and anything else speaking InfluxDB Line Protocol works as-is.

=== "Prometheus Remote Write"

    ```rust
    use alopex_skulk::ingest::remote_write::RemoteWriteDecoder;

    let batch = RemoteWriteDecoder::new(limits)
        .decode("application/x-protobuf", "snappy", &body)?;
    ```

    Accepts v1 float samples. v2, metadata, exemplars, and native histograms
    are rejected explicitly rather than silently dropped.

=== "JSON"

    ```rust
    use alopex_skulk::ingest::json::JsonIngestDecoder;

    let batch = JsonIngestDecoder::new(limits).decode(
        br#"{"metrics":[{
            "name":"events",
            "tags":{"host":"edge"},
            "fields":{"count":3,"healthy":true},
            "timestamp":1609459200000000000
        }]}"#,
        now,
    )?;
    ```

    Also accepts a single-point `{"metric":...}` form.

All three produce the same batch type, so the validation, limits, and
durability behaviour below apply identically no matter which one you use.

## Partial Success

A malformed row does not fail the batch. Good rows are accepted; bad rows come
back with their position so you can log or retry exactly what failed.

```rust
let outcome = ingestor.ingest(batch, now)?;

println!("accepted {}", outcome.accepted_count());
for rejection in outcome.rejections() {
    // source() tells you which line or item was bad; reason() tells you why
    eprintln!("rejected at {:?}: {}", rejection.source(), rejection.reason());
}
```

## Retention

Set a TTL per measurement. It persists across restarts.

```rust
use alopex_skulk::store::retention::{LateWritePolicy, RetentionPolicy, HOUR_NANOS};

let policy = RetentionPolicy::new(24 * HOUR_NANOS as u64, LateWritePolicy::Reject)?;
store.set_retention_policy("cpu", policy)?;
```

`LateWritePolicy::Reject` refuses writes older than the retention window;
`Accept` takes them. Expiry itself is idempotent — running it twice is safe.

## What You Get for Durability

Skulk acknowledges a write only after it is in the WAL. If the process dies
between the acknowledgement and the next Parquet flush, recovery replays from
the WAL up to the manifest fence.

- A torn WAL tail is truncated, not misread
- Parquet files become visible atomically — a crash mid-write leaves no
  half-published file
- Orphaned temporary files are cleaned on the next open
- One writer per data root, enforced by an OS lock

You do not have to configure any of this.

## Where to Go Next

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **[How Skulk Works](../concepts/skulk.md)**

    ---

    The wide row model, the Arrow/Parquet storage design, and why DataFusion
    was not adopted.

-   :material-map-marker-path:{ .lg .middle } **[Roadmap](../roadmap.md#skulk)**

    ---

    Query engine at v0.4, downsampling at v0.5, HTTP serving at v0.6,
    distribution on Chirps at v0.8.

-   :material-console:{ .lg .middle } **[Trail](../concepts/trail.md)**

    ---

    Same storage machinery, different data shape — logs and events with a
    schema you don't declare up front.

</div>

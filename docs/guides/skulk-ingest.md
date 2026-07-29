---
title: Skulk Ingest Guide
description: Practical patterns for running Skulk ingestion — backpressure, flushing, retention, and compaction
---

# Skulk Ingest Guide

Practical patterns for running Skulk in a real ingest path. This guide assumes
you have been through the [Quick Start](../getting-started/skulk.md).

## Choosing When to Flush

Writes are durable as soon as `ingest()` returns — that is the WAL boundary.
`flush_all()` is a separate decision: it converts buffered rows into Parquet
files and lets the WAL be checkpointed.

```rust
let outcome = ingestor.ingest(batch, now)?;
// Durable here. A crash now replays from the WAL.

ingestor.sink_mut().flush_all()?;
// Parquet published, WAL checkpointed.
```

Flushing on every batch produces many small Parquet files and wastes
compression. Never flushing lets the WAL grow without bound. Drive it from the
buffer instead:

```rust
const FLUSH_ROWS: usize = 50_000;

ingestor.ingest(batch, now)?;

if ingestor.sink().pending_row_count() >= FLUSH_ROWS {
    ingestor.sink_mut().flush_all()?;
}
```

A time-based flush alongside the row threshold keeps a low-traffic stream from
sitting in the buffer indefinitely. Skulk does not run a background timer for
you — flushing is always your call, which means it never happens at a moment
you didn't choose.

## Reacting to Backpressure

Skulk bounds itself. When buffered rows, buffer bytes, or WAL bytes exceed the
admission limits, `ingest()` returns a resource-limit error instead of growing
without bound.

Read the pressure before you get there. `pressure()` comes from the
`IngestSink` trait, so bring it into scope:

```rust
use alopex_skulk::ingest::IngestSink;

let pressure = ingestor.sink().pressure()?;

println!(
    "rows={} bytes={} wal={}",
    pressure.buffered_rows(),
    pressure.buffered_bytes(),
    pressure.wal_bytes(),
);
```

The usual response to rising pressure is to flush, not to widen the limits:

```rust
let pressure = ingestor.sink().pressure()?;
if pressure.buffered_bytes() > SOFT_LIMIT {
    ingestor.sink_mut().flush_all()?;
}
```

If you are consistently hitting the ceiling with flushing in place, the
producer is faster than the storage path, and the fix belongs upstream —
batching, sampling, or shedding — rather than in a larger buffer.

### Tuning the limits

```rust
use alopex_skulk::ingest::{AdmissionLimits, IngestLimits, RequestLimits, RowLimits};

let limits = IngestLimits::new(
    RequestLimits::default(),
    RowLimits::default(),
    AdmissionLimits::new(
        250_000,            // buffered rows
        256 * 1024 * 1024,  // buffer bytes
        1024 * 1024 * 1024, // WAL bytes
    )?,
);
```

Raise these when you have memory to spare and want fewer, larger Parquet files.
Lower them on constrained devices where a bounded footprint matters more than
throughput.

## Handling Partial Failures

A bad row never fails a good batch. Treat rejections as data, not as an
exception path:

```rust
let outcome = ingestor.ingest(batch, now)?;

metrics.accepted.increment(outcome.accepted_count() as u64);
metrics.rejected.increment(outcome.rejected_count() as u64);

for rejection in outcome.rejections() {
    tracing::warn!(
        source = ?rejection.source(),
        reason = rejection.reason(),
        "row rejected"
    );
}
```

`source()` identifies the position — which line of a Line Protocol payload, or
which item of a JSON batch — and `reason()` says what was wrong, so a rejection
is actionable without re-parsing the request.

!!! warning "Silent loss is the failure mode to avoid"

    Ignoring `rejections()` means dropping data with no signal. Log it or count
    it; do not discard it.

## Retention

Retention is per measurement and survives restarts.

```rust
use alopex_skulk::store::retention::{LateWritePolicy, RetentionPolicy, HOUR_NANOS};

let policy = RetentionPolicy::new(7 * 24 * HOUR_NANOS as u64, LateWritePolicy::Accept)?;
store.set_retention_policy("cpu", policy)?;
```

### Choosing a late-write policy

| Policy | Behaviour | Use when |
|:-------|:----------|:---------|
| `Reject` | Writes older than the window are refused | Late data is a bug you want surfaced |
| `Accept` | Old writes land, then expire on the normal schedule | Agents buffer during outages and replay |

`Reject` gives you a loud signal at the cost of losing genuinely delayed data.
`Accept` is the safer default for anything with an at-least-once agent in front
of it.

### Running expiry

Expiry is explicit and idempotent — running it twice does nothing extra.

```rust
let result = store.expire_retention("cpu", now)?;
```

Call it on a schedule that matches your partition granularity. Skulk partitions
hourly, so hourly or daily expiry is typical; running it every minute mostly
does no work.

## Compaction

Flushing frequently produces many small files. Compaction merges them within a
partition and resolves duplicates with last-ingest-wins.

```rust
if let Some(result) = store.compact_measurement("cpu")? {
    tracing::info!(
        inputs = result.input_file_count(),
        rows = result.output_row_count(),
        "compacted"
    );
}
```

It returns `None` when there is nothing to merge, and handles one partition per
call — so a loop drives it to completion:

```rust
while store.compact_measurement("cpu")?.is_some() {}
```

Schedule this off the write path. It reads and rewrites files, so running it
during a traffic spike competes with ingestion for exactly the resources you
need.

## Inspecting What's on Disk

```rust
let state = store.manifest_state()?;
let partitions = store.list_partitions("cpu")?;
```

The manifest is the authority on which files are live. Anything in the data
root that the manifest does not list is an orphan, and Skulk removes those on
the next open — so do not place your own files inside the data root.

## Running Multiple Measurements

One store handles many measurements. Buffers, retention policies, and
compaction are all per measurement:

```rust
for measurement in ["cpu", "memory", "disk"] {
    store.set_retention_policy(measurement, policy)?;
}
```

`flush_all()` publishes every measurement's buffer at once, each into its own
Parquet file per time partition. There is no need to flush them individually.

## Moving an Existing v0.2 Data Root

Skulk v0.3 does not read v0.2 TSM or WAL files. Legacy magic is rejected before
the source is modified, so pointing v0.3 at a v0.2 data root fails cleanly
rather than corrupting it — but it does mean the data does not come across on
its own, and there is no migration tool.

Export with v0.2 and re-ingest into a **new** data root:

1. Stop the v0.2 writer.
2. Read the series out with the v0.2 reader and emit Line Protocol or JSON.
3. Ingest that into a v0.3 store rooted at a different path.
4. Set retention policies on the new root before backfilling — with
   `LateWritePolicy::Accept`, or historical points are refused on arrival.

```rust
use alopex_skulk::store::retention::{LateWritePolicy, RetentionPolicy, HOUR_NANOS};

let policy = RetentionPolicy::new(90 * 24 * HOUR_NANOS as u64, LateWritePolicy::Accept)?;
store.set_retention_policy("cpu", policy)?;
// Backfill now; points older than the window would be rejected under `Reject`.
```

Keep the v0.2 root read-only until you have verified row counts on the new one.
Backfilled data lands in the same hourly partitions as live writes, so flush and
compact as usual once the load finishes.

## Operational Checklist

- [ ] Flush is driven by a row or byte threshold, not per batch
- [ ] Backpressure errors are handled by flushing or shedding, not by raising limits blindly
- [ ] `rejections()` is logged or counted — never silently dropped
- [ ] Retention policy set per measurement, with a deliberate late-write choice
- [ ] Expiry and compaction run on a schedule, off the write path
- [ ] Nothing else writes into the data root
- [ ] Only one process opens a given data root — Skulk enforces this with an OS lock, and the second opener fails

## Related

- [Skulk Quick Start](../getting-started/skulk.md)
- [How Skulk Works](../concepts/skulk.md)
- [Roadmap](../roadmap.md#skulk) — query engine at v0.4, HTTP serving at v0.6

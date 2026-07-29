---
title: Trail Preview
description: What using Alopex Trail is designed to feel like — and how to shape it
---

# Trail: What It Will Feel Like

Trail is being designed in the open. This page shows the intended developer
experience **before** the API is frozen, so it can still change based on what
you tell us.

!!! tip "This is the moment to push back"

    Everything below is a proposal. If a name reads wrong, if a default would
    bite you, if the shape doesn't fit how you actually ship logs — say so now.
    After v0.1 ships, these choices are much harder to undo.

    [Open a discussion :fontawesome-brands-github:](https://github.com/alopex-db/alopex-skulk/discussions){ .md-button .md-button--primary }
    [Read the full design](https://github.com/alopex-db/docs/blob/main/design/alopex-trail-proposal.md){ .md-button }

---

## The Experience We're Aiming For

### Write an event. Any event.

No table to create. No schema to declare. No migration when the shape changes.

```rust
let store = TrailStore::open("./trail-data", TrailConfig::default())?;
let mut ingestor = Ingestor::new(store, IngestLimits::default());

let batch = JsonLinesDecoder::new(limits).decode(br#"
{"stream":"api","level":"info","route":"/users","status":200,"ms":12}
{"stream":"api","level":"error","route":"/orders","status":500,"ms":840,"trace":"abc123"}
"#, now)?;

ingestor.ingest(batch, now)?;
```

The second event carries a `trace` field the first one didn't. That is not an
error and not a migration — the column appears, and earlier rows read back as
null for it.

### The day a field changes type

This is the moment most log pipelines break. In Trail it is a non-event.

```jsonl
{"stream":"api","status":200}
{"stream":"api","status":"upstream_timeout"}
```

Both are accepted. Internally they become `status@i64` and `status@str`;
reading `status` coalesces them. Your ingestion does not stop at 3am because a
service started emitting strings where it used to emit integers.

```rust
for event in store.read_stream("api")? {
    // Returns Int(200) for one row, Str("upstream_timeout") for the other
    println!("{:?}", event.attr("status"));
}
```

If you need the split explicitly, ask for it: `event.attr("status@str")`.

### Ask what's in there

Because every file records its own column set, the catalog answers without
touching Parquet data.

```rust
let columns = store.columns("api")?;
// ["level", "route", "status@i64", "status@str", "ms", "trace"]
```

That same information is what lets a query skip files that cannot contain the
column you filtered on.

### Events without a usable timestamp

Accepted and stamped on arrival, rather than rejected at the door.

```jsonl
{"stream":"audit","actor":"deploy-bot","action":"rollout"}
```

### From Python

Log analysis usually happens in Python, so a binding is planned for v0.4.
Results cross into pandas or Polars over Arrow — Trail already holds data in
Arrow internally, so nothing is converted on the way out.

```python
import alopex_trail as trail

store = trail.open("./trail-data")

store.write("api", {"level": "error", "route": "/orders", "status": 500})
store.write("api", {"level": "info", "route": "/users", "status": "cached"})

# Columns are discovered, not declared
store.columns("api")
# ['level', 'route', 'status@i64', 'status@str']

df = store.query("api").since("1h").to_polars()
```

A late-bound schema fits the DataFrame model closely: you do not declare
columns before reading them, and the shadowed type variants collapse into one
logical column unless you ask for a specific one.

---

## Design Questions We Want Answered

These are genuinely undecided. Your input changes the outcome.

<div class="grid cards" markdown>

-   :material-help-circle:{ .lg .middle } **How should the query syntax read?**

    ---

    The shape is settled — an aggregation DSL with cross-signal joins, plus
    TraceQL/LogQL for Grafana. What isn't settled is the spelling: operators,
    how you write a type binding, join notation.

-   :material-help-circle:{ .lg .middle } **Do you need full-text search?**

    ---

    If yes, an inverted index has to be in the foundation, not bolted on at
    v0.4. That is a much bigger commitment — worth making only if it is
    genuinely needed.

-   :material-help-circle:{ .lg .middle } **Is `status@str` the right spelling?**

    ---

    The shadow-column syntax is visible to you whenever you disambiguate a
    type. Does it read clearly? Would you rather it were hidden entirely?

-   :material-help-circle:{ .lg .middle } **What throughput do you actually need?**

    ---

    This decides whether rows borrow from the input buffer or own their data —
    a decision that is hard to reverse once the row model is fixed.

-   :material-help-circle:{ .lg .middle } **Is Python where you'd reach for this?**

    ---

    Bindings are planned for v0.4. If Python is your entry point rather than
    Rust, that changes what gets built first — and whether the ingest side
    needs to be as ergonomic as the query side.

</div>

---

## What Already Exists

Trail is not starting from zero. The parts that are hardest to get right are
already running in [Skulk](../concepts/skulk.md) and carry over directly:

| Piece | Status |
|:------|:-------|
| Dynamic column union with null back-fill | Running in Skulk today |
| WAL framing, torn-tail truncation, crash recovery | Running in Skulk today |
| Atomic Parquet publication | Running in Skulk today |
| Two-generation manifest with checksum fallback | Running in Skulk today |
| Single-writer locking | Running in Skulk today |
| Type shadowing | New in Trail |
| Time-optional events | New in Trail |
| Manifest column summaries | Extends Skulk's manifest |

That is why this is a design worth commenting on rather than speculation — the
storage foundation is proven, and what is being designed is the model above it.

---

## Timeline

Trail's WAL and ingest layers reuse code that Skulk v0.3.1 is currently
changing, so that portion follows v0.3.1. The storage, manifest, and locking
pieces are independent and can start earlier.

See the [Trail roadmap](../roadmap.md#trail) for the version breakdown.

---

## Follow Along

- [Concept page](../concepts/trail.md) — the problem, the approach, the open decisions
- [Full design document](https://github.com/alopex-db/docs/blob/main/design/alopex-trail-proposal.md) — the reasoning in full, including what was rejected
- [Skulk](../concepts/skulk.md) — the storage core Trail builds on, available today

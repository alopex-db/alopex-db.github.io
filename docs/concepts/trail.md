---
title: Trail
description: Proposed log and event store with late-bound schema
---

# Trail - Late-Bound Schema Log Store

!!! warning "Proposal — not an implemented product"

    Trail is a **design proposal at the concept stage**. There is no code, no
    crate, and no repository. Nothing on this page is available to install or
    use, and the design may change or be dropped entirely.

    This page exists because Alopex publishes its design reasoning before
    implementation, not after. Treat every statement here as an intention,
    not a specification.

Trail is a proposed append-only store for logs and events whose **schema is not
known in advance**. Columns are built from the attributes that actually arrive,
and persisted columnar in Parquet.

## The Problem

[Skulk](skulk.md) handles time-series where the shape is known up front: a
metric, its tags, and its fields. That strictness is correct for a TSDB and
wrong for logs.

Skulk enforces the following at the type level:

| Constraint | Why it blocks log ingestion |
| --- | --- |
| Timestamp is mandatory | Logs routinely arrive with missing or malformed time |
| Tags and fields are separate types | Logs have no such distinction |
| Exactly five value types | Cannot represent nested JSON or binary payloads |
| Type conflicts are rejected | A field that is `200` one day and `"timeout"` the next **stops ingestion** |
| At least one field required | Cannot represent an event with an empty payload |

The fourth row is the decisive one. In a metrics system, rejecting a type change
is a correctness guarantee. In a log system, it is an outage.

## The Approach

Trail keeps the same storage foundation as Skulk — append-only, columnar,
Parquet — and changes only the data model above it.

<div class="grid cards" markdown>

-   :material-shape-plus:{ .lg .middle } **Columns Appear On Arrival**

    ---

    An unknown attribute creates a new column, and every prior row in the
    buffer is back-filled with null. Rows missing a column get null.

    No declaration, no migration, no `ALTER TABLE`.

-   :material-call-split:{ .lg .middle } **Type Conflicts Shadow, Never Reject**

    ---

    When `status` arrives as an integer and later as a string, Trail creates
    a second physical column rather than failing.

    Reads coalesce the shadows back into one logical column.
    **Ingestion never stops.**

-   :material-file-tree:{ .lg .middle } **Schema Lives in the Manifest**

    ---

    Each file records its column set and a schema fingerprint, so a catalog
    query is answered without opening any Parquet footer — and files lacking
    a queried column are skipped entirely.

-   :material-timer-outline:{ .lg .middle } **Time Is Optional**

    ---

    Events without a usable timestamp are accepted and stamped at ingestion,
    rather than rejected at the door.

</div>

### Type shadowing

```
attrs: { status: 200 }         →  physical column  status@i64
attrs: { status: "timeout" }   →  physical column  status@str   (new)
```

Reading the logical column `status` coalesces both. Reading `status@str`
addresses one directly. The Parquet physical schema never conflicts, because
the conflict is resolved at read time instead of write time.

This is what "late-bound schema" means in practice: **type mismatch is a read
concern, not an ingestion error.**

## Relationship to Skulk

Trail is not a fork of Skulk's purpose — it is a reuse of Skulk's machinery.

The durability layer Skulk already proves in production is directly applicable:
single-writer locking, atomic Parquet publication, two-generation manifest
rotation with checksum fallback, WAL framing with torn-tail truncation, and
staged crash-recovery boundaries.

What changes is the row model, the sort order (time-first rather than tag-first),
and the treatment of type conflicts.

!!! note "Why this is feasible"

    Skulk already builds its Arrow schema dynamically from arriving rows and
    back-fills nulls for columns that appear late. That mechanism is more
    general than a TSDB needs — and it is exactly what a late-bound schema
    store requires. Trail promotes it from an implementation detail to the
    central feature.

## Proposed Milestones

Version numbers below are **proposed**, not scheduled. No delivery date exists.

| Version | Scope |
| --- | --- |
| v0.1 | Event model, WAL, dynamic column union, Parquet publication, manifest with column summaries, crash recovery |
| v0.2 | Type shadowing with read-time coalesce, JSON Lines and OTLP log decoders, retention |
| v0.3 | Predicate pushdown, column projection, manifest-driven file pruning |
| v0.4 | Compaction with sidecar indexes; full-text search evaluated |

## Open Questions

These are unresolved and are the reason Trail remains a proposal.

- **Code sharing with Skulk** — a shared crate propagates improvements
  automatically but risks distorting Skulk's interfaces with immature
  requirements. The current recommendation is to fork first and re-evaluate later.
- **Throughput target** — undecided, and it determines whether the row
  representation borrows from the input buffer or owns its data.
- **Query interface** — SQL or a search-oriented DSL.
- **Full-text search** — if required, an inverted index becomes a design
  premise rather than a later addition.

## Learn More

- [Full proposal document](https://github.com/alopex-db/docs/blob/main/design/alopex-trail-proposal.md)
- [Skulk](skulk.md) — the time-series product whose machinery Trail reuses

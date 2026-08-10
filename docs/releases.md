---
title: Release History
description: Recent releases across Alopex DB, Skulk, and Chirps
---

# Release History

The Alopex family uses independent version series. This page records the latest
published releases as verified from each repository on **August 10, 2026**.
Follow the linked release and changelog for the complete compatibility notes.

## Current Releases

| Project | Latest | Published | Highlights |
|:--------|:-------|:----------|:-----------|
| Alopex DB | [v0.8.3](https://github.com/alopex-db/alopex/releases/tag/v0.8.3) | Aug 3, 2026 | SQL name-resolution and JOIN correctness fixes; faster wide-schema and nested-scope resolution |
| Skulk | [v0.4.0](https://github.com/alopex-db/alopex-skulk/releases/tag/alopex-skulk-v0.4.0) | Jul 31, 2026 | Embedded PromQL and SQL-TS query engine, Arrow result streams, pruning, and out-of-order policy |
| Chirps | [v0.6.1](https://github.com/alopex-db/alopex-chirps/releases/tag/chirps-v0.6.1) | Aug 9, 2026 | Raft storage/node APIs plus hardened QUIC, SWIM, and resumable file transfer |

## Alopex DB v0.8 Series

### v0.8.3 — SQL correctness and name resolution

- Numeric JOIN keys now match by value across integer and floating-point types.
- `USING` and `NATURAL JOIN` keys remain correctly merged across chained joins.
- Duplicate aliases, quoted/unquoted identifier rules, derived-table scope, and
  parser diagnostic spans are handled consistently.
- Wide-schema and deeply nested name resolution were optimized.

### v0.8.2 — SQL correctness

- Fixed `TIMESTAMP` input, numeric promotion, integer `SUM`, `CAST`, `IN`,
  `BETWEEN`, subquery scope, and `RIGHT`/`FULL` JOIN merged keys.
- Added `INSERT ... SELECT`, qualified wildcards, and statement-stable `NOW()`.
- `SUM(INTEGER)` now returns `BIGINT`; this is a documented result-type change.

### v0.8.1 — Parser contracts

- Added PromQL and SQL-TS contracts to Nim parser ABI 0.2.0.
- Hardened Windows release coverage for Python, streaming, and server surfaces.

### v0.8.0 — Cluster-aware streaming

- Added cluster metadata, lifecycle, routing diagnostics, and authenticated
  distributed-read contracts.
- Added multi-statement and streaming SQL over HTTP, gRPC, and CLI.
- Added bounded CSV/Parquet DataFrame streaming and sync/async Python APIs.
- Single-node remains the default; remote execution and distributed
  transactions are not part of the v0.8 supported scope.

[Full Alopex DB changelog](https://github.com/alopex-db/alopex/blob/main/CHANGELOG.md)

## Skulk v0.4.0

- `QueryEngine` executes PromQL instant/range queries, SQL-TS, and pre-built
  logical plans without requiring an HTTP server; results stream as Arrow
  `RecordBatch` values.
- PromQL covers selectors, ranges, offsets, arithmetic, core range functions,
  classic histogram quantiles, and grouped aggregates. SQL-TS covers
  projection, filtering, ordering, aggregates, `TIME_BUCKET`, `RATE`, `DELTA`,
  `DERIVATIVE`, `FIRST`, and `LAST`.
- `StorageReader` combines pending and durable latest-write-wins data with time,
  tag, and field pruning. v0.3 WAL, manifest, and Parquet data remains readable.
- The default build enables PromQL and SQL-TS through the Nim parser. A
  `--no-default-features` pure-Rust embedded profile remains available.
- HTTP query endpoints are still planned for v0.6; the text frontends implement
  documented subsets and reject unsupported semantics explicitly.

[Full Skulk changelog](https://github.com/alopex-db/alopex-skulk/blob/main/CHANGELOG.md)

## Chirps v0.6.1

- Ships OpenRaft-compatible WAL-backed Raft storage, state-machine and snapshot
  helpers, a `RaftNode` wrapper, Chirps transport, membership changes, and
  proposal/query APIs.
- Hardens real QUIC transport with ALPN and trust anchors, queue limits,
  priority scheduling, reconnection coverage, and SWIM liveness fixes.
- File transfer verifies hashes before completion, supports resumable transfers,
  compression, retransmission, atomic placement, metadata preservation, and
  bounded concurrency.
- `MessageProfile::Durable` still awaits the planned Iggy backend.

[Full Chirps changelog](https://github.com/alopex-db/alopex-chirps/blob/main/CHANGELOG.md)

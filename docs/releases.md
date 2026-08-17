---
title: Release History
description: Recent releases across Alopex DB, Skulk, and Chirps
---

# Release History

The top-level Alopex DB, Skulk, and Chirps repositories use independent version
series. Within Alopex DB, all public Rust crates and the Python package use one
aligned version. This page records the latest published releases as verified
from each repository on **August 18, 2026**.
Follow the linked release and changelog for the complete compatibility notes.

## Current Releases

| Project | Latest | Published | Highlights |
|:--------|:-------|:----------|:-----------|
| Alopex DB | [v0.8.6](https://github.com/alopex-db/alopex/releases/tag/v0.8.6) | Aug 17, 2026 | Alias resolution, `REAL`, `CASE`, set operations, CTEs, and basic window functions |
| Skulk | [v0.4.0](https://github.com/alopex-db/alopex-skulk/releases/tag/alopex-skulk-v0.4.0) | Jul 31, 2026 | Embedded PromQL and SQL-TS query engine, Arrow result streams, pruning, and out-of-order policy |
| Chirps | [v0.6.3](https://github.com/alopex-db/alopex-chirps/releases/tag/chirps-v0.6.3) | Aug 11, 2026 | Memory-contract and mTLS conformance on the bounded QUIC transport |

## Alopex DB v0.8 Series

!!! warning "v0.9 is frozen"

    The active publication order is v0.8.7 through v0.8.11. v0.9 development
    and release operations resume only after that entire train is published
    and post-publication verification succeeds.

### v0.8.6 — Single-node SQL correctness

- Added projection-alias resolution in `ORDER BY` and `HAVING`, with explicit
  scope errors where aliases are not visible.
- Added `REAL`, searched/simple `CASE`, and `UNION`/`INTERSECT`/`EXCEPT`.
- Added non-recursive CTEs and basic aggregate/ranking window functions.
- Rebuilt every native Nim parser asset from the v0.8.6 tag while retaining
  parser contract `0.4.0`.

### v0.8.5 — Public surface and release hardening

- Restored release parity for Python vector, HNSW, SQL-stream, and scan APIs.
- Hardened parser asset assembly, wheel linkage, security gates, and
  post-publication verification.

### v0.8.4 — Parser contract 0.4.0

- Added `CREATE CONTINUOUS AGGREGATE` to the parser contract.
- Shipped target-qualified parser assets and checksum manifests for supported
  Linux, macOS, and Windows targets.

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

## Chirps v0.6.3

- Restores conformance with the memory and mTLS specifications.
- Builds on v0.6.2's per-connection memory bounds in the production QUIC path.
- Retains the v0.6.1 OpenRaft-compatible storage/node APIs, hardened SWIM,
  resumable file transfer, and observability surface.

- `MessageProfile::Durable` still awaits the planned Iggy backend.

[Full Chirps changelog](https://github.com/alopex-db/alopex-chirps/blob/main/CHANGELOG.md)

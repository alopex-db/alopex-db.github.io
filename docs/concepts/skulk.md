---
title: Skulk (Time-Series)
description: Alopex Skulk - the time-series database of the Alopex family, built on Alopex Core
---

# Alopex Skulk — Time-Series Database

[![crates.io](https://img.shields.io/crates/v/alopex-skulk.svg)](https://crates.io/crates/alopex-skulk)

> Time-series database built on Alopex Core. Gorilla compression, automatic TTL/downsampling, PromQL & SQL-TS queries. Scales from embedded to distributed.

**Skulk** (noun): a group of foxes. Like a skulk silently tracking prey, Alopex Skulk quietly collects and manages your time-series data in the background.

[View on GitHub :fontawesome-brands-github:](https://github.com/alopex-db/alopex-skulk){ .md-button .md-button--primary }

## Core Values

- **Ephemeral** — data is consumable: automatic TTL and downsampling for freshness management
- **Streaming** — high-speed ingestion, continuous queries, real-time alerts
- **Observable** — unified foundation for metrics, logs, and traces

## Features

| Feature | Description |
|:--------|:------------|
| **Gorilla Compression** | 10:1+ compression ratio with Delta-of-Delta timestamps and XOR-encoded values |
| **Automatic Lifecycle** | Time-based TTL, cascading downsampling (1s → 1h → 1d) |
| **PromQL Compatible** | Query with familiar Prometheus syntax |
| **SQL-TS Extension** | `TIME_BUCKET`, `RATE`, `DELTA`, `FIRST`, `LAST` functions |
| **Multi-Mode Deployment** | Embedded → Single-Node → Distributed cluster |
| **Alopex Core Foundation** | Built on battle-tested WAL, MemTable, and Compaction |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Layer                           │
│  (Prometheus, Telegraf, Grafana, Custom Apps)               │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                   Ingest Gateway                            │
│  Line Protocol │ Prometheus Remote Write │ JSON API         │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                   Query Engine                              │
│  PromQL Parser │ SQL-TS Parser │ Planner │ Executor         │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                  Lifecycle Manager                          │
│  TTL Manager │ Downsampler │ Retention Policy               │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                   Storage Layer                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ TSM Engine (Time-Structured Merge)                  │   │
│  │  MemTable → Immutable → TSM Files (.skulk)          │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Alopex Core (WAL, Compaction)                       │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## When to Use Skulk vs. Alopex DB

| Aspect | Alopex DB | Alopex Skulk |
|:-------|:----------|:-------------|
| **Use Case** | RAG/AI, Knowledge Base, OLTP | Monitoring, IoT, Log Analysis |
| **Data Lifespan** | Long-term (asset) | Short-term rotation (consumable) |
| **Primary Ops** | CRUD + Vector Search | Append + Aggregate + TTL Delete |
| **Query Pattern** | Point lookup, JOIN, Vector | Range aggregation, Downsampling |
| **Delete Pattern** | Explicit DELETE | Automatic TTL expiry |

Both share the same foundation: Alopex Core's WAL, MemTable, and compaction machinery. Choose Alopex DB when your data is a long-lived asset, and Skulk when your data is a continuously flowing stream with a natural expiry.

## Installation

```bash
cargo add alopex-skulk
```

## See Also

- [:octicons-arrow-right-24: GitHub repository](https://github.com/alopex-db/alopex-skulk)
- [:octicons-arrow-right-24: Skulk roadmap](../roadmap.md#skulk)
- [:octicons-arrow-right-24: Chirps (cluster messaging)](chirps.md)
- [:octicons-arrow-right-24: Alopex DB architecture](architecture.md)

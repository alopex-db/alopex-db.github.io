---
title: Architecture
description: Technical architecture of Alopex DB
---

# Architecture

Alopex DB is built in **Rust** for safety, performance, and reliability. This page covers the technical architecture and design decisions.

## System Overview

```mermaid
graph TB
    subgraph "API Layer"
        REST[REST API]
        GRPC[gRPC API]
        WIRE[Postgres Wire Protocol]
        LIB[Embedded Library]
    end

    subgraph "Query Layer"
        PARSER[SQL Parser]
        ANALYZER[Semantic Analyzer]
        PLANNER[Query Planner]
        OPTIMIZER[Cost-Based Optimizer]
        EXECUTOR[Query Executor]
    end

    subgraph "Transaction Layer"
        TXN[Transaction Manager]
        MVCC[MVCC Engine]
        LOCK[Lock Manager]
        WAL[Write-Ahead Log]
    end

    subgraph "Storage Layer"
        MEMTABLE[MemTable]
        LSM[LSM-Tree]
        SSTABLE[SSTable Files]
        VECIDX[Vector Index]
        BLOOM[Bloom Filters]
    end

    subgraph "Cluster Layer"
        RAFT[Raft Consensus]
        SHARD[Range Sharding]
        CHIRPS[Chirps Mesh]
        META[Metadata Store]
    end

    REST --> PARSER
    GRPC --> PARSER
    WIRE --> PARSER
    LIB --> PARSER

    PARSER --> ANALYZER
    ANALYZER --> PLANNER
    PLANNER --> OPTIMIZER
    OPTIMIZER --> EXECUTOR

    EXECUTOR --> TXN
    TXN --> MVCC
    MVCC --> LOCK
    TXN --> WAL

    MVCC --> MEMTABLE
    MEMTABLE --> LSM
    LSM --> SSTABLE
    LSM --> VECIDX
    LSM --> BLOOM

    LSM --> RAFT
    RAFT --> SHARD
    SHARD --> CHIRPS
    CHIRPS --> META
```

## Storage Engine

### LSM-Tree Design

Alopex uses a Log-Structured Merge-Tree (LSM-Tree) optimized for both key-value and vector workloads.

```mermaid
graph TB
    subgraph "Write Path"
        W[Write] --> WAL[WAL]
        WAL --> MT[MemTable]
        MT -->|Flush| L0[Level 0 SSTable]
    end

    subgraph "Compaction"
        L0 -->|Compact| L1[Level 1]
        L1 -->|Compact| L2[Level 2]
        L2 -->|Compact| LN[Level N]
    end

    subgraph "Read Path"
        R[Read] --> MT
        R --> L0
        R --> L1
        R --> LN
    end
```

#### Key Components

| Component | Description |
|:----------|:------------|
| **MemTable** | In-memory sorted map (skip list) for recent writes |
| **WAL** | Write-ahead log for durability |
| **SSTable** | Sorted String Table, immutable on-disk files |
| **Bloom Filter** | Probabilistic structure for fast key lookups |
| **Block Cache** | LRU cache for frequently accessed blocks |

#### Write Path

1. **WAL Append**: Write logged for durability
2. **MemTable Insert**: Data added to in-memory structure
3. **MemTable Flush**: When full, written as L0 SSTable
4. **Compaction**: Background merge of SSTables

#### Read Path

1. **MemTable Check**: Search recent writes
2. **Block Cache**: Check cached data blocks
3. **Bloom Filter**: Probabilistic key existence check
4. **SSTable Search**: Binary search within files

### Vector Index Integration

Vector indexes are co-located with data for locality:

```mermaid
graph LR
    subgraph "SSTable"
        DATA[Data Blocks]
        META[Metadata]
        BLOOM[Bloom Filter]
        VEC[Vector Index Segment]
    end

    DATA --> VEC
```

#### HNSW Implementation

```
Layer 3: [sparse connections for long-range jumps]
    ↓
Layer 2: [more connections]
    ↓
Layer 1: [dense connections]
    ↓
Layer 0: [all nodes, maximum connectivity]
```

Search algorithm:
1. Enter at top layer
2. Greedily traverse to nearest neighbor
3. Descend to next layer
4. Repeat until layer 0
5. Return top-k neighbors

## Transaction Layer

### MVCC (Multi-Version Concurrency Control)

Alopex uses MVCC for snapshot isolation:

```mermaid
sequenceDiagram
    participant T1 as Transaction 1
    participant DB as Database
    participant T2 as Transaction 2

    T1->>DB: BEGIN (ts=100)
    T2->>DB: BEGIN (ts=101)
    T1->>DB: UPDATE row (version=100)
    T2->>DB: READ row
    Note over T2,DB: Sees original version<br/>(snapshot at ts=101)
    T1->>DB: COMMIT
    T2->>DB: READ row
    Note over T2,DB: Still sees original<br/>(snapshot isolation)
    T2->>DB: COMMIT
```

### Transaction States

| State | Description |
|:------|:------------|
| `Active` | Transaction in progress |
| `Committed` | Successfully committed |
| `Aborted` | Rolled back |
| `Prepared` | 2PC prepared state |

### Isolation Levels

| Level | Dirty Read | Non-Repeatable | Phantom |
|:------|:-----------|:---------------|:--------|
| Read Uncommitted | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Read Committed | :x: | :white_check_mark: | :white_check_mark: |
| Repeatable Read | :x: | :x: | :white_check_mark: |
| **Snapshot** (default) | :x: | :x: | :x: |
| Serializable | :x: | :x: | :x: |

## Query Layer

### SQL Parser

Built on `sqlparser-rs` with extensions for vectors:

```sql
-- Extended grammar
vector_type ::= VECTOR '(' dimension ')'
vector_literal ::= '[' number (',' number)* ']'
vector_function ::= cosine_similarity | l2_distance | inner_product
```

### Query Planner

Cost-based optimizer with vector-aware planning:

```mermaid
graph TD
    SQL[SQL Query] --> PARSE[Parse Tree]
    PARSE --> LOGICAL[Logical Plan]
    LOGICAL --> OPTIMIZE[Optimization Rules]
    OPTIMIZE --> PHYSICAL[Physical Plan]
    PHYSICAL --> EXEC[Execution]

    subgraph "Optimization Rules"
        R1[Predicate Pushdown]
        R2[Join Reordering]
        R3[Index Selection]
        R4[Vector Index Routing]
    end
```

### Execution Engine

Volcano-style iterator model:

```rust
trait Executor {
    fn open(&mut self) -> Result<()>;
    fn next(&mut self) -> Result<Option<Row>>;
    fn close(&mut self) -> Result<()>;
}
```

## Cluster Layer

### Raft Consensus

Each data range forms a Raft group:

```mermaid
graph TB
    subgraph "Range [a-m)"
        L1[Leader]
        F1[Follower]
        F2[Follower]
    end

    subgraph "Range [m-z)"
        L2[Leader]
        F3[Follower]
        F4[Follower]
    end

    L1 <-.->|Raft| F1
    L1 <-.->|Raft| F2
    L2 <-.->|Raft| F3
    L2 <-.->|Raft| F4
```

#### Raft Operations

| Operation | Description |
|:----------|:------------|
| Leader Election | Automatic failover on leader failure |
| Log Replication | Synchronous replication to followers |
| Snapshot | Periodic state snapshots for recovery |
| Membership Change | Dynamic cluster reconfiguration |

### Range Sharding

Data partitioned by key range:

```
Key Space: [0000...FFFF]
├── Range 1: [0000...3FFF] → Node 1 (Leader), Node 2, Node 3
├── Range 2: [4000...7FFF] → Node 2 (Leader), Node 3, Node 1
├── Range 3: [8000...BFFF] → Node 3 (Leader), Node 1, Node 2
└── Range 4: [C000...FFFF] → Node 1 (Leader), Node 3, Node 2
```

### Chirps Mesh

QUIC-based gossip protocol for cluster communication:

```mermaid
graph LR
    subgraph "Chirps Network"
        N1[Node 1]
        N2[Node 2]
        N3[Node 3]
        N4[Node 4]
    end

    N1 <-.->|QUIC| N2
    N2 <-.->|QUIC| N3
    N3 <-.->|QUIC| N4
    N4 <-.->|QUIC| N1
    N1 <-.->|QUIC| N3
    N2 <-.->|QUIC| N4
```

Features:
- **SWIM protocol** for failure detection
- **QUIC transport** for low-latency, encrypted communication
- **Gossip-based** metadata propagation

## Memory Management

### Buffer Pool

```
┌─────────────────────────────────────┐
│           Buffer Pool               │
├─────────┬─────────┬─────────┬───────┤
│ Block 1 │ Block 2 │ Block 3 │ ...   │
└─────────┴─────────┴─────────┴───────┘
     ↑         ↑         ↑
     │         │         │
   Page      Page      Page
   Table     Table     Table
```

### Memory Budget

| Component | Default | Configurable |
|:----------|:--------|:-------------|
| Buffer Pool | 25% of RAM | `buffer_pool_size` |
| MemTable | 64 MB | `memtable_size` |
| Block Cache | 512 MB | `block_cache_size` |
| Vector Index | 1 GB | `vector_index_memory` |

## File Format

### SSTable Structure

```
┌──────────────────────────────────┐
│         Data Blocks              │
├──────────────────────────────────┤
│         Meta Blocks              │
├──────────────────────────────────┤
│         Index Block              │
├──────────────────────────────────┤
│         Bloom Filter             │
├──────────────────────────────────┤
│      Vector Index Segment        │
├──────────────────────────────────┤
│           Footer                 │
└──────────────────────────────────┘
```

### WAL Format

```
┌─────────┬──────────┬─────────┬──────────┐
│ Length  │ Checksum │  Type   │  Data    │
│ (4 bytes)│ (4 bytes)│ (1 byte)│ (var)    │
└─────────┴──────────┴─────────┴──────────┘
```

## Performance Characteristics

| Operation | Complexity | Notes |
|:----------|:-----------|:------|
| Point Read | O(log N) | With bloom filter: O(1) expected |
| Range Scan | O(log N + K) | K = result count |
| Write | O(1) amortized | Plus WAL sync |
| Vector Search (HNSW) | O(log N) | Approximate |
| Vector Search (Flat) | O(N × D) | Exact, D = dimensions |

## Next Steps

- [:octicons-arrow-right-24: SQL + Vector Guide](../guides/sql-vector.md)
- [:octicons-arrow-right-24: Contributing](../contributing.md)

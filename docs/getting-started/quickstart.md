---
title: Quick Start
description: Get started with Alopex DB in minutes
---

# Quick Start

Get up and running with Alopex DB in just a few minutes. Alopex DB v0.3 is now available on **crates.io** with full SQL support and HNSW indexing.

[![crates.io](https://img.shields.io/crates/v/alopex-embedded.svg)](https://crates.io/crates/alopex-embedded)
[![crates.io](https://img.shields.io/crates/v/alopex-sql.svg)](https://crates.io/crates/alopex-sql)
[![crates.io](https://img.shields.io/crates/v/alopex-core.svg)](https://crates.io/crates/alopex-core)

## Prerequisites

- **Rust** 1.75 or later
- **Cargo** (comes with Rust)

## Installation

### Using Cargo (Recommended)

```bash
# Add to your Cargo.toml
cargo add alopex-embedded alopex-sql
```

Or add manually to `Cargo.toml`:

```toml
[dependencies]
alopex-embedded = "0.3"
alopex-sql = "0.3"
```

### From Source

```bash
git clone https://github.com/alopex-db/alopex.git
cd alopex
cargo build --release
```

## Your First Database

### Basic KV Operations

```rust
use alopex_embedded::{Database, TxnMode};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Open or create a database
    let db = Database::open("./my_data")?;

    // Start a read-write transaction
    let tx = db.begin(TxnMode::ReadWrite)?;

    // Insert data
    tx.put(b"user:1", b"Alice")?;
    tx.put(b"user:2", b"Bob")?;

    // Commit the transaction
    tx.commit()?;

    // Read data (auto-transaction)
    let value = db.get(b"user:1")?;
    println!("Got: {:?}", String::from_utf8_lossy(&value.unwrap()));

    Ok(())
}
```

### SQL Operations

```rust
use alopex_embedded::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open("./sql_data")?;

    // Create a table
    db.execute_sql("CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT
    )", &[])?;

    // Insert data
    db.execute_sql(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        &[&1i64, &"Alice", &"alice@example.com"]
    )?;

    // Query data
    let results = db.execute_sql(
        "SELECT id, name FROM users WHERE id = ?",
        &[&1i64]
    )?;

    for row in results.rows() {
        println!("User: {} - {}", row.get::<i64>("id")?, row.get::<String>("name")?);
    }

    Ok(())
}
```

### Vector Search with HNSW

```rust
use alopex_embedded::{Database, Metric};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open("./vector_data")?;

    // Create table with vector column
    db.execute_sql("CREATE TABLE documents (
        id INTEGER PRIMARY KEY,
        content TEXT,
        embedding VECTOR(384)
    )", &[])?;

    // Insert documents with embeddings
    let embedding = vec![0.1f32; 384]; // Your actual embedding
    db.execute_sql(
        "INSERT INTO documents (id, content, embedding) VALUES (?, ?, ?)",
        &[&1i64, &"Hello world", &embedding]
    )?;

    // Create HNSW index for fast similarity search
    db.create_hnsw_index(
        "documents",
        "embedding",
        Metric::Cosine,
        16,   // m parameter
        200,  // ef_construction
    )?;

    // Search similar vectors
    let query = vec![0.1f32; 384];
    let results = db.search_hnsw("documents", &query, 10)?;

    for (doc_id, score) in results {
        println!("Document {}: score = {:.4}", doc_id, score);
    }

    Ok(())
}
```

### Hybrid SQL + Vector Search

Combine SQL filtering with vector similarity:

```rust
use alopex_embedded::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open("./hybrid_data")?;

    // Query with vector similarity function
    let query_embedding = vec![0.1f32; 384];
    let results = db.execute_sql(
        "SELECT id, content, vector_similarity(embedding, ?) AS score
         FROM documents
         WHERE score > 0.8
         ORDER BY score DESC
         LIMIT 5",
        &[&query_embedding]
    )?;

    for row in results.rows() {
        println!(
            "{}: {} (score: {:.4})",
            row.get::<i64>("id")?,
            row.get::<String>("content")?,
            row.get::<f64>("score")?
        );
    }

    Ok(())
}
```

## In-Memory Mode

For testing or temporary data:

```rust
use alopex_embedded::Database;

let db = Database::open_in_memory()?;

// All data is stored in memory
db.execute_sql("CREATE TABLE temp (id INTEGER PRIMARY KEY, value TEXT)", &[])?;
db.execute_sql("INSERT INTO temp VALUES (1, 'temporary')", &[])?;

// Data is lost when db is dropped
```

## Run the Examples

```bash
# Clone the repository
git clone https://github.com/alopex-db/alopex.git
cd alopex

# Run SQL example
cargo run --example embedded-sql

# Run Vector example
cargo run --example embedded-vector

# Run HNSW example
cargo run --example embedded-hnsw
```

## Configuration Options

```rust
use alopex_embedded::{Database, Config};

let config = Config::default()
    .path("./my_data")
    .memory_limit(1024 * 1024 * 512)  // 512MB
    .wal_sync(true)                    // Sync WAL on commit
    .compression(true);                // Enable compression

let db = Database::open_with_config(config)?;
```

## What's Next?

<div class="grid cards" markdown>

-   :material-book-open:{ .lg .middle } **Concepts**

    ---

    Learn about Alopex DB's architecture and design philosophy.

    [:octicons-arrow-right-24: Read concepts](../concepts/overview.md)

-   :material-database:{ .lg .middle } **Deployment Modes**

    ---

    Understand embedded, single-node, and distributed modes.

    [:octicons-arrow-right-24: Explore modes](../concepts/modes.md)

-   :material-magnify:{ .lg .middle } **Vector Search**

    ---

    Deep dive into vector operations and HNSW indexing.

    [:octicons-arrow-right-24: Learn vectors](../concepts/vector-search.md)

-   :material-code-braces:{ .lg .middle } **SQL + Vector Guide**

    ---

    Combine SQL queries with vector similarity search.

    [:octicons-arrow-right-24: View guide](../guides/sql-vector.md)

</div>

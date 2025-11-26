---
title: Quick Start
description: Get started with Alopex DB in minutes
---

# Quick Start

Get up and running with Alopex DB in just a few minutes.

## Prerequisites

- **Rust** 1.75 or later
- **Cargo** (comes with Rust)

## Installation

### Using Cargo

```bash
# Add to your Cargo.toml
cargo add alopex-embedded
```

### From Source

```bash
git clone https://github.com/alopex-db/alopex.git
cd alopex
cargo build --release
```

## Your First Database

### Embedded Mode (Library)

```rust
use alopex_embedded::{Database, Config};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Open or create a database
    let config = Config::default()
        .path("./my_data");

    let db = Database::open(config)?;

    // Start a transaction
    let tx = db.begin()?;

    // Insert data
    tx.put(b"key1", b"value1")?;
    tx.put(b"key2", b"value2")?;

    // Commit the transaction
    tx.commit()?;

    // Read data
    let value = db.get(b"key1")?;
    println!("Got: {:?}", value);

    Ok(())
}
```

### Vector Operations

```rust
use alopex_embedded::{Database, Vector};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open_default("./vector_data")?;

    // Insert vectors
    let embedding = Vector::from_slice(&[0.1, 0.2, 0.3, /* ... 1536 dims */]);
    db.upsert_vector("doc_1", &embedding, Some(b"metadata"))?;

    // Search similar vectors
    let query = Vector::from_slice(&[0.15, 0.25, 0.35, /* ... */]);
    let results = db.search_vectors(&query, 10)?;

    for (id, score) in results {
        println!("Found: {} with score {}", id, score);
    }

    Ok(())
}
```

## Run the Demo

```bash
# Key-Value demo
./examples/embedded-kv/demo.sh

# Vector search demo
./examples/embedded-vector/demo_vector.sh
```

## What's Next?

<div class="grid cards" markdown>

-   :material-book-open:{ .lg .middle } **Concepts**

    ---

    Learn about Alopex DB's architecture and design philosophy.

    [:octicons-arrow-right-24: Read concepts](../concepts/overview.md)

-   :material-database:{ .lg .middle } **Three Modes**

    ---

    Understand embedded, single-node, and distributed modes.

    [:octicons-arrow-right-24: Explore modes](../concepts/modes.md)

-   :material-magnify:{ .lg .middle } **Vector Search**

    ---

    Deep dive into vector operations and hybrid queries.

    [:octicons-arrow-right-24: Learn vectors](../concepts/vector-search.md)

-   :material-code-braces:{ .lg .middle } **SQL + Vector Guide**

    ---

    Combine SQL queries with vector similarity search.

    [:octicons-arrow-right-24: View guide](../guides/sql-vector.md)

</div>

---
title: Python Guide
description: Using Alopex DB with Python (alopex-py)
---

# Python Guide

!!! info "Coming in v0.3.1"

    Python bindings (alopex-py) are currently in development and will be released in v0.3.1. This guide provides a preview of the upcoming API.

## Overview

**alopex-py** provides Python bindings for Alopex DB via PyO3, enabling Python developers to use the full power of Alopex DB's embedded database engine.

### Features

- **Database API**: Full access to embedded database operations
- **SQL API**: Execute SQL queries with parameter binding
- **Vector/HNSW API**: High-performance vector similarity search
- **NumPy Integration**: Zero-copy array operations
- **Type Stubs**: Full IDE support with `.pyi` files

## Installation

```bash
# Coming soon to PyPI
pip install alopex
```

## Quick Start

### Basic Database Operations

```python
import alopex

# Open or create a database
db = alopex.Database.open("./my_data")

# Execute SQL
db.execute_sql("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT
    )
""")

# Insert data with parameters
db.execute_sql(
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
    [1, "Alice", "alice@example.com"]
)

# Query data
results = db.execute_sql("SELECT * FROM users WHERE id = ?", [1])
for row in results:
    print(f"User: {row['name']} ({row['email']})")
```

### Vector Search with HNSW

```python
import alopex
import numpy as np

db = alopex.Database.open("./vector_data")

# Create table with vector column
db.execute_sql("""
    CREATE TABLE documents (
        id INTEGER PRIMARY KEY,
        content TEXT,
        embedding VECTOR(384)
    )
""")

# Insert documents with embeddings
embedding = np.random.rand(384).astype(np.float32)
db.execute_sql(
    "INSERT INTO documents (id, content, embedding) VALUES (?, ?, ?)",
    [1, "Hello world", embedding]
)

# Create HNSW index
db.create_hnsw_index(
    table="documents",
    column="embedding",
    metric="cosine",
    m=16,
    ef_construction=200
)

# Search similar vectors
query = np.random.rand(384).astype(np.float32)
results = db.search_hnsw("documents", query, k=10)

for doc_id, score in results:
    print(f"Document {doc_id}: score = {score:.4f}")
```

### Hybrid SQL + Vector Search

```python
import alopex
import numpy as np

db = alopex.Database.open("./hybrid_data")

# Hybrid search with SQL filtering
query_embedding = np.random.rand(384).astype(np.float32)

results = db.execute_sql("""
    SELECT id, content, vector_similarity(embedding, ?) AS score
    FROM documents
    WHERE score > 0.8
    ORDER BY score DESC
    LIMIT 5
""", [query_embedding])

for row in results:
    print(f"{row['id']}: {row['content']} (score: {row['score']:.4f})")
```

## Transaction Support

```python
import alopex

db = alopex.Database.open("./tx_data")

# Explicit transaction
tx = db.begin()
try:
    tx.execute_sql("INSERT INTO users (id, name) VALUES (?, ?)", [1, "Alice"])
    tx.execute_sql("INSERT INTO users (id, name) VALUES (?, ?)", [2, "Bob"])
    tx.commit()
except Exception as e:
    tx.rollback()
    raise
```

## NumPy Integration

alopex-py provides zero-copy integration with NumPy arrays:

```python
import alopex
import numpy as np

db = alopex.Database.open("./numpy_data")

# Direct NumPy array support
embeddings = np.random.rand(100, 384).astype(np.float32)

# Batch insert with NumPy arrays
for i, embedding in enumerate(embeddings):
    db.execute_sql(
        "INSERT INTO documents (id, embedding) VALUES (?, ?)",
        [i, embedding]  # NumPy array passed directly
    )

# Query returns NumPy-compatible data
results = db.execute_sql("SELECT embedding FROM documents WHERE id = ?", [0])
embedding = np.array(results[0]['embedding'])
```

## Configuration Options

```python
import alopex

# Configure database options
config = alopex.Config(
    path="./my_data",
    memory_limit=512 * 1024 * 1024,  # 512MB
    wal_sync=True,
    compression=True
)

db = alopex.Database.open_with_config(config)
```

## In-Memory Mode

```python
import alopex

# Create in-memory database for testing
db = alopex.Database.open_in_memory()

db.execute_sql("CREATE TABLE temp (id INTEGER PRIMARY KEY, value TEXT)")
db.execute_sql("INSERT INTO temp VALUES (1, 'temporary')")

# Data is lost when db is closed
```

## API Reference

### Database

| Method | Description |
|:-------|:------------|
| `open(path)` | Open or create a database at the given path |
| `open_in_memory()` | Create an in-memory database |
| `open_with_config(config)` | Open with custom configuration |
| `execute_sql(sql, params)` | Execute SQL query with parameters |
| `begin()` | Start a new transaction |
| `create_hnsw_index(...)` | Create HNSW index on vector column |
| `search_hnsw(table, query, k)` | Search for k nearest neighbors |
| `close()` | Close the database connection |

### Transaction

| Method | Description |
|:-------|:------------|
| `execute_sql(sql, params)` | Execute SQL within transaction |
| `commit()` | Commit the transaction |
| `rollback()` | Rollback the transaction |

### Config

| Option | Type | Default | Description |
|:-------|:-----|:--------|:------------|
| `path` | str | - | Database file path |
| `memory_limit` | int | 256MB | Maximum memory usage |
| `wal_sync` | bool | True | Sync WAL on commit |
| `compression` | bool | True | Enable compression |

## Development Roadmap

| Version | Phase | Features |
|:--------|:------|:---------|
| **v0.1.0** | Phase 1 | Database/Transaction basic API |
| v0.1.1 | Phase 1 | Vector/HNSW API |
| v0.1.2 | Phase 1 | NumPy integration, GIL release |
| **v0.2.0** | Phase 2 | DataFrame API (via alopex-dataframe) |
| **v0.3.0** | Phase 3 | Client API (Server connection) |

## See Also

- [:octicons-arrow-right-24: Quick Start](../getting-started/quickstart.md) - Get started with Alopex DB
- [:octicons-arrow-right-24: SQL + Vector Guide](sql-vector.md) - Hybrid SQL and vector queries
- [:octicons-arrow-right-24: DataFrame API](dataframe.md) - Polars-compatible DataFrame operations
- [:octicons-arrow-right-24: Roadmap](../roadmap.md) - Development timeline

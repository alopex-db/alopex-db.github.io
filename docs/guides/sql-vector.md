---
title: SQL + Vector Guide
description: Practical guide to combining SQL queries with vector operations in Alopex DB
---

# SQL + Vector Guide

This guide demonstrates practical patterns for combining SQL queries with vector similarity search in Alopex DB.

## Basic Setup

### Creating a Table with Vectors

```sql
-- Document storage with embeddings
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    category TEXT,
    created_at TIMESTAMP
);

-- Create HNSW index for fast similarity search
CREATE INDEX idx_embedding ON documents
USING HNSW (embedding)
WITH (m = 16, ef_construction = 200);
```

## Inserting Data

### From Rust Application

```rust
use alopex_embedded::Database;

fn insert_document(
    db: &Database,
    id: i64,
    title: &str,
    content: &str,
    embedding: Vec<f32>,
    category: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    db.execute_sql(
        "INSERT INTO documents (id, title, content, embedding, category)
         VALUES (?, ?, ?, ?, ?)",
        &[&id, &title, &content, &embedding, &category],
    )?;
    Ok(())
}
```

### From Python (Coming in v0.3.1)

```python
import alopex
import numpy as np

def insert_document(db, id, title, content, embedding, category):
    db.execute_sql("""
        INSERT INTO documents (id, title, content, embedding, category)
        VALUES (?, ?, ?, ?, ?)
    """, [id, title, content, embedding.tolist(), category])
```

## Query Patterns

### Pure Vector Search

Find the most similar documents to a query embedding:

```sql
-- Top 10 most similar documents
SELECT id, title, content,
       vector_similarity(embedding, ?) AS score
FROM documents
ORDER BY score DESC
LIMIT 10;
```

```rust
use alopex_embedded::Database;

let query_embedding = vec![0.1f32; 1536]; // Your query vector
let results = db.execute_sql(
    "SELECT id, title, content, vector_similarity(embedding, ?) AS score
     FROM documents
     ORDER BY score DESC
     LIMIT 10",
    &[&query_embedding]
)?;

for row in results.rows() {
    println!("{}: {} (score: {:.4})",
        row.get::<i64>("id")?,
        row.get::<String>("title")?,
        row.get::<f64>("score")?
    );
}
```

### Hybrid Search (Recommended)

Combine SQL filters with vector similarity:

```sql
-- Semantic search within a category
SELECT id, title, content,
       vector_similarity(embedding, ?) AS score
FROM documents
WHERE category = 'technology'
ORDER BY score DESC
LIMIT 10;
```

```rust
let results = db.execute_sql(
    "SELECT id, title, content, vector_similarity(embedding, ?) AS score
     FROM documents
     WHERE category = ?
     ORDER BY score DESC
     LIMIT 10",
    &[&query_embedding, &"technology"]
)?;
```

### Threshold-Based Search

Return only results above a similarity threshold:

```sql
-- Only return highly similar results
SELECT id, title, content,
       vector_similarity(embedding, ?) AS score
FROM documents
WHERE score > 0.8
ORDER BY score DESC
LIMIT 10;
```

!!! tip "HNSW Index Acceleration"

    When using HNSW index, similarity search is accelerated automatically:

    ```rust
    // Direct HNSW search for maximum performance
    let results = db.search_hnsw("documents", &query_embedding, 10)?;

    for (doc_id, score) in results {
        println!("Document {}: {:.4}", doc_id, score);
    }
    ```

## Advanced Patterns

### Multi-Vector Search

Search across multiple embedding spaces:

```sql
-- Products with both text and image embeddings
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    text_embedding VECTOR(384),
    image_embedding VECTOR(512)
);

-- Combined similarity search
SELECT id, name,
       0.6 * vector_similarity(text_embedding, ?) +
       0.4 * vector_similarity(image_embedding, ?) AS combined_score
FROM products
ORDER BY combined_score DESC
LIMIT 10;
```

### Two-Stage Retrieval

Efficient retrieval with HNSW + SQL:

```rust
use alopex_embedded::Database;

fn two_stage_search(
    db: &Database,
    query: &[f32],
    category: &str,
    limit: usize,
) -> Result<Vec<(i64, String, f64)>, Box<dyn std::error::Error>> {
    // Stage 1: Fast HNSW retrieval (100 candidates)
    let candidates = db.search_hnsw("documents", query, 100)?;

    let candidate_ids: Vec<i64> = candidates.iter().map(|(id, _)| *id).collect();

    // Stage 2: SQL filtering and ranking
    let results = db.execute_sql(
        "SELECT id, title, vector_similarity(embedding, ?) AS score
         FROM documents
         WHERE id IN (SELECT value FROM json_each(?))
           AND category = ?
         ORDER BY score DESC
         LIMIT ?",
        &[&query.to_vec(), &serde_json::to_string(&candidate_ids)?, &category, &(limit as i64)]
    )?;

    Ok(results.rows()
        .map(|row| (
            row.get::<i64>("id").unwrap(),
            row.get::<String>("title").unwrap(),
            row.get::<f64>("score").unwrap()
        ))
        .collect())
}
```

## RAG Application Pattern

### Complete RAG Context Retrieval

```rust
use alopex_embedded::Database;

struct RAGContext {
    content: String,
    score: f64,
}

fn retrieve_rag_context(
    db: &Database,
    query_embedding: &[f32],
    category: &str,
    threshold: f64,
    limit: usize,
) -> Result<Vec<RAGContext>, Box<dyn std::error::Error>> {
    let results = db.execute_sql(
        "SELECT content, vector_similarity(embedding, ?) AS score
         FROM documents
         WHERE category = ?
           AND vector_similarity(embedding, ?) > ?
         ORDER BY score DESC
         LIMIT ?",
        &[
            &query_embedding.to_vec(),
            &category,
            &query_embedding.to_vec(),
            &threshold,
            &(limit as i64)
        ]
    )?;

    Ok(results.rows()
        .map(|row| RAGContext {
            content: row.get::<String>("content").unwrap(),
            score: row.get::<f64>("score").unwrap(),
        })
        .collect())
}
```

### Python RAG Example (Coming in v0.3.1)

```python
import alopex
import numpy as np

def retrieve_context(db, query_embedding, category, threshold=0.7, limit=5):
    """Retrieve relevant context for RAG applications."""
    results = db.execute_sql("""
        SELECT content, vector_similarity(embedding, ?) AS score
        FROM documents
        WHERE category = ?
        ORDER BY score DESC
        LIMIT ?
    """, [query_embedding, category, limit])

    return [
        {"content": row["content"], "score": row["score"]}
        for row in results
        if row["score"] > threshold
    ]

# Usage
db = alopex.Database.open("./rag_data")
query = get_embedding("What is machine learning?")
context = retrieve_context(db, query, "ml-docs")

# Use context for LLM prompt
prompt = f"""Based on the following context:
{chr(10).join(c['content'] for c in context)}

Answer: What is machine learning?"""
```

## Performance Tips

### Use HNSW for Large Datasets

```rust
// For datasets > 10,000 vectors, always use HNSW
db.create_hnsw_index(
    "documents",
    "embedding",
    alopex_embedded::Metric::Cosine,
    16,   // m: neighbors per layer
    200,  // ef_construction: build quality
)?;

// Direct HNSW search is 10-100x faster than SQL scan
let results = db.search_hnsw("documents", &query, 10)?;
```

### Batch Operations

```rust
use alopex_embedded::{Database, TxnMode};

fn batch_insert(
    db: &Database,
    documents: Vec<(i64, String, String, Vec<f32>)>,
) -> Result<(), Box<dyn std::error::Error>> {
    let tx = db.begin(TxnMode::ReadWrite)?;

    for (id, title, content, embedding) in documents {
        tx.execute_sql(
            "INSERT INTO documents (id, title, content, embedding) VALUES (?, ?, ?, ?)",
            &[&id, &title, &content, &embedding]
        )?;
    }

    tx.commit()?;
    Ok(())
}
```

### Filter Before Vector Search

Apply SQL filters to reduce the search space:

```sql
-- GOOD: Category filter reduces candidates
SELECT id, title, vector_similarity(embedding, ?) AS score
FROM documents
WHERE category = 'technology'  -- Filter first
ORDER BY score DESC
LIMIT 10;
```

## Common Mistakes

!!! warning "Avoid Full Table Scans"

    For large datasets, always create HNSW indexes:

    ```rust
    // Create index before searching
    db.create_hnsw_index("documents", "embedding", Metric::Cosine, 16, 200)?;

    // Use search_hnsw for indexed search
    let results = db.search_hnsw("documents", &query, 10)?;
    ```

!!! warning "Match Vector Dimensions"

    Ensure query vectors match the column dimension:

    ```sql
    -- Column is VECTOR(1536)
    -- Query must also be 1536 dimensions
    SELECT vector_similarity(embedding, ?) AS score  -- ? must be 1536-dim
    FROM documents;
    ```

!!! warning "Handle NULL Embeddings"

    Filter out rows with NULL embeddings:

    ```sql
    SELECT id, title, vector_similarity(embedding, ?) AS score
    FROM documents
    WHERE embedding IS NOT NULL
    ORDER BY score DESC
    LIMIT 10;
    ```

## Next Steps

- [:octicons-arrow-right-24: Python Guide](python.md) - Using alopex-py
- [:octicons-arrow-right-24: DataFrame API](dataframe.md) - Polars-compatible operations
- [:octicons-arrow-right-24: Vector Search Concepts](../concepts/vector-search.md) - Deep dive into vector operations

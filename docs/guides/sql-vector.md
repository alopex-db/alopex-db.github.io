---
title: SQL + Vector Guide
description: Practical guide to combining SQL queries with vector operations
---

# SQL + Vector Guide

This guide demonstrates practical patterns for combining SQL queries with vector similarity search in Alopex DB.

## Basic Setup

### Creating a Table with Vectors

```sql
-- Document storage with embeddings
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536),  -- OpenAI text-embedding-3-large
    category TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    metadata JSONB
);

-- Create vector index for fast similarity search
CREATE INDEX documents_embedding_idx ON documents
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 200);

-- Create standard indexes for filters
CREATE INDEX documents_category_idx ON documents (category);
CREATE INDEX documents_created_at_idx ON documents (created_at);
```

## Inserting Data

### From Application Code

=== "Rust"

    ```rust
    use alopex::{Client, Vector};

    async fn insert_document(
        client: &Client,
        title: &str,
        content: &str,
        embedding: Vec<f32>,
        category: &str,
    ) -> Result<Uuid> {
        let id: Uuid = client
            .query_one(
                "INSERT INTO documents (title, content, embedding, category)
                 VALUES ($1, $2, $3, $4)
                 RETURNING id",
                &[&title, &content, &Vector::from(embedding), &category],
            )
            .await?
            .get(0);
        Ok(id)
    }
    ```

=== "Python"

    ```python
    import alopex
    import numpy as np

    async def insert_document(conn, title, content, embedding, category):
        return await conn.fetchval("""
            INSERT INTO documents (title, content, embedding, category)
            VALUES ($1, $2, $3, $4)
            RETURNING id
        """, title, content, embedding.tolist(), category)
    ```

### Batch Insert

```sql
-- Efficient batch insert
INSERT INTO documents (title, content, embedding, category)
SELECT * FROM UNNEST(
    $1::text[],      -- titles
    $2::text[],      -- contents
    $3::vector[],    -- embeddings
    $4::text[]       -- categories
);
```

## Query Patterns

### Pure Vector Search

Find the most similar documents to a query embedding:

```sql
-- Top 10 most similar documents
SELECT id, title, content,
       cosine_similarity(embedding, $1) AS score
FROM documents
ORDER BY score DESC
LIMIT 10;
```

### Hybrid Search (Recommended)

Combine SQL filters with vector similarity:

```sql
-- Semantic search within a category
SELECT id, title, content,
       cosine_similarity(embedding, $1) AS score
FROM documents
WHERE category = 'technology'
  AND created_at > NOW() - INTERVAL '30 days'
ORDER BY score DESC
LIMIT 10;
```

### Threshold-Based Search

Return only results above a similarity threshold:

```sql
-- Only return highly similar results
SELECT id, title, content,
       cosine_similarity(embedding, $1) AS score
FROM documents
WHERE category = $2
  AND cosine_similarity(embedding, $1) > 0.8  -- Threshold
ORDER BY score DESC
LIMIT 10;
```

!!! tip "Use Index for Threshold Queries"

    For threshold queries, the vector index can prune candidates efficiently:

    ```sql
    -- This uses the index effectively
    SELECT id, title, score
    FROM (
        SELECT id, title,
               cosine_similarity(embedding, $1) AS score
        FROM documents
        ORDER BY embedding <=> $1  -- Index scan
        LIMIT 100  -- Candidate pool
    ) candidates
    WHERE score > 0.8
    ORDER BY score DESC;
    ```

## Advanced Patterns

### Multi-Vector Search

Search across multiple embedding spaces:

```sql
-- Products with both text and image embeddings
CREATE TABLE products (
    id UUID PRIMARY KEY,
    name TEXT,
    description TEXT,
    text_embedding VECTOR(384),
    image_embedding VECTOR(512)
);

-- Combined similarity search
SELECT id, name,
       0.6 * cosine_similarity(text_embedding, $1) +
       0.4 * cosine_similarity(image_embedding, $2) AS combined_score
FROM products
WHERE category = $3
ORDER BY combined_score DESC
LIMIT 10;
```

### Two-Stage Retrieval

Efficient retrieval with re-ranking:

```sql
-- Stage 1: Fast approximate retrieval
WITH candidates AS (
    SELECT id, title, content, embedding
    FROM documents
    WHERE category = $2
    ORDER BY embedding <=> $1  -- Approximate NN (uses index)
    LIMIT 100
)
-- Stage 2: Exact re-ranking
SELECT id, title, content,
       cosine_similarity(embedding, $1) AS score
FROM candidates
ORDER BY score DESC
LIMIT 10;
```

### Diversity Sampling

Avoid returning too-similar results:

```sql
-- Maximal Marginal Relevance (MMR)
WITH RECURSIVE diverse_results AS (
    -- Start with the most similar
    SELECT id, title, embedding, 1 AS rank,
           cosine_similarity(embedding, $1) AS relevance
    FROM documents
    ORDER BY relevance DESC
    LIMIT 1

    UNION ALL

    -- Add next most diverse result
    SELECT d.id, d.title, d.embedding, dr.rank + 1,
           cosine_similarity(d.embedding, $1)
    FROM documents d, diverse_results dr
    WHERE d.id NOT IN (SELECT id FROM diverse_results)
      AND dr.rank < 10
    ORDER BY
        0.7 * cosine_similarity(d.embedding, $1) -  -- Relevance
        0.3 * MAX(cosine_similarity(d.embedding, dr.embedding))  -- Diversity
    LIMIT 1
)
SELECT id, title, relevance AS score
FROM diverse_results
ORDER BY rank;
```

### Aggregated Embeddings

Search using averaged embeddings:

```sql
-- Find documents similar to a collection
WITH query_centroid AS (
    SELECT AVG(embedding) AS centroid
    FROM documents
    WHERE id = ANY($1::uuid[])  -- Reference document IDs
)
SELECT d.id, d.title,
       cosine_similarity(d.embedding, q.centroid) AS score
FROM documents d, query_centroid q
WHERE d.id != ALL($1::uuid[])  -- Exclude reference docs
ORDER BY score DESC
LIMIT 10;
```

## RAG Application Pattern

### Complete RAG Query

```sql
-- Full RAG context retrieval
WITH relevant_chunks AS (
    SELECT id, content, metadata,
           cosine_similarity(embedding, $1) AS score
    FROM documents
    WHERE category = $2
      AND created_at > $3
      AND score > 0.7
    ORDER BY score DESC
    LIMIT 5
)
SELECT
    json_agg(
        json_build_object(
            'content', content,
            'score', score,
            'metadata', metadata
        )
        ORDER BY score DESC
    ) AS context
FROM relevant_chunks;
```

### Conversation Memory

```sql
-- Store conversation with embeddings
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL,
    role TEXT NOT NULL,  -- 'user' or 'assistant'
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Retrieve relevant conversation history
SELECT role, content, created_at
FROM messages
WHERE conversation_id = $1
  AND cosine_similarity(embedding, $2) > 0.75
ORDER BY created_at DESC
LIMIT 10;
```

## Performance Tips

### Index Tuning

```sql
-- Tune HNSW for your use case
ALTER INDEX documents_embedding_idx
SET (ef_search = 150);  -- Higher = more accurate, slower

-- Check index statistics
SELECT * FROM alopex_vector_index_stats('documents_embedding_idx');
```

### Query Analysis

```sql
-- Analyze query performance
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT id, title, cosine_similarity(embedding, $1) AS score
FROM documents
WHERE category = 'technology'
ORDER BY score DESC
LIMIT 10;
```

### Batch Operations

```sql
-- Batch similarity computation
SELECT d.id, d.title,
       cosine_similarity(d.embedding, q.embedding) AS score
FROM documents d
CROSS JOIN (
    SELECT embedding
    FROM queries
    WHERE query_id = $1
) q
WHERE d.category = $2
ORDER BY score DESC
LIMIT 10;
```

## Common Mistakes

!!! warning "Avoid Full Table Scans"

    Always create vector indexes for large tables:

    ```sql
    -- BAD: Full table scan
    SELECT * FROM documents
    ORDER BY cosine_similarity(embedding, $1) DESC
    LIMIT 10;

    -- GOOD: Uses index
    SELECT * FROM documents
    ORDER BY embedding <=> $1  -- Index operator
    LIMIT 10;
    ```

!!! warning "Filter Before Vector Search"

    Apply SQL filters before vector similarity when possible:

    ```sql
    -- GOOD: Filters reduce candidate set
    SELECT * FROM documents
    WHERE category = 'tech' AND created_at > '2024-01-01'
    ORDER BY embedding <=> $1
    LIMIT 10;
    ```

!!! warning "Normalize Embeddings"

    For cosine similarity, normalize vectors:

    ```sql
    -- Normalize on insert
    INSERT INTO documents (embedding)
    VALUES (vector_normalize($1));
    ```

## Next Steps

- [:octicons-arrow-right-24: Lake-Link Guide](lake-link.md) - Import from Parquet
- [:octicons-arrow-right-24: Vector Search Concepts](../concepts/vector-search.md)

---
title: DataFrame API
description: Polars-compatible DataFrame operations with Alopex DB
---

# DataFrame API

!!! info "Coming in v0.4"

    The DataFrame API (alopex-dataframe) is planned for v0.4. This guide provides a preview of the upcoming API design.

## Overview

**alopex-dataframe** provides a Polars-compatible DataFrame engine in pure Rust, enabling high-performance data analysis directly within Alopex DB.

### Key Features

- **Polars Compatibility**: Familiar API for Polars users
- **Lazy Evaluation**: Query optimization through deferred execution
- **Arrow Integration**: Zero-copy data interchange
- **Database Integration**: Seamless integration with Alopex DB tables

## Quick Start

### Rust API

```rust
use alopex_dataframe::{DataFrame, col, lit};

// Read from Parquet file
let df = DataFrame::read_parquet("data.parquet")?;

// Lazy evaluation with query optimization
let result = df
    .lazy()
    .filter(col("score").gt(lit(0.5)))
    .select([col("id"), col("content"), col("score")])
    .group_by([col("category")])
    .agg([
        col("score").mean().alias("avg_score"),
        col("id").count().alias("count")
    ])
    .sort("avg_score", SortOptions::default().descending())
    .collect()?;

println!("{:?}", result);
```

### Python API (via alopex-py)

```python
import alopex

# Polars-compatible DataFrame API
df = alopex.read_parquet("data.parquet")

result = (
    df.lazy()
    .filter(alopex.col("score") > 0.5)
    .select(["id", "content", "score"])
    .group_by("category")
    .agg([
        alopex.col("score").mean().alias("avg_score"),
        alopex.col("id").count().alias("count")
    ])
    .sort("avg_score", descending=True)
    .collect()
)

print(result)
```

## I/O Operations

### Reading Data

```rust
use alopex_dataframe::DataFrame;

// Read Parquet
let df = DataFrame::read_parquet("data.parquet")?;

// Read CSV
let df = DataFrame::read_csv("data.csv")?;

// Scan (lazy loading)
let lf = DataFrame::scan_parquet("large_data.parquet")?;
let lf = DataFrame::scan_csv("large_data.csv")?;
```

### Writing Data

```rust
use alopex_dataframe::DataFrame;

let df = /* ... */;

// Write Parquet
df.write_parquet("output.parquet")?;

// Write CSV
df.write_csv("output.csv")?;
```

## DataFrame Operations

### Selection and Filtering

```rust
use alopex_dataframe::{DataFrame, col, lit};

let df = DataFrame::read_parquet("data.parquet")?;

// Select columns
let selected = df.select([col("id"), col("name"), col("score")])?;

// Filter rows
let filtered = df.filter(col("score").gt(lit(0.5)))?;

// Combined
let result = df
    .lazy()
    .filter(col("active").eq(lit(true)))
    .select([col("id"), col("name")])
    .collect()?;
```

### Aggregations

```rust
use alopex_dataframe::{DataFrame, col};

let df = DataFrame::read_parquet("sales.parquet")?;

let result = df
    .lazy()
    .group_by([col("region"), col("product")])
    .agg([
        col("amount").sum().alias("total"),
        col("amount").mean().alias("average"),
        col("amount").min().alias("min"),
        col("amount").max().alias("max"),
        col("id").count().alias("count")
    ])
    .collect()?;
```

### Joins (Coming in v0.3.0)

```rust
use alopex_dataframe::{DataFrame, col};

let users = DataFrame::read_parquet("users.parquet")?;
let orders = DataFrame::read_parquet("orders.parquet")?;

// Inner join
let result = users
    .lazy()
    .join(
        orders.lazy(),
        [col("id")],
        [col("user_id")],
        JoinType::Inner
    )
    .collect()?;
```

### Sorting

```rust
use alopex_dataframe::{DataFrame, col, SortOptions};

let df = DataFrame::read_parquet("data.parquet")?;

let sorted = df
    .lazy()
    .sort("score", SortOptions::default().descending())
    .collect()?;

// Multi-column sort
let sorted = df
    .lazy()
    .sort_by_exprs(
        [col("category"), col("score")],
        [false, true]  // ascending, descending
    )
    .collect()?;
```

## Lazy Evaluation

Lazy evaluation enables query optimization before execution:

```rust
use alopex_dataframe::{DataFrame, col, lit};

let lf = DataFrame::scan_parquet("large_data.parquet")?;

// Build query plan (no execution yet)
let query = lf
    .filter(col("date").gt(lit("2025-01-01")))
    .select([col("id"), col("value")])
    .group_by([col("category")])
    .agg([col("value").sum()]);

// Optimizations applied:
// - Predicate pushdown (filter applied during scan)
// - Projection pushdown (only required columns read)
// - Query plan optimization

// Execute
let result = query.collect()?;
```

## Expression System

### Column Expressions

```rust
use alopex_dataframe::{col, lit};

// Column reference
col("name")

// Literal value
lit(42)
lit("hello")
lit(3.14)

// Arithmetic
col("a") + col("b")
col("a") - lit(10)
col("a") * col("b")
col("a") / lit(2)

// Comparison
col("score").gt(lit(0.5))
col("score").lt(lit(1.0))
col("score").eq(lit(0.8))
col("name").is_null()
col("name").is_not_null()

// Logical
col("active").and(col("verified"))
col("a").or(col("b"))
col("flag").not()
```

### String Operations (Coming in v0.4.0)

```rust
use alopex_dataframe::col;

// String namespace
col("name").str().to_lowercase()
col("name").str().to_uppercase()
col("name").str().contains("pattern")
col("name").str().starts_with("prefix")
col("name").str().ends_with("suffix")
col("name").str().len_chars()
```

### Date/Time Operations (Coming in v0.4.0)

```rust
use alopex_dataframe::col;

// Datetime namespace
col("timestamp").dt().year()
col("timestamp").dt().month()
col("timestamp").dt().day()
col("timestamp").dt().hour()
col("timestamp").dt().minute()
```

## Database Integration

### Query Alopex DB Tables

```rust
use alopex_embedded::Database;
use alopex_dataframe::DataFrame;

let db = Database::open("./my_data")?;

// Load table as DataFrame
let df = db.table_to_dataframe("users")?;

// Process with DataFrame API
let result = df
    .lazy()
    .filter(col("active").eq(lit(true)))
    .select([col("id"), col("name"), col("email")])
    .collect()?;

// Write back to database
db.dataframe_to_table(&result, "active_users")?;
```

### Vector Operations

```rust
use alopex_dataframe::{DataFrame, col};

let df = db.table_to_dataframe("documents")?;

// Vector similarity in DataFrame context
let query_vector = vec![0.1f32; 384];

let result = df
    .lazy()
    .with_column(
        col("embedding")
            .vector_similarity(&query_vector)
            .alias("score")
    )
    .filter(col("score").gt(lit(0.8)))
    .sort("score", SortOptions::default().descending())
    .limit(10)
    .collect()?;
```

## Development Roadmap

| Version | Phase | Features |
|:--------|:------|:---------|
| **v0.1.0** | DF-0 | DataFrame/Series types, Arrow integration |
| **v0.2.0** | DF-1 | CSV/Parquet I/O, select/filter/group_by, LazyFrame |
| **v0.3.0** | DF-2 | JOIN, sort, fill_null, Predicate Pushdown |
| **v0.4.0** | DF-3 | Window functions, pivot/unpivot, str/dt namespaces |

## Comparison with Polars

| Feature | alopex-dataframe | Polars |
|:--------|:-----------------|:-------|
| Language | Pure Rust | Rust + Python |
| Database Integration | Native Alopex DB | External |
| Vector Operations | Built-in | Via extension |
| SQL Integration | Native | Via SQLContext |
| Lazy Evaluation | Yes | Yes |
| Arrow Backend | Yes | Yes |

## See Also

- [:octicons-arrow-right-24: Python Guide](python.md) - Using alopex-py with DataFrame
- [:octicons-arrow-right-24: SQL + Vector Guide](sql-vector.md) - SQL-based queries
- [:octicons-arrow-right-24: Quick Start](../getting-started/quickstart.md) - Getting started
- [:octicons-arrow-right-24: Roadmap](../roadmap.md) - Development timeline

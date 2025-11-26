---
title: Contributing
description: How to contribute to Alopex DB
---

# Contributing to Alopex DB

Thank you for your interest in contributing to Alopex DB! This guide will help you get started.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

## Ways to Contribute

### :bug: Report Bugs

Found a bug? Please open an issue with:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Rust version, etc.)

[:octicons-issue-opened-24: Open an Issue](https://github.com/alopex-db/alopex/issues/new){ .md-button }

### :bulb: Suggest Features

Have an idea? We'd love to hear it:

- Describe the use case
- Explain why it would be useful
- Share any implementation ideas

[:octicons-light-bulb-24: Start a Discussion](https://github.com/alopex-db/alopex/discussions){ .md-button }

### :memo: Improve Documentation

Documentation improvements are always welcome:

- Fix typos and errors
- Add examples
- Clarify confusing sections
- Translate to other languages

### :computer: Contribute Code

Ready to code? Here's how to get started.

## Development Setup

### Prerequisites

- **Rust** 1.75+ (toolchain 1.90.0 recommended)
- **Git**
- **Make** (optional, for convenience scripts)

### Clone and Build

```bash
# Clone the repository
git clone https://github.com/alopex-db/alopex.git
cd alopex

# Build all crates
cargo build

# Run tests
cargo test

# Run benchmarks
cargo bench
```

### Project Structure

```
alopex/
├── alopex-core/       # Storage engine
├── alopex-sql/        # SQL parser and executor
├── alopex-embedded/   # Embedded mode API
├── alopex-server/     # Single-node server
├── alopex-cluster/    # Distributed mode
├── alopex-cli/        # Command-line tools
├── alopex-tools/      # Development utilities
├── chirps/            # Cluster messaging
│   ├── alopex-chirps/
│   ├── chirps-transport-quic/
│   ├── chirps-gossip-swim/
│   └── chirps-wire/
├── design/            # Design documents
└── examples/          # Example applications
```

### Running Tests

```bash
# All tests
cargo test

# Specific crate
cargo test -p alopex-core

# With logging
RUST_LOG=debug cargo test

# Integration tests only
cargo test --test '*'
```

## Pull Request Process

### 1. Fork and Branch

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/alopex.git
cd alopex
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write clean, documented code
- Follow existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Format code
cargo fmt

# Run linter
cargo clippy -- -D warnings

# Run all tests
cargo test

# Check documentation builds
cargo doc --no-deps
```

### 4. Commit

Write clear commit messages:

```
feat(core): add HNSW vector index

- Implement hierarchical navigable small world graph
- Add configurable M and ef_construction parameters
- Include benchmark comparing to flat search

Closes #123
```

Commit types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

### 5. Submit PR

- Fill out the PR template
- Link related issues
- Request review from maintainers

## Code Style

### Rust Guidelines

```rust
// Use descriptive names
fn calculate_cosine_similarity(a: &Vector, b: &Vector) -> f32 { ... }

// Document public APIs
/// Inserts a key-value pair into the database.
///
/// # Arguments
/// * `key` - The key to insert
/// * `value` - The value to associate with the key
///
/// # Returns
/// * `Ok(())` on success
/// * `Err(Error)` if the write fails
pub fn put(&self, key: &[u8], value: &[u8]) -> Result<()> { ... }

// Handle errors explicitly
let result = db.get(key)?;

// Use type inference where clear
let map: HashMap<String, Vec<u8>> = HashMap::new();
let map = HashMap::<String, Vec<u8>>::new();  // Also OK
```

### Error Handling

```rust
// Use thiserror for error types
#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("key not found: {0}")]
    KeyNotFound(String),

    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
}

// Use anyhow for application code
fn main() -> anyhow::Result<()> {
    let db = Database::open("./data")?;
    Ok(())
}
```

### Testing

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_operations() {
        let db = Database::open_temp().unwrap();
        db.put(b"key", b"value").unwrap();
        assert_eq!(db.get(b"key").unwrap(), Some(b"value".to_vec()));
    }

    #[test]
    fn test_error_case() {
        let db = Database::open_temp().unwrap();
        assert!(db.get(b"nonexistent").unwrap().is_none());
    }
}
```

## Architecture Decisions

Major changes should go through the RFC process:

1. Open a discussion with your proposal
2. Get feedback from maintainers
3. Write an RFC document in `design/rfcs/`
4. Get approval before implementation

## Getting Help

- [:material-chat: GitHub Discussions](https://github.com/alopex-db/alopex/discussions) - Questions and ideas
- [:material-bug: Issues](https://github.com/alopex-db/alopex/issues) - Bug reports

## Recognition

Contributors are recognized in:

- `CONTRIBUTORS.md` file
- Release notes
- Project documentation

Thank you for contributing to Alopex DB! :fox_face:

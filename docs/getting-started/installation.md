---
title: Installation
description: Detailed installation guide for Alopex DB
---

# Installation

This guide covers all installation methods for Alopex DB.

## System Requirements

| Requirement | Minimum | Recommended |
|:------------|:--------|:------------|
| **Rust** | 1.75+ | 1.90+ (toolchain) |
| **Memory** | 256 MB | 1 GB+ |
| **Disk** | 100 MB | Depends on data |
| **OS** | Linux, macOS, Windows | Linux (Ubuntu 22.04+) |

## Installation Methods

### As a Library (Embedded Mode)

Add Alopex to your Rust project:

=== "Cargo.toml"

    ```toml
    [dependencies]
    alopex-embedded = "0.3"
    alopex-sql = "0.3"
    ```

=== "Cargo CLI"

    ```bash
    cargo add alopex-embedded alopex-sql
    ```

### From Source

Clone and build from source:

```bash
# Clone the repository
git clone https://github.com/alopex-db/alopex.git
cd alopex

# Build all crates
cargo build --release

# Run tests
cargo test

# Install CLI tools (optional)
cargo install --path alopex-cli
```

### Feature Flags

| Feature | Description | Default |
|:--------|:------------|:--------|
| `hnsw` | Enable HNSW vector indexing | :white_check_mark: |
| `compression` | Enable data compression | :white_check_mark: |
| `metrics` | Prometheus metrics export | :x: |
| `tracing` | Distributed tracing support | :x: |

```toml
[dependencies]
alopex-embedded = { version = "0.3", features = ["hnsw", "metrics"] }
alopex-sql = "0.3"
```

## Platform-Specific Notes

### Linux

No additional dependencies required. For optimal performance:

```bash
# Increase file descriptor limits
ulimit -n 65536

# Enable huge pages (optional, for large datasets)
sudo sysctl -w vm.nr_hugepages=1024
```

### macOS

Works out of the box with Xcode Command Line Tools:

```bash
xcode-select --install
```

### Windows

Requires Visual Studio Build Tools:

1. Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
2. Install "Desktop development with C++"
3. Restart terminal and build

### WebAssembly

For browser deployments:

```bash
# Install wasm-pack
cargo install wasm-pack

# Build for WASM
wasm-pack build --target web alopex-wasm
```

## Verifying Installation

```bash
# Check version
alopex --version

# Run built-in tests
alopex test

# Quick benchmark
alopex bench --quick
```

## Troubleshooting

??? question "Build fails with 'linker not found'"

    Install the C toolchain for your platform:

    - **Ubuntu/Debian**: `sudo apt install build-essential`
    - **macOS**: `xcode-select --install`
    - **Windows**: Install Visual Studio Build Tools

??? question "Out of memory during build"

    Reduce parallel jobs:

    ```bash
    cargo build --release -j 2
    ```

??? question "Permission denied on Linux"

    Check file system permissions:

    ```bash
    # Data directory needs write access
    chmod 755 /path/to/data
    ```

## Next Steps

- [:octicons-arrow-right-24: Quick Start Guide](quickstart.md)
- [:octicons-arrow-right-24: Configuration Reference](../concepts/overview.md)

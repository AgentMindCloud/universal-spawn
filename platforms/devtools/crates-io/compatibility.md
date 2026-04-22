# crates.io compatibility — field-by-field

| universal-spawn v1.0 field | crates.io behavior |
|---|---|
| `version` | Required. |
| `platforms.crates-io.crate_name` | Crate name. |
| `platforms.crates-io.edition` | Rust edition. |
| `platforms.crates-io.msrv` | Minimum supported Rust version. |
| `platforms.crates-io.shape` | `library`, `bin`, `both`. |
| `platforms.crates-io.features` | Named features. |

## Coexistence with `Cargo.toml`

universal-spawn does NOT replace Cargo.toml. Both files coexist; consumers read both and warn on conflicts.

### `Cargo.toml` (provider-native)

```toml
[package]
name = "your_crate"
version = "0.1.0"
edition = "2021"
rust-version = "1.78"
description = "Your crate"
license = "Apache-2.0"

[features]
default = []
serde = ["dep:serde"]

[dependencies]
```

### `universal-spawn.yaml` (platforms.crates-io block)

```yaml
platforms:
  crates-io:
    crate_name: your_crate
    edition: "2021"
    msrv: "1.78"
    shape: library
    features: [default, serde]
```

## Additive — not a replacement

`Cargo.toml` keeps ownership of `dependencies`, `features` implementations, `[[bin]]` / `[lib]`, workspace config, and Cargo-specific metadata. universal-spawn just mirrors the cross-platform-relevant subset.

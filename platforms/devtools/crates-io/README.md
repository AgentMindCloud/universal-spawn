# crates.io — universal-spawn platform extension

A universal-spawn manifest does NOT replace `Cargo.toml`. Cargo owns dependencies, features, binary targets, and `[[bin]]` / `[lib]` definitions. `platforms.crates-io` is additive cross-platform metadata.

## What this platform cares about

The crate name, edition, MSRV, and whether the crate ships a library, a binary, or both.

## Compatibility table

| Manifest field | crates.io behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`. |
| `platforms.crates-io` | Strict. |

### `platforms.crates-io` fields

| Field | Purpose |
|---|---|
| `platforms.crates-io.crate_name` | Crate name. |
| `platforms.crates-io.edition` | Rust edition. |
| `platforms.crates-io.msrv` | MSRV. |
| `platforms.crates-io.shape` | `library`, `bin`, `both`. |
| `platforms.crates-io.features` | Named features. |

See [`compatibility.md`](./compatibility.md) for more.

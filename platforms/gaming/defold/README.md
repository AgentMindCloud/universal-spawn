# Defold — universal-spawn platform extension

Defold projects are described by `game.project`. Native extensions ship as separate manifests. A universal-spawn manifest picks `kind` and pins the engine version + target platforms.

## What this platform cares about

The `kind` (`project`, `extension`), engine version, and target platforms.

## Compatibility table

| Manifest field | Defold behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `extension`. |
| `platforms.defold` | Strict. |

### `platforms.defold` fields

| Field | Purpose |
|---|---|
| `platforms.defold.kind` | `project` or `extension`. |
| `platforms.defold.engine_version` | Defold engine version. |
| `platforms.defold.target_platforms` | Target platforms. |
| `platforms.defold.entry_collection` | Entry collection. |

See [`compatibility.md`](./compatibility.md) for more.

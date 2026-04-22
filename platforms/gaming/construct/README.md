# Construct — universal-spawn platform extension

Construct (Construct 3) ships projects as `.c3p` archives. A universal-spawn manifest pins the project file and the export targets.

## What this platform cares about

.c3p file path and export targets.

## Compatibility table

| Manifest field | Construct behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `creative-tool`. |
| `platforms.construct` | Strict. |

### `platforms.construct` fields

| Field | Purpose |
|---|---|
| `platforms.construct.project_file` | .c3p file. |
| `platforms.construct.exports` | Export targets. |

See [`compatibility.md`](./compatibility.md) for more.

# GDevelop — universal-spawn platform extension

GDevelop projects ship as `game.json`. A universal-spawn manifest pins the project file and the export targets.

## What this platform cares about

game.json path and export targets.

## Compatibility table

| Manifest field | GDevelop behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `creative-tool`. |
| `platforms.gdevelop` | Strict. |

### `platforms.gdevelop` fields

| Field | Purpose |
|---|---|
| `platforms.gdevelop.project_file` | game.json path. |
| `platforms.gdevelop.exports` | Export targets. |
| `platforms.gdevelop.engine_version` | Engine version. |

See [`compatibility.md`](./compatibility.md) for more.

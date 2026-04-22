# Rhinoceros 3D — universal-spawn platform extension

Rhino ships .rhp plugins, Grasshopper `.gh` definitions, and Yak packages for Food4Rhino distribution. A universal-spawn manifest targets one of those shapes.

## What this platform cares about

The `kind` (`rhp-plugin`, `grasshopper`, `yak-package`), the Rhino version range, and the entry file.

## Compatibility table

| Manifest field | Rhinoceros 3D behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `plugin`, `design-template`. |
| `platforms.rhinoceros` | Strict. |

### `platforms.rhinoceros` fields

| Field | Purpose |
|---|---|
| `platforms.rhinoceros.kind` | `rhp-plugin`, `grasshopper`, `yak-package`. |
| `platforms.rhinoceros.min_version` | Minimum Rhino version. |
| `platforms.rhinoceros.entry_file` | Entry file path. |
| `platforms.rhinoceros.yak` | Yak package manifest settings. |

See [`compatibility.md`](./compatibility.md) for more.

# Cinema 4D — universal-spawn platform extension

Cinema 4D runs Python-scripted generators, Python Tags, and ships asset libraries as `.lib4d` archives. A universal-spawn manifest targets one of those shapes plus the C4D version range.

## What this platform cares about

The `kind` (`plugin`, `scene`, `asset-library`), the minimum Cinema 4D version, and the entry file.

## Compatibility table

| Manifest field | Cinema 4D behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `design-template`, `plugin`. |
| `platforms.cinema4d` | Strict. |

### `platforms.cinema4d` fields

| Field | Purpose |
|---|---|
| `platforms.cinema4d.kind` | `plugin`, `scene`, or `asset-library`. |
| `platforms.cinema4d.min_version` | Minimum Cinema 4D version. |
| `platforms.cinema4d.entry_file` | Entry file. |

See [`compatibility.md`](./compatibility.md) for more.

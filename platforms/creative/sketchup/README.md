# SketchUp — universal-spawn platform extension

SketchUp ships Ruby extensions (RBZ archives) and reusable components (.skp). A universal-spawn manifest points at one.

## What this platform cares about

The `kind` (`rbz-extension`, `component`), the minimum SketchUp year, and the entry file.

## Compatibility table

| Manifest field | SketchUp behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `plugin`, `design-template`. |
| `platforms.sketchup` | Strict. |

### `platforms.sketchup` fields

| Field | Purpose |
|---|---|
| `platforms.sketchup.kind` | `rbz-extension`, `component`. |
| `platforms.sketchup.min_year` | Minimum SketchUp year (e.g. 2024). |
| `platforms.sketchup.entry_file` | Entry file path. |
| `platforms.sketchup.extension_warehouse` | Extension Warehouse settings. |

See [`compatibility.md`](./compatibility.md) for more.

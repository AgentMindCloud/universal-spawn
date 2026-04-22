# Blender — universal-spawn platform extension

Blender ships a vast Python add-on ecosystem plus .blend files that act as projects and asset libraries. The extension captures the `kind`, the entry Python module (for add-ons), and the asset library path (for libraries).

## What this platform cares about

The `kind` (`addon`, `project`, `asset-library`), the Blender version range, and the entry point for each kind.

## Compatibility table

| Manifest field | Blender behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `design-template`, `extension`. |
| `platforms.blender` | Strict. |

### `platforms.blender` fields

| Field | Purpose |
|---|---|
| `platforms.blender.kind` | `addon`, `project`, `asset-library`. |
| `platforms.blender.blender_version` | Minimum Blender version. |
| `platforms.blender.entry_module` | `__init__.py` for add-ons. |
| `platforms.blender.entry_blend` | `.blend` file for projects. |
| `platforms.blender.asset_library_path` | Directory for asset libraries. |
| `platforms.blender.render_engine` | `cycles`, `eevee`, or `workbench`. |

See [`compatibility.md`](./compatibility.md) for more.

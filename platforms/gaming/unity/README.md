# Unity (gaming) — universal-spawn platform extension

Unity creations split between Asset Store packages (drop into an existing project) and full project templates (start a new project from). A universal-spawn manifest picks one with `kind` and pins the editor + render-pipeline range.

## What this platform cares about

The `kind` (`asset-store-package`, `project-template`), the minimum Unity editor, the render pipeline, and Asset Store category for asset-store entries.

## Compatibility table

| Manifest field | Unity (gaming) behavior |
|---|---|
| `version` | Required. |
| `type` | `game-mod`, `game-world`, `creative-tool`, `extension`. |
| `platforms.unity` | Strict. |

### `platforms.unity` fields

| Field | Purpose |
|---|---|
| `platforms.unity.kind` | `asset-store-package` or `project-template`. |
| `platforms.unity.min_editor` | Minimum Unity editor. |
| `platforms.unity.render_pipeline` | `built-in`, `urp`, `hdrp`. |
| `platforms.unity.entry_scene` | Entry scene file. |
| `platforms.unity.asset_store_category` | Asset Store category. |
| `platforms.unity.upm_packages` | Required UPM packages. |

See [`compatibility.md`](./compatibility.md) for more.

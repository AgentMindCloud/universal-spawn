# PlayCanvas — universal-spawn platform extension

PlayCanvas hosts WebGL projects in the cloud editor. A universal-spawn manifest pins the project id, the published scene, and the engine version.

## What this platform cares about

Project id, published scene id, engine version, and the Editor URL.

## Compatibility table

| Manifest field | PlayCanvas behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `creative-tool`, `web-app`. |
| `platforms.playcanvas` | Strict. |

### `platforms.playcanvas` fields

| Field | Purpose |
|---|---|
| `platforms.playcanvas.project_id` | PlayCanvas project id. |
| `platforms.playcanvas.scene_id` | Default scene id. |
| `platforms.playcanvas.engine_version` | Engine version. |
| `platforms.playcanvas.editor_url` | Editor URL. |

See [`compatibility.md`](./compatibility.md) for more.

# Paperspace — universal-spawn platform extension

Paperspace (DigitalOcean) hosts Gradient notebooks, deployments, and standalone Machines. A universal-spawn manifest pins the surface and the GPU class.

## What this platform cares about

The `surface` (`gradient-notebook`, `gradient-deployment`, `machine`), the GPU class, and the team / project ids.

## Compatibility table

| Manifest field | Paperspace behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `workflow`, `container`. |
| `platforms.paperspace` | Strict. |

### `platforms.paperspace` fields

| Field | Purpose |
|---|---|
| `platforms.paperspace.surface` | Surface kind. |
| `platforms.paperspace.gpu` | GPU class. |
| `platforms.paperspace.team_id` | Team id. |
| `platforms.paperspace.project_id` | Project id. |
| `platforms.paperspace.image` | Container image. |

See [`compatibility.md`](./compatibility.md) for more.

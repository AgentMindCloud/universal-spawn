# Gitpod — universal-spawn platform extension

Gitpod runs ephemeral cloud workspaces driven by `.gitpod.yml`. A universal-spawn manifest pins the workspace image, the tasks Gitpod runs at start, and the Gitpod Flex tier.

## What this platform cares about

The image, tasks list (init / command), exposed ports, and the workspace tier.

## Compatibility table

| Manifest field | Gitpod behavior |
|---|---|
| `version` | Required. |
| `type` | `container`, `web-app`, `workflow`. |
| `platforms.gitpod` | Strict. |

### `platforms.gitpod` fields

| Field | Purpose |
|---|---|
| `platforms.gitpod.image` | Workspace image. |
| `platforms.gitpod.tasks` | Start-up tasks. |
| `platforms.gitpod.ports` | Port config. |
| `platforms.gitpod.tier` | Workspace tier. |
| `platforms.gitpod.tools` | Pre-installed tools. |

See [`compatibility.md`](./compatibility.md) for more.

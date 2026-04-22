# GitHub Codespaces — universal-spawn platform extension

Codespaces is GitHub's hosted Dev Containers runtime. A universal-spawn manifest pins the devcontainer file, the default machine class, and any prebuild settings.

## What this platform cares about

The devcontainer file path, the default machine class, prebuild config, and forwarded ports.

## Compatibility table

| Manifest field | GitHub Codespaces behavior |
|---|---|
| `version` | Required. |
| `type` | `container`, `web-app`, `workflow`. |
| `platforms.codespaces` | Strict. |

### `platforms.codespaces` fields

| Field | Purpose |
|---|---|
| `platforms.codespaces.devcontainer` | devcontainer.json path. |
| `platforms.codespaces.machine` | Machine class. |
| `platforms.codespaces.prebuild` | Prebuild trigger. |
| `platforms.codespaces.forward_ports` | Auto-forwarded ports. |
| `platforms.codespaces.region` | Suggested region. |

See [`compatibility.md`](./compatibility.md) for more.

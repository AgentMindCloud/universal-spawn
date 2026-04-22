# Docker — universal-spawn platform extension

Docker deployments split cleanly between single-container images built from a Dockerfile and Compose-orchestrated multi-container stacks. A universal-spawn manifest picks exactly one via `kind`.

## What this platform cares about

The `kind` (`single-container`, `compose`), the Dockerfile path, the Compose file path, the registry target, and the platforms to build for (`linux/amd64`, `linux/arm64`, `...`).

## Compatibility table

| Manifest field | Docker behavior |
|---|---|
| `version` | Required. |
| `type` | `container`, `web-app`, `api-service`, `workflow`, `bot`. |
| `platforms.docker` | Strict. |

### `platforms.docker` fields

| Field | Purpose |
|---|---|
| `platforms.docker.kind` | `single-container` or `compose`. |
| `platforms.docker.dockerfile` | Dockerfile path. |
| `platforms.docker.compose_file` | Compose file path. |
| `platforms.docker.image` | Image reference. |
| `platforms.docker.build_platforms` | buildx target platforms. |
| `platforms.docker.build_args` | Build args. |
| `platforms.docker.registry` | Registry host. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

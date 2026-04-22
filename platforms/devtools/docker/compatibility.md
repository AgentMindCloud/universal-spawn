# Docker compatibility — field-by-field

| universal-spawn v1.0 field | Docker behavior |
|---|---|
| `version` | Required. |
| `platforms.docker.kind` | `single-container` or `compose`. |
| `platforms.docker.dockerfile` | Dockerfile path. |
| `platforms.docker.compose_file` | Compose file path. |
| `platforms.docker.image` | Image reference (registry/name:tag). |
| `platforms.docker.build_platforms` | buildx target platforms. |
| `platforms.docker.build_args` | Build args map. |
| `platforms.docker.registry` | Registry (`docker.io`, `ghcr.io`, `mcr.microsoft.com`). |

## Coexistence with `Dockerfile + compose.yaml`

universal-spawn does NOT replace Dockerfile + compose.yaml. Both files coexist; consumers read both and warn on conflicts.

### `Dockerfile + compose.yaml` (provider-native)

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build
CMD ["node", "dist/server.js"]
```

### `universal-spawn.yaml` (platforms.docker block)

```yaml
platforms:
  docker:
    kind: single-container
    dockerfile: Dockerfile
    image: ghcr.io/yourhandle/your-app:latest
    build_platforms: [linux/amd64, linux/arm64]
    registry: ghcr.io
```

## Compose vs single-container

`single-container` manifests point at exactly one Dockerfile and one resulting image. `compose` manifests point at a `compose.yaml` and expect a consumer to run `docker compose up`. A universal-spawn consumer SHOULD refuse to spawn a `compose` manifest on a host that has no Compose runtime.

"""Docker — Dockerfile + Compose."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "docker",
    "title": "Docker",
    "lede": (
        "Docker deployments split cleanly between single-container "
        "images built from a Dockerfile and Compose-orchestrated "
        "multi-container stacks. A universal-spawn manifest picks "
        "exactly one via `kind`."
    ),
    "cares": (
        "The `kind` (`single-container`, `compose`), the Dockerfile "
        "path, the Compose file path, the registry target, and the "
        "platforms to build for (`linux/amd64`, `linux/arm64`, `...`)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`container`, `web-app`, `api-service`, `workflow`, `bot`."),
        ("platforms.docker", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.docker.kind", "`single-container` or `compose`."),
        ("platforms.docker.dockerfile", "Dockerfile path."),
        ("platforms.docker.compose_file", "Compose file path."),
        ("platforms.docker.image", "Image reference (registry/name:tag)."),
        ("platforms.docker.build_platforms", "buildx target platforms."),
        ("platforms.docker.build_args", "Build args map."),
        ("platforms.docker.registry", "Registry (`docker.io`, `ghcr.io`, `mcr.microsoft.com`)."),
    ],
    "platform_fields": {
        "kind": "`single-container` or `compose`.",
        "dockerfile": "Dockerfile path.",
        "compose_file": "Compose file path.",
        "image": "Image reference.",
        "build_platforms": "buildx target platforms.",
        "build_args": "Build args.",
        "registry": "Registry host.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["single-container", "compose"]),
            "dockerfile": str_prop(),
            "compose_file": str_prop(),
            "image": str_prop(),
            "build_platforms": {
                "type": "array",
                "items": enum(["linux/amd64", "linux/arm64", "linux/arm/v7", "linux/386", "linux/ppc64le", "linux/riscv64", "linux/s390x"]),
            },
            "build_args": {"type": "object", "additionalProperties": {"type": "string"}},
            "registry": enum(["docker.io", "ghcr.io", "mcr.microsoft.com", "quay.io", "registry.gitlab.com", "private"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Docker Template
type: container
description: Template for a Docker-targeted universal-spawn manifest.

platforms:
  docker:
    kind: single-container
    dockerfile: Dockerfile
    image: ghcr.io/yourhandle/your-app:latest
    build_platforms: [linux/amd64, linux/arm64]
    registry: ghcr.io

safety:
  min_permissions: [network:outbound]

env_vars_required: []

deployment:
  targets: [docker]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/docker-template }
""",
    "native_config_name": "Dockerfile + compose.yaml",
    "native_config_lang": "dockerfile",
    "native_config": """
FROM node:22-alpine
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build
CMD ["node", "dist/server.js"]
""",
    "universal_excerpt": """
platforms:
  docker:
    kind: single-container
    dockerfile: Dockerfile
    image: ghcr.io/yourhandle/your-app:latest
    build_platforms: [linux/amd64, linux/arm64]
    registry: ghcr.io
""",
    "compatibility_extras": (
        "## Compose vs single-container\n\n"
        "`single-container` manifests point at exactly one Dockerfile "
        "and one resulting image. `compose` manifests point at a "
        "`compose.yaml` and expect a consumer to run `docker compose "
        "up`. A universal-spawn consumer SHOULD refuse to spawn a "
        "`compose` manifest on a host that has no Compose runtime."
    ),
    "perks": STANDARD_PERKS,
    "examples": {
        "single-container": """
version: "1.0"
name: Parchment API Image
type: container
summary: Minimal single-container manifest for a Node API image.
description: Build-and-publish a Node 22 Alpine image for amd64 + arm64 to GHCR.

platforms:
  docker:
    kind: single-container
    dockerfile: Dockerfile
    image: ghcr.io/plate-studio/parchment-api:latest
    build_platforms: [linux/amd64, linux/arm64]
    registry: ghcr.io

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: false

env_vars_required:
  - name: API_SECRET
    description: API secret at runtime.
    secret: true

deployment:
  targets: [docker]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-api-image }
  id: com.plate-studio.parchment-api-image
""",
        "compose": """
version: "1.0"
name: Plate Stack Compose
type: container
summary: Full Compose stack — web + worker + Postgres + Redis.
description: docker-compose.yaml with four services. Pairs with the Dockerfile of the web service.

platforms:
  docker:
    kind: compose
    compose_file: compose.yaml
    build_platforms: [linux/amd64, linux/arm64]
    registry: ghcr.io

safety:
  min_permissions: [network:inbound, network:outbound, fs:write]
  safe_for_auto_spawn: false

env_vars_required:
  - name: POSTGRES_PASSWORD
    description: Postgres password.
    secret: true
  - name: REDIS_PASSWORD
    description: Redis password.
    secret: true

deployment:
  targets: [docker]

metadata:
  license: Apache-2.0
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/plate-stack-compose }
  id: com.stack-co.plate-stack-compose
""",
    },
}

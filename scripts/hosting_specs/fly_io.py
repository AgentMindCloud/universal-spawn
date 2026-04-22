"""Fly.io — fly.toml + `fly launch`."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "fly-io",
    "title": "Fly.io",
    "native_config_name": "fly.toml",
    "native_config_lang": "toml",

    "lede": (
        "Fly.io runs your Dockerfile as Firecracker microVMs, globally "
        "distributed, with anycast networking and built-in Postgres / "
        "Redis-compatible storage. The extension describes the VM "
        "size, regions, services, mounts, and any required app-level "
        "secrets."
    ),
    "cares": (
        "The app name (fly-unique), primary region, per-machine VM "
        "size, HTTP services (ports, TLS, auto-stop), and mounted "
        "volumes."
    ),
    "extras": (
        "`http_service` maps the primary HTTP port with TLS + force "
        "HTTPS. `mounts[]` attaches persistent volumes. `processes[]` "
        "runs multiple entry commands from the same image."
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Fly app card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Fly secrets."),
        ("deployment.targets", "Must include `fly-io`."),
        ("platforms.fly-io", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Fly app-name suggestion."),
        ("name, description", "Card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("safety.min_permissions", "Informational."),
        ("safety.cost_limit_usd_daily", "Advisory; Fly has its own spend guardrails."),
        ("env_vars_required", "`fly secrets set`."),
        ("platforms.fly-io.app", "App name."),
        ("platforms.fly-io.primary_region", "Primary region."),
        ("platforms.fly-io.regions", "Replica regions."),
        ("platforms.fly-io.vm", "VM size."),
        ("platforms.fly-io.http_service", "HTTP service ports + TLS."),
        ("platforms.fly-io.mounts", "Volume mounts."),
        ("platforms.fly-io.processes", "Process group commands."),
        ("platforms.fly-io.healthcheck", "HTTP healthcheck."),
    ],
    "platform_fields": {
        "app": "App name.",
        "primary_region": "Primary region.",
        "regions": "Replica regions.",
        "vm": "VM size.",
        "http_service": "HTTP service port / TLS / auto-stop.",
        "mounts": "Persistent volume mounts.",
        "processes": "Process group commands.",
        "healthcheck": "HTTP healthcheck.",
    },

    "schema_body": schema_object(
        required=["app", "primary_region"],
        properties={
            "app": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            "primary_region": str_prop(pattern=r"^[a-z]{3}$"),
            "regions": {
                "type": "array",
                "items": {"type": "string", "pattern": r"^[a-z]{3}$"},
            },
            "vm": schema_object(
                properties={
                    "size": enum(["shared-cpu-1x", "shared-cpu-2x", "shared-cpu-4x", "shared-cpu-8x",
                                  "performance-1x", "performance-2x", "performance-4x", "performance-8x",
                                  "a100-40gb", "a100-80gb", "l40s"]),
                    "memory_mb": {"type": "integer", "minimum": 256, "maximum": 524288},
                },
            ),
            "http_service": schema_object(
                properties={
                    "internal_port": {"type": "integer", "minimum": 1, "maximum": 65535},
                    "force_https": bool_prop(True),
                    "auto_stop_machines": bool_prop(True),
                    "auto_start_machines": bool_prop(True),
                    "min_machines_running": {"type": "integer", "minimum": 0, "maximum": 200},
                },
            ),
            "mounts": {
                "type": "array",
                "items": schema_object(
                    required=["source", "destination"],
                    properties={
                        "source": str_prop(),
                        "destination": str_prop(),
                        "size_gb": {"type": "integer", "minimum": 1, "maximum": 4096},
                    },
                ),
            },
            "processes": {
                "type": "object",
                "additionalProperties": {"type": "string"},
            },
            "healthcheck": schema_object(
                properties={
                    "path": str_prop(),
                    "interval_seconds": {"type": "integer", "minimum": 1},
                    "timeout_seconds": {"type": "integer", "minimum": 1},
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Fly.io Template
type: api-service
description: Template for a Fly.io-targeted universal-spawn manifest.

platforms:
  fly-io:
    app: your-app
    primary_region: iad
    regions: [iad, cdg, syd]
    vm: { size: shared-cpu-1x, memory_mb: 512 }
    http_service:
      internal_port: 8080
      force_https: true
      auto_stop_machines: true
      auto_start_machines: true
      min_machines_running: 0
    healthcheck: { path: /healthz, interval_seconds: 10, timeout_seconds: 5 }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true

deployment:
  targets: [fly-io]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/fly-template }
""",

    "native_config": """
app = "your-app"
primary_region = "iad"

[build]
  dockerfile = "Dockerfile"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  size = "shared-cpu-1x"
  memory = "512mb"

[[mounts]]
  source = "data"
  destination = "/data"
""",

    "universal_excerpt": """
platforms:
  fly-io:
    app: your-app
    primary_region: iad
    vm: { size: shared-cpu-1x, memory_mb: 512 }
    http_service:
      internal_port: 8080
      force_https: true
      auto_stop_machines: true
      auto_start_machines: true
      min_machines_running: 0
    mounts:
      - { source: data, destination: /data, size_gb: 1 }
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`fly.toml`** for `[build]` args, `[env]` (non-secret), "
        "`[metrics]`, `[statics]`, and machine-level settings (kernel, "
        "swap).\n"
        "- Use **`universal-spawn.yaml`** for the manifest-level "
        "safety, secrets, and cross-platform siblings.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy on Fly.io](https://fly.io/static/images/launch/deploy.svg)]"
            "(https://fly.io/launch?repo=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://fly.io/launch?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://fly.io/static/images/launch/deploy.svg" alt="Deploy on Fly.io" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Fly launch URL accepts:\n\n"
            "- `repo` — URL-encoded git repo URL.\n"
            "- `name` — suggested app name.\n"
            "- `region` — primary region (e.g. `iad`, `cdg`, `syd`).\n\n"
            "Generators MAY fill `name` from `platforms.fly-io.app` and "
            "`region` from `platforms.fly-io.primary_region`."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Region fan-out** — `regions[]` pre-schedules replica "
        "machines; `min_machines_running: 0` enables the pay-when-busy "
        "auto-scaling model.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Fly Static Site
type: site
summary: Minimal static site on Fly.io via an nginx container.
description: Dockerfile-packaged nginx serving static assets. Primary region only.

platforms:
  fly-io:
    app: static-site
    primary_region: iad
    vm: { size: shared-cpu-1x, memory_mb: 256 }
    http_service:
      internal_port: 80
      force_https: true
      auto_stop_machines: true
      auto_start_machines: true
      min_machines_running: 0

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [fly-io]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/fly-static }
  id: com.static-co.fly-static
""",
        "serverless-api": """
version: \"1.0\"
name: Fly Multi-Region API
type: api-service
summary: Global HTTP API on Fly.io spread across three regions.
description: >
  Stateless JSON API deployed in three regions, auto-starting machines
  on first request, stopping after idle.

platforms:
  fly-io:
    app: edge-api
    primary_region: iad
    regions: [iad, cdg, syd]
    vm: { size: performance-1x, memory_mb: 1024 }
    http_service:
      internal_port: 8080
      force_https: true
      auto_stop_machines: true
      auto_start_machines: true
      min_machines_running: 1
    healthcheck: { path: /healthz, interval_seconds: 10, timeout_seconds: 3 }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 200

env_vars_required:
  - name: API_SECRET
    description: Shared secret for signed routes.
    secret: true

deployment:
  targets: [fly-io]

metadata:
  license: Apache-2.0
  author: { name: Edge Co., handle: edge-co }
  source: { type: git, url: https://github.com/edge-co/fly-edge-api }
  id: com.edge-co.fly-edge-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Fly Full Stack
type: web-app
summary: Full-stack SvelteKit + Postgres app on Fly.io with mounted volume.
description: >
  SvelteKit app packaged via Dockerfile. Uses a Fly Postgres cluster
  (provisioned separately) connected via DATABASE_URL. A mounted volume
  holds user uploads. Two process groups — one web, one worker.

platforms:
  fly-io:
    app: full-stack
    primary_region: cdg
    regions: [cdg, iad]
    vm: { size: shared-cpu-2x, memory_mb: 1024 }
    http_service:
      internal_port: 3000
      force_https: true
      auto_stop_machines: false
      auto_start_machines: true
      min_machines_running: 2
    mounts:
      - { source: uploads, destination: /data/uploads, size_gb: 10 }
    processes:
      web: \"node build/index.js\"
      worker: \"node build/worker.js\"
    healthcheck: { path: /healthz, interval_seconds: 10, timeout_seconds: 5 }

safety:
  min_permissions:
    - network:inbound
    - network:outbound
    - fs:write:/data
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Fly Postgres connection string.
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true

deployment:
  targets: [fly-io]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/fly-full-stack }
  id: com.stack-co.fly-full-stack
""",
    },
}

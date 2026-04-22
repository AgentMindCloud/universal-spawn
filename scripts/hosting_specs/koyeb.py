"""Koyeb — global serverless containers."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "koyeb",
    "title": "Koyeb",
    "native_config_name": "koyeb.yaml",
    "native_config_lang": "yaml",

    "lede": (
        "Koyeb runs containers globally with automatic scaling and "
        "geo-routing. The extension captures the service kind, the "
        "build source (git or Docker image), regions, instance type, "
        "and scale settings."
    ),
    "cares": (
        "The build source (`git`, `docker`), the regions list, the "
        "instance type, port routing, and autoscaling bounds."
    ),
    "extras": (
        "`autoscaling.targets[]` sets CPU / RPS / concurrent_request "
        "targets; Koyeb scales between `min` and `max` to hold them."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`."),
        ("env_vars_required", "Koyeb secrets."),
        ("deployment.targets", "Must include `koyeb`."),
        ("platforms.koyeb", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "App-name suggestion."),
        ("name, description", "Card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Koyeb secrets."),
        ("platforms.koyeb.service_kind", "`web`, `worker`."),
        ("platforms.koyeb.build", "`git` or `docker`."),
        ("platforms.koyeb.regions", "Regions list."),
        ("platforms.koyeb.instance_type", "Instance type."),
        ("platforms.koyeb.ports", "HTTP port routing."),
        ("platforms.koyeb.autoscaling", "Autoscaling bounds + targets."),
    ],
    "platform_fields": {
        "service_kind": "`web` or `worker`.",
        "build": "Build source.",
        "regions": "Regions list.",
        "instance_type": "Instance type.",
        "ports": "HTTP port routing.",
        "autoscaling": "Autoscaling config.",
    },

    "schema_body": schema_object(
        required=["service_kind", "build", "regions"],
        properties={
            "service_kind": enum(["web", "worker"]),
            "build": schema_object(
                required=["kind"],
                properties={
                    "kind": enum(["git", "docker"]),
                    "image": str_prop(),
                    "build_command": str_prop(),
                    "run_command": str_prop(),
                },
            ),
            "regions": {
                "type": "array",
                "minItems": 1,
                "items": enum(["fra", "par", "was", "sfo", "sin", "tyo"]),
            },
            "instance_type": enum(["free", "eco-nano", "eco-micro", "eco-small", "eco-medium", "nano", "micro", "small", "medium", "large", "xlarge", "2xlarge", "gpu-nvidia-a100"]),
            "ports": {
                "type": "array",
                "items": schema_object(
                    required=["port"],
                    properties={
                        "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                        "protocol": enum(["http", "http2", "tcp"]),
                        "path": str_prop(),
                    },
                ),
            },
            "autoscaling": schema_object(
                properties={
                    "min": {"type": "integer", "minimum": 0, "maximum": 100},
                    "max": {"type": "integer", "minimum": 1, "maximum": 100},
                    "targets": schema_object(
                        properties={
                            "cpu_percent": {"type": "integer", "minimum": 1, "maximum": 95},
                            "requests_per_second": {"type": "integer", "minimum": 1, "maximum": 10000},
                            "concurrent_requests": {"type": "integer", "minimum": 1, "maximum": 10000},
                        },
                    ),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Koyeb Template
type: web-app
description: Template for a Koyeb-targeted universal-spawn manifest.

platforms:
  koyeb:
    service_kind: web
    build: { kind: git, build_command: \"pnpm build\", run_command: \"pnpm start\" }
    regions: [fra, was]
    instance_type: nano
    ports:
      - { port: 8080, protocol: http, path: / }
    autoscaling:
      min: 1
      max: 5
      targets: { cpu_percent: 80 }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: API_SECRET
    description: API signing secret.
    secret: true

deployment:
  targets: [koyeb]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/koyeb-template }
""",

    "native_config": """
name: your-app
service:
  type: web
  regions: [fra, was]
  instance_type: nano
  ports:
    - port: 8080
      protocol: http
      path: /
  autoscaling:
    min: 1
    max: 5
    targets:
      cpu: { value: 80 }
""",

    "universal_excerpt": """
platforms:
  koyeb:
    service_kind: web
    build: { kind: git, build_command: \"pnpm build\", run_command: \"pnpm start\" }
    regions: [fra, was]
    instance_type: nano
    ports:
      - { port: 8080, protocol: http, path: / }
    autoscaling: { min: 1, max: 5, targets: { cpu_percent: 80 } }
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": (
            "[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)]"
            "(https://app.koyeb.com/deploy?type=git&repository=github.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://app.koyeb.com/deploy?type=git&repository=github.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" />\n'
            '</a>'
        ),
        "params_doc": "The Koyeb deploy URL accepts `type`, `repository`, `branch`, and `env[KEY]=value` pairs.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: Koyeb Static
type: site
summary: Static site served from Koyeb via a nginx container.
description: Minimal Docker-built nginx serving static assets.

platforms:
  koyeb:
    service_kind: web
    build: { kind: docker, image: nginx:stable-alpine }
    regions: [fra]
    instance_type: free
    ports: [ { port: 80, protocol: http, path: / } ]

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [koyeb]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/koyeb-static }
  id: com.static-co.koyeb-static
""",
        "serverless-api": """
version: \"1.0\"
name: Koyeb Edge API
type: api-service
summary: Koyeb HTTP API across three regions with CPU-target autoscaling.
description: Node API. Three regions. 1-3 instances. CPU target 75%.

platforms:
  koyeb:
    service_kind: web
    build: { kind: git, build_command: \"pnpm build\", run_command: \"node dist/server.js\" }
    regions: [fra, was, sin]
    instance_type: nano
    ports: [ { port: 8080, protocol: http, path: / } ]
    autoscaling: { min: 1, max: 3, targets: { cpu_percent: 75 } }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: API_SECRET
    description: API secret.
    secret: true

deployment:
  targets: [koyeb]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/koyeb-edge-api }
  id: com.api-co.koyeb-edge-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Koyeb Full Stack
type: web-app
summary: Full-stack Koyeb deployment with a GPU worker sidecar.
description: >
  Web service + a GPU worker (A100) for ML post-processing. Demonstrates
  mixing instance types across sibling Koyeb services.

platforms:
  koyeb:
    service_kind: web
    build: { kind: docker, image: ghcr.io/stack-co/app:latest }
    regions: [fra]
    instance_type: medium
    ports: [ { port: 3000, protocol: http2, path: / } ]
    autoscaling: { min: 2, max: 10, targets: { concurrent_requests: 80 } }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true
  - name: SESSION_SECRET
    description: Session secret.
    secret: true

deployment:
  targets: [koyeb]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/koyeb-full-stack }
  id: com.stack-co.koyeb-full-stack
""",
    },
}

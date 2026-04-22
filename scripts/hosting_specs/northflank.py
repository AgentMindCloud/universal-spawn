"""Northflank — containers, jobs, addons (self-service Kubernetes)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "northflank",
    "title": "Northflank",
    "native_config_name": "northflank.yaml (Spec CLI)",
    "native_config_lang": "yaml",

    "lede": (
        "Northflank runs container services, cron jobs, pipelines, and "
        "managed databases on a self-service Kubernetes substrate. "
        "The extension captures the kind (combined service, deployment, "
        "job), build source, resources, and attached addons."
    ),
    "cares": (
        "The `kind` (`combined`, `deployment`, `job`), build + Docker "
        "settings, resources, ports, and addons (Postgres / MongoDB / "
        "MySQL / Redis / ClickHouse)."
    ),
    "extras": (
        "`addons[]` provisions managed services. `pipeline` captures "
        "the Northflank pipeline id this service is part of."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`."),
        ("env_vars_required", "Northflank secret groups."),
        ("deployment.targets", "Must include `northflank`."),
        ("platforms.northflank", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Project name suggestion."),
        ("name, description", "Card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secret groups."),
        ("platforms.northflank.kind", "`combined`, `deployment`, `job`."),
        ("platforms.northflank.build", "Git build configuration."),
        ("platforms.northflank.image", "Image reference when `kind: deployment`."),
        ("platforms.northflank.resources", "CPU + RAM allocation."),
        ("platforms.northflank.replicas", "Replica count."),
        ("platforms.northflank.ports", "HTTP ports."),
        ("platforms.northflank.addons", "Managed addons."),
        ("platforms.northflank.pipeline", "Pipeline id."),
        ("platforms.northflank.region", "Region."),
    ],
    "platform_fields": {
        "kind": "`combined`, `deployment`, `job`.",
        "build": "Git build configuration.",
        "image": "Image reference.",
        "resources": "CPU + RAM allocation.",
        "replicas": "Replica count.",
        "ports": "HTTP ports.",
        "addons": "Managed addons.",
        "pipeline": "Pipeline id.",
        "region": "Region.",
    },

    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["combined", "deployment", "job"]),
            "build": schema_object(
                properties={
                    "git_ref": str_prop(desc="Git branch, tag, or commit."),
                    "dockerfile_path": str_prop(),
                    "context_path": str_prop(),
                    "build_args": {"type": "array", "items": str_prop()},
                },
            ),
            "image": str_prop(),
            "resources": schema_object(
                properties={
                    "plan": enum(["nf-compute-10", "nf-compute-20", "nf-compute-50", "nf-compute-100", "nf-compute-200", "nf-compute-400", "nf-compute-gpu-small", "nf-compute-gpu-medium"]),
                    "storage_gb": {"type": "integer", "minimum": 1, "maximum": 2000},
                },
            ),
            "replicas": {"type": "integer", "minimum": 0, "maximum": 100},
            "ports": {
                "type": "array",
                "items": schema_object(
                    required=["port"],
                    properties={
                        "name": str_prop(),
                        "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                        "protocol": enum(["HTTP", "HTTP2", "TCP", "GRPC"]),
                        "public": bool_prop(True),
                    },
                ),
            },
            "addons": {
                "type": "array",
                "items": schema_object(
                    required=["kind"],
                    properties={
                        "kind": enum(["postgres", "mysql", "mongodb", "redis", "clickhouse"]),
                        "name": str_prop(),
                        "plan": str_prop(),
                    },
                ),
            },
            "pipeline": str_prop(),
            "region": str_prop(pattern=r"^[a-z0-9-]+$"),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Northflank Template
type: web-app
description: Template for a Northflank-targeted universal-spawn manifest.

platforms:
  northflank:
    kind: combined
    build: { git_ref: main, dockerfile_path: Dockerfile }
    resources: { plan: nf-compute-20 }
    replicas: 1
    ports:
      - { name: web, port: 8080, protocol: HTTP, public: true }
    addons:
      - { kind: postgres, name: db, plan: nf-compute-20 }
    region: europe-west

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the Postgres addon.
    secret: true

deployment:
  targets: [northflank]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/northflank-template }
""",

    "native_config": """
kind: Project
spec:
  name: your-app
services:
  - kind: CombinedService
    spec:
      name: web
      deployment: { instances: 1 }
      runtimeEnvironment: { DATABASE_URL: \"addon:db:connectionString\" }
      ports:
        - name: web
          internalPort: 8080
          protocol: HTTP
          public: true
addons:
  - kind: Addon
    spec:
      name: db
      type: postgres
      plan: nf-compute-20
""",

    "universal_excerpt": """
platforms:
  northflank:
    kind: combined
    build: { git_ref: main, dockerfile_path: Dockerfile }
    resources: { plan: nf-compute-20 }
    replicas: 1
    ports:
      - { name: web, port: 8080, protocol: HTTP, public: true }
    addons:
      - { kind: postgres, name: db, plan: nf-compute-20 }
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": "[![Deploy on Northflank](https://assets.northflank.com/deploy-on-northflank.svg)](https://app.northflank.com/s/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)",
        "html": (
            '<a href="https://app.northflank.com/s/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://assets.northflank.com/deploy-on-northflank.svg" alt="Deploy on Northflank" />\n'
            '</a>'
        ),
        "params_doc": "Northflank's deploy URL accepts `template` (URL-encoded git repo URL) and looks for a `northflank.yaml` at the repo root.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: Northflank Static Nginx
type: site
summary: Static site on Northflank via an nginx image.
description: Docker deployment of nginx:stable-alpine serving static assets.

platforms:
  northflank:
    kind: deployment
    image: nginx:stable-alpine
    resources: { plan: nf-compute-10 }
    replicas: 1
    ports:
      - { name: web, port: 80, protocol: HTTP, public: true }
    region: europe-west

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [northflank]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/nf-static }
  id: com.static-co.nf-static
""",
        "serverless-api": """
version: \"1.0\"
name: Northflank API and Job
type: api-service
summary: Combined service API plus a cron job on Northflank.
description: API web service plus a daily job that runs rollups.

platforms:
  northflank:
    kind: combined
    build: { git_ref: main, dockerfile_path: Dockerfile }
    resources: { plan: nf-compute-20 }
    replicas: 2
    ports:
      - { name: web, port: 8080, protocol: HTTP2, public: true }
    pipeline: main

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: API_SECRET
    description: API signing secret.
    secret: true

deployment:
  targets: [northflank]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/nf-api-and-job }
  id: com.api-co.nf-api-and-job
""",
        "full-stack-app": """
version: \"1.0\"
name: Northflank Full Stack
type: web-app
summary: Full-stack Northflank deployment with Postgres, Redis, and ClickHouse addons.
description: >
  Combined web service + three addons (Postgres primary, Redis cache,
  ClickHouse for analytics). Two replicas. GPU sidecar example omitted
  for brevity.

platforms:
  northflank:
    kind: combined
    build: { git_ref: main, dockerfile_path: Dockerfile }
    resources: { plan: nf-compute-100, storage_gb: 20 }
    replicas: 2
    ports:
      - { name: web, port: 3000, protocol: HTTP2, public: true }
    addons:
      - { kind: postgres,   name: db,    plan: nf-compute-50 }
      - { kind: redis,      name: cache, plan: nf-compute-20 }
      - { kind: clickhouse, name: ch,    plan: nf-compute-100 }
    pipeline: main
    region: europe-west

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true
  - name: REDIS_URL
    description: Redis URL.
    secret: true
  - name: CLICKHOUSE_URL
    description: ClickHouse URL.
    secret: true
  - name: SESSION_SECRET
    description: Session secret.
    secret: true

deployment:
  targets: [northflank]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/nf-full-stack }
  id: com.stack-co.nf-full-stack
""",
    },
}

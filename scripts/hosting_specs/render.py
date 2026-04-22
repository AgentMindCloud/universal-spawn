"""Render — PaaS with render.yaml blueprint."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "render",
    "title": "Render",
    "native_config_name": "render.yaml",
    "native_config_lang": "yaml",

    "lede": (
        "Render's Blueprint (`render.yaml`) declares an entire app — "
        "web services, background workers, cron jobs, static sites, "
        "managed Postgres, and Redis — in one file. The extension "
        "maps the Blueprint shape onto `platforms.render`."
    ),
    "cares": (
        "The services array (with `kind`, plan, autodeploy), managed "
        "databases, and the envVarGroups that share secrets across "
        "services."
    ),
    "extras": (
        "`databases[]` provisions managed Postgres / Redis. "
        "`env_var_groups[]` lets multiple services share the same "
        "envelope of secrets."
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Blueprint project + card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Render dashboard + env var groups."),
        ("deployment.targets", "Must include `render`."),
        ("platforms.render", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Suggested Blueprint name."),
        ("name, description", "Blueprint card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Dashboard / envVarGroups."),
        ("platforms.render.services", "Render services (`web`, `worker`, `cron`, `static`, `private_service`)."),
        ("platforms.render.databases", "Managed Postgres."),
        ("platforms.render.env_var_groups", "Shared env var groups."),
        ("platforms.render.region", "Render region."),
    ],
    "platform_fields": {
        "services": "Render services.",
        "databases": "Managed databases.",
        "env_var_groups": "Shared env var groups.",
        "region": "Default region.",
    },

    "schema_body": schema_object(
        required=["services"],
        properties={
            "services": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["name", "kind"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "kind": enum(["web", "worker", "cron", "static", "private_service"]),
                        "runtime": enum(["node", "python", "ruby", "go", "elixir", "rust", "docker", "static"]),
                        "plan": enum(["free", "starter", "standard", "pro", "pro-plus", "pro-max"]),
                        "build_command": str_prop(),
                        "start_command": str_prop(),
                        "schedule": str_prop(desc="Cron expression (only when kind=cron)."),
                        "health_check_path": str_prop(),
                        "auto_deploy": bool_prop(True),
                        "env_var_group": str_prop(),
                    },
                ),
            },
            "databases": {
                "type": "array",
                "items": schema_object(
                    required=["name", "kind"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "kind": enum(["postgresql", "redis"]),
                        "plan": enum(["free", "starter", "standard", "pro"]),
                        "postgres_major_version": {"type": "integer", "minimum": 13, "maximum": 17},
                    },
                ),
            },
            "env_var_groups": {
                "type": "array",
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                    },
                ),
            },
            "region": enum(["oregon", "frankfurt", "ohio", "singapore", "virginia"]),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Render Template
type: web-app
description: Template for a Render-targeted universal-spawn manifest.

platforms:
  render:
    region: oregon
    services:
      - name: web
        kind: web
        runtime: node
        plan: starter
        build_command: \"pnpm install && pnpm build\"
        start_command: \"pnpm start\"
        health_check_path: /healthz
        auto_deploy: true
        env_var_group: app
    databases:
      - { name: db, kind: postgresql, plan: starter, postgres_major_version: 16 }
    env_var_groups:
      - { name: app }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the managed Postgres service.
    secret: true

deployment:
  targets: [render]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/render-template }
""",

    "native_config": """
services:
  - name: web
    type: web
    runtime: node
    plan: starter
    buildCommand: pnpm install && pnpm build
    startCommand: pnpm start
    healthCheckPath: /healthz
    autoDeploy: true
    envVars:
      - fromGroup: app

databases:
  - name: db
    plan: starter
    postgresMajorVersion: 16

envVarGroups:
  - name: app
""",

    "universal_excerpt": """
platforms:
  render:
    services:
      - name: web
        kind: web
        runtime: node
        plan: starter
        build_command: \"pnpm install && pnpm build\"
        start_command: \"pnpm start\"
        health_check_path: /healthz
        auto_deploy: true
        env_var_group: app
    databases:
      - { name: db, kind: postgresql, plan: starter, postgres_major_version: 16 }
    env_var_groups:
      - { name: app }
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`render.yaml`** for per-service `envVars[]` with "
        "`generateValue`, `sync: false`, and the fine-grained control "
        "over Render's environment-synchronisation rules.\n"
        "- Use **`universal-spawn.yaml`** for the service-level shape "
        "and cross-platform parity.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)]"
            "(https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Render deploy URL accepts:\n\n"
            "- `repo` — URL-encoded git repo URL.\n\n"
            "Everything else is read from `render.yaml` at the root of "
            "the repo."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Blueprint preview** — consoles render a diff of the "
        "services + databases before first deploy so the user sees "
        "exactly what gets created.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Render Static Docs
type: site
summary: Minimal Render static site.
description: Static site service. No databases. Auto-deploy on push.

platforms:
  render:
    region: oregon
    services:
      - name: docs
        kind: static
        runtime: static
        build_command: \"pnpm build\"
        auto_deploy: true

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [render]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/render-docs }
  id: com.docs-team.render-docs
""",
        "serverless-api": """
version: \"1.0\"
name: Render Web API and Worker
type: api-service
summary: Render Blueprint with one web service, one worker, Postgres.
description: >
  Node web service + background worker + managed Postgres. Workers
  read from Postgres for job queue processing.

platforms:
  render:
    region: frankfurt
    services:
      - name: api
        kind: web
        runtime: node
        plan: standard
        build_command: \"pnpm install && pnpm build\"
        start_command: \"pnpm start\"
        health_check_path: /healthz
        env_var_group: app
      - name: worker
        kind: worker
        runtime: node
        plan: starter
        build_command: \"pnpm install && pnpm build:worker\"
        start_command: \"pnpm worker\"
        env_var_group: app
    databases:
      - { name: db, kind: postgresql, plan: standard, postgres_major_version: 16 }
    env_var_groups:
      - { name: app }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the Postgres service.
    secret: true
  - name: API_SECRET
    description: API signing secret.
    secret: true

deployment:
  targets: [render]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/render-api-worker }
  id: com.api-co.render-api-worker
""",
        "full-stack-app": """
version: \"1.0\"
name: Render Full Stack
type: web-app
summary: Full-stack Render Blueprint with web + worker + cron + Postgres + Redis.
description: >
  Full Blueprint: web (Node), worker (Python), cron (daily),
  Postgres primary, Redis cache. Two env var groups separate
  app secrets from observability secrets.

platforms:
  render:
    region: virginia
    services:
      - name: web
        kind: web
        runtime: node
        plan: standard
        build_command: \"pnpm install && pnpm build\"
        start_command: \"pnpm start\"
        health_check_path: /healthz
        env_var_group: app
      - name: worker
        kind: worker
        runtime: python
        plan: standard
        build_command: \"pip install -r requirements.txt\"
        start_command: \"python worker.py\"
        env_var_group: app
      - name: nightly
        kind: cron
        runtime: node
        plan: starter
        schedule: \"0 3 * * *\"
        build_command: \"pnpm install\"
        start_command: \"pnpm run nightly\"
        env_var_group: obs
    databases:
      - { name: db, kind: postgresql, plan: pro, postgres_major_version: 16 }
      - { name: cache, kind: redis, plan: starter }
    env_var_groups:
      - { name: app }
      - { name: obs }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the Postgres service.
    secret: true
  - name: REDIS_URL
    description: Injected by the Redis service.
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true

deployment:
  targets: [render]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/render-full-stack }
  id: com.stack-co.render-full-stack
""",
    },
}

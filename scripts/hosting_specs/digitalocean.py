"""DigitalOcean — App Platform + Functions + Droplets."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "digitalocean",
    "title": "DigitalOcean",
    "native_config_name": "app.yaml (App Platform) / project.yml (Functions)",
    "native_config_lang": "yaml",

    "lede": (
        "DigitalOcean's managed application surfaces are App Platform "
        "(buildpack + container web services, workers, and static "
        "sites) and Functions (serverless). The extension models both "
        "with `surface: app_platform` or `surface: functions`."
    ),
    "cares": (
        "The surface, the region, the service list (App Platform) or "
        "function list (Functions), and managed database attachments."
    ),
    "extras": (
        "`services[]` covers App Platform's `web`, `worker`, `job`, "
        "`static_site` kinds. `databases[]` attaches managed Postgres / "
        "MySQL / Redis clusters."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `site`."),
        ("env_vars_required", "Per-component environment variables."),
        ("deployment.targets", "Must include `digitalocean`."),
        ("platforms.digitalocean", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "App name suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.*", "Informational."),
        ("env_vars_required", "App Platform component env."),
        ("platforms.digitalocean.surface", "`app_platform` or `functions`."),
        ("platforms.digitalocean.region", "Region slug."),
        ("platforms.digitalocean.services", "App Platform components."),
        ("platforms.digitalocean.databases", "Managed databases."),
        ("platforms.digitalocean.functions", "Functions runtime config."),
    ],
    "platform_fields": {
        "surface": "`app_platform` or `functions`.",
        "region": "Region slug.",
        "services": "App Platform components.",
        "databases": "Managed databases.",
        "functions": "Functions runtime config.",
    },

    "schema_body": schema_object(
        required=["surface", "region"],
        properties={
            "surface": enum(["app_platform", "functions"]),
            "region": enum(["nyc", "ams", "sfo", "fra", "tor", "lon", "blr", "sgp", "syd"]),
            "services": {
                "type": "array",
                "items": schema_object(
                    required=["name", "kind"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "kind": enum(["web", "worker", "job", "static_site"]),
                        "instance_size": enum(["basic-xxs", "basic-xs", "basic-s", "basic-m", "professional-xs", "professional-s", "professional-m", "professional-l"]),
                        "instance_count": {"type": "integer", "minimum": 0, "maximum": 100},
                        "build_command": str_prop(),
                        "run_command": str_prop(),
                        "http_port": {"type": "integer", "minimum": 1, "maximum": 65535},
                    },
                ),
            },
            "databases": {
                "type": "array",
                "items": schema_object(
                    required=["name", "engine"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "engine": enum(["PG", "MYSQL", "REDIS", "MONGODB"]),
                        "size": enum(["db-s-dev", "db-s-1vcpu-1gb", "db-s-1vcpu-2gb", "db-s-2vcpu-4gb"]),
                    },
                ),
            },
            "functions": schema_object(
                properties={
                    "runtime": enum(["nodejs:20", "python:3.11", "go:1.22"]),
                    "package": str_prop(),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: DigitalOcean Template
type: web-app
description: Template for a DigitalOcean-targeted universal-spawn manifest.

platforms:
  digitalocean:
    surface: app_platform
    region: nyc
    services:
      - name: web
        kind: web
        instance_size: basic-xs
        instance_count: 1
        build_command: \"pnpm build\"
        run_command: \"pnpm start\"
        http_port: 8080
    databases:
      - { name: db, engine: PG, size: db-s-dev }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the managed Postgres attachment.
    secret: true

deployment:
  targets: [digitalocean]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/do-template }
""",

    "native_config": """
name: your-app
region: nyc
services:
  - name: web
    instance_size_slug: basic-xs
    instance_count: 1
    build_command: pnpm build
    run_command: pnpm start
    http_port: 8080
databases:
  - name: db
    engine: PG
    size: db-s-dev
""",

    "universal_excerpt": """
platforms:
  digitalocean:
    surface: app_platform
    region: nyc
    services:
      - name: web
        kind: web
        instance_size: basic-xs
        instance_count: 1
        build_command: \"pnpm build\"
        run_command: \"pnpm start\"
        http_port: 8080
    databases:
      - { name: db, engine: PG, size: db-s-dev }
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": (
            "[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)]"
            "(https://cloud.digitalocean.com/apps/new?repo=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://cloud.digitalocean.com/apps/new?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://www.deploytodo.com/do-btn-blue.svg" alt="Deploy to DO" />\n'
            '</a>'
        ),
        "params_doc": "The DO App Platform new-app URL accepts `repo` (URL-encoded git repo URL) and `refresh` (to redeploy).",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: DO Static Docs
type: site
summary: Minimal App Platform static site.
description: Static component only. basic-xxs instance. NYC region.

platforms:
  digitalocean:
    surface: app_platform
    region: nyc
    services:
      - name: docs
        kind: static_site
        build_command: \"pnpm build\"
        instance_size: basic-xxs
        instance_count: 1

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [digitalocean]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/do-static-docs }
  id: com.docs-team.do-static-docs
""",
        "serverless-api": """
version: \"1.0\"
name: DO Functions API
type: api-service
summary: DigitalOcean Functions serverless API.
description: Node 20 serverless function package.

platforms:
  digitalocean:
    surface: functions
    region: fra
    functions:
      runtime: nodejs:20
      package: packages/api

safety:
  min_permissions: [network:outbound]
  rate_limit_qps: 50

env_vars_required:
  - name: API_SECRET
    description: API signing secret.
    secret: true

deployment:
  targets: [digitalocean]

metadata:
  license: Apache-2.0
  author: { name: Functions Co., handle: functions-co }
  source: { type: git, url: https://github.com/functions-co/do-functions-api }
  id: com.functions-co.do-functions-api
""",
        "full-stack-app": """
version: \"1.0\"
name: DO Full Stack
type: web-app
summary: Full-stack App Platform deployment with web + worker + Postgres + Redis.
description: >
  Two components (web + worker) plus managed Postgres and Redis. FRA
  region for EU data residency.

platforms:
  digitalocean:
    surface: app_platform
    region: fra
    services:
      - { name: web,    kind: web,    instance_size: professional-s, instance_count: 2, build_command: \"pnpm build\",        run_command: \"pnpm start\",  http_port: 8080 }
      - { name: worker, kind: worker, instance_size: basic-s,        instance_count: 1, build_command: \"pnpm build:worker\", run_command: \"pnpm worker\" }
    databases:
      - { name: db,    engine: PG,    size: db-s-1vcpu-2gb }
      - { name: cache, engine: REDIS, size: db-s-1vcpu-1gb }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true
  - name: REDIS_URL
    description: Redis URL.
    secret: true
  - name: SESSION_SECRET
    description: Session secret.
    secret: true

deployment:
  targets: [digitalocean]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/do-full-stack }
  id: com.stack-co.do-full-stack
""",
    },
}

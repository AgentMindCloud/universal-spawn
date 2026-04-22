"""Railway — PaaS with railway.json + template system."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "railway",
    "title": "Railway",
    "native_config_name": "railway.json",
    "native_config_lang": "json",

    "lede": (
        "Railway runs services from a Git repo using Nixpacks (default) "
        "or a Dockerfile, attaches managed databases, and auto-provisions "
        "private networking between services. The extension captures "
        "the build provider, the start command, per-service plugins "
        "(Postgres, Redis, Mongo, MySQL), and the template registration."
    ),
    "cares": (
        "The build provider (`nixpacks`, `docker`, `buildpacks`), the "
        "start command, the plugins (managed services), the healthcheck "
        "endpoint, and whether this manifest registers a Railway "
        "template."
    ),
    "extras": (
        "`plugins[]` declares managed services Railway provisions for "
        "you. `template` opts this manifest into Railway's template "
        "marketplace."
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Service name + card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Railway secrets; missing required blocks deploy."),
        ("deployment.targets", "Must include `railway`."),
        ("platforms.railway", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Service-id suggestion."),
        ("name, description", "Railway card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("safety.min_permissions", "Informational."),
        ("safety.cost_limit_usd_daily", "Advisory; Railway enforces at project."),
        ("env_vars_required", "Railway secrets."),
        ("platforms.railway.build", "Build provider + Dockerfile/Nixpacks settings."),
        ("platforms.railway.start_command", "Start command."),
        ("platforms.railway.healthcheck", "Healthcheck path."),
        ("platforms.railway.plugins", "Managed services (Postgres/Redis/Mongo/MySQL)."),
        ("platforms.railway.replicas", "Replica count."),
        ("platforms.railway.region", "Railway region."),
        ("platforms.railway.template", "Template-registration block."),
    ],
    "platform_fields": {
        "build": "Build provider + config.",
        "start_command": "Start command.",
        "healthcheck": "Healthcheck path + timeout.",
        "plugins": "Managed services.",
        "replicas": "Replica count.",
        "region": "Railway region.",
        "template": "Template registration block.",
    },

    "schema_body": schema_object(
        properties={
            "build": schema_object(
                properties={
                    "provider": enum(["nixpacks", "docker", "buildpacks"]),
                    "dockerfile_path": str_prop(),
                    "watch_patterns": {"type": "array", "items": str_prop()},
                },
            ),
            "start_command": str_prop(),
            "healthcheck": schema_object(
                properties={
                    "path": str_prop(),
                    "timeout_seconds": {"type": "integer", "minimum": 1, "maximum": 600},
                },
            ),
            "plugins": {
                "type": "array",
                "items": schema_object(
                    required=["kind"],
                    properties={
                        "kind": enum(["postgresql", "mysql", "redis", "mongodb"]),
                        "name": str_prop(),
                        "volume_size_gb": {"type": "integer", "minimum": 1, "maximum": 500},
                    },
                ),
            },
            "replicas": {"type": "integer", "minimum": 1, "maximum": 100},
            "region": enum(["us-west1", "us-east4", "europe-west4", "asia-southeast1"]),
            "template": schema_object(
                properties={
                    "slug": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                    "description": str_prop(),
                    "category": enum(["web", "api", "bot", "database", "job", "other"]),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Railway Template
type: web-app
description: Template for a Railway-targeted universal-spawn manifest.

platforms:
  railway:
    build: { provider: nixpacks }
    start_command: \"pnpm start\"
    healthcheck: { path: /healthz, timeout_seconds: 10 }
    plugins:
      - { kind: postgresql, name: db }
    replicas: 1
    region: us-west1

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the postgresql plugin.
    secret: true

deployment:
  targets: [railway]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/railway-template }
""",

    "native_config": """
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": { "builder": "NIXPACKS" },
  "deploy": {
    "startCommand": "pnpm start",
    "healthcheckPath": "/healthz",
    "healthcheckTimeout": 10,
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE"
  }
}
""",

    "universal_excerpt": """
platforms:
  railway:
    build: { provider: nixpacks }
    start_command: \"pnpm start\"
    healthcheck: { path: /healthz, timeout_seconds: 10 }
    replicas: 1
    plugins:
      - { kind: postgresql, name: db }
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`railway.json`** for the `restartPolicyType`, preview "
        "deploy triggers, and webhook configuration.\n"
        "- Use **`universal-spawn.yaml`** for cross-platform parity "
        "and the plugin roster.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy on Railway](https://railway.com/button.svg)]"
            "(https://railway.com/new/template?template=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://railway.com/new/template?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://railway.com/button.svg" alt="Deploy on Railway" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Railway template URL accepts:\n\n"
            "- `template` — URL-encoded git repo URL.\n"
            "- `referralCode` — referral code.\n"
            "- `plugins` — comma-separated plugin list (pg, redis, …).\n\n"
            "Generators MAY fill `plugins` from `platforms.railway.plugins[*].kind`."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Plugin auto-provision** — every `plugins[]` entry provisions "
        "the managed service on first deploy and injects the standard "
        "env vars (`DATABASE_URL`, `REDIS_URL`, etc.).",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Railway Static Site
type: site
summary: Minimal static site served from Railway via nginx image.
description: Single Docker service serving static assets through nginx.

platforms:
  railway:
    build: { provider: docker, dockerfile_path: Dockerfile }
    start_command: \"nginx -g 'daemon off;'\"
    healthcheck: { path: /, timeout_seconds: 5 }
    replicas: 1
    region: us-west1

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [railway]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/railway-static }
  id: com.static-co.railway-static
""",
        "serverless-api": """
version: \"1.0\"
name: Railway API
type: api-service
summary: Node API with Redis-backed rate limiting on Railway.
description: Fastify API. Redis plugin provisioned. Healthcheck + 2 replicas.

platforms:
  railway:
    build: { provider: nixpacks }
    start_command: \"node dist/server.js\"
    healthcheck: { path: /healthz, timeout_seconds: 10 }
    plugins:
      - { kind: redis, name: cache }
    replicas: 2
    region: us-east4

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: API_SECRET
    description: API signing secret.
    secret: true
  - name: REDIS_URL
    description: Injected by the redis plugin.
    secret: true

deployment:
  targets: [railway]

metadata:
  license: MIT
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/railway-api }
  id: com.api-co.railway-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Railway Full Stack
type: web-app
summary: Full-stack Remix app with Postgres + Redis, template-registered.
description: >
  Full stack Remix app with a Postgres primary db, Redis cache, and
  a worker replica. Registered as a Railway template for one-click
  reuse.

platforms:
  railway:
    build: { provider: nixpacks, watch_patterns: [\"app/**\", \"prisma/**\"] }
    start_command: \"pnpm start\"
    healthcheck: { path: /healthz, timeout_seconds: 15 }
    plugins:
      - { kind: postgresql, name: db, volume_size_gb: 20 }
      - { kind: redis, name: cache }
    replicas: 2
    region: europe-west4
    template:
      slug: remix-full-stack
      description: Remix full-stack starter with Postgres + Redis.
      category: web

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 15
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Injected by the postgresql plugin.
    secret: true
  - name: REDIS_URL
    description: Injected by the redis plugin.
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true

deployment:
  targets: [railway]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/railway-full-stack }
  id: com.stack-co.railway-full-stack
""",
    },
}

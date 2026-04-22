"""Cloudflare — Workers + Pages + R2 + D1 + KV + Queues."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "cloudflare",
    "title": "Cloudflare",
    "native_config_name": "wrangler.toml",
    "native_config_lang": "toml",

    "lede": (
        "Cloudflare's developer platform spans Workers, Pages, R2 "
        "(object storage), D1 (SQLite at the edge), KV (key-value), "
        "Queues, and Durable Objects. The extension covers all four "
        "primary surfaces — Workers, Pages, R2 buckets, D1 databases "
        "— plus the bindings that glue them together."
    ),
    "cares": (
        "The surface (`workers`, `pages`), the entry script, the "
        "bindings map (KV, R2, D1, Queues, Durable Objects, service "
        "bindings), and whether the creation runs on the `nodejs_compat` "
        "runtime."
    ),
    "extras": (
        "`bindings.r2[]`, `bindings.d1[]`, `bindings.kv[]` declare "
        "resources and the binding name the Worker imports them as. "
        "`nodejs_compat: true` enables the Node.js compatibility mode."
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Worker / Pages project name + card."),
        ("type", "`web-app`, `api-service`, `site`, `workflow`."),
        ("env_vars_required", "Wrangler secret upload; missing required block deploy."),
        ("deployment.targets", "Must include `cloudflare`."),
        ("platforms.cloudflare", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Default Worker name."),
        ("name, description", "Dashboard card."),
        ("type", "`web-app`, `api-service`, `site`, `workflow`."),
        ("safety.min_permissions", "Informational."),
        ("safety.cost_limit_usd_daily", "Advisory; Cloudflare's billing is plan-based."),
        ("env_vars_required", "Wrangler secrets; missing required blocks deploy."),
        ("platforms.cloudflare.surface", "`workers` or `pages`."),
        ("platforms.cloudflare.main", "Entry script path (Workers surface)."),
        ("platforms.cloudflare.build", "Pages build command + output dir."),
        ("platforms.cloudflare.compatibility_date", "Compatibility date (YYYY-MM-DD)."),
        ("platforms.cloudflare.nodejs_compat", "nodejs_compat flag."),
        ("platforms.cloudflare.routes", "HTTP routes (Workers)."),
        ("platforms.cloudflare.bindings.r2", "R2 bucket bindings."),
        ("platforms.cloudflare.bindings.d1", "D1 database bindings."),
        ("platforms.cloudflare.bindings.kv", "KV namespace bindings."),
        ("platforms.cloudflare.bindings.queues", "Queue bindings (producer + consumer)."),
        ("platforms.cloudflare.bindings.durable_objects", "Durable Object bindings."),
        ("platforms.cloudflare.bindings.services", "Service bindings (Worker-to-Worker)."),
    ],
    "platform_fields": {
        "surface": "`workers` or `pages`.",
        "main": "Worker entry script path.",
        "build": "Pages build settings.",
        "compatibility_date": "Compatibility date.",
        "nodejs_compat": "Enable nodejs_compat.",
        "routes": "HTTP routes (Workers).",
        "bindings": "Resource bindings (R2 / D1 / KV / Queues / Durable Objects / services).",
    },

    "schema_body": schema_object(
        required=["surface"],
        properties={
            "surface": enum(["workers", "pages"]),
            "main": str_prop(),
            "build": schema_object(
                properties={
                    "command": str_prop(),
                    "output": str_prop(),
                    "root_dir": str_prop(),
                },
            ),
            "compatibility_date": str_prop(pattern=r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"),
            "nodejs_compat": bool_prop(False),
            "routes": {
                "type": "array",
                "items": schema_object(
                    required=["pattern"],
                    properties={
                        "pattern": str_prop(),
                        "zone_name": str_prop(),
                    },
                ),
            },
            "bindings": schema_object(
                properties={
                    "r2": {
                        "type": "array",
                        "items": schema_object(
                            required=["binding", "bucket_name"],
                            properties={
                                "binding": str_prop(pattern=r"^[A-Z][A-Z0-9_]{0,63}$"),
                                "bucket_name": str_prop(),
                            },
                        ),
                    },
                    "d1": {
                        "type": "array",
                        "items": schema_object(
                            required=["binding", "database_name"],
                            properties={
                                "binding": str_prop(pattern=r"^[A-Z][A-Z0-9_]{0,63}$"),
                                "database_name": str_prop(),
                                "database_id": str_prop(),
                            },
                        ),
                    },
                    "kv": {
                        "type": "array",
                        "items": schema_object(
                            required=["binding", "id"],
                            properties={
                                "binding": str_prop(pattern=r"^[A-Z][A-Z0-9_]{0,63}$"),
                                "id": str_prop(),
                            },
                        ),
                    },
                    "queues": {
                        "type": "array",
                        "items": schema_object(
                            required=["binding"],
                            properties={
                                "binding": str_prop(pattern=r"^[A-Z][A-Z0-9_]{0,63}$"),
                                "producer_of": str_prop(),
                                "consumer_of": str_prop(),
                            },
                        ),
                    },
                    "durable_objects": {
                        "type": "array",
                        "items": schema_object(
                            required=["name", "class_name"],
                            properties={
                                "name": str_prop(),
                                "class_name": str_prop(),
                                "script_name": str_prop(),
                            },
                        ),
                    },
                    "services": {
                        "type": "array",
                        "items": schema_object(
                            required=["binding", "service"],
                            properties={
                                "binding": str_prop(pattern=r"^[A-Z][A-Z0-9_]{0,63}$"),
                                "service": str_prop(),
                            },
                        ),
                    },
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Cloudflare Template
type: api-service
description: Template for a Cloudflare-targeted universal-spawn manifest.

platforms:
  cloudflare:
    surface: workers
    main: src/index.ts
    compatibility_date: \"2025-01-15\"
    nodejs_compat: true
    bindings:
      r2:
        - { binding: ASSETS, bucket_name: my-assets }
      d1:
        - { binding: DB, database_name: my-db }
      kv:
        - { binding: CACHE, id: \"00000000000000000000000000000000\" }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: API_SECRET
    description: API authentication secret.
    secret: true

deployment:
  targets: [cloudflare]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/cloudflare-template }
""",

    "native_config": """
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2025-01-15"
compatibility_flags = ["nodejs_compat"]

[[r2_buckets]]
binding = "ASSETS"
bucket_name = "my-assets"

[[d1_databases]]
binding = "DB"
database_name = "my-db"
database_id = "00000000-0000-0000-0000-000000000000"

[[kv_namespaces]]
binding = "CACHE"
id = "00000000000000000000000000000000"
""",

    "universal_excerpt": """
platforms:
  cloudflare:
    surface: workers
    main: src/index.ts
    compatibility_date: \"2025-01-15\"
    nodejs_compat: true
    bindings:
      r2:
        - { binding: ASSETS, bucket_name: my-assets }
      d1:
        - { binding: DB, database_name: my-db, database_id: 00000000-0000-0000-0000-000000000000 }
      kv:
        - { binding: CACHE, id: \"00000000000000000000000000000000\" }
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`wrangler.toml`** for per-environment overrides "
        "(`[env.preview]`, `[env.production]`), `triggers.crons[]`, "
        "custom domains, and tail logs config.\n"
        "- Use **`universal-spawn.yaml`** for cross-platform siblings "
        "(e.g. a `platforms.vercel` parallel deployment) plus "
        "`env_vars_required`, safety, metadata.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)]"
            "(https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-worker)"
        ),
        "html": (
            '<a href="https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-worker">\n'
            '  <img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare Workers" />\n'
            '</a>'
        ),
        "params_doc": (
            "The `deploy.workers.cloudflare.com` endpoint accepts:\n\n"
            "- `url` (required) — URL-encoded git repo URL.\n\n"
            "Pages deployments use a different button: see the "
            "Cloudflare Pages docs. The button above targets Workers."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Binding auto-provision** — `bindings.r2[]`, `bindings.d1[]`, "
        "`bindings.kv[]` pre-create the named resources if they do not "
        "exist at first deploy.",
        "**Queue pairing** — a `producer_of` binding and a matching "
        "`consumer_of` binding on a sibling Worker auto-wire a queue.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Cloudflare Pages Docs
type: site
summary: Minimal Cloudflare Pages docs site with static output.
description: Astro docs site deployed to Cloudflare Pages.

platforms:
  cloudflare:
    surface: pages
    build:
      command: \"pnpm build\"
      output: dist
    compatibility_date: \"2025-01-15\"

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [cloudflare]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/cf-pages-docs }
  id: com.docs-team.cf-pages-docs
""",
        "serverless-api": """
version: \"1.0\"
name: CF Worker API
type: api-service
summary: Cloudflare Worker API with KV cache + D1 database.
description: >
  API Worker with one D1 database (tickets) and one KV namespace
  (cache). nodejs_compat enabled so common Node libraries work.

platforms:
  cloudflare:
    surface: workers
    main: src/index.ts
    compatibility_date: \"2025-01-15\"
    nodejs_compat: true
    routes:
      - { pattern: \"api.example.com/*\", zone_name: example.com }
    bindings:
      d1:
        - { binding: DB, database_name: tickets, database_id: 11111111-1111-1111-1111-111111111111 }
      kv:
        - { binding: CACHE, id: \"11111111111111111111111111111111\" }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: API_SECRET
    description: API signing secret.
    secret: true

deployment:
  targets: [cloudflare]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/cf-worker-api }
  id: com.api-co.cf-worker-api
""",
        "full-stack-app": """
version: \"1.0\"
name: CF Full Stack
type: web-app
summary: Full-stack Cloudflare app using Workers + Pages + R2 + D1 + Queues + service bindings.
description: >
  Workers handle /api routes with D1 (Postgres-style SQLite at the edge)
  and R2 (uploads). Pages serves the SvelteKit front end. An upload
  Queue buffers R2 writes. A service binding lets the Pages Worker
  call the API Worker.

platforms:
  cloudflare:
    surface: workers
    main: src/api.ts
    compatibility_date: \"2025-01-15\"
    nodejs_compat: true
    routes:
      - { pattern: \"app.example.com/api/*\", zone_name: example.com }
    bindings:
      r2:
        - { binding: UPLOADS, bucket_name: app-uploads }
      d1:
        - { binding: DB, database_name: app-db, database_id: 22222222-2222-2222-2222-222222222222 }
      kv:
        - { binding: SESSIONS, id: \"22222222222222222222222222222222\" }
      queues:
        - { binding: UPLOAD_QUEUE, producer_of: uploads }
        - { binding: UPLOAD_CONSUMER, consumer_of: uploads }
      durable_objects:
        - { name: ROOM, class_name: ChatRoom }
      services:
        - { binding: PAGES_ASSETS, service: app-pages }

safety:
  min_permissions:
    - network:inbound
    - network:outbound:api.stripe.com
  cost_limit_usd_daily: 15
  safe_for_auto_spawn: false

env_vars_required:
  - name: STRIPE_SECRET
    description: Stripe server key.
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true

deployment:
  targets: [cloudflare]

metadata:
  license: MIT
  author: { name: App Co., handle: app-co }
  source: { type: git, url: https://github.com/app-co/cf-full-stack }
  id: com.app-co.cf-full-stack
""",
    },
}

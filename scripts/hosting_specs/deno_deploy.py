"""Deno Deploy — globally-distributed JavaScript runtime."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "deno-deploy",
    "title": "Deno Deploy",
    "native_config_name": "deno.json",
    "native_config_lang": "json",

    "lede": (
        "Deno Deploy runs Deno (and increasingly Node.js) modules at "
        "the edge. A manifest captures the entry module, import map, "
        "required permissions for Deno's permission model, and KV "
        "namespaces."
    ),
    "cares": (
        "The entry module, the Deno version or std @ version, the "
        "import map path, the granted permissions (`--allow-net`, "
        "`--allow-read`, etc.), and Deno KV namespaces."
    ),
    "extras": (
        "`deno_permissions[]` maps to the Deno permission flags the "
        "consumer grants at run time. `kv_namespaces[]` lists Deno KV "
        "namespaces the module uses."
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Project name + card."),
        ("type", "`api-service`, `web-app`, `workflow`, `cli-tool`."),
        ("env_vars_required", "Deno Deploy environment variables."),
        ("deployment.targets", "Must include `deno-deploy`."),
        ("platforms.deno-deploy", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Project-slug suggestion."),
        ("name, description", "Card."),
        ("type", "`api-service`, `web-app`, `workflow`, `cli-tool`."),
        ("safety.min_permissions", "Mirrored into `deno_permissions[]`."),
        ("env_vars_required", "Deno Deploy env vars."),
        ("platforms.deno-deploy.entrypoint", "Entry module path or URL."),
        ("platforms.deno-deploy.import_map", "Path to import_map.json."),
        ("platforms.deno-deploy.deno_permissions", "Deno permission flags."),
        ("platforms.deno-deploy.kv_namespaces", "Deno KV namespaces."),
        ("platforms.deno-deploy.regions", "Regions."),
    ],
    "platform_fields": {
        "entrypoint": "Entry module path or URL.",
        "import_map": "Path to `import_map.json`.",
        "deno_version": "Deno version (major).",
        "deno_permissions": "Deno permission flags.",
        "kv_namespaces": "Deno KV namespaces.",
        "regions": "Deno Deploy regions.",
    },

    "schema_body": schema_object(
        required=["entrypoint"],
        properties={
            "entrypoint": str_prop(),
            "import_map": str_prop(),
            "deno_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+){0,2}$"),
            "deno_permissions": {
                "type": "array",
                "items": enum([
                    "allow-net", "allow-read", "allow-write", "allow-env",
                    "allow-run", "allow-sys", "allow-ffi", "allow-hrtime",
                ]),
            },
            "kv_namespaces": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            },
            "regions": {
                "type": "array",
                "items": enum(["americas", "europe", "asia", "oceania", "africa", "any"]),
            },
            "compatibility_mode": enum(["deno", "node"]),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Deno Deploy Template
type: api-service
description: Template for a Deno-Deploy-targeted universal-spawn manifest.

platforms:
  deno-deploy:
    entrypoint: main.ts
    import_map: import_map.json
    deno_version: \"2\"
    deno_permissions: [allow-net, allow-env]
    kv_namespaces: [default]
    regions: [any]
    compatibility_mode: deno

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: API_SECRET
    description: API secret.
    secret: true

deployment:
  targets: [deno-deploy]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/deno-deploy-template }
""",

    "native_config": """
{
  "tasks": { "start": "deno run -A main.ts" },
  "imports": { "std/": "https://deno.land/std@0.224.0/" },
  "deploy": {
    "entrypoint": "main.ts",
    "include": ["**/*.ts"],
    "exclude": ["tests/"]
  }
}
""",

    "universal_excerpt": """
platforms:
  deno-deploy:
    entrypoint: main.ts
    import_map: import_map.json
    deno_version: \"2\"
    deno_permissions: [allow-net, allow-env]
""",

    "compatibility_extras": (
        "## Deno permissions map\n\n"
        "A `safety.min_permissions` entry maps onto a "
        "`deno_permissions` flag where equivalent:\n\n"
        "| universal                               | Deno flag       |\n"
        "|------------------------------------------|------------------|\n"
        "| `network:outbound`, `network:inbound`    | `allow-net`      |\n"
        "| `fs:read`                                | `allow-read`     |\n"
        "| `fs:write:*`                             | `allow-write`    |\n"
        "| `fs:exec:*`                              | `allow-run`      |\n"
        "\nA consumer that finds both MUST union them (widest wins)."
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Deno](https://deno.com/button)]"
            "(https://dash.deno.com/new?url=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://dash.deno.com/new?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://deno.com/button" alt="Deploy to Deno" />\n'
            '</a>'
        ),
        "params_doc": (
            "The `dash.deno.com/new` endpoint accepts:\n\n"
            "- `url` — URL-encoded git repo URL.\n"
            "- `entrypoint` — pre-fill the entry module path.\n"
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Permission minimisation** — consumers refuse to grant a "
        "Deno permission flag not listed in `deno_permissions[]`.",
        "**Import-map audit** — consoles render a diff of new import "
        "specifiers between the committed `import_map.json` and the "
        "one referenced by the manifest.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Fresh Static Site
type: site
summary: Minimal Fresh static-mode site on Deno Deploy.
description: Fresh in static-only mode. No KV, no env.

platforms:
  deno-deploy:
    entrypoint: main.ts
    deno_version: \"2\"
    deno_permissions: [allow-read]
    regions: [any]
    compatibility_mode: deno

safety:
  min_permissions: [network:inbound, fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [deno-deploy]

metadata:
  license: MIT
  author: { name: Fresh Co., handle: fresh-co }
  source: { type: git, url: https://github.com/fresh-co/fresh-static }
  id: com.fresh-co.fresh-static
""",
        "serverless-api": """
version: \"1.0\"
name: Deno Edge API
type: api-service
summary: Deno HTTP API with KV-backed rate limiting.
description: >
  HTTP API running on Deno Deploy with a KV-backed rate limiter and
  a simple Hono router. Permissions pared to net + env only.

platforms:
  deno-deploy:
    entrypoint: main.ts
    import_map: import_map.json
    deno_version: \"2\"
    deno_permissions: [allow-net, allow-env]
    kv_namespaces: [ratelimit]
    regions: [americas, europe]
    compatibility_mode: deno

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 200

env_vars_required:
  - name: API_SECRET
    description: API secret for protected routes.
    secret: true

deployment:
  targets: [deno-deploy]

metadata:
  license: Apache-2.0
  author: { name: Edge Co., handle: edge-co }
  source: { type: git, url: https://github.com/edge-co/deno-edge-api }
  id: com.edge-co.deno-edge-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Deno Full Stack
type: web-app
summary: Full-stack Fresh app using Deno KV and the Node.js compat mode.
description: >
  Fresh app with auth + comments. Stores users and posts in Deno KV.
  Uses the Node.js compatibility mode for a legacy ORM dependency.

platforms:
  deno-deploy:
    entrypoint: main.ts
    import_map: import_map.json
    deno_version: \"2\"
    deno_permissions: [allow-net, allow-env, allow-read]
    kv_namespaces: [users, posts]
    regions: [americas]
    compatibility_mode: node

safety:
  min_permissions: [network:inbound, network:outbound, fs:read]
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false

env_vars_required:
  - name: AUTH_SECRET
    description: JWT signing secret.
    secret: true
  - name: SMTP_URL
    description: Outbound SMTP URL for email.
    secret: true

deployment:
  targets: [deno-deploy]

metadata:
  license: MIT
  author: { name: App Co., handle: app-co }
  source: { type: git, url: https://github.com/app-co/deno-fresh-app }
  id: com.app-co.deno-fresh-app
""",
    },
}

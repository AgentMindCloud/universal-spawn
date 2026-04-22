"""Heroku — app.json + Heroku Button."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "heroku",
    "title": "Heroku",
    "native_config_name": "app.json",
    "native_config_lang": "json",

    "lede": (
        "Heroku's `app.json` describes everything the Heroku Button "
        "needs to clone a repo into a new app: stack, buildpacks, "
        "formation (which dynos run), addons, and prompted env vars. "
        "The extension mirrors that shape."
    ),
    "cares": (
        "The stack (`heroku-24`, `heroku-22`, `container`), buildpacks, "
        "the formation (dyno type + count), addons, scripts "
        "(`postdeploy`, `pr-predestroy`), and prompted env vars."
    ),
    "extras": (
        "`addons[]` provisions managed services (`heroku-postgresql`, "
        "`heroku-redis`, `papertrail`). `formation{}` sizes each "
        "Procfile process."
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "App card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Prompted on Button deploy + dashboard."),
        ("deployment.targets", "Must include `heroku`."),
        ("platforms.heroku", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Suggested app name."),
        ("name, description", "Card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Prompted on Heroku Button deploy."),
        ("platforms.heroku.stack", "Heroku stack."),
        ("platforms.heroku.buildpacks", "Ordered buildpack list."),
        ("platforms.heroku.formation", "Dyno formation."),
        ("platforms.heroku.addons", "Managed services."),
        ("platforms.heroku.scripts", "Lifecycle scripts."),
        ("platforms.heroku.region", "Heroku region."),
    ],
    "platform_fields": {
        "stack": "Heroku stack.",
        "buildpacks": "Ordered buildpack list.",
        "formation": "Dyno formation.",
        "addons": "Managed services.",
        "scripts": "Lifecycle scripts (`postdeploy`, `pr-predestroy`).",
        "region": "Heroku region.",
    },

    "schema_body": schema_object(
        properties={
            "stack": enum(["heroku-24", "heroku-22", "container"]),
            "buildpacks": {
                "type": "array",
                "items": schema_object(
                    required=["url"],
                    properties={"url": str_prop()},
                ),
            },
            "formation": {
                "type": "object",
                "additionalProperties": schema_object(
                    required=["quantity", "size"],
                    properties={
                        "quantity": {"type": "integer", "minimum": 0, "maximum": 100},
                        "size": enum(["eco", "basic", "standard-1x", "standard-2x",
                                      "performance-m", "performance-l", "private-s",
                                      "private-m", "private-l", "shield-s", "shield-m", "shield-l"]),
                    },
                ),
            },
            "addons": {
                "type": "array",
                "items": schema_object(
                    required=["plan"],
                    properties={
                        "plan": str_prop(desc="e.g. heroku-postgresql:essential-0"),
                        "as": str_prop(),
                    },
                ),
            },
            "scripts": schema_object(
                properties={
                    "postdeploy": str_prop(),
                    "pr_predestroy": str_prop(),
                },
            ),
            "region": enum(["us", "eu"]),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Heroku Template
type: web-app
description: Template for a Heroku-targeted universal-spawn manifest.

platforms:
  heroku:
    stack: heroku-24
    buildpacks:
      - { url: heroku/nodejs }
    formation:
      web: { quantity: 1, size: basic }
      worker: { quantity: 0, size: basic }
    addons:
      - { plan: \"heroku-postgresql:essential-0\", as: DATABASE }
    scripts: { postdeploy: \"npm run migrate\" }
    region: us

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true

deployment:
  targets: [heroku]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/heroku-template }
""",

    "native_config": """
{
  "name": "Your App",
  "description": "Template app.",
  "stack": "heroku-24",
  "buildpacks": [{ "url": "heroku/nodejs" }],
  "formation": {
    "web":    { "quantity": 1, "size": "basic" },
    "worker": { "quantity": 0, "size": "basic" }
  },
  "addons": [{ "plan": "heroku-postgresql:essential-0", "as": "DATABASE" }],
  "env": {
    "SESSION_SECRET": { "description": "Session cookie secret", "generator": "secret" }
  },
  "scripts": { "postdeploy": "npm run migrate" }
}
""",

    "universal_excerpt": """
platforms:
  heroku:
    stack: heroku-24
    buildpacks: [{ url: heroku/nodejs }]
    formation:
      web: { quantity: 1, size: basic }
      worker: { quantity: 0, size: basic }
    addons:
      - { plan: \"heroku-postgresql:essential-0\", as: DATABASE }
    scripts: { postdeploy: \"npm run migrate\" }
    region: us
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`app.json`** for env `generator: secret`, "
        "`require: true`, `value: X` hints, review-app config, and "
        "environment overrides.\n"
        "- Use **`universal-spawn.yaml`** for the top-level manifest "
        "and cross-platform parity.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy](https://www.herokucdn.com/deploy/button.svg)]"
            "(https://heroku.com/deploy?template=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://heroku.com/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Heroku Button URL accepts:\n\n"
            "- `template` (required) — URL-encoded git repo URL.\n\n"
            "Heroku reads `app.json` at the root of the repo to build "
            "the deploy form; the env vars prompted come from "
            "`app.json`'s `env` map."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Review-apps pairing** — a manifest that declares "
        "`platforms.heroku` and uses `safe_for_auto_spawn: false` "
        "auto-disables review-app promotion.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Heroku Static Assets
type: site
summary: Minimal Heroku static-assets app via the static buildpack.
description: Static site served by heroku-community/static buildpack.

platforms:
  heroku:
    stack: heroku-24
    buildpacks:
      - { url: \"https://github.com/heroku/heroku-buildpack-static\" }
    formation:
      web: { quantity: 1, size: eco }
    region: us

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [heroku]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/heroku-static }
  id: com.static-co.heroku-static
""",
        "serverless-api": """
version: \"1.0\"
name: Heroku API with Worker
type: api-service
summary: Node API with worker dyno and Postgres.
description: Web + worker dynos + heroku-postgresql. Migrations on postdeploy.

platforms:
  heroku:
    stack: heroku-24
    buildpacks:
      - { url: heroku/nodejs }
    formation:
      web:    { quantity: 1, size: standard-1x }
      worker: { quantity: 1, size: standard-1x }
    addons:
      - { plan: \"heroku-postgresql:essential-0\", as: DATABASE }
    scripts: { postdeploy: \"npm run migrate\" }
    region: us

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 50

env_vars_required:
  - name: SESSION_SECRET
    description: Session secret.
    secret: true

deployment:
  targets: [heroku]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/heroku-api-worker }
  id: com.api-co.heroku-api-worker
""",
        "full-stack-app": """
version: \"1.0\"
name: Heroku Full Stack
type: web-app
summary: Full-stack Heroku app with container stack, Postgres, Redis, Papertrail.
description: >
  Container stack app (image built locally), Postgres primary, Redis
  cache, Papertrail logs. EU region for data residency.

platforms:
  heroku:
    stack: container
    formation:
      web:    { quantity: 2, size: standard-2x }
      worker: { quantity: 1, size: standard-1x }
    addons:
      - { plan: \"heroku-postgresql:standard-0\", as: DATABASE }
      - { plan: \"heroku-redis:premium-0\", as: REDIS }
      - { plan: \"papertrail:choklad\" }
    scripts:
      postdeploy: \"./bin/release\"
      pr_predestroy: \"./bin/pr-destroy\"
    region: eu

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: SESSION_SECRET
    description: Session cookie signing secret.
    secret: true
  - name: NEWRELIC_LICENSE_KEY
    description: New Relic license key.
    required: false
    secret: true

deployment:
  targets: [heroku]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co, org: Stack }
  source: { type: git, url: https://github.com/stack-co/heroku-full-stack }
  id: com.stack-co.heroku-full-stack
""",
    },
}

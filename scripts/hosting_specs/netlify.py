"""Netlify — netlify.toml coexistence, Functions, Edge Functions, Forms."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "netlify",
    "title": "Netlify",
    "native_config_name": "netlify.toml",
    "native_config_lang": "toml",

    "lede": (
        "Netlify builds a site from a Git repo, deploys it on a CDN, "
        "and runs Functions / Edge Functions alongside. The extension "
        "captures the build command, publish directory, function and "
        "edge-function paths, and which deploy contexts required "
        "secrets must exist in."
    ),
    "cares": (
        "The publish directory, the Functions / Edge Functions paths, "
        "build plugins, redirects/headers files, and the env "
        "contexts (`production`, `deploy-preview`, `branch-deploy`, "
        "`dev`) required secrets must exist in."
    ),
    "extras": (
        "`plugins[]` enables Netlify Build plugins by package name. "
        "`redirects_file` and `headers_file` point at `_redirects` / "
        "`_headers`."
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Site name + card."),
        ("type", "`web-app`, `site`, `api-service`, `container`."),
        ("env_vars_required", "Build blocked when required secrets missing in listed env_contexts."),
        ("deployment.targets", "Must include `netlify`."),
        ("platforms.netlify", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Default site-slug suggestion."),
        ("name, description", "Dashboard card."),
        ("type", "`web-app`, `site`, `api-service`, `container`, `workflow`."),
        ("safety.min_permissions", "Informational; not sandbox-enforced."),
        ("safety.cost_limit_usd_daily", "Advisory."),
        ("env_vars_required", "Build-blocking gate per env context."),
        ("platforms.netlify.base", "Base directory inside the repo."),
        ("platforms.netlify.build_command", "Build command."),
        ("platforms.netlify.publish", "Directory containing built assets."),
        ("platforms.netlify.functions", "Path to Functions directory."),
        ("platforms.netlify.edge_functions", "Path to Edge Functions directory."),
        ("platforms.netlify.node_version", "Node.js version."),
        ("platforms.netlify.plugins", "Netlify Build plugins."),
        ("platforms.netlify.env_contexts", "Env contexts required secrets must exist in."),
        ("platforms.netlify.redirects_file", "Path to `_redirects`."),
        ("platforms.netlify.headers_file", "Path to `_headers`."),
    ],
    "platform_fields": {
        "base": "Base directory inside the repo.",
        "install_command": "Install command.",
        "build_command": "Build command.",
        "publish": "Publish directory.",
        "functions": "Functions directory path.",
        "edge_functions": "Edge Functions directory path.",
        "node_version": "Node.js version.",
        "plugins": "Netlify Build plugins.",
        "env_contexts": "Env contexts required secrets must exist in.",
        "redirects_file": "Path to `_redirects`.",
        "headers_file": "Path to `_headers`.",
    },

    "schema_body": schema_object(
        properties={
            "base": str_prop(),
            "install_command": str_prop(),
            "build_command": str_prop(),
            "publish": str_prop(),
            "functions": str_prop(),
            "edge_functions": str_prop(),
            "node_version": str_prop(),
            "plugins": {
                "type": "array",
                "items": schema_object(
                    required=["package"],
                    properties={
                        "package": str_prop(),
                        "inputs": {"type": "object"},
                    },
                ),
            },
            "env_contexts": {
                "type": "array",
                "items": enum(["production", "deploy-preview", "branch-deploy", "dev"]),
            },
            "redirects_file": str_prop(),
            "headers_file": str_prop(),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Netlify Template
type: web-app
description: Template for a Netlify-targeted universal-spawn manifest.

platforms:
  netlify:
    build_command: \"pnpm build\"
    publish: dist
    node_version: \"20\"
    env_contexts: [production]

safety:
  min_permissions: [network:inbound]

env_vars_required: []

deployment:
  targets: [netlify]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/netlify-template }
""",

    "native_config": """
[build]
  command = "pnpm build"
  publish = "dist"
  functions = "netlify/functions"

[build.environment]
  NODE_VERSION = "20"

[[plugins]]
  package = "@netlify/plugin-nextjs"
""",

    "universal_excerpt": """
platforms:
  netlify:
    build_command: \"pnpm build\"
    publish: dist
    functions: netlify/functions
    node_version: \"20\"
    plugins:
      - package: \"@netlify/plugin-nextjs\"
    env_contexts: [production, deploy-preview]
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`netlify.toml`** for redirects, headers, per-branch "
        "build config, and plugin inputs that don't fit cleanly into "
        "the universal schema's flat key space.\n"
        "- Use **`universal-spawn.yaml`** for discovery, safety, "
        "`env_vars_required`, and cross-platform siblings.\n"
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)]"
            "(https://app.netlify.com/start/deploy?repository=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://app.netlify.com/start/deploy?repository=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://www.netlify.com/img/deploy/button.svg" alt="Deploy to Netlify" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Netlify deploy link accepts:\n\n"
            "- `repository` (required) — URL-encoded git repo URL.\n"
            "- `base` — sub-directory inside the repo.\n"
            "- `branch` — branch to deploy.\n"
            "- `site_name` — suggested site slug.\n"
            "- `env` — env vars to prompt the user for.\n\n"
            "Generators MAY fill `env` from `env_vars_required[*].name`."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Deploy context gating** — `env_contexts[]` controls which "
        "contexts a required secret must exist in before a build "
        "proceeds.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Astro Docs Netlify
type: site
summary: Minimal Astro static docs deployed to Netlify.
description: Static Astro docs site. Publish `dist`. Production only.

platforms:
  netlify:
    build_command: \"pnpm build\"
    publish: dist
    node_version: \"20\"
    env_contexts: [production]
    headers_file: public/_headers

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [netlify]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/astro-docs-netlify }
  id: com.docs-team.astro-docs-netlify
""",
        "serverless-api": """
version: \"1.0\"
name: Netlify Functions API
type: api-service
summary: Netlify Functions API with a Stripe webhook + nextjs plugin.
description: >
  HTTP API at /.netlify/functions/api plus a Stripe webhook at
  /.netlify/functions/stripe. Node 20. Builds on production and
  deploy-preview contexts.

platforms:
  netlify:
    build_command: \"pnpm build\"
    publish: dist
    functions: netlify/functions
    node_version: \"20\"
    env_contexts: [production, deploy-preview]
    plugins:
      - package: \"@netlify/plugin-nextjs\"

safety:
  min_permissions:
    - network:inbound
    - network:outbound:api.stripe.com
  rate_limit_qps: 50
  cost_limit_usd_daily: 25

env_vars_required:
  - name: STRIPE_WEBHOOK_SECRET
    description: Stripe webhook signing secret.
    secret: true
  - name: DATABASE_URL
    description: Database connection string.
    secret: true

deployment:
  targets: [netlify]

metadata:
  license: Apache-2.0
  author: { name: Functions Co., handle: functions-co }
  source: { type: git, url: https://github.com/functions-co/netlify-functions-api }
  id: com.functions-co.netlify-functions-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Netlify Full Stack
type: web-app
summary: Full-stack Remix app with edge functions, Postgres, and Auth0.
description: >
  Remix app with auth (Auth0), a Postgres database (Neon), and edge
  functions that personalise responses per-region. Builds on every
  context.

platforms:
  netlify:
    build_command: \"pnpm build\"
    publish: build/client
    functions: netlify/functions
    edge_functions: netlify/edge-functions
    node_version: \"20\"
    env_contexts: [production, deploy-preview, branch-deploy]
    plugins:
      - package: \"@netlify/plugin-remix\"
    redirects_file: public/_redirects
    headers_file: public/_headers

safety:
  min_permissions:
    - network:inbound
    - network:outbound:app-co.auth0.com
    - network:outbound:ep-dark-sun-0.us-east-2.aws.neon.tech
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Neon Postgres connection string.
    secret: true
  - name: AUTH0_CLIENT_ID
    description: Auth0 application client id.
  - name: AUTH0_CLIENT_SECRET
    description: Auth0 application client secret.
    secret: true

deployment:
  targets: [netlify]

metadata:
  license: MIT
  author: { name: App Co., handle: app-co }
  source: { type: git, url: https://github.com/app-co/netlify-full-stack }
  id: com.app-co.netlify-full-stack
""",
    },
}

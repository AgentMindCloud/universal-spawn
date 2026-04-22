"""Vercel — Next.js, edge functions, Image Optimization, Preview Deployments."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "vercel",
    "title": "Vercel",
    "native_config_name": "vercel.json",
    "native_config_lang": "json",

    "lede": (
        "Vercel ships static sites, Next.js apps, Edge Functions, and "
        "background functions from a Git repository. The extension "
        "captures the framework preset, build command, output "
        "directory, regions, per-route function config, and the env "
        "scopes required secrets must exist in."
    ),
    "cares": (
        "The framework preset (`nextjs`, `remix`, `svelte-kit`, "
        "`astro`, `vite`, `other`), install/build commands, output "
        "directory, regions, per-route functions, and env promotion "
        "scopes (`production`, `preview`, `development`)."
    ),
    "extras": (
        "`functions[]` sets per-route runtime, memory, maxDuration. "
        "`env_promotion[]` blocks builds missing required secrets in "
        "a listed scope."
    ),
    "runtimes": (
        "| Route kind | Runtime options |\n"
        "|---|---|\n"
        "| `api/*`            | `nodejs`, `edge`, `python`, `go` |\n"
        "| `app/*` (Next.js)  | Node.js server runtime or React server components |\n"
        "| static assets      | CDN only |\n"
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Project name + card metadata."),
        ("type", "`web-app`, `api-service`, `site`, `container`, `workflow`."),
        ("env_vars_required", "Build blocked when a required non-optional secret is missing in a scope listed by `env_promotion`."),
        ("deployment.targets", "Must include `vercel`."),
        ("platforms.vercel", "Strict; see below."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Default project-name suggestion; user may rename."),
        ("name, description", "Card + dashboard text."),
        ("type", "`web-app`, `api-service`, `site`, `container`, `workflow`."),
        ("safety.min_permissions", "Surfaced in project settings; not sandbox-enforced."),
        ("safety.cost_limit_usd_daily", "Advisory; spend-management honors it when linked."),
        ("env_vars_required", "Build-blocking gate."),
        ("platforms.vercel.framework", "Preset → Vercel builder."),
        ("platforms.vercel.install_command", "Overrides autodetect."),
        ("platforms.vercel.build_command", "Overrides autodetect."),
        ("platforms.vercel.output", "Build output directory."),
        ("platforms.vercel.root_directory", "Monorepo subdir."),
        ("platforms.vercel.regions", "Deploy-region codes (e.g. `iad1`, `cdg1`)."),
        ("platforms.vercel.functions", "Per-route runtime / memory / maxDuration."),
        ("platforms.vercel.env_promotion", "Scopes where required secrets must exist."),
    ],
    "platform_fields": {
        "framework": "Vercel framework preset.",
        "install_command": "Install command override.",
        "build_command": "Build command override.",
        "output": "Output directory.",
        "root_directory": "Monorepo sub-directory.",
        "node_version": "Node.js major version (`18`, `20`, `22`).",
        "regions": "Preferred Vercel regions.",
        "functions": "Per-route runtime/memory/duration.",
        "env_promotion": "Env scopes required secrets must exist in.",
    },

    "schema_body": schema_object(
        properties={
            "framework": enum([
                "nextjs", "next", "remix", "nuxt", "astro", "svelte-kit",
                "vite", "create-react-app", "solid", "docusaurus", "hugo",
                "eleventy", "other",
            ]),
            "install_command": str_prop(),
            "build_command": str_prop(),
            "dev_command": str_prop(),
            "output": str_prop(),
            "root_directory": str_prop(),
            "node_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+){0,2}$"),
            "regions": {
                "type": "array",
                "items": {"type": "string", "pattern": r"^[a-z]{3}[0-9]$"},
            },
            "functions": {
                "type": "array",
                "items": schema_object(
                    required=["match"],
                    properties={
                        "match": str_prop(desc="Glob matching function files (e.g. `api/*.ts`)."),
                        "runtime": enum(["nodejs", "edge", "python", "go"]),
                        "memory_mb": {"type": "integer", "minimum": 128, "maximum": 3009},
                        "max_duration_seconds": {"type": "integer", "minimum": 1, "maximum": 900},
                    },
                ),
            },
            "env_promotion": {
                "type": "array",
                "items": enum(["development", "preview", "production"]),
            },
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Vercel Template
type: web-app
description: Template for a Vercel-targeted universal-spawn manifest.

platforms:
  vercel:
    framework: nextjs
    install_command: \"pnpm install\"
    build_command: \"pnpm build\"
    output: .next
    node_version: \"20\"
    regions: [iad1]
    env_promotion: [production, preview]

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Connection string for the primary database.
    secret: true

deployment:
  targets: [vercel]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/vercel-template }
""",

    "native_config": """
{
  "framework": "nextjs",
  "installCommand": "pnpm install",
  "buildCommand": "pnpm build",
  "outputDirectory": ".next",
  "regions": ["iad1"],
  "functions": {
    "api/*.ts": { "runtime": "edge", "memory": 256, "maxDuration": 15 }
  }
}
""",

    "universal_excerpt": """
platforms:
  vercel:
    framework: nextjs
    install_command: \"pnpm install\"
    build_command: \"pnpm build\"
    output: .next
    regions: [iad1]
    functions:
      - match: \"api/*.ts\"
        runtime: edge
        memory_mb: 256
        max_duration_seconds: 15
""",

    "compatibility_extras": (
        "## What to keep where\n\n"
        "- Use **`vercel.json`** for one-off knobs the schema does not "
        "yet model (`crons[]`, `headers[]`, `redirects[]`, "
        "`rewrites[]`, per-project image-optimization config).\n"
        "- Use **`universal-spawn.yaml`** for everything that makes "
        "the creation discoverable and spawnable on non-Vercel "
        "platforms too (`metadata`, `safety`, `env_vars_required`, "
        "cross-platform `platforms.*` siblings).\n"
        "- A minor-version bump of the universal schema will absorb "
        "`crons[]`, `redirects[]`, and `rewrites[]`; until then they "
        "stay in `vercel.json`."
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Vercel]"
            "(https://vercel.com/button)]"
            "(https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://vercel.com/button" alt="Deploy to Vercel" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Vercel clone URL accepts the following params:\n\n"
            "- `repository-url` (required) — URL-encoded git repo URL.\n"
            "- `project-name` — suggested project name.\n"
            "- `repository-name` — suggested repo name at destination.\n"
            "- `env` — comma-separated env var names to prompt for.\n"
            "- `envDescription` — blurb shown above the env form.\n"
            "- `envLink` — link to docs explaining the env vars.\n\n"
            "Generators MAY fill `env` from `env_vars_required[*].name`."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Preview-deployment gating** — `safe_for_auto_spawn: false` "
        "disables auto-promotion of preview deploys to production.",
        "**Region auto-pick** — `safety.data_residency` picks a "
        "default region if `regions` is unset.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Docs Static Site
type: site
summary: Minimal Astro docs site deployed to Vercel in iad1.
description: >
  A small Astro documentation site. No API routes, one HTTP
  entrypoint serving the root. Default preset; CDN-only.

platforms:
  vercel:
    framework: astro
    install_command: \"pnpm install\"
    build_command: \"pnpm build\"
    output: dist
    node_version: \"20\"
    regions: [iad1]
    env_promotion: [production]

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [vercel]

metadata:
  license: MIT
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/docs-site }
  id: com.docs-team.docs-site
""",
        "serverless-api": """
version: \"1.0\"
name: Edge API
type: api-service
summary: Stateless edge-runtime API + Stripe webhook in three Vercel regions.
description: >
  A stateless HTTP API on Vercel's edge runtime deployed in iad1,
  cdg1, and hnd1. Demonstrates per-route function config and a
  Stripe webhook endpoint.

platforms:
  vercel:
    framework: nextjs
    build_command: \"pnpm build\"
    output: .next
    node_version: \"20\"
    regions: [iad1, cdg1, hnd1]
    functions:
      - match: \"api/**/*.ts\"
        runtime: edge
        memory_mb: 256
        max_duration_seconds: 15
    env_promotion: [production, preview]

safety:
  min_permissions:
    - network:inbound
    - network:outbound:api.stripe.com
  rate_limit_qps: 100
  cost_limit_usd_daily: 50

env_vars_required:
  - name: STRIPE_WEBHOOK_SECRET
    description: Stripe webhook signing secret.
    secret: true

deployment:
  targets: [vercel]

metadata:
  license: Apache-2.0
  author: { name: Edge Co., handle: edge-co }
  source: { type: git, url: https://github.com/edge-co/vercel-edge-api }
  id: com.edge-co.vercel-edge-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Notes App
type: web-app
summary: Full-stack Next.js notes app with Postgres and NextAuth.
description: >
  Public-facing notes app with authentication and a Postgres database.
  Deploys to Vercel with preview deploys, env promotion in both
  production and preview, and one background cron.

platforms:
  vercel:
    framework: nextjs
    install_command: \"pnpm install\"
    build_command: \"pnpm build\"
    output: .next
    node_version: \"20\"
    regions: [iad1, sfo1]
    functions:
      - match: \"api/notes/*.ts\"
        runtime: nodejs
        memory_mb: 512
        max_duration_seconds: 30
    env_promotion: [production, preview]

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true
  - name: NEXTAUTH_SECRET
    description: NextAuth JWT signing secret.
    secret: true
  - name: NEXTAUTH_URL
    description: Canonical deployment URL.

deployment:
  targets: [vercel]

metadata:
  license: MIT
  author: { name: Notes Co., handle: notes-co }
  source: { type: git, url: https://github.com/notes-co/notes-app }
  id: com.notes-co.notes-app
""",
    },
}

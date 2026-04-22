"""Supabase — Postgres + Auth + Storage + Edge Functions + Realtime."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "supabase",
    "title": "Supabase",
    "native_config_name": "supabase/config.toml",
    "native_config_lang": "toml",

    "lede": (
        "Supabase is an open-source Firebase alternative built on "
        "Postgres. A universal-spawn manifest targeting Supabase treats "
        "database provisioning as a first-class deployment concern: "
        "the manifest declares the Postgres schema migrations, the "
        "Auth providers, the Storage buckets, the Realtime channels, "
        "and any Edge Functions — all in one place."
    ),
    "cares": (
        "The project reference, the Postgres migration directory, the "
        "Auth provider list, the storage buckets, the realtime "
        "channels, and the Edge Functions."
    ),
    "extras": (
        "`db.migrations_dir` points at SQL migration files. "
        "`edge_functions[]` lists Deno-based functions deployed via "
        "`supabase functions deploy`."
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Project dashboard."),
        ("type", "`web-app`, `api-service`, `workflow`, `container`."),
        ("env_vars_required", "Supabase secrets + per-function env."),
        ("deployment.targets", "Must include `supabase`."),
        ("platforms.supabase", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Project-slug suggestion."),
        ("name, description", "Dashboard card."),
        ("type", "`web-app`, `api-service`, `workflow`, `container`."),
        ("safety.min_permissions", "Informational."),
        ("safety.cost_limit_usd_daily", "Advisory; enforced at project plan level."),
        ("env_vars_required", "Dashboard secrets + per-function env."),
        ("platforms.supabase.project_ref", "Project reference (20 chars)."),
        ("platforms.supabase.region", "Supabase region."),
        ("platforms.supabase.db", "Postgres configuration + migrations."),
        ("platforms.supabase.auth", "Auth providers + URL."),
        ("platforms.supabase.storage", "Storage buckets."),
        ("platforms.supabase.realtime", "Realtime channels."),
        ("platforms.supabase.edge_functions", "Deno Edge Functions."),
    ],
    "platform_fields": {
        "project_ref": "Project reference.",
        "region": "Supabase region.",
        "db": "Postgres configuration + migrations.",
        "auth": "Auth providers + redirect URLs.",
        "storage": "Storage buckets.",
        "realtime": "Realtime channels.",
        "edge_functions": "Edge Functions.",
    },

    "schema_body": schema_object(
        required=["project_ref"],
        properties={
            "project_ref": str_prop(pattern=r"^[a-z0-9]{20}$"),
            "region": enum([
                "us-east-1", "us-west-1", "eu-west-1", "eu-central-1",
                "ap-southeast-1", "ap-northeast-1", "ap-south-1", "sa-east-1",
            ]),
            "db": schema_object(
                properties={
                    "postgres_major_version": {"type": "integer", "minimum": 14, "maximum": 17},
                    "migrations_dir": str_prop(),
                    "seed_file": str_prop(),
                    "pooler": enum(["transaction", "session", "none"]),
                },
            ),
            "auth": schema_object(
                properties={
                    "providers": {
                        "type": "array",
                        "items": enum(["email", "github", "google", "apple", "twitter", "discord", "azure", "gitlab", "slack", "linkedin_oidc"]),
                    },
                    "site_url": {"type": "string", "format": "uri"},
                    "jwt_expiry_seconds": {"type": "integer", "minimum": 60, "maximum": 604800},
                },
            ),
            "storage": schema_object(
                properties={
                    "buckets": {
                        "type": "array",
                        "items": schema_object(
                            required=["name"],
                            properties={
                                "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,62}$"),
                                "public": bool_prop(False),
                                "max_file_size_mb": {"type": "integer", "minimum": 1, "maximum": 50000},
                                "allowed_mime_types": {"type": "array", "items": str_prop()},
                            },
                        ),
                    },
                },
            ),
            "realtime": schema_object(
                properties={
                    "channels": {
                        "type": "array",
                        "items": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                    },
                },
            ),
            "edge_functions": {
                "type": "array",
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "entrypoint": str_prop(),
                        "verify_jwt": bool_prop(True),
                    },
                ),
            },
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Supabase Template
type: web-app
description: Template for a Supabase-targeted universal-spawn manifest.

platforms:
  supabase:
    project_ref: \"abcdefghijklmnopqrst\"
    region: us-east-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
      seed_file: supabase/seed.sql
      pooler: transaction
    auth:
      providers: [email, github]
      site_url: https://your-app.example.com
      jwt_expiry_seconds: 3600
    storage:
      buckets:
        - { name: avatars, public: true, max_file_size_mb: 5, allowed_mime_types: [image/png, image/jpeg] }
    edge_functions:
      - { name: hello, entrypoint: supabase/functions/hello/index.ts, verify_jwt: true }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: SUPABASE_SERVICE_ROLE_KEY
    description: Service role key for server-side access.
    secret: true

deployment:
  targets: [supabase]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/supabase-template }
""",

    "native_config": """
[db]
major_version = 16

[db.pooler]
enabled = true
default_pool_mode = "transaction"

[auth]
site_url = "http://localhost:3000"
jwt_expiry = 3600

[auth.external.github]
enabled = true

[[storage.buckets]]
name = "avatars"
public = true
file_size_limit = "5MiB"
""",

    "universal_excerpt": """
platforms:
  supabase:
    project_ref: \"abcdefghijklmnopqrst\"
    region: us-east-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
      pooler: transaction
    auth:
      providers: [email, github]
      site_url: https://your-app.example.com
      jwt_expiry_seconds: 3600
    storage:
      buckets:
        - { name: avatars, public: true, max_file_size_mb: 5 }
""",

    "compatibility_extras": (
        "## DB provisioning as first-class\n\n"
        "Supabase treats Postgres migrations as a deployment artifact, "
        "not an afterthought. `db.migrations_dir` is where a consumer "
        "finds `*.sql` files to apply with `supabase db push`. "
        "`seed_file` seeds development data. The universal-spawn "
        "consumer MUST run migrations (in the provided order) before "
        "marking the first deploy healthy."
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Supabase](https://supabase.com/docs/img/deploy-to-supabase.svg)]"
            "(https://supabase.com/dashboard/new?templateUrl=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://supabase.com/dashboard/new?templateUrl=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://supabase.com/docs/img/deploy-to-supabase.svg" alt="Deploy to Supabase" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Supabase dashboard new-project URL accepts:\n\n"
            "- `templateUrl` — URL-encoded git repo URL.\n"
            "- `orgId` — target organization id.\n"
            "- `region` — region slug.\n\n"
            "The template repo's `supabase/config.toml` and "
            "`universal-spawn.yaml` jointly drive provisioning."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Schema diff** — consoles show the SQL diff between the "
        "committed migrations and the current remote schema before "
        "applying `db push`.",
        "**Bucket-policy preview** — storage bucket visibility "
        "(`public: true|false`) pre-selects the Row Level Security "
        "starter policies.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Supabase Landing
type: site
summary: Minimal Supabase-backed landing page with a waitlist form.
description: >
  Static landing page writes signups to a single Postgres table via
  the Supabase JS client. One table migration. Email-only auth.

platforms:
  supabase:
    project_ref: \"landing0000000000000\"
    region: us-east-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
    auth:
      providers: [email]
      site_url: https://landing.example.com
      jwt_expiry_seconds: 3600

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: true

env_vars_required:
  - name: SUPABASE_ANON_KEY
    description: Anon key used from the browser.
    secret: false

deployment:
  targets: [supabase]

metadata:
  license: Apache-2.0
  author: { name: Landing Co., handle: landing-co }
  source: { type: git, url: https://github.com/landing-co/supabase-landing }
  id: com.landing-co.supabase-landing
""",
        "serverless-api": """
version: \"1.0\"
name: Supabase Edge Functions API
type: api-service
summary: Supabase Edge Functions API with three endpoints and JWT verification.
description: >
  Three Deno-based Edge Functions (orders, webhooks, reports). Each
  verifies the incoming JWT. Reads/writes via the service role key.

platforms:
  supabase:
    project_ref: \"ordersapi0000000000a\"
    region: eu-west-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
      pooler: transaction
    edge_functions:
      - { name: orders,   entrypoint: supabase/functions/orders/index.ts,   verify_jwt: true }
      - { name: webhooks, entrypoint: supabase/functions/webhooks/index.ts, verify_jwt: false }
      - { name: reports,  entrypoint: supabase/functions/reports/index.ts,  verify_jwt: true }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: SUPABASE_SERVICE_ROLE_KEY
    description: Service role key.
    secret: true
  - name: STRIPE_WEBHOOK_SECRET
    description: Stripe webhook signing secret.
    secret: true

deployment:
  targets: [supabase]

metadata:
  license: Apache-2.0
  author: { name: Orders Co., handle: orders-co }
  source: { type: git, url: https://github.com/orders-co/supabase-edge-api }
  id: com.orders-co.supabase-edge-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Supabase Full Stack
type: web-app
summary: Full-stack Supabase deployment with Auth, Storage, Realtime, Edge Functions, and migrations.
description: >
  Production-shape Supabase manifest: Postgres with migrations + seed,
  multi-provider auth, two buckets (avatars + uploads), three realtime
  channels, two Edge Functions. EU region for data residency.

platforms:
  supabase:
    project_ref: \"stackco00000000000aa\"
    region: eu-central-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
      seed_file: supabase/seed.sql
      pooler: transaction
    auth:
      providers: [email, github, google, apple]
      site_url: https://app.stack.example.com
      jwt_expiry_seconds: 3600
    storage:
      buckets:
        - { name: avatars, public: true,  max_file_size_mb: 5,  allowed_mime_types: [image/png, image/jpeg] }
        - { name: uploads, public: false, max_file_size_mb: 50, allowed_mime_types: [application/pdf, text/csv] }
    realtime:
      channels: [chat, presence, alerts]
    edge_functions:
      - { name: webhooks, entrypoint: supabase/functions/webhooks/index.ts, verify_jwt: false }
      - { name: admin,    entrypoint: supabase/functions/admin/index.ts,    verify_jwt: true }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: SUPABASE_SERVICE_ROLE_KEY
    description: Service role key.
    secret: true
  - name: STRIPE_WEBHOOK_SECRET
    description: Stripe webhook signing secret.
    secret: true
  - name: SENDGRID_API_KEY
    description: SendGrid API key for transactional email.
    secret: true

deployment:
  targets: [supabase]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co, org: Stack }
  source: { type: git, url: https://github.com/stack-co/supabase-full-stack }
  id: com.stack-co.supabase-full-stack
""",
    },
}

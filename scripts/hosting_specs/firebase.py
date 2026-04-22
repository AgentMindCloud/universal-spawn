"""Firebase — Functions + Hosting + Firestore + Auth + Storage + Extensions."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "firebase",
    "title": "Firebase",
    "native_config_name": "firebase.json",
    "native_config_lang": "json",

    "lede": (
        "Firebase bundles Hosting (static + SSR), Cloud Functions for "
        "Firebase, Firestore / Realtime Database, Auth, Storage, and "
        "App Check under one manifest. DB provisioning is first-class: "
        "the manifest lists Firestore indexes, security rules, and "
        "seed data alongside the rest of the deployment."
    ),
    "cares": (
        "The project id, which services are enabled (`hosting`, "
        "`functions`, `firestore`, `realtime_db`, `storage`, `auth`, "
        "`extensions`), and per-service configuration."
    ),
    "extras": (
        "`firestore.rules_file` and `firestore.indexes_file` drive "
        "security + indexes. `extensions[]` installs official "
        "Firebase Extensions (e.g. `delete-user-data`, `resize-images`)."
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Firebase project metadata."),
        ("type", "`web-app`, `api-service`, `workflow`, `bot`, `site`."),
        ("env_vars_required", "Firebase secrets manager (Functions config)."),
        ("deployment.targets", "Must include `firebase`."),
        ("platforms.firebase", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Firebase project slug suggestion."),
        ("name, description", "Card."),
        ("type", "`web-app`, `api-service`, `workflow`, `bot`, `site`."),
        ("safety.min_permissions", "Informational."),
        ("safety.cost_limit_usd_daily", "Advisory; Blaze plan budget alert honors it."),
        ("env_vars_required", "Functions config + secrets."),
        ("platforms.firebase.project_id", "Firebase project id."),
        ("platforms.firebase.region", "Primary region."),
        ("platforms.firebase.hosting", "Hosting configuration."),
        ("platforms.firebase.functions", "Cloud Functions for Firebase."),
        ("platforms.firebase.firestore", "Firestore rules + indexes."),
        ("platforms.firebase.realtime_db", "Realtime Database rules."),
        ("platforms.firebase.storage", "Storage rules + buckets."),
        ("platforms.firebase.auth", "Auth providers."),
        ("platforms.firebase.extensions", "Firebase Extensions."),
    ],
    "platform_fields": {
        "project_id": "Firebase project id.",
        "region": "Primary region (for Functions).",
        "hosting": "Hosting block.",
        "functions": "Cloud Functions block.",
        "firestore": "Firestore block (rules + indexes).",
        "realtime_db": "Realtime Database rules.",
        "storage": "Storage rules + buckets.",
        "auth": "Auth providers.",
        "extensions": "Firebase Extensions.",
    },

    "schema_body": schema_object(
        required=["project_id"],
        properties={
            "project_id": str_prop(pattern=r"^[a-z][a-z0-9-]{5,29}$"),
            "region": enum([
                "us-central1", "us-east1", "us-east4", "us-west1", "us-west2",
                "europe-west1", "europe-west2", "europe-west3", "europe-west4",
                "asia-northeast1", "asia-east1", "asia-south1",
                "southamerica-east1", "australia-southeast1",
            ]),
            "hosting": schema_object(
                properties={
                    "site_id": str_prop(),
                    "public_dir": str_prop(),
                    "ssr": bool_prop(False),
                    "framework": enum(["next", "nuxt", "astro", "svelte-kit", "angular", "static"]),
                    "rewrites_to_function": str_prop(),
                },
            ),
            "functions": schema_object(
                properties={
                    "source": str_prop(),
                    "runtime": enum(["nodejs20", "nodejs22", "python311", "python312"]),
                    "functions_list": {
                        "type": "array",
                        "items": schema_object(
                            required=["name"],
                            properties={
                                "name": str_prop(pattern=r"^[a-z][a-zA-Z0-9]{0,62}$"),
                                "trigger": enum(["https", "firestore", "auth", "storage", "pubsub", "scheduler"]),
                                "memory_mb": {"type": "integer", "minimum": 128, "maximum": 32768},
                                "timeout_seconds": {"type": "integer", "minimum": 1, "maximum": 540},
                            },
                        ),
                    },
                },
            ),
            "firestore": schema_object(
                properties={
                    "rules_file": str_prop(),
                    "indexes_file": str_prop(),
                    "database_id": str_prop(),
                },
            ),
            "realtime_db": schema_object(
                properties={
                    "rules_file": str_prop(),
                    "instance": str_prop(),
                },
            ),
            "storage": schema_object(
                properties={
                    "rules_file": str_prop(),
                    "default_bucket": str_prop(),
                },
            ),
            "auth": schema_object(
                properties={
                    "providers": {
                        "type": "array",
                        "items": enum(["email", "google.com", "facebook.com", "twitter.com", "github.com", "apple.com", "microsoft.com", "phone", "anonymous"]),
                    },
                },
            ),
            "extensions": {
                "type": "array",
                "items": schema_object(
                    required=["ref"],
                    properties={
                        "ref": str_prop(desc="Extension reference, e.g. firebase/delete-user-data@0.1.24"),
                        "instance_id": str_prop(),
                    },
                ),
            },
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Firebase Template
type: web-app
description: Template for a Firebase-targeted universal-spawn manifest.

platforms:
  firebase:
    project_id: your-firebase-project
    region: us-central1
    hosting:
      site_id: default
      public_dir: dist
      ssr: false
      framework: astro
    functions:
      source: functions
      runtime: nodejs22
      functions_list:
        - { name: onUserCreate, trigger: auth, memory_mb: 256, timeout_seconds: 30 }
    firestore:
      rules_file: firestore.rules
      indexes_file: firestore.indexes.json
    auth:
      providers: [email, google.com]

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: SENDGRID_KEY
    description: SendGrid key for transactional email.
    secret: true

deployment:
  targets: [firebase]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/firebase-template }
""",

    "native_config": """
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"]
  },
  "functions": {
    "source": "functions",
    "runtime": "nodejs22"
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "storage": { "rules": "storage.rules" }
}
""",

    "universal_excerpt": """
platforms:
  firebase:
    project_id: your-firebase-project
    region: us-central1
    hosting:
      public_dir: dist
      ssr: false
    functions:
      source: functions
      runtime: nodejs22
    firestore:
      rules_file: firestore.rules
      indexes_file: firestore.indexes.json
    storage:
      rules_file: storage.rules
""",

    "compatibility_extras": (
        "## DB provisioning as first-class\n\n"
        "Firestore's `rules_file` and `indexes_file` are deployment "
        "artifacts — a consumer MUST apply them before marking the "
        "deploy healthy. Same for `realtime_db.rules_file` and "
        "`storage.rules_file`. Rules changes that deny existing "
        "queries block the deploy unless the consumer is told to "
        "force through via `safety.safe_for_auto_spawn: true`."
    ),

    "deploy_button": {
        "markdown": (
            "[![Try it on Firebase](https://img.shields.io/badge/Try%20it%20on-Firebase-orange)]"
            "(https://console.firebase.google.com/?githubImport=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://console.firebase.google.com/?githubImport=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://img.shields.io/badge/Try%20it%20on-Firebase-orange" alt="Try it on Firebase" />\n'
            '</a>'
        ),
        "params_doc": (
            "Firebase does not ship an official Deploy-to-Firebase "
            "button. The common pattern links to the Firebase console "
            "with a `githubImport` query param. Generators SHOULD "
            "document that the user needs to run `firebase init` and "
            "`firebase deploy` locally after cloning."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Rules diff** — consoles show the Firestore / Storage rules "
        "diff before applying. A rule change that denies a previously-"
        "allowed query blocks the deploy.",
        "**Extension manifest** — `extensions[]` becomes a one-click "
        "install list; the extension inputs are pre-filled from "
        "`env_vars_required`.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Firebase Hosting Astro
type: site
summary: Minimal Astro static site on Firebase Hosting.
description: Static Astro site. No Functions. Default site id.

platforms:
  firebase:
    project_id: astro-landing-dev
    region: us-central1
    hosting:
      site_id: default
      public_dir: dist
      ssr: false
      framework: astro

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [firebase]

metadata:
  license: Apache-2.0
  author: { name: Landing Co., handle: landing-co }
  source: { type: git, url: https://github.com/landing-co/firebase-astro }
  id: com.landing-co.firebase-astro
""",
        "serverless-api": """
version: \"1.0\"
name: Firebase Functions API
type: api-service
summary: Firebase Cloud Functions API with Firestore + scheduler.
description: >
  HTTPS + Firestore + scheduler triggers. Firestore rules + indexes
  shipped alongside. One extension: delete-user-data.

platforms:
  firebase:
    project_id: orders-api-prod
    region: us-central1
    functions:
      source: functions
      runtime: nodejs22
      functions_list:
        - { name: createOrder, trigger: https,      memory_mb: 512, timeout_seconds: 30 }
        - { name: onOrder,     trigger: firestore,  memory_mb: 256, timeout_seconds: 30 }
        - { name: nightlyRoll, trigger: scheduler,  memory_mb: 256, timeout_seconds: 540 }
    firestore:
      rules_file: firestore.rules
      indexes_file: firestore.indexes.json
    extensions:
      - { ref: \"firebase/delete-user-data@0.1.24\", instance_id: delete-user-data }

safety:
  min_permissions: [network:outbound]
  rate_limit_qps: 100

env_vars_required:
  - name: STRIPE_SECRET
    description: Stripe server key.
    secret: true

deployment:
  targets: [firebase]

metadata:
  license: Apache-2.0
  author: { name: Orders Co., handle: orders-co }
  source: { type: git, url: https://github.com/orders-co/firebase-functions-api }
  id: com.orders-co.firebase-functions-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Firebase Full Stack
type: web-app
summary: Full-stack Firebase deployment spanning Hosting, Functions, Firestore, Storage, Auth, and Extensions.
description: >
  Production Firebase manifest: Hosting (SSR Next), Functions (six
  triggers), Firestore (rules + indexes + named database), Storage
  (rules), Realtime DB (legacy channel), multi-provider Auth, and
  three Extensions. EU region.

platforms:
  firebase:
    project_id: stackco-prod
    region: europe-west1
    hosting:
      site_id: default
      public_dir: out
      ssr: true
      framework: next
      rewrites_to_function: ssr
    functions:
      source: functions
      runtime: nodejs22
      functions_list:
        - { name: ssr,              trigger: https,     memory_mb: 1024, timeout_seconds: 60 }
        - { name: onUserCreate,     trigger: auth,      memory_mb: 256,  timeout_seconds: 30 }
        - { name: onOrder,          trigger: firestore, memory_mb: 512,  timeout_seconds: 60 }
        - { name: onUpload,         trigger: storage,   memory_mb: 512,  timeout_seconds: 120 }
        - { name: dailyRoll,        trigger: scheduler, memory_mb: 256,  timeout_seconds: 540 }
        - { name: webhookListener,  trigger: pubsub,    memory_mb: 256,  timeout_seconds: 60 }
    firestore:
      rules_file: firestore.rules
      indexes_file: firestore.indexes.json
      database_id: primary
    realtime_db:
      rules_file: database.rules.json
      instance: stackco-prod-rtdb
    storage:
      rules_file: storage.rules
      default_bucket: stackco-prod.appspot.com
    auth:
      providers: [email, google.com, apple.com, microsoft.com]
    extensions:
      - { ref: \"firebase/delete-user-data@0.1.24\",     instance_id: delete-user-data }
      - { ref: \"firebase/resize-images@0.2.4\",         instance_id: resize-avatars }
      - { ref: \"firebase/firestore-send-email@0.2.1\",  instance_id: send-email }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: STRIPE_SECRET
    description: Stripe server key.
    secret: true
  - name: SENDGRID_KEY
    description: SendGrid key for transactional email (used by the send-email extension).
    secret: true

deployment:
  targets: [firebase]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co, org: Stack }
  source: { type: git, url: https://github.com/stack-co/firebase-full-stack }
  id: com.stack-co.firebase-full-stack
""",
    },
}

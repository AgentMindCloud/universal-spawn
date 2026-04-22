"""GCP — Cloud Run + Cloud Functions + App Engine."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "gcp",
    "title": "Google Cloud (GCP)",
    "native_config_name": "app.yaml / cloudbuild.yaml",
    "native_config_lang": "yaml",

    "lede": (
        "GCP ships three primary application hosting surfaces that "
        "fit a universal-spawn manifest: Cloud Run (managed "
        "containers), Cloud Functions (single-file serverless), and "
        "App Engine (managed platform). The extension picks one via "
        "`runtime` and models the surface-specific fields."
    ),
    "cares": (
        "The runtime (`cloud_run`, `cloud_functions`, `app_engine`), "
        "the project id, the region, and the surface-specific block."
    ),
    "extras": (
        "`cloud_run.ingress` controls the ingress policy. "
        "`cloud_functions.trigger` attaches an event source "
        "(`http`, `pubsub`, `storage`, `firestore`, `scheduler`)."
    ),
    "runtimes": (
        "| Runtime           | GCP service       | Typical shape                 |\n"
        "|-------------------|-------------------|-------------------------------|\n"
        "| `cloud_run`       | Cloud Run         | Managed container web service |\n"
        "| `cloud_functions` | Cloud Functions   | Single-file serverless fn     |\n"
        "| `app_engine`      | App Engine Standard / Flex | Managed platform     |\n"
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Service / app card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`, `site`."),
        ("env_vars_required", "Secret Manager secrets."),
        ("deployment.targets", "Must include `gcp`."),
        ("platforms.gcp", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Resource name suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.min_permissions", "Mapped onto the service-account IAM role."),
        ("safety.cost_limit_usd_daily", "Advisory; Budget alerts honor it."),
        ("env_vars_required", "Secret Manager."),
        ("platforms.gcp.runtime", "`cloud_run`, `cloud_functions`, `app_engine`."),
        ("platforms.gcp.project_id", "GCP project id."),
        ("platforms.gcp.region", "GCP region."),
        ("platforms.gcp.service_account", "Service account email override."),
        ("platforms.gcp.cloud_run", "Cloud Run service block."),
        ("platforms.gcp.cloud_functions", "Cloud Function block."),
        ("platforms.gcp.app_engine", "App Engine block."),
    ],
    "platform_fields": {
        "runtime": "`cloud_run`, `cloud_functions`, `app_engine`.",
        "project_id": "GCP project id.",
        "region": "GCP region.",
        "service_account": "Service-account email override.",
        "cloud_run": "Cloud Run service block.",
        "cloud_functions": "Cloud Function block.",
        "app_engine": "App Engine service block.",
    },

    "schema_body": schema_object(
        required=["runtime", "region"],
        properties={
            "runtime": enum(["cloud_run", "cloud_functions", "app_engine"]),
            "project_id": str_prop(pattern=r"^[a-z][a-z0-9-]{4,29}$"),
            "region": str_prop(pattern=r"^[a-z]+-[a-z]+[0-9]*$"),
            "service_account": str_prop(pattern=r"^[a-z][a-z0-9-]*@[a-z0-9.-]+\.iam\.gserviceaccount\.com$"),
            "cloud_run": schema_object(
                properties={
                    "service_name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,62}$"),
                    "image": str_prop(),
                    "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                    "cpu": enum(["0.5", "1", "2", "4", "8"]),
                    "memory": enum(["128Mi", "256Mi", "512Mi", "1Gi", "2Gi", "4Gi", "8Gi", "16Gi", "32Gi"]),
                    "concurrency": {"type": "integer", "minimum": 1, "maximum": 1000},
                    "min_instances": {"type": "integer", "minimum": 0, "maximum": 1000},
                    "max_instances": {"type": "integer", "minimum": 1, "maximum": 1000},
                    "ingress": enum(["all", "internal", "internal-and-cloud-load-balancing"]),
                    "allow_unauthenticated": bool_prop(False),
                },
            ),
            "cloud_functions": schema_object(
                properties={
                    "function_name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,62}$"),
                    "runtime_id": enum(["nodejs20", "nodejs22", "python311", "python312", "go122", "java21"]),
                    "entry_point": str_prop(),
                    "memory_mb": {"type": "integer", "minimum": 128, "maximum": 32768},
                    "timeout_seconds": {"type": "integer", "minimum": 1, "maximum": 3600},
                    "trigger": schema_object(
                        properties={
                            "kind": enum(["http", "pubsub", "storage", "firestore", "scheduler"]),
                            "topic": str_prop(),
                            "bucket": str_prop(),
                            "firestore_document": str_prop(),
                            "schedule": str_prop(),
                        },
                    ),
                },
            ),
            "app_engine": schema_object(
                properties={
                    "service": str_prop(),
                    "runtime_id": enum(["nodejs20", "nodejs22", "python311", "python312", "go122", "java21", "custom"]),
                    "instance_class": enum(["F1", "F2", "F4", "F4_1G", "B1", "B2", "B4", "B4_1G", "B8"]),
                    "scaling": enum(["automatic", "basic", "manual"]),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: GCP Template
type: api-service
description: Template for a GCP-targeted universal-spawn manifest.

platforms:
  gcp:
    runtime: cloud_run
    project_id: your-project
    region: us-central1
    cloud_run:
      service_name: hello
      image: us-central1-docker.pkg.dev/your-project/images/hello:latest
      port: 8080
      cpu: \"1\"
      memory: 512Mi
      concurrency: 80
      min_instances: 0
      max_instances: 10
      ingress: all
      allow_unauthenticated: true

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: API_SECRET
    description: Stored in Secret Manager.
    secret: true

deployment:
  targets: [gcp]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/gcp-template }
""",

    "native_config": """
runtime: nodejs22
instance_class: F2
automatic_scaling:
  target_cpu_utilization: 0.65
  max_instances: 10
""",

    "universal_excerpt": """
platforms:
  gcp:
    runtime: app_engine
    project_id: your-project
    region: us-central
    app_engine:
      service: default
      runtime_id: nodejs22
      instance_class: F2
      scaling: automatic
""",

    "compatibility_extras": (
        "## Relation to existing GCP configs\n\n"
        "- **Cloud Run** normally uses `gcloud run deploy` flags; "
        "this extension models those flags declaratively so a "
        "universal-spawn consumer can emit the equivalent command.\n"
        "- **Cloud Functions** traditionally uses `gcloud functions "
        "deploy` flags or a `functions-framework` entry — again, "
        "declaratively captured here.\n"
        "- **App Engine** uses `app.yaml`; the side-by-side above "
        "shows how App Engine content maps to the extension."
    ),

    "deploy_button": {
        "markdown": (
            "[![Run on Google Cloud](https://deploy.cloud.run/button.svg)]"
            "(https://deploy.cloud.run/?git_repo=https%3A%2F%2Fgithub.com%2F"
            "yourhandle%2Fyour-project)"
        ),
        "html": (
            '<a href="https://deploy.cloud.run/?git_repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">\n'
            '  <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" />\n'
            '</a>'
        ),
        "params_doc": (
            "The `deploy.cloud.run` endpoint accepts:\n\n"
            "- `git_repo` — URL-encoded git repo URL.\n"
            "- `dir` — subdirectory with the Dockerfile.\n"
            "- `revision` — branch, tag, or commit.\n\n"
            "The button targets Cloud Run only; Cloud Functions and "
            "App Engine deploys require `gcloud` today."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**IAM minimisation** — `safety.min_permissions` narrows the "
        "service-account IAM bindings to the smallest envelope.",
        "**Region allowlist** — `safety.data_residency` constrains "
        "the allowed GCP regions.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: GCP App Engine Static
type: site
summary: Minimal static site on App Engine Standard using the static handler.
description: Single default App Engine service serving static assets.

platforms:
  gcp:
    runtime: app_engine
    project_id: your-project
    region: us-central
    app_engine:
      service: default
      runtime_id: nodejs22
      instance_class: F1
      scaling: automatic

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [gcp]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/gcp-app-engine-static }
  id: com.static-co.gcp-app-engine-static
""",
        "serverless-api": """
version: \"1.0\"
name: GCP Cloud Functions Webhook
type: api-service
summary: Pub/Sub-triggered Cloud Function.
description: Python 3.12 Cloud Function subscribed to a Pub/Sub topic.

platforms:
  gcp:
    runtime: cloud_functions
    project_id: your-project
    region: us-central1
    cloud_functions:
      function_name: on-order-placed
      runtime_id: python312
      entry_point: on_order_placed
      memory_mb: 512
      timeout_seconds: 60
      trigger:
        kind: pubsub
        topic: projects/your-project/topics/orders-placed

safety:
  min_permissions: [network:outbound]
  rate_limit_qps: 50

env_vars_required:
  - name: DDB_WEBHOOK_SECRET
    description: Signing secret stored in Secret Manager.
    secret: true

deployment:
  targets: [gcp]

metadata:
  license: Apache-2.0
  author: { name: Events Co., handle: events-co }
  source: { type: git, url: https://github.com/events-co/gcp-pubsub-function }
  id: com.events-co.gcp-pubsub-function
""",
        "full-stack-app": """
version: \"1.0\"
name: GCP Cloud Run App
type: web-app
summary: Full-stack Cloud Run deployment with custom service account and Secret Manager.
description: >
  Cloud Run service with 1 vCPU / 1Gi, min 1 / max 20 instances,
  internal ingress plus load balancer, and a dedicated service
  account. DATABASE_URL stored in Secret Manager.

platforms:
  gcp:
    runtime: cloud_run
    project_id: acme-prod
    region: europe-west4
    service_account: app@acme-prod.iam.gserviceaccount.com
    cloud_run:
      service_name: web
      image: europe-west4-docker.pkg.dev/acme-prod/images/web:latest
      port: 3000
      cpu: \"1\"
      memory: 1Gi
      concurrency: 80
      min_instances: 1
      max_instances: 20
      ingress: internal-and-cloud-load-balancing
      allow_unauthenticated: false

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 50
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string (Secret Manager).
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret (Secret Manager).
    secret: true

deployment:
  targets: [gcp]

metadata:
  license: MIT
  author: { name: Acme IT, handle: acme-it, org: Acme }
  source: { type: git, url: https://github.com/acme-it/gcp-cloud-run-app }
  id: com.acme-it.gcp-cloud-run-app
""",
    },
}

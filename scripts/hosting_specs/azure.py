"""Azure — Static Web Apps + Functions + Container Apps."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "azure",
    "title": "Azure",
    "native_config_name": "azure.yaml (azd) / function.json",
    "native_config_lang": "yaml",

    "lede": (
        "Azure's three modern application hosting surfaces are Static "
        "Web Apps (Jamstack + SWA Functions), Azure Functions (full "
        "serverless), and Azure Container Apps (managed Kubernetes-"
        "backed containers). The extension picks one runtime and "
        "models its shape; the Azure Developer CLI (`azd`) file drives "
        "provisioning."
    ),
    "cares": (
        "The runtime (`static_web_apps`, `functions`, `container_apps`), "
        "the subscription / resource-group context, and the runtime-"
        "specific block."
    ),
    "extras": (
        "`static_web_apps.api_location` enables SWA Functions. "
        "`container_apps.ingress.external` toggles public ingress. "
        "`functions.trigger` selects the trigger binding."
    ),
    "runtimes": (
        "| Runtime             | Azure service          | Typical shape                      |\n"
        "|---------------------|------------------------|------------------------------------|\n"
        "| `static_web_apps`   | Static Web Apps        | Jamstack site + optional Functions |\n"
        "| `functions`         | Azure Functions        | Event-triggered serverless         |\n"
        "| `container_apps`    | Azure Container Apps   | Managed containerized services     |\n"
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Resource card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`, `site`."),
        ("env_vars_required", "Azure Key Vault / App Service settings."),
        ("deployment.targets", "Must include `azure`."),
        ("platforms.azure", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Resource-name suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.min_permissions", "Mapped onto managed-identity role assignments."),
        ("safety.cost_limit_usd_daily", "Advisory; Cost Management budgets honor it."),
        ("env_vars_required", "Key Vault / App Service settings."),
        ("platforms.azure.runtime", "`static_web_apps`, `functions`, `container_apps`."),
        ("platforms.azure.location", "Azure location."),
        ("platforms.azure.resource_group", "Resource group."),
        ("platforms.azure.static_web_apps", "SWA block."),
        ("platforms.azure.functions", "Functions block."),
        ("platforms.azure.container_apps", "Container Apps block."),
    ],
    "platform_fields": {
        "runtime": "`static_web_apps`, `functions`, `container_apps`.",
        "location": "Azure location (e.g. `westus2`).",
        "resource_group": "Resource group name.",
        "static_web_apps": "Static Web Apps block.",
        "functions": "Azure Functions block.",
        "container_apps": "Container Apps block.",
    },

    "schema_body": schema_object(
        required=["runtime", "location"],
        properties={
            "runtime": enum(["static_web_apps", "functions", "container_apps"]),
            "location": str_prop(pattern=r"^[a-z0-9]+$"),
            "resource_group": str_prop(pattern=r"^[A-Za-z0-9_.()-]{1,90}$"),
            "static_web_apps": schema_object(
                properties={
                    "app_location": str_prop(),
                    "api_location": str_prop(),
                    "output_location": str_prop(),
                    "app_build_command": str_prop(),
                    "sku": enum(["Free", "Standard"]),
                },
            ),
            "functions": schema_object(
                properties={
                    "plan": enum(["Consumption", "Premium", "Dedicated", "FlexConsumption"]),
                    "runtime_id": enum(["node-20", "node-22", "python-3.11", "python-3.12", "dotnet-isolated-8.0", "java-21"]),
                    "trigger": schema_object(
                        properties={
                            "kind": enum(["http", "timer", "queue", "blob", "servicebus", "eventgrid"]),
                            "queue_name": str_prop(),
                            "schedule": str_prop(),
                            "blob_path": str_prop(),
                        },
                    ),
                },
            ),
            "container_apps": schema_object(
                properties={
                    "environment": str_prop(),
                    "image": str_prop(),
                    "cpu": enum(["0.25", "0.5", "0.75", "1.0", "1.25", "1.5", "1.75", "2.0"]),
                    "memory": enum(["0.5Gi", "1.0Gi", "1.5Gi", "2.0Gi", "2.5Gi", "3.0Gi", "3.5Gi", "4.0Gi"]),
                    "min_replicas": {"type": "integer", "minimum": 0, "maximum": 30},
                    "max_replicas": {"type": "integer", "minimum": 1, "maximum": 300},
                    "ingress": schema_object(
                        properties={
                            "external": bool_prop(True),
                            "target_port": {"type": "integer", "minimum": 1, "maximum": 65535},
                            "transport": enum(["auto", "http", "http2", "tcp"]),
                        },
                    ),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Azure Template
type: web-app
description: Template for an Azure-targeted universal-spawn manifest.

platforms:
  azure:
    runtime: container_apps
    location: westus2
    resource_group: rg-your-app
    container_apps:
      environment: cae-your-app
      image: yourregistry.azurecr.io/your-app:latest
      cpu: \"0.5\"
      memory: 1.0Gi
      min_replicas: 1
      max_replicas: 10
      ingress:
        external: true
        target_port: 8080
        transport: auto

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Connection string (Key Vault).
    secret: true

deployment:
  targets: [azure]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/azure-template }
""",

    "native_config": """
name: your-app
metadata:
  template: your-template@0.0.1
services:
  web:
    project: ./src
    language: ts
    host: containerapp
""",

    "universal_excerpt": """
platforms:
  azure:
    runtime: container_apps
    location: westus2
    resource_group: rg-your-app
    container_apps:
      environment: cae-your-app
      image: yourregistry.azurecr.io/your-app:latest
      cpu: \"0.5\"
      memory: 1.0Gi
      min_replicas: 1
      max_replicas: 10
      ingress: { external: true, target_port: 8080, transport: auto }
""",

    "compatibility_extras": (
        "## Relation to Azure Developer CLI (`azd`)\n\n"
        "`azure.yaml` captures which azd template to apply and which "
        "services exist; the detailed runtime config lives in the "
        "Bicep modules `azd` generates. `platforms.azure` carries that "
        "detailed runtime config in one place so a consumer can emit "
        "Bicep, `az deployment group create`, or direct REST calls."
    ),

    "deploy_button": {
        "markdown": (
            "[![Deploy to Azure](https://aka.ms/deploytoazurebutton)]"
            "(https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2F"
            "yourhandle%2Fyour-project%2Fmain%2Fazuredeploy.json)"
        ),
        "html": (
            '<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fyourhandle%2Fyour-project%2Fmain%2Fazuredeploy.json">\n'
            '  <img src="https://aka.ms/deploytoazurebutton" alt="Deploy to Azure" />\n'
            '</a>'
        ),
        "params_doc": (
            "The Azure portal deploy URL accepts:\n\n"
            "- `uri` — URL-encoded URL to an ARM template JSON.\n\n"
            "Static Web Apps and Functions have their own deployment "
            "shortcuts; container-based deployments typically use an "
            "ARM / Bicep template."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**Managed-identity minimisation** — `safety.min_permissions` "
        "narrows the managed-identity role assignments applied at "
        "provision time.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: Azure Static Web App
type: site
summary: Minimal Azure Static Web Apps site with no API.
description: Astro static site on SWA Free plan.

platforms:
  azure:
    runtime: static_web_apps
    location: westeurope
    resource_group: rg-docs
    static_web_apps:
      app_location: /
      output_location: dist
      app_build_command: \"pnpm build\"
      sku: Free

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [azure]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/azure-swa-docs }
  id: com.docs-team.azure-swa-docs
""",
        "serverless-api": """
version: \"1.0\"
name: Azure Functions Queue Worker
type: api-service
summary: Queue-triggered Azure Function on the Premium plan.
description: Node 22 Azure Function consuming a Service Bus queue.

platforms:
  azure:
    runtime: functions
    location: northeurope
    resource_group: rg-events
    functions:
      plan: Premium
      runtime_id: node-22
      trigger:
        kind: servicebus
        queue_name: orders

safety:
  min_permissions: [network:outbound]

env_vars_required:
  - name: SERVICEBUS_CONNECTION_STRING
    description: Service Bus connection string (Key Vault reference).
    secret: true

deployment:
  targets: [azure]

metadata:
  license: Apache-2.0
  author: { name: Events Co., handle: events-co }
  source: { type: git, url: https://github.com/events-co/azure-queue-worker }
  id: com.events-co.azure-queue-worker
""",
        "full-stack-app": """
version: \"1.0\"
name: Azure Container Apps Full Stack
type: web-app
summary: Container Apps full-stack deployment with external ingress + managed identity.
description: >
  Production web service on Azure Container Apps: 1 vCPU / 2Gi,
  min 1 / max 20 replicas, HTTP/2 ingress. Database connection via
  Key Vault reference.

platforms:
  azure:
    runtime: container_apps
    location: westus2
    resource_group: rg-acme-prod
    container_apps:
      environment: cae-acme-prod
      image: acmeprod.azurecr.io/web:latest
      cpu: \"1.0\"
      memory: 2.0Gi
      min_replicas: 1
      max_replicas: 20
      ingress:
        external: true
        target_port: 3000
        transport: http2

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 50
  safe_for_auto_spawn: false
  data_residency: [us]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string (Key Vault reference).
    secret: true
  - name: SESSION_SECRET
    description: Session cookie signing secret (Key Vault reference).
    secret: true

deployment:
  targets: [azure]

metadata:
  license: MIT
  author: { name: Acme IT, handle: acme-it, org: Acme }
  source: { type: git, url: https://github.com/acme-it/azure-container-apps-web }
  id: com.acme-it.azure-container-apps-web
""",
    },
}

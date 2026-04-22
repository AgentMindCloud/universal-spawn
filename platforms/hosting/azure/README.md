# Azure — universal-spawn platform extension

Azure's three modern application hosting surfaces are Static Web Apps (Jamstack + SWA Functions), Azure Functions (full serverless), and Azure Container Apps (managed Kubernetes-backed containers). The extension picks one runtime and models its shape; the Azure Developer CLI (`azd`) file drives provisioning.

## What this platform cares about

The runtime (`static_web_apps`, `functions`, `container_apps`), the subscription / resource-group context, and the runtime-specific block.

## What platform-specific extras unlock

`static_web_apps.api_location` enables SWA Functions. `container_apps.ingress.external` toggles public ingress. `functions.trigger` selects the trigger binding.

## Supported runtime targets

| Runtime             | Azure service          | Typical shape                      |
|---------------------|------------------------|------------------------------------|
| `static_web_apps`   | Static Web Apps        | Jamstack site + optional Functions |
| `functions`         | Azure Functions        | Event-triggered serverless         |
| `container_apps`    | Azure Container Apps   | Managed containerized services     |


## Compatibility table

| Manifest field | Azure behavior |
|---|---|
| `version` | Required. |
| `name, description` | Resource card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`, `site`. |
| `env_vars_required` | Azure Key Vault / App Service settings. |
| `deployment.targets` | Must include `azure`. |
| `platforms.azure` | Strict. |

### `platforms.azure` fields

| Field | Purpose |
|---|---|
| `platforms.azure.runtime` | `static_web_apps`, `functions`, `container_apps`. |
| `platforms.azure.location` | Azure location (e.g. `westus2`). |
| `platforms.azure.resource_group` | Resource group name. |
| `platforms.azure.static_web_apps` | Static Web Apps block. |
| `platforms.azure.functions` | Azure Functions block. |
| `platforms.azure.container_apps` | Container Apps block. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `azure.yaml (azd) / function.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Azure consumer SHOULD offer manifests that
declare `platforms.azure`.

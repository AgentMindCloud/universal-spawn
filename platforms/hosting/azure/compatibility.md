# Azure compatibility — field-by-field

Azure already has a native config format
(`azure.yaml (azd) / function.json`). universal-spawn does not replace it; the two
coexist. A Azure consumer reads both:

- `azure.yaml (azd) / function.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.azure`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `azure.yaml (azd) / function.json` (provider-native)

```yaml
name: your-app
metadata:
  template: your-template@0.0.1
services:
  web:
    project: ./src
    language: ts
    host: containerapp
```

### `universal-spawn.yaml` (platforms.azure block)

```yaml
platforms:
  azure:
    runtime: container_apps
    location: westus2
    resource_group: rg-your-app
    container_apps:
      environment: cae-your-app
      image: yourregistry.azurecr.io/your-app:latest
      cpu: "0.5"
      memory: 1.0Gi
      min_replicas: 1
      max_replicas: 10
      ingress: { external: true, target_port: 8080, transport: auto }
```

## Field-by-field

| universal-spawn v1.0 field | Azure behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Resource-name suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.min_permissions` | Mapped onto managed-identity role assignments. |
| `safety.cost_limit_usd_daily` | Advisory; Cost Management budgets honor it. |
| `env_vars_required` | Key Vault / App Service settings. |
| `platforms.azure.runtime` | `static_web_apps`, `functions`, `container_apps`. |
| `platforms.azure.location` | Azure location. |
| `platforms.azure.resource_group` | Resource group. |
| `platforms.azure.static_web_apps` | SWA block. |
| `platforms.azure.functions` | Functions block. |
| `platforms.azure.container_apps` | Container Apps block. |

## Relation to Azure Developer CLI (`azd`)

`azure.yaml` captures which azd template to apply and which services exist; the detailed runtime config lives in the Bicep modules `azd` generates. `platforms.azure` carries that detailed runtime config in one place so a consumer can emit Bicep, `az deployment group create`, or direct REST calls.

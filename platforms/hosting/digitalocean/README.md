# DigitalOcean — universal-spawn platform extension

DigitalOcean's managed application surfaces are App Platform (buildpack + container web services, workers, and static sites) and Functions (serverless). The extension models both with `surface: app_platform` or `surface: functions`.

## What this platform cares about

The surface, the region, the service list (App Platform) or function list (Functions), and managed database attachments.

## What platform-specific extras unlock

`services[]` covers App Platform's `web`, `worker`, `job`, `static_site` kinds. `databases[]` attaches managed Postgres / MySQL / Redis clusters.

## Compatibility table

| Manifest field | DigitalOcean behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `site`. |
| `env_vars_required` | Per-component environment variables. |
| `deployment.targets` | Must include `digitalocean`. |
| `platforms.digitalocean` | Strict. |

### `platforms.digitalocean` fields

| Field | Purpose |
|---|---|
| `platforms.digitalocean.surface` | `app_platform` or `functions`. |
| `platforms.digitalocean.region` | Region slug. |
| `platforms.digitalocean.services` | App Platform components. |
| `platforms.digitalocean.databases` | Managed databases. |
| `platforms.digitalocean.functions` | Functions runtime config. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `app.yaml (App Platform) / project.yml (Functions)`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant DigitalOcean consumer SHOULD offer manifests that
declare `platforms.digitalocean`.

# Heroku — universal-spawn platform extension

Heroku's `app.json` describes everything the Heroku Button needs to clone a repo into a new app: stack, buildpacks, formation (which dynos run), addons, and prompted env vars. The extension mirrors that shape.

## What this platform cares about

The stack (`heroku-24`, `heroku-22`, `container`), buildpacks, the formation (dyno type + count), addons, scripts (`postdeploy`, `pr-predestroy`), and prompted env vars.

## What platform-specific extras unlock

`addons[]` provisions managed services (`heroku-postgresql`, `heroku-redis`, `papertrail`). `formation{}` sizes each Procfile process.

## Compatibility table

| Manifest field | Heroku behavior |
|---|---|
| `version` | Required. |
| `name, description` | App card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Prompted on Button deploy + dashboard. |
| `deployment.targets` | Must include `heroku`. |
| `platforms.heroku` | Strict. |

### `platforms.heroku` fields

| Field | Purpose |
|---|---|
| `platforms.heroku.stack` | Heroku stack. |
| `platforms.heroku.buildpacks` | Ordered buildpack list. |
| `platforms.heroku.formation` | Dyno formation. |
| `platforms.heroku.addons` | Managed services. |
| `platforms.heroku.scripts` | Lifecycle scripts (`postdeploy`, `pr-predestroy`). |
| `platforms.heroku.region` | Heroku region. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `app.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Heroku consumer SHOULD offer manifests that
declare `platforms.heroku`.

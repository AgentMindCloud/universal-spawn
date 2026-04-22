# Render — universal-spawn platform extension

Render's Blueprint (`render.yaml`) declares an entire app — web services, background workers, cron jobs, static sites, managed Postgres, and Redis — in one file. The extension maps the Blueprint shape onto `platforms.render`.

## What this platform cares about

The services array (with `kind`, plan, autodeploy), managed databases, and the envVarGroups that share secrets across services.

## What platform-specific extras unlock

`databases[]` provisions managed Postgres / Redis. `env_var_groups[]` lets multiple services share the same envelope of secrets.

## Compatibility table

| Manifest field | Render behavior |
|---|---|
| `version` | Required. |
| `name, description` | Blueprint project + card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Render dashboard + env var groups. |
| `deployment.targets` | Must include `render`. |
| `platforms.render` | Strict. |

### `platforms.render` fields

| Field | Purpose |
|---|---|
| `platforms.render.services` | Render services. |
| `platforms.render.databases` | Managed databases. |
| `platforms.render.env_var_groups` | Shared env var groups. |
| `platforms.render.region` | Default region. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `render.yaml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Render consumer SHOULD offer manifests that
declare `platforms.render`.

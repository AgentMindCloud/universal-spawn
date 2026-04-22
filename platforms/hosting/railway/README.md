# Railway — universal-spawn platform extension

Railway runs services from a Git repo using Nixpacks (default) or a Dockerfile, attaches managed databases, and auto-provisions private networking between services. The extension captures the build provider, the start command, per-service plugins (Postgres, Redis, Mongo, MySQL), and the template registration.

## What this platform cares about

The build provider (`nixpacks`, `docker`, `buildpacks`), the start command, the plugins (managed services), the healthcheck endpoint, and whether this manifest registers a Railway template.

## What platform-specific extras unlock

`plugins[]` declares managed services Railway provisions for you. `template` opts this manifest into Railway's template marketplace.

## Compatibility table

| Manifest field | Railway behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Service name + card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Railway secrets; missing required blocks deploy. |
| `deployment.targets` | Must include `railway`. |
| `platforms.railway` | Strict. |

### `platforms.railway` fields

| Field | Purpose |
|---|---|
| `platforms.railway.build` | Build provider + config. |
| `platforms.railway.start_command` | Start command. |
| `platforms.railway.healthcheck` | Healthcheck path + timeout. |
| `platforms.railway.plugins` | Managed services. |
| `platforms.railway.replicas` | Replica count. |
| `platforms.railway.region` | Railway region. |
| `platforms.railway.template` | Template registration block. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `railway.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Railway consumer SHOULD offer manifests that
declare `platforms.railway`.

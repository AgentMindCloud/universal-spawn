# Koyeb — universal-spawn platform extension

Koyeb runs containers globally with automatic scaling and geo-routing. The extension captures the service kind, the build source (git or Docker image), regions, instance type, and scale settings.

## What this platform cares about

The build source (`git`, `docker`), the regions list, the instance type, port routing, and autoscaling bounds.

## What platform-specific extras unlock

`autoscaling.targets[]` sets CPU / RPS / concurrent_request targets; Koyeb scales between `min` and `max` to hold them.

## Compatibility table

| Manifest field | Koyeb behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`. |
| `env_vars_required` | Koyeb secrets. |
| `deployment.targets` | Must include `koyeb`. |
| `platforms.koyeb` | Strict. |

### `platforms.koyeb` fields

| Field | Purpose |
|---|---|
| `platforms.koyeb.service_kind` | `web` or `worker`. |
| `platforms.koyeb.build` | Build source. |
| `platforms.koyeb.regions` | Regions list. |
| `platforms.koyeb.instance_type` | Instance type. |
| `platforms.koyeb.ports` | HTTP port routing. |
| `platforms.koyeb.autoscaling` | Autoscaling config. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `koyeb.yaml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Koyeb consumer SHOULD offer manifests that
declare `platforms.koyeb`.

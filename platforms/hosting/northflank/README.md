# Northflank — universal-spawn platform extension

Northflank runs container services, cron jobs, pipelines, and managed databases on a self-service Kubernetes substrate. The extension captures the kind (combined service, deployment, job), build source, resources, and attached addons.

## What this platform cares about

The `kind` (`combined`, `deployment`, `job`), build + Docker settings, resources, ports, and addons (Postgres / MongoDB / MySQL / Redis / ClickHouse).

## What platform-specific extras unlock

`addons[]` provisions managed services. `pipeline` captures the Northflank pipeline id this service is part of.

## Compatibility table

| Manifest field | Northflank behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`. |
| `env_vars_required` | Northflank secret groups. |
| `deployment.targets` | Must include `northflank`. |
| `platforms.northflank` | Strict. |

### `platforms.northflank` fields

| Field | Purpose |
|---|---|
| `platforms.northflank.kind` | `combined`, `deployment`, `job`. |
| `platforms.northflank.build` | Git build configuration. |
| `platforms.northflank.image` | Image reference. |
| `platforms.northflank.resources` | CPU + RAM allocation. |
| `platforms.northflank.replicas` | Replica count. |
| `platforms.northflank.ports` | HTTP ports. |
| `platforms.northflank.addons` | Managed addons. |
| `platforms.northflank.pipeline` | Pipeline id. |
| `platforms.northflank.region` | Region. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `northflank.yaml (Spec CLI)`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Northflank consumer SHOULD offer manifests that
declare `platforms.northflank`.

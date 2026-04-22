# Vultr — universal-spawn platform extension

Vultr offers VPS (cloud compute), bare metal, Vultr Kubernetes Engine, object storage, and managed databases. The extension captures the region, plan, OS, cloud-init user-data, attached block storage, private networking, and managed databases.

## What this platform cares about

The region, plan id, OS, cloud-init path, attached block storage, private networks, and managed databases.

## What platform-specific extras unlock

`managed_databases[]` provisions Vultr's managed Postgres / MySQL / Redis. `vpc[]` attaches the instance to a named private VPC.

## Compatibility table

| Manifest field | Vultr behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`. |
| `env_vars_required` | Cloud-init injected. |
| `deployment.targets` | Must include `vultr`. |
| `platforms.vultr` | Strict. |

### `platforms.vultr` fields

| Field | Purpose |
|---|---|
| `platforms.vultr.region` | Region. |
| `platforms.vultr.plan` | Plan id. |
| `platforms.vultr.os` | OS slug. |
| `platforms.vultr.cloud_init` | cloud-init user-data path. |
| `platforms.vultr.block_storage` | Attached block storage. |
| `platforms.vultr.vpc` | Private VPCs. |
| `platforms.vultr.managed_databases` | Managed databases. |
| `platforms.vultr.firewall_group` | Attached firewall group. |
| `platforms.vultr.backups` | Automatic backups. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `cloud-init.yaml + Vultr API`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Vultr consumer SHOULD offer manifests that
declare `platforms.vultr`.

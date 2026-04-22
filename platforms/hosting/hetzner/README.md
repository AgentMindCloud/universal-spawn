# Hetzner Cloud — universal-spawn platform extension

Hetzner Cloud gives you VPS servers, snapshots, volumes, networks, and load balancers through `hcloud` or Terraform. The extension captures the server type, image, cloud-init script path, networking, and firewalls — everything an installer needs to provision reproducibly.

## What this platform cares about

The location (datacenter), server type, image, cloud-init script, attached volumes, assigned networks, and SSH keys.

## What platform-specific extras unlock

`firewall_rules[]` applies a set of hcloud firewall rules. `networks[]` attaches the server to private networks by name.

## Compatibility table

| Manifest field | Hetzner Cloud behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Cloud-init-injected env or dotenv on disk. |
| `deployment.targets` | Must include `hetzner`. |
| `platforms.hetzner` | Strict. |

### `platforms.hetzner` fields

| Field | Purpose |
|---|---|
| `platforms.hetzner.location` | Datacenter (`fsn1`, `nbg1`, `hel1`, `ash`, `hil`, `sin`). |
| `platforms.hetzner.server_type` | Server type id (`cx22`, `cpx31`, `ax41-nvme`, …). |
| `platforms.hetzner.image` | OS image. |
| `platforms.hetzner.ssh_keys` | SSH key names. |
| `platforms.hetzner.cloud_init` | cloud-init user-data path. |
| `platforms.hetzner.volumes` | Attached volumes. |
| `platforms.hetzner.networks` | Attached private networks. |
| `platforms.hetzner.firewall_rules` | Firewall ruleset. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `cloud-init.yaml (+ hcloud CLI)`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Hetzner Cloud consumer SHOULD offer manifests that
declare `platforms.hetzner`.

# Linode (Akamai Cloud) — universal-spawn platform extension

Linode — now Akamai Cloud Compute — offers Linodes (VPS), Object Storage, block volumes, LKE (managed Kubernetes), and NodeBalancers. The canonical declarative layer is StackScripts: bash scripts the provisioner runs on first boot. The extension captures the Linode type, region, StackScript, volumes, and firewall.

## What this platform cares about

The region, Linode type, image, the StackScript id (+ UDF answers), attached volumes, private IP, and backups.

## What platform-specific extras unlock

`stackscript.udf[]` provides answers to StackScript UDF prompts so provisioning is fully non-interactive.

## Compatibility table

| Manifest field | Linode (Akamai Cloud) behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Baked into the StackScript. |
| `deployment.targets` | Must include `linode`. |
| `platforms.linode` | Strict. |

### `platforms.linode` fields

| Field | Purpose |
|---|---|
| `platforms.linode.region` | Region. |
| `platforms.linode.instance_type` | Linode plan. |
| `platforms.linode.image` | OS image. |
| `platforms.linode.stackscript` | StackScript id + UDF answers. |
| `platforms.linode.volumes` | Block-storage volumes. |
| `platforms.linode.private_ip` | Private IP toggle. |
| `platforms.linode.backups` | Automatic backups toggle. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `StackScript + linode-cli`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Linode (Akamai Cloud) consumer SHOULD offer manifests that
declare `platforms.linode`.

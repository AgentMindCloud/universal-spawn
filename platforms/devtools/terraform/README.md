# Terraform — universal-spawn platform extension

Terraform configurations are either root-level deployables or reusable modules published to the Terraform Registry. A universal-spawn manifest points at one and captures the required providers + min CLI version.

## What this platform cares about

The `kind` (`root-config`, `module`), the required providers map, the min Terraform CLI version, and the Registry namespace/name when `kind: module`.

## Compatibility table

| Manifest field | Terraform behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `library`, `container`. |
| `platforms.terraform` | Strict. |

### `platforms.terraform` fields

| Field | Purpose |
|---|---|
| `platforms.terraform.kind` | `root-config` or `module`. |
| `platforms.terraform.entry_dir` | Directory with `*.tf` files. |
| `platforms.terraform.required_providers` | Provider id → version constraint. |
| `platforms.terraform.min_cli_version` | Minimum Terraform CLI. |
| `platforms.terraform.registry` | Registry namespace + name. |
| `platforms.terraform.backend` | State backend kind. |

See [`compatibility.md`](./compatibility.md) for more.

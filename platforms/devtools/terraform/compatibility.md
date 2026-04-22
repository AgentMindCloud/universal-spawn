# Terraform compatibility — field-by-field

| universal-spawn v1.0 field | Terraform behavior |
|---|---|
| `version` | Required. |
| `platforms.terraform.kind` | `root-config` or `module`. |
| `platforms.terraform.entry_dir` | Directory with `*.tf` files. |
| `platforms.terraform.required_providers` | Provider id → version constraint. |
| `platforms.terraform.min_cli_version` | Minimum Terraform CLI. |
| `platforms.terraform.registry` | Registry namespace + name (module). |
| `platforms.terraform.backend` | Backend kind (`s3`, `gcs`, `remote`, `local`, `http`). |

## Coexistence with `*.tf + terraform block`

universal-spawn does NOT replace *.tf + terraform block. Both files coexist; consumers read both and warn on conflicts.

### `*.tf + terraform block` (provider-native)

```hcl
terraform {
  required_version = ">= 1.8"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
  backend "s3" {}
}
```

### `universal-spawn.yaml` (platforms.terraform block)

```yaml
platforms:
  terraform:
    kind: root-config
    entry_dir: infra/terraform
    required_providers:
      aws: "~> 5.0"
    min_cli_version: ">=1.8"
    backend: s3
```

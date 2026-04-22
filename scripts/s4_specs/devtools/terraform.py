"""Terraform — modules + root configs (including the Registry)."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "terraform",
    "title": "Terraform",
    "lede": (
        "Terraform configurations are either root-level deployables "
        "or reusable modules published to the Terraform Registry. A "
        "universal-spawn manifest points at one and captures the "
        "required providers + min CLI version."
    ),
    "cares": (
        "The `kind` (`root-config`, `module`), the required providers "
        "map, the min Terraform CLI version, and the Registry namespace/"
        "name when `kind: module`."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `library`, `container`."),
        ("platforms.terraform", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.terraform.kind", "`root-config` or `module`."),
        ("platforms.terraform.entry_dir", "Directory with `*.tf` files."),
        ("platforms.terraform.required_providers", "Provider id → version constraint."),
        ("platforms.terraform.min_cli_version", "Minimum Terraform CLI."),
        ("platforms.terraform.registry", "Registry namespace + name (module)."),
        ("platforms.terraform.backend", "Backend kind (`s3`, `gcs`, `remote`, `local`, `http`)."),
    ],
    "platform_fields": {
        "kind": "`root-config` or `module`.",
        "entry_dir": "Directory with `*.tf` files.",
        "required_providers": "Provider id → version constraint.",
        "min_cli_version": "Minimum Terraform CLI.",
        "registry": "Registry namespace + name.",
        "backend": "State backend kind.",
    },
    "schema_body": schema_object(
        required=["kind", "entry_dir"],
        properties={
            "kind": enum(["root-config", "module"]),
            "entry_dir": str_prop(),
            "required_providers": {
                "type": "object",
                "additionalProperties": str_prop(),
            },
            "min_cli_version": str_prop(pattern=r"^[><=~^]*[0-9]+(\.[0-9]+)*$"),
            "registry": schema_object(
                properties={
                    "namespace": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                    "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                    "provider": str_prop(),
                },
            ),
            "backend": enum(["s3", "gcs", "azurerm", "remote", "local", "http", "kubernetes"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Terraform Template
type: workflow
description: Template for a Terraform-targeted universal-spawn manifest.

platforms:
  terraform:
    kind: root-config
    entry_dir: infra/terraform
    required_providers:
      aws: "~> 5.0"
      random: "~> 3.0"
    min_cli_version: ">=1.8"
    backend: s3

safety:
  min_permissions: [network:outbound]

env_vars_required:
  - name: AWS_ACCESS_KEY_ID
    description: AWS key.
    secret: true
  - name: AWS_SECRET_ACCESS_KEY
    description: AWS secret.
    secret: true

deployment:
  targets: [terraform]

metadata:
  license: MPL-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/terraform-template }
""",
    "native_config_name": "*.tf + terraform block",
    "native_config_lang": "hcl",
    "native_config": """
terraform {
  required_version = ">= 1.8"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
  backend "s3" {}
}
""",
    "universal_excerpt": """
platforms:
  terraform:
    kind: root-config
    entry_dir: infra/terraform
    required_providers:
      aws: "~> 5.0"
    min_cli_version: ">=1.8"
    backend: s3
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Infra
type: workflow
summary: Minimal Terraform root-config for the plate-studio infra.
description: Provisions an S3 bucket + CloudFront distribution. AWS-only.

platforms:
  terraform:
    kind: root-config
    entry_dir: infra
    required_providers:
      aws: "~> 5.0"
    min_cli_version: ">=1.8"
    backend: s3

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: false

env_vars_required:
  - name: AWS_ACCESS_KEY_ID
    description: AWS key.
    secret: true
  - name: AWS_SECRET_ACCESS_KEY
    description: AWS secret.
    secret: true

deployment:
  targets: [terraform]

metadata:
  license: MPL-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/terraform-plate-infra }
  id: com.plate-studio.terraform-plate-infra
""",
        "example-2": """
version: "1.0"
name: Parchment Static Site Module
type: library
summary: Full Terraform module for a static-site pipeline, published to the Registry.
description: >
  Reusable Terraform module provisioning S3 + CloudFront + Route53.
  Listed on registry.terraform.io under `plate-studio/parchment-static-site/aws`.

platforms:
  terraform:
    kind: module
    entry_dir: .
    required_providers:
      aws: "~> 5.0"
    min_cli_version: ">=1.5"
    registry:
      namespace: plate-studio
      name: parchment-static-site
      provider: aws

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [terraform]

metadata:
  license: MPL-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/terraform-aws-parchment-static-site }
  id: com.plate-studio.terraform-parchment-static-site
""",
    },
}

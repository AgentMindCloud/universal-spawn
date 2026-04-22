"""Pulumi — programs + component packages across 4 languages."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "pulumi",
    "title": "Pulumi",
    "lede": (
        "Pulumi programs declare cloud resources in real code "
        "(TypeScript, Python, Go, C#). Reusable component packages "
        "publish to the Pulumi Registry. A universal-spawn manifest "
        "picks program-vs-component and the language."
    ),
    "cares": (
        "The `kind` (`program`, `component-package`), the language, "
        "the project name, and the backend."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `library`, `container`."),
        ("platforms.pulumi", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.pulumi.kind", "`program` or `component-package`."),
        ("platforms.pulumi.runtime", "`nodejs`, `python`, `go`, `dotnet`, `java`."),
        ("platforms.pulumi.project", "Pulumi project name."),
        ("platforms.pulumi.stack", "Default stack name."),
        ("platforms.pulumi.backend", "State backend."),
        ("platforms.pulumi.registry", "Pulumi Registry namespace + name (component)."),
    ],
    "platform_fields": {
        "kind": "`program` or `component-package`.",
        "runtime": "`nodejs`, `python`, `go`, `dotnet`, `java`.",
        "project": "Pulumi project name.",
        "stack": "Default stack.",
        "backend": "State backend.",
        "registry": "Pulumi Registry namespace + name.",
    },
    "schema_body": schema_object(
        required=["kind", "runtime", "project"],
        properties={
            "kind": enum(["program", "component-package"]),
            "runtime": enum(["nodejs", "python", "go", "dotnet", "java"]),
            "project": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9_-]{0,63}$"),
            "stack": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9_-]{0,63}$"),
            "backend": enum(["service", "s3", "gcs", "azblob", "file"]),
            "registry": schema_object(
                properties={
                    "namespace": str_prop(),
                    "name": str_prop(),
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Pulumi Template
type: workflow
description: Template for a Pulumi-targeted universal-spawn manifest.

platforms:
  pulumi:
    kind: program
    runtime: nodejs
    project: your-infra
    stack: dev
    backend: service

safety:
  min_permissions: [network:outbound]

env_vars_required:
  - name: PULUMI_ACCESS_TOKEN
    description: Pulumi Cloud access token.
    secret: true

deployment:
  targets: [pulumi]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/pulumi-template }
""",
    "native_config_name": "Pulumi.yaml + Pulumi.<stack>.yaml",
    "native_config_lang": "yaml",
    "native_config": """
name: your-infra
runtime: nodejs
description: Your infra
""",
    "universal_excerpt": """
platforms:
  pulumi:
    kind: program
    runtime: nodejs
    project: your-infra
    stack: dev
    backend: service
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Pulumi Program
type: workflow
summary: Minimal Pulumi TypeScript program that provisions a bucket + CDN.
description: One stack (`dev`). Pulumi Cloud backend. No registry publication.

platforms:
  pulumi:
    kind: program
    runtime: nodejs
    project: plate-infra
    stack: dev
    backend: service

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: false

env_vars_required:
  - name: PULUMI_ACCESS_TOKEN
    description: Pulumi Cloud access token.
    secret: true

deployment:
  targets: [pulumi]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/pulumi-plate-infra }
  id: com.plate-studio.pulumi-plate-infra
""",
        "example-2": """
version: "1.0"
name: Parchment Component Package
type: library
summary: Full Pulumi component package — reusable parchment-static-site component, published to the Registry.
description: >
  Go-based Pulumi component package that exposes a reusable
  ParchmentStaticSite component. Publishes to the Pulumi Registry.

platforms:
  pulumi:
    kind: component-package
    runtime: go
    project: parchment-static-site
    backend: service
    registry:
      namespace: plate-studio
      name: parchment-static-site

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: true

env_vars_required:
  - name: PULUMI_ACCESS_TOKEN
    description: Pulumi Cloud access token (for publish).
    secret: true

deployment:
  targets: [pulumi]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/pulumi-parchment-static-site }
  id: com.plate-studio.pulumi-parchment-static-site
""",
    },
}

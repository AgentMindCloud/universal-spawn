"""GitHub Codespaces — devcontainer + Codespaces machine class."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "codespaces",
    "title": "GitHub Codespaces",
    "lede": (
        "Codespaces is GitHub's hosted Dev Containers runtime. A "
        "universal-spawn manifest pins the devcontainer file, the "
        "default machine class, and any prebuild settings."
    ),
    "cares": (
        "The devcontainer file path, the default machine class, "
        "prebuild config, and forwarded ports."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`container`, `web-app`, `workflow`."),
        ("platforms.codespaces", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.codespaces.devcontainer", "Path to devcontainer.json."),
        ("platforms.codespaces.machine", "Default machine class."),
        ("platforms.codespaces.prebuild", "Prebuild trigger."),
        ("platforms.codespaces.forward_ports", "Auto-forwarded ports."),
        ("platforms.codespaces.region", "Suggested region."),
    ],
    "platform_fields": {
        "devcontainer": "devcontainer.json path.",
        "machine": "Machine class.",
        "prebuild": "Prebuild trigger.",
        "forward_ports": "Auto-forwarded ports.",
        "region": "Suggested region.",
    },
    "schema_body": schema_object(
        properties={
            "devcontainer": str_prop(),
            "machine": enum(["basicLinux32gb", "standardLinux32gb", "premiumLinux", "largePremiumLinux", "xLargePremiumLinux"]),
            "prebuild": enum(["never", "on-push", "on-pr-merge"]),
            "forward_ports": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": 65535},
            },
            "region": enum(["UsEast", "UsWest", "EuropeWest", "SoutheastAsia"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Codespaces Template
type: container
description: Template for a Codespaces-targeted universal-spawn manifest.

platforms:
  codespaces:
    devcontainer: .devcontainer/devcontainer.json
    machine: standardLinux32gb
    prebuild: on-push
    forward_ports: [3000, 5432]

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]

env_vars_required: []

deployment:
  targets: [codespaces]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/codespaces-template }
""",
    "native_config_name": ".devcontainer/devcontainer.json",
    "native_config_lang": "json",
    "native_config": """
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node:20",
  "features": { "ghcr.io/devcontainers/features/github-cli:1": {} },
  "forwardPorts": [3000, 5432]
}
""",
    "universal_excerpt": """
platforms:
  codespaces:
    devcontainer: .devcontainer/devcontainer.json
    machine: standardLinux32gb
    forward_ports: [3000, 5432]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Studio Codespace
type: container
summary: Minimal Codespaces config for the plate-studio repo.
description: 4-core machine. Devcontainer with Node 20 + pnpm + svg-lint.

platforms:
  codespaces:
    devcontainer: .devcontainer/devcontainer.json
    machine: basicLinux32gb
    forward_ports: [3000]

safety:
  min_permissions: [fs:read, fs:write, network:outbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [codespaces]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/codespaces-config }
  id: com.plate-studio.codespaces-config
""",
        "example-2": """
version: "1.0"
name: ML Workspace Codespace
type: container
summary: Full GPU-class Codespace for ML notebook work with prebuilds enabled.
description: xLargePremiumLinux + on-push prebuilds; useful for cold-start research.

platforms:
  codespaces:
    devcontainer: .devcontainer/devcontainer.json
    machine: xLargePremiumLinux
    prebuild: on-push
    forward_ports: [8888, 6006]
    region: EuropeWest

safety:
  min_permissions: [fs:read, fs:write, network:outbound]
  safe_for_auto_spawn: false
  cost_limit_usd_daily: 30

env_vars_required:
  - name: WANDB_API_KEY
    description: Weights & Biases key.
    secret: true

deployment:
  targets: [codespaces]

metadata:
  license: Apache-2.0
  author: { name: Research Lab, handle: research-lab }
  source: { type: git, url: https://github.com/research-lab/codespaces-ml-workspace }
  id: com.research-lab.codespaces-ml-workspace
""",
    },
}

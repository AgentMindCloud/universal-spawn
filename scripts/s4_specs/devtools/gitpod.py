"""Gitpod — .gitpod.yml + Gitpod Flex."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "gitpod",
    "title": "Gitpod",
    "lede": (
        "Gitpod runs ephemeral cloud workspaces driven by `.gitpod.yml`. "
        "A universal-spawn manifest pins the workspace image, the "
        "tasks Gitpod runs at start, and the Gitpod Flex tier."
    ),
    "cares": (
        "The image, tasks list (init / command), exposed ports, and "
        "the workspace tier."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`container`, `web-app`, `workflow`."),
        ("platforms.gitpod", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.gitpod.image", "Workspace image."),
        ("platforms.gitpod.tasks", "Tasks Gitpod runs at start."),
        ("platforms.gitpod.ports", "Exposed ports config."),
        ("platforms.gitpod.tier", "Workspace tier."),
        ("platforms.gitpod.tools", "Pre-installed tools (vscode, ssh)."),
    ],
    "platform_fields": {
        "image": "Workspace image.",
        "tasks": "Start-up tasks.",
        "ports": "Port config.",
        "tier": "Workspace tier.",
        "tools": "Pre-installed tools.",
    },
    "schema_body": schema_object(
        properties={
            "image": str_prop(),
            "tasks": {
                "type": "array",
                "items": schema_object(
                    properties={
                        "name": str_prop(),
                        "init": str_prop(),
                        "command": str_prop(),
                        "before": str_prop(),
                    },
                ),
            },
            "ports": {
                "type": "array",
                "items": schema_object(
                    required=["port"],
                    properties={
                        "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                        "visibility": enum(["private", "public", "org"]),
                        "on_open": enum(["open-browser", "open-preview", "notify", "ignore"]),
                    },
                ),
            },
            "tier": enum(["small", "standard", "large", "x-large"]),
            "tools": {"type": "array", "items": enum(["vscode", "ssh", "jetbrains"])},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Gitpod Template
type: container
description: Template for a Gitpod-targeted universal-spawn manifest.

platforms:
  gitpod:
    image: gitpod/workspace-full:latest
    tasks:
      - { name: install, init: "pnpm install", command: "pnpm dev" }
    ports:
      - { port: 3000, visibility: public, on_open: open-preview }
    tier: standard
    tools: [vscode]

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]

env_vars_required: []

deployment:
  targets: [gitpod]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/gitpod-template }
""",
    "native_config_name": ".gitpod.yml",
    "native_config_lang": "yaml",
    "native_config": """
image: gitpod/workspace-full:latest
tasks:
  - name: install
    init: pnpm install
    command: pnpm dev
ports:
  - port: 3000
    visibility: public
    onOpen: open-preview
""",
    "universal_excerpt": """
platforms:
  gitpod:
    image: gitpod/workspace-full:latest
    tasks:
      - { name: install, init: "pnpm install", command: "pnpm dev" }
    ports:
      - { port: 3000, visibility: public, on_open: open-preview }
    tier: standard
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Studio Gitpod
type: container
summary: Minimal Gitpod workspace for the plate-studio repo.
description: Standard tier, vscode tool, one task running pnpm dev.

platforms:
  gitpod:
    image: gitpod/workspace-full:latest
    tasks:
      - { name: dev, init: "pnpm install", command: "pnpm dev" }
    ports:
      - { port: 3000, visibility: public, on_open: open-preview }
    tier: standard
    tools: [vscode]

safety:
  min_permissions: [fs:read, fs:write, network:outbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [gitpod]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/gitpod-config }
  id: com.plate-studio.gitpod-config
""",
        "example-2": """
version: "1.0"
name: GPU Notebook Workspace
type: container
summary: Full Gitpod workspace at the x-large tier with both VS Code and JetBrains.
description: Provisioned with GPU-friendly base image; private ports for Jupyter.

platforms:
  gitpod:
    image: gitpod/workspace-python:latest
    tasks:
      - { name: install, init: "pip install -r requirements.txt", command: "jupyter lab" }
    ports:
      - { port: 8888, visibility: private, on_open: notify }
    tier: x-large
    tools: [vscode, jetbrains, ssh]

safety:
  min_permissions: [fs:read, fs:write, network:outbound]
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: WANDB_API_KEY
    description: W&B key.
    secret: true

deployment:
  targets: [gitpod]

metadata:
  license: Apache-2.0
  author: { name: Research Lab, handle: research-lab }
  source: { type: git, url: https://github.com/research-lab/gitpod-gpu-notebook }
  id: com.research-lab.gitpod-gpu-notebook
""",
    },
}

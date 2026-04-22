"""Paperspace — Gradient notebooks + deployments + Machines."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "paperspace",
    "title": "Paperspace",
    "lede": (
        "Paperspace (DigitalOcean) hosts Gradient notebooks, "
        "deployments, and standalone Machines. A universal-spawn "
        "manifest pins the surface and the GPU class."
    ),
    "cares": (
        "The `surface` (`gradient-notebook`, `gradient-deployment`, "
        "`machine`), the GPU class, and the team / project ids."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `workflow`, `container`."),
        ("platforms.paperspace", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.paperspace.surface", "`gradient-notebook`, `gradient-deployment`, `machine`."),
        ("platforms.paperspace.gpu", "GPU class."),
        ("platforms.paperspace.team_id", "Paperspace team id."),
        ("platforms.paperspace.project_id", "Paperspace project id."),
        ("platforms.paperspace.image", "Container image (deployment / notebook)."),
    ],
    "platform_fields": {
        "surface": "Surface kind.",
        "gpu": "GPU class.",
        "team_id": "Team id.",
        "project_id": "Project id.",
        "image": "Container image.",
    },
    "schema_body": schema_object(
        required=["surface"],
        properties={
            "surface": enum(["gradient-notebook", "gradient-deployment", "machine"]),
            "gpu": enum(["cpu", "M4000", "P4000", "P5000", "P6000", "RTX4000", "RTX5000", "A4000", "A5000", "A6000", "A100", "H100"]),
            "team_id": str_prop(pattern=r"^[a-z0-9]{6,32}$"),
            "project_id": str_prop(pattern=r"^[a-z0-9-]{6,64}$"),
            "image": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Paperspace Template
type: notebook
description: Template for a Paperspace-targeted universal-spawn manifest.

platforms:
  paperspace:
    surface: gradient-notebook
    gpu: A4000
    image: paperspace/gradient-base:pt230-tf215-cudaa122-py311

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: PAPERSPACE_API_KEY
    description: Paperspace API key.
    secret: true

deployment:
  targets: [paperspace]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/paperspace-template }
""",
    "native_config_name": "Paperspace dashboard / Gradient project",
    "native_config_lang": "text",
    "native_config": "# Paperspace stores resource state in the Gradient project; this manifest mirrors it.\n",
    "universal_excerpt": """
platforms:
  paperspace:
    surface: gradient-notebook
    gpu: A4000
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Notebook
type: notebook
summary: Minimal Paperspace Gradient notebook for parchment EDA.
description: A4000 GPU. Default container.

platforms:
  paperspace:
    surface: gradient-notebook
    gpu: A4000

safety:
  min_permissions: [network:outbound, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required:
  - name: PAPERSPACE_API_KEY
    description: API key.
    secret: true

deployment:
  targets: [paperspace]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/paperspace-plate-notebook }
  id: com.plate-studio.paperspace-plate-notebook
""",
        "example-2": """
version: "1.0"
name: Plate Inference Deployment
type: workflow
summary: Full Gradient deployment serving a parchment classifier behind a custom image.
description: Gradient deployment on H100. Custom image. Production tier.

platforms:
  paperspace:
    surface: gradient-deployment
    gpu: H100
    image: ghcr.io/plate-studio/parchment-infer:latest

safety:
  min_permissions: [network:inbound, network:outbound, gpu:compute]
  cost_limit_usd_daily: 120
  safe_for_auto_spawn: false

env_vars_required:
  - name: PAPERSPACE_API_KEY
    description: API key.
    secret: true
  - name: HF_TOKEN
    description: HF token.
    secret: true

deployment:
  targets: [paperspace]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/paperspace-plate-deployment }
  id: com.plate-studio.paperspace-plate-deployment
""",
    },
}

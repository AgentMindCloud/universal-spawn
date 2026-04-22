"""Lightning AI — cloud Studios."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "lightning-ai",
    "title": "Lightning AI",
    "lede": (
        "Lightning AI runs Studios — cloud dev environments that pair "
        "a notebook + terminal + jobs runner. A universal-spawn "
        "manifest pins the Studio template, machine class, and "
        "default app entry."
    ),
    "cares": (
        "The Studio template, the machine class (CPU/GPU), and the "
        "entry app or notebook."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `workflow`, `web-app`."),
        ("platforms.lightning-ai", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.lightning-ai.template", "Studio template."),
        ("platforms.lightning-ai.machine", "Machine class."),
        ("platforms.lightning-ai.entry_file", "Entry .py / .ipynb file."),
        ("platforms.lightning-ai.team_id", "Lightning team id."),
    ],
    "platform_fields": {
        "template": "Studio template.",
        "machine": "Machine class.",
        "entry_file": "Entry file.",
        "team_id": "Lightning team id.",
    },
    "schema_body": schema_object(
        properties={
            "template": enum(["python", "pytorch", "jax", "tensorflow", "lightning"]),
            "machine": enum(["cpu", "T4", "L4", "A10G", "A100", "L40S", "H100"]),
            "entry_file": str_prop(),
            "team_id": str_prop(pattern=r"^[a-z0-9-]{6,64}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Lightning AI Template
type: notebook
description: Template for a Lightning-AI-targeted universal-spawn manifest.

platforms:
  lightning-ai:
    template: pytorch
    machine: T4
    entry_file: notebook.ipynb

safety:
  min_permissions: [network:outbound]

env_vars_required:
  - name: LIGHTNING_API_KEY
    description: Lightning AI API key.
    secret: true

deployment:
  targets: [lightning-ai]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/lightning-ai-template }
""",
    "native_config_name": "Lightning Studio template + machine settings",
    "native_config_lang": "text",
    "native_config": "# Lightning Studio config lives in the Studio's web UI; this manifest mirrors it.\n",
    "universal_excerpt": """
platforms:
  lightning-ai:
    template: pytorch
    machine: T4
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate PyTorch Studio
type: notebook
summary: Minimal Lightning AI Studio for plate ML on a T4.
description: PyTorch template, T4 machine, single notebook.

platforms:
  lightning-ai:
    template: pytorch
    machine: T4
    entry_file: notebook.ipynb

safety:
  min_permissions: [network:outbound, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required:
  - name: LIGHTNING_API_KEY
    description: Lightning API key.
    secret: true

deployment:
  targets: [lightning-ai]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/lightning-plate-pytorch }
  id: com.plate-studio.lightning-plate-pytorch
""",
        "example-2": """
version: "1.0"
name: Multi-GPU Plate Trainer
type: workflow
summary: Full Lightning AI Studio on an A100 with a Lightning Trainer entry.
description: PyTorch Lightning template, A100 machine, lightning_module entry.

platforms:
  lightning-ai:
    template: lightning
    machine: A100
    entry_file: train.py

safety:
  min_permissions: [network:outbound, gpu:compute]
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: LIGHTNING_API_KEY
    description: Lightning API key.
    secret: true
  - name: WANDB_API_KEY
    description: W&B key.
    secret: true

deployment:
  targets: [lightning-ai]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/lightning-plate-trainer }
  id: com.plate-studio.lightning-plate-trainer
""",
    },
}

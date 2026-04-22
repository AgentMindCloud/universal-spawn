"""Google Colab — runnable .ipynb hosted on Drive."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "google-colab",
    "title": "Google Colab",
    "lede": (
        "Colab runs Drive-hosted .ipynb notebooks with a Python "
        "runtime. A universal-spawn manifest pins the notebook URL, "
        "the runtime kind (CPU / GPU / TPU), and the recommended "
        "machine type."
    ),
    "cares": (
        "The notebook URL or GitHub path, the runtime kind, machine "
        "type, and required Drive scopes."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `workflow`."),
        ("platforms.google-colab", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.google-colab.notebook_url", "Drive or GitHub notebook URL."),
        ("platforms.google-colab.runtime", "`cpu`, `gpu`, `tpu`."),
        ("platforms.google-colab.machine_type", "Machine type."),
        ("platforms.google-colab.runtime_version", "Python runtime version."),
        ("platforms.google-colab.requires_drive", "True if the notebook mounts Drive."),
    ],
    "platform_fields": {
        "notebook_url": "Notebook URL.",
        "runtime": "`cpu`, `gpu`, `tpu`.",
        "machine_type": "Machine type.",
        "runtime_version": "Python runtime version.",
        "requires_drive": "Mounts Drive.",
    },
    "schema_body": schema_object(
        required=["notebook_url"],
        properties={
            "notebook_url": {"type": "string", "format": "uri"},
            "runtime": enum(["cpu", "gpu", "tpu"]),
            "machine_type": enum(["standard", "high-ram", "a100", "v100", "t4", "l4", "v2-8", "v3-8"]),
            "runtime_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)*$"),
            "requires_drive": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Colab Template
type: notebook
description: Template for a Colab-targeted universal-spawn manifest.

platforms:
  google-colab:
    notebook_url: "https://colab.research.google.com/github/yourhandle/your-repo/blob/main/notebook.ipynb"
    runtime: cpu
    machine_type: standard

safety:
  min_permissions: [network:outbound]

env_vars_required: []

deployment:
  targets: [google-colab]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/colab-template }
""",
    "native_config_name": ".ipynb hosted on Drive or GitHub",
    "native_config_lang": "json",
    "native_config": "// Notebook .ipynb file; no separate config file by convention.\n",
    "universal_excerpt": """
platforms:
  google-colab:
    notebook_url: "https://colab.research.google.com/github/yourhandle/your-repo/blob/main/notebook.ipynb"
    runtime: cpu
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate EDA Colab
type: notebook
summary: Minimal Colab notebook for parchment-plate EDA.
description: CPU-only standard machine.

platforms:
  google-colab:
    notebook_url: "https://colab.research.google.com/github/plate-studio/plate-eda-colab/blob/main/eda.ipynb"
    runtime: cpu
    machine_type: standard

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [google-colab]

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/plate-eda-colab }
  id: com.plate-studio.plate-eda-colab
""",
        "example-2": """
version: "1.0"
name: Train ViT on Plates
type: notebook
summary: Full Colab notebook training a ViT classifier on parchment-plate images.
description: A100 runtime; mounts Drive for the dataset and checkpoints.

platforms:
  google-colab:
    notebook_url: "https://colab.research.google.com/github/plate-studio/train-vit-colab/blob/main/train.ipynb"
    runtime: gpu
    machine_type: a100
    runtime_version: "3.11"
    requires_drive: true

safety:
  min_permissions: [network:outbound, fs:read, fs:write, gpu:compute]
  cost_limit_usd_daily: 12
  safe_for_auto_spawn: false

env_vars_required:
  - name: WANDB_API_KEY
    description: W&B key for experiment tracking.
    secret: true

deployment:
  targets: [google-colab]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/train-vit-colab }
  id: com.plate-studio.train-vit-colab
""",
    },
}

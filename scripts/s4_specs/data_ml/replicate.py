"""Replicate (data-ml view) — training + notebook ergonomics.

Cross-link: ../../ai/replicate/ owns the inference shape (model +
version + input_schema). This data-ml entry adds the training-loop +
notebook ergonomics for the same Cog format.
"""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "replicate",
    "title": "Replicate (data-ml)",
    "lede": (
        "This is the data-ml view of Replicate — a thin extension "
        "covering training and notebook ergonomics. The inference "
        "side (`model`, `version`, `input_schema_ref`) lives in "
        "`../../ai/replicate/`; ship both when a creation does both."
    ),
    "cares": (
        "The Cog file path, training config, the notebook link, and "
        "the bundled dataset slug."
    ),
    "cross_links": (
        "Inference + version pinning live at "
        "[`../../ai/replicate/`](../../ai/replicate/). A single "
        "creation typically declares both `platforms.replicate` "
        "blocks — one in each subtree."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `notebook`, `library`."),
        ("platforms.replicate", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.replicate.cog_file", "Path to cog.yaml."),
        ("platforms.replicate.training", "Training config."),
        ("platforms.replicate.notebook_url", "Companion notebook URL."),
        ("platforms.replicate.dataset_slug", "Bundled dataset slug."),
    ],
    "platform_fields": {
        "cog_file": "cog.yaml path.",
        "training": "Training config block.",
        "notebook_url": "Companion notebook URL.",
        "dataset_slug": "Bundled dataset slug.",
    },
    "schema_body": schema_object(
        properties={
            "cog_file": str_prop(),
            "training": schema_object(
                properties={
                    "command": str_prop(),
                    "hardware": enum(["cpu", "t4", "a40", "a100-40gb", "a100-80gb", "h100"]),
                    "max_run_time_minutes": {"type": "integer", "minimum": 1, "maximum": 4320},
                },
            ),
            "notebook_url": {"type": "string", "format": "uri"},
            "dataset_slug": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Replicate Data-ML Template
type: workflow
description: Template for a Replicate-data-ml-targeted universal-spawn manifest.

platforms:
  replicate:
    cog_file: cog.yaml
    training:
      command: "cog train"
      hardware: a40
      max_run_time_minutes: 60
    notebook_url: "https://colab.research.google.com/github/yourhandle/your-replicate-train/blob/main/train.ipynb"

safety:
  min_permissions: [network:outbound:api.replicate.com]

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate token.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/replicate-train-template }
""",
    "native_config_name": "cog.yaml (shared with the AI track)",
    "native_config_lang": "yaml",
    "native_config": """
build:
  python_version: "3.11"
  python_packages: [torch, accelerate]
predict: predict.py:Predictor
train: train.py:trainer
""",
    "universal_excerpt": """
platforms:
  replicate:
    cog_file: cog.yaml
    training: { command: "cog train", hardware: a40, max_run_time_minutes: 60 }
""",
    "compatibility_extras": (
        "## Why two folders\n\n"
        "`../../ai/replicate/` owns the inference (model + version + "
        "input_schema_ref) shape. This folder owns the training + "
        "notebook ergonomics on top of the same Cog format. Both are "
        "thin extensions that compose with the master schema; their "
        "fields do not overlap."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Classifier Train
type: workflow
summary: Minimal training run for the parchment-plate classifier.
description: Single training run on an A40, 30-minute cap.

platforms:
  replicate:
    cog_file: cog.yaml
    training: { command: "cog train", hardware: a40, max_run_time_minutes: 30 }

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate token.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/replicate-classifier-train }
  id: com.plate-studio.replicate-classifier-train
""",
        "example-2": """
version: "1.0"
name: Plate ControlNet Notebook
type: notebook
summary: Full Replicate training notebook + companion Colab link.
description: Notebook walks through training a ControlNet variant for parchment plates; companion Colab opens with one click.

platforms:
  replicate:
    cog_file: cog.yaml
    training: { command: "cog train", hardware: a100-40gb, max_run_time_minutes: 240 }
    notebook_url: "https://colab.research.google.com/github/plate-studio/replicate-controlnet/blob/main/train.ipynb"
    dataset_slug: plate-studio/parchment-train

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate token.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/replicate-controlnet }
  id: com.plate-studio.replicate-controlnet
""",
    },
}

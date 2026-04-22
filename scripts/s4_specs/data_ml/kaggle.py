"""Kaggle — kernel-metadata.json + datasets."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "kaggle",
    "title": "Kaggle",
    "lede": (
        "Kaggle hosts notebooks ('kernels') and datasets. A "
        "universal-spawn manifest declares the kernel id, the source "
        "language, the GPU class, the input datasets, and the "
        "competition link if any."
    ),
    "cares": (
        "The kernel slug, language, GPU/Internet enablement, the "
        "input datasets, and the competition link."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `dataset`, `workflow`."),
        ("platforms.kaggle", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.kaggle.kind", "`notebook` or `dataset`."),
        ("platforms.kaggle.slug", "Kaggle slug (`username/title`)."),
        ("platforms.kaggle.language", "Notebook language."),
        ("platforms.kaggle.kernel_type", "`notebook` or `script`."),
        ("platforms.kaggle.enable_gpu", "GPU toggle."),
        ("platforms.kaggle.enable_internet", "Internet toggle."),
        ("platforms.kaggle.dataset_sources", "Input datasets."),
        ("platforms.kaggle.competition", "Competition slug if entered."),
    ],
    "platform_fields": {
        "kind": "`notebook` or `dataset`.",
        "slug": "Kaggle slug.",
        "language": "Notebook language.",
        "kernel_type": "`notebook` or `script`.",
        "enable_gpu": "GPU toggle.",
        "enable_internet": "Internet toggle.",
        "dataset_sources": "Input datasets.",
        "competition": "Competition slug.",
    },
    "schema_body": schema_object(
        required=["kind", "slug"],
        properties={
            "kind": enum(["notebook", "dataset"]),
            "slug": str_prop(pattern=r"^[a-z0-9_][a-z0-9_-]+/[a-z0-9_][a-z0-9_-]+$"),
            "language": enum(["python", "r", "rust"]),
            "kernel_type": enum(["notebook", "script"]),
            "enable_gpu": bool_prop(False),
            "enable_internet": bool_prop(False),
            "dataset_sources": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z0-9_][a-z0-9_-]+/[a-z0-9_][a-z0-9_-]+$"),
            },
            "competition": str_prop(pattern=r"^[a-z0-9-]+$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Kaggle Template
type: notebook
description: Template for a Kaggle-targeted universal-spawn manifest.

platforms:
  kaggle:
    kind: notebook
    slug: yourhandle/your-notebook
    language: python
    kernel_type: notebook
    enable_gpu: false

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [kaggle]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/kaggle-template }
""",
    "native_config_name": "kernel-metadata.json",
    "native_config_lang": "json",
    "native_config": """
{
  "id": "yourhandle/your-notebook",
  "title": "Your Notebook",
  "code_file": "notebook.ipynb",
  "language": "python",
  "kernel_type": "notebook",
  "enable_gpu": false,
  "enable_internet": false
}
""",
    "universal_excerpt": """
platforms:
  kaggle:
    kind: notebook
    slug: yourhandle/your-notebook
    language: python
    kernel_type: notebook
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate EDA Notebook
type: notebook
summary: Minimal Kaggle Python notebook exploring the parchment-plate dataset.
description: One notebook, no GPU, no internet. Reads from one input dataset.

platforms:
  kaggle:
    kind: notebook
    slug: plate-studio/plate-eda
    language: python
    kernel_type: notebook
    enable_gpu: false
    enable_internet: false
    dataset_sources: [plate-studio/parchment-plates]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [kaggle]

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/kaggle-plate-eda }
  id: com.plate-studio.kaggle-plate-eda
""",
        "example-2": """
version: "1.0"
name: Plate Classifier Submission
type: notebook
summary: Full Kaggle competition entry with GPU + internet + private dataset upload.
description: GPU-enabled notebook entering the parchment-classifier competition. Trains, predicts, submits.

platforms:
  kaggle:
    kind: notebook
    slug: plate-studio/plate-classifier-submission
    language: python
    kernel_type: notebook
    enable_gpu: true
    enable_internet: true
    dataset_sources: [plate-studio/parchment-train, plate-studio/parchment-test]
    competition: parchment-classifier

safety:
  min_permissions: [network:outbound, fs:read, gpu:compute]
  cost_limit_usd_daily: 0
  safe_for_auto_spawn: false

env_vars_required:
  - name: KAGGLE_API_TOKEN
    description: Kaggle API token used for submission.
    secret: true

deployment:
  targets: [kaggle]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/kaggle-plate-submission }
  id: com.plate-studio.kaggle-plate-submission
""",
    },
}

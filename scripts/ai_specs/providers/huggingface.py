"""Hugging Face — Spaces + Inference Endpoints + Models."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "huggingface",
    "title": "Hugging Face",
    "location": ".",
    "lede": (
        "Hugging Face is three surfaces in one: Model repositories, "
        "Dataset repositories, and Spaces (Gradio, Streamlit, Docker, "
        "static). This extension covers all three, plus Inference "
        "Endpoints deployment."
    ),
    "cares": (
        "`repo_kind` (model / dataset / space), visibility, the card "
        "README, and — for Spaces — the SDK and hardware tier."
    ),
    "extras": (
        "`inference.endpoints[]` describes Inference Endpoints "
        "deployments. `base_model` links a finetune to its origin."
    ),
    "compat_table": [
        ("version", "Required."),
        ("license", "Required by HF for publication."),
        ("name, description", "Repo card."),
        ("type", "Mapped to `repo_kind`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "HF Space secrets."),
        ("platforms.huggingface", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("metadata.license", "Required for HF publication."),
        ("name, description", "Repo card header."),
        ("type", "`ai-model` → model; `dataset` → dataset; `web-app`/`notebook`/`creative-tool` → space."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Space secrets."),
        ("platforms.huggingface.repo_kind", "`model`, `dataset`, `space`."),
        ("platforms.huggingface.visibility", "`public`, `private`."),
        ("platforms.huggingface.card_file", "Repo card README path."),
        ("platforms.huggingface.tags", "HF-specific tags."),
        ("platforms.huggingface.space_sdk", "Space SDK (when `repo_kind: space`)."),
        ("platforms.huggingface.hardware", "Space hardware tier."),
        ("platforms.huggingface.inference", "Inference Endpoints deployment."),
        ("platforms.huggingface.base_model", "Base model id (for finetunes)."),
    ],
    "platform_fields": {
        "repo_kind": "`model`, `dataset`, or `space`.",
        "visibility": "`public` or `private`.",
        "card_file": "Repo card README path.",
        "tags": "HF-specific tags.",
        "space_sdk": "Space SDK (`docker`, `gradio`, `streamlit`, `static`).",
        "hardware": "Space hardware tier.",
        "inference": "Inference Endpoints deployment block.",
        "base_model": "Base model HF repo id (for finetunes).",
    },
    "schema_body": schema_object(
        required=["repo_kind", "visibility"],
        properties={
            "repo_kind": enum(["model", "dataset", "space"]),
            "visibility": enum(["public", "private"]),
            "card_file": str_prop(),
            "tags": {
                "type": "array",
                "items": {"type": "string", "pattern": r"^[a-z0-9][a-z0-9:.-]{0,63}$"},
            },
            "space_sdk": enum(["docker", "gradio", "streamlit", "static"]),
            "hardware": enum([
                "cpu-basic", "cpu-upgrade",
                "t4-small", "t4-medium",
                "a10g-small", "a10g-large",
                "a100-large", "zero-gpu",
            ]),
            "inference": schema_object(
                properties={
                    "pipeline_tag": str_prop(),
                    "library_name": enum(["transformers", "diffusers", "sentence-transformers", "timm", "other"]),
                    "endpoints": {
                        "type": "array",
                        "items": schema_object(
                            required=["name"],
                            properties={
                                "name": str_prop(),
                                "accelerator": enum(["cpu", "gpu"]),
                                "instance_type": str_prop(),
                            },
                        ),
                    },
                },
            ),
            "base_model": str_prop(pattern=r"^[^/]+/[^/]+$"),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Hugging Face Template
type: ai-model
description: Template for a Hugging Face-targeted universal-spawn manifest.

platforms:
  huggingface:
    repo_kind: model
    visibility: public
    card_file: README.md
    tags: [\"text-generation\", \"parchment\"]
    inference:
      pipeline_tag: text-generation
      library_name: transformers

safety:
  min_permissions: [network:outbound:huggingface.co]

env_vars_required:
  - name: HF_TOKEN
    description: Hugging Face access token.
    secret: true

deployment:
  targets: [huggingface]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/hf-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Space hardware auto-pick** — when `runtime.gpu_required` "
        "is true and `hardware` is unset, consumers suggest `t4-small` "
        "or better.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Plate Classifier
type: ai-model
summary: Minimal ViT-base finetune for parchment plate classification on HF.
description: Public HF model repo with one inference-API endpoint.

platforms:
  huggingface:
    repo_kind: model
    visibility: public
    card_file: README.md
    tags: [\"image-classification\", \"vit\", \"parchment\"]
    base_model: google/vit-base-patch16-224
    inference:
      pipeline_tag: image-classification
      library_name: transformers

safety:
  min_permissions: [network:outbound:huggingface.co]
  safe_for_auto_spawn: true

env_vars_required:
  - name: HF_TOKEN
    description: Hugging Face access token.
    secret: true

deployment:
  targets: [huggingface]

metadata:
  license: Apache-2.0
  author: { name: Classifier Team, handle: classifier-team }
  source: { type: git, url: https://github.com/classifier-team/plate-classifier }
  id: com.classifier-team.plate-classifier
"""},
        {"yaml": """
version: \"1.0\"
name: Plate Gradio Demo
type: web-app
summary: Full Gradio Space that previews plate archetypes with GPU inference.
description: >
  Gradio Space that serves a plate-archetype classifier with a UI.
  Public visibility, zero-GPU hardware tier. Mirrors assets under
  assets/.

platforms:
  huggingface:
    repo_kind: space
    visibility: public
    card_file: README.md
    tags: [\"gradio\", \"parchment\", \"demo\"]
    space_sdk: gradio
    hardware: zero-gpu

safety:
  min_permissions: [network:inbound, network:outbound:huggingface.co]
  safe_for_auto_spawn: true

env_vars_required:
  - name: HF_TOKEN
    description: Hugging Face access token used to publish the Space.
    secret: true

deployment:
  targets: [huggingface]

visuals: { palette: parchment, icon: assets/icon.svg, hero_plate: assets/hero.svg }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/hf-plate-demo }
  id: com.plate-studio.hf-plate-demo
"""},
        {"yaml": """
version: \"1.0\"
name: Parchment Dataset
type: dataset
summary: Creative HF dataset repo containing Residual Frequencies plate metadata.
description: >
  A HF dataset repo that aggregates plate metadata (archetype, year,
  author, palette) for 10k parchment plates across the open design
  commons. Private during beta, public after review.

platforms:
  huggingface:
    repo_kind: dataset
    visibility: private
    card_file: README.md
    tags: [\"design\", \"plate\", \"metadata\", \"parchment\"]

safety:
  min_permissions: [network:outbound:huggingface.co]
  data_residency: [us, eu]

env_vars_required:
  - name: HF_TOKEN
    description: Hugging Face access token.
    secret: true

deployment:
  targets: [huggingface]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-dataset }
  categories: [data, graphics]
  id: com.plate-studio.parchment-dataset
"""},
    ],
}

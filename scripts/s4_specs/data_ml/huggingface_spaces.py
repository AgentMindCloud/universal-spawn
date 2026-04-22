"""Hugging Face Spaces — Gradio / Streamlit / Docker / static."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "huggingface-spaces",
    "title": "Hugging Face Spaces",
    "lede": (
        "HF Spaces hosts notebook-style demos in four flavors: "
        "Gradio, Streamlit, Docker, or static. A universal-spawn "
        "manifest declares the SDK + hardware tier + visibility "
        "+ the README-frontmatter fields HF reads."
    ),
    "cares": (
        "The space SDK, hardware tier, visibility, and the README "
        "front-matter fields (`title`, `emoji`, `colorFrom`, `colorTo`, "
        "`pinned`)."
    ),
    "cross_links": (
        "Complementary to `../../ai/huggingface/` (models + datasets). "
        "A creation that ships a model AND a Space targets both."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `notebook`, `creative-tool`."),
        ("platforms.huggingface-spaces", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.huggingface-spaces.sdk", "`gradio`, `streamlit`, `docker`, `static`."),
        ("platforms.huggingface-spaces.hardware", "Hardware tier."),
        ("platforms.huggingface-spaces.visibility", "`public` or `private`."),
        ("platforms.huggingface-spaces.front_matter", "README front-matter fields."),
    ],
    "platform_fields": {
        "sdk": "`gradio`, `streamlit`, `docker`, `static`.",
        "hardware": "Hardware tier.",
        "visibility": "`public` or `private`.",
        "front_matter": "README front-matter (title, emoji, colorFrom/To, pinned).",
    },
    "schema_body": schema_object(
        required=["sdk", "visibility"],
        properties={
            "sdk": enum(["gradio", "streamlit", "docker", "static"]),
            "hardware": enum(["cpu-basic", "cpu-upgrade", "t4-small", "t4-medium", "a10g-small", "a10g-large", "a100-large", "zero-gpu"]),
            "visibility": enum(["public", "private"]),
            "front_matter": schema_object(
                properties={
                    "title": str_prop(),
                    "emoji": str_prop(),
                    "color_from": str_prop(),
                    "color_to": str_prop(),
                    "pinned": bool_prop(False),
                    "license": str_prop(),
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: HF Spaces Template
type: web-app
description: Template for a HF-Spaces-targeted universal-spawn manifest.

platforms:
  huggingface-spaces:
    sdk: gradio
    visibility: public
    hardware: zero-gpu
    front_matter:
      title: Your Demo
      pinned: false

safety:
  min_permissions: [network:inbound, network:outbound:huggingface.co]

env_vars_required:
  - name: HF_TOKEN
    description: HF token used to publish the Space.
    secret: true

deployment:
  targets: [huggingface-spaces]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/hf-spaces-template }
""",
    "native_config_name": "README.md front-matter (HF Spaces convention)",
    "native_config_lang": "yaml",
    "native_config": """
title: Your Demo
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
""",
    "universal_excerpt": """
platforms:
  huggingface-spaces:
    sdk: gradio
    visibility: public
    hardware: zero-gpu
    front_matter:
      title: Your Demo
      license: apache-2.0
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Gradio Demo
type: web-app
summary: Minimal Gradio Space previewing parchment plate archetypes.
description: Public Gradio Space, zero-GPU tier.

platforms:
  huggingface-spaces:
    sdk: gradio
    visibility: public
    hardware: zero-gpu
    front_matter:
      title: Plate Demo
      pinned: false
      license: apache-2.0

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required:
  - name: HF_TOKEN
    description: HF token.
    secret: true

deployment:
  targets: [huggingface-spaces]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/hf-plate-demo }
  id: com.plate-studio.hf-plate-demo
""",
        "example-2": """
version: "1.0"
name: Inference Streamlit App
type: web-app
summary: Full Streamlit-SDK Space backed by an A10g-small GPU for live inference.
description: Streamlit interface; calls a HF inference endpoint.

platforms:
  huggingface-spaces:
    sdk: streamlit
    visibility: private
    hardware: a10g-small
    front_matter:
      title: Inference UI
      pinned: true

safety:
  min_permissions: [network:inbound, network:outbound:huggingface.co]
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: HF_TOKEN
    description: HF token.
    secret: true

deployment:
  targets: [huggingface-spaces]

metadata:
  license: Apache-2.0
  author: { name: Inference Co., handle: inference-co }
  source: { type: git, url: https://github.com/inference-co/hf-inference-streamlit }
  id: com.inference-co.hf-inference-streamlit
""",
    },
}

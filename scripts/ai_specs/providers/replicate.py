"""Replicate — model hosting target (versioned, input-schema-driven)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "replicate",
    "title": "Replicate",
    "location": ".",
    "lede": (
        "Replicate hosts models behind a pinned-version URL. Every "
        "request is `POST /predictions` with the model's declared "
        "input schema. This extension models that shape: each manifest "
        "pins one model + version + input-schema."
    ),
    "cares": (
        "The model slug (`stability-ai/sdxl`), the version hash, and "
        "the path to the input-schema JSON that Replicate generates "
        "for each model."
    ),
    "extras": (
        "`hardware` pins a GPU class when the model supports it; "
        "`webhook_ref` points to a relative spec file describing the "
        "completion webhook."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Replicate model card."),
        ("type", "`ai-model`, `ai-skill`, `creative-tool`."),
        ("safety.cost_limit_usd_daily", "Advisory; Replicate bills per-prediction."),
        ("env_vars_required", "Replicate secret store."),
        ("platforms.replicate", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Model card."),
        ("type", "`ai-model`, `ai-skill`, `creative-tool`."),
        ("safety.*", "Advisory."),
        ("env_vars_required", "Secret store."),
        ("platforms.replicate.model", "Model slug (`owner/name`)."),
        ("platforms.replicate.version", "Model version hash."),
        ("platforms.replicate.input_schema_ref", "Replicate input schema JSON."),
        ("platforms.replicate.hardware", "GPU class hint."),
        ("platforms.replicate.webhook_ref", "Completion webhook spec."),
    ],
    "platform_fields": {
        "model": "Replicate model slug (`owner/name`).",
        "version": "Model version hash (64 hex chars).",
        "input_schema_ref": "Relative path to the Replicate-generated input schema.",
        "hardware": "GPU class hint (`cpu`, `t4`, `a40`, `a100-80gb`).",
        "webhook_ref": "Relative path to the completion webhook spec.",
    },
    "schema_body": schema_object(
        required=["model", "version"],
        properties={
            "model": str_prop(
                pattern=r"^[a-z0-9-]+/[a-z0-9._-]+$",
                desc="Replicate model slug `owner/name`.",
            ),
            "version": str_prop(
                pattern=r"^[a-f0-9]{64}$",
                desc="Model version hash (SHA-256).",
            ),
            "input_schema_ref": str_prop(desc="Relative path to the Replicate input schema JSON."),
            "hardware": enum(["cpu", "t4", "a40", "a100-40gb", "a100-80gb", "h100"]),
            "webhook_ref": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Replicate Template
type: ai-model
description: Template for a Replicate-targeted universal-spawn manifest.

platforms:
  replicate:
    model: owner/example-model
    version: \"0000000000000000000000000000000000000000000000000000000000000000\"
    input_schema_ref: schemas/input.json
    hardware: a40

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 5

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate API token.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/replicate-template }
""",
    "compatibility_extras": (
        "## Pinning versions\n\n"
        "A Replicate manifest **MUST** pin `version` so every spawn "
        "runs the exact model snapshot the author validated. Consumers "
        "refuse a manifest whose `version` does not exist on Replicate."
    ),
    "perks": STANDARD_PERKS + [
        "**Hardware auto-pick** — consumers match `hardware` against "
        "the model's supported classes and downgrade with a warning "
        "if the class is unavailable.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Replicate SDXL
type: ai-model
summary: Minimal SDXL image-generation manifest on Replicate.
description: Pinned SDXL model for the Residual Frequencies plate pipeline.

platforms:
  replicate:
    model: stability-ai/sdxl
    version: \"7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc\"
    input_schema_ref: schemas/sdxl-input.json
    hardware: a40

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 3
  safe_for_auto_spawn: true

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate API token.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/replicate-sdxl }
  id: com.plate-studio.replicate-sdxl
"""},
        {"yaml": """
version: \"1.0\"
name: Replicate Whisper Pipeline
type: ai-model
summary: Full Whisper-large-v3 transcription pipeline with webhook.
description: >
  Replicate pipeline that transcribes audio via Whisper-large-v3 and
  notifies the caller via a completion webhook. Runs on an a100-40gb.

platforms:
  replicate:
    model: openai/whisper
    version: \"8099696689d249cf8b122d833c36ac3f75505c666a395ca40ef26f68e7d3d16e\"
    input_schema_ref: schemas/whisper-input.json
    hardware: a100-40gb
    webhook_ref: webhooks/completion.json

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate API token.
    secret: true
  - name: WEBHOOK_SIGNING_SECRET
    description: Shared secret for verifying completion webhooks.
    secret: true

deployment:
  targets: [replicate]

metadata:
  license: MIT
  author: { name: Transcription Co., handle: transcription-co }
  source: { type: git, url: https://github.com/transcription-co/replicate-whisper }
  id: com.transcription-co.replicate-whisper
"""},
        {"yaml": """
version: \"1.0\"
name: ControlNet Plate Composer
type: creative-tool
summary: Creative ControlNet pipeline that composes parchment plates from sketches.
description: >
  Replicate ControlNet model that takes a rough canny-edge sketch and
  renders a finished Residual Frequencies plate. Creative pipeline
  for the Plate Studio gallery.

platforms:
  replicate:
    model: jagilley/controlnet-canny
    version: \"aff48af9c68d162388d230a2ab003f68d2638d88307bdaf1c2f1ac95079c9613\"
    input_schema_ref: schemas/controlnet-input.json
    hardware: a40

safety:
  min_permissions: [network:outbound:api.replicate.com]
  cost_limit_usd_daily: 8
  safe_for_auto_spawn: true

env_vars_required:
  - name: REPLICATE_API_TOKEN
    description: Replicate API token.
    secret: true

deployment:
  targets: [replicate]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/controlnet-plates }
  categories: [ai, graphics]
  id: com.plate-studio.controlnet-plates
"""},
    ],
}

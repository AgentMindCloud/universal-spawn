"""LM Studio — desktop + local API server."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "lm-studio",
    "title": "LM Studio",
    "location": "local",
    "lede": (
        "LM Studio is a desktop app with a built-in model library and "
        "a local HTTP server at `http://localhost:1234/v1`. A manifest "
        "targets LM Studio's server surface (OpenAI-compatible) plus "
        "the desktop-specific preset metadata."
    ),
    "cares": (
        "The model id (a huggingface repo slug once loaded in LM "
        "Studio), the preset file that captures inference settings, "
        "and whether GPU offload is engaged."
    ),
    "extras": (
        "`preset_file` points at an LM Studio preset JSON. "
        "`gpu_offload` is `max`, `auto`, or an integer layer count."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Usually none — LM Studio runs locally."),
        ("platforms.lm-studio", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Shown in LM Studio's chat preset picker."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Usually none."),
        ("platforms.lm-studio.model", "HF repo slug loaded in LM Studio."),
        ("platforms.lm-studio.server_url", "Default `http://localhost:1234/v1`."),
        ("platforms.lm-studio.preset_file", "Preset JSON."),
        ("platforms.lm-studio.gpu_offload", "GPU offload level."),
        ("platforms.lm-studio.context_length", "Context length override."),
    ],
    "platform_fields": {
        "model": "HF repo slug.",
        "server_url": "LM Studio server URL.",
        "preset_file": "Preset JSON.",
        "gpu_offload": "`max`, `auto`, or layer count.",
        "context_length": "Context length override.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": str_prop(pattern=r"^[^/\s]+/[^/\s]+$"),
            "server_url": str_prop(pattern=r"^https?://"),
            "preset_file": str_prop(),
            "gpu_offload": {
                "oneOf": [
                    {"type": "string", "enum": ["max", "auto"]},
                    {"type": "integer", "minimum": 0, "maximum": 200},
                ]
            },
            "context_length": {"type": "integer", "minimum": 512, "maximum": 1048576},
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: LM Studio Template
type: ai-agent
description: Template for an LM-Studio-targeted universal-spawn manifest.

platforms:
  lm-studio:
    model: lmstudio-community/Llama-3.3-70B-Instruct-GGUF
    server_url: http://localhost:1234/v1
    preset_file: presets/default.json
    gpu_offload: max
    context_length: 8192
    temperature: 0.2

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [lm-studio]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/lm-studio-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: LM Studio Minimal
type: ai-agent
summary: Minimal LM Studio chat on default localhost URL.
description: One preset, default URL, auto GPU offload.

platforms:
  lm-studio:
    model: lmstudio-community/Qwen2.5-7B-Instruct-GGUF
    gpu_offload: auto
    context_length: 8192

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [lm-studio]

metadata:
  license: Apache-2.0
  author: { name: Local Co., handle: local-co }
  source: { type: git, url: https://github.com/local-co/lm-studio-minimal }
  id: com.local-co.lm-studio-minimal
"""},
        {"yaml": """
version: \"1.0\"
name: LM Studio Preset Pack
type: ai-skill
summary: Full LM Studio preset pack for long-context technical writing.
description: >
  Ships three presets for the same Qwen-2.5 32B model tuned for
  different writing modes (drafting, editing, summarisation). Manifest
  points at one of the presets; the rest ship as siblings.

platforms:
  lm-studio:
    model: lmstudio-community/Qwen2.5-32B-Instruct-GGUF
    preset_file: presets/drafting.json
    gpu_offload: 40
    context_length: 32768
    temperature: 0.4

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [lm-studio]

metadata:
  license: Apache-2.0
  author: { name: Writing Co., handle: writing-co }
  source: { type: git, url: https://github.com/writing-co/lm-studio-preset-pack }
  id: com.writing-co.lm-studio-preset-pack
"""},
        {"yaml": """
version: \"1.0\"
name: Offline Plate Assistant
type: ai-skill
summary: Creative LM Studio preset for fully offline plate writing.
description: >
  Offline parchment-plate writing assistant. Runs entirely on a laptop
  — no external network at all. Max GPU offload, 16k context.

platforms:
  lm-studio:
    model: lmstudio-community/gemma-3-27b-it-GGUF
    gpu_offload: max
    context_length: 16384
    temperature: 0.7

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [lm-studio]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/lm-studio-offline-plate }
  categories: [ai, graphics, writing]
  id: com.plate-studio.lm-studio-offline-plate
"""},
    ],
}

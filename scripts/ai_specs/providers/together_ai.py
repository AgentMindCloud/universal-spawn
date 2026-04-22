"""Together AI — open-model inference target."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "together-ai",
    "title": "Together AI",
    "location": ".",
    "lede": (
        "Together AI hosts hundreds of open-weight models (Llama, "
        "Qwen, DeepSeek, Mixtral, FLUX) behind a single OpenAI-"
        "compatible endpoint plus dedicated endpoints for fine-tuning "
        "and image generation. This extension targets the Chat + "
        "Images + Embeddings surfaces."
    ),
    "cares": (
        "The model id (the exact Together catalogue string), which "
        "surface is being called (chat, images, embeddings), and "
        "whether JSON mode is engaged."
    ),
    "extras": (
        "`surface` selects the endpoint family. `image.size` and "
        "`image.steps` control the image-generation request shape."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Dashboard card text."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.cost_limit_usd_daily", "Enforced at the workspace budget level."),
        ("env_vars_required", "Together secret store."),
        ("platforms.together-ai", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Dashboard card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory; cost cap enforced."),
        ("env_vars_required", "Secret store."),
        ("platforms.together-ai.model", "Together catalogue id."),
        ("platforms.together-ai.surface", "`chat`, `images`, `embeddings`."),
        ("platforms.together-ai.tools", "Function tools (chat surface only)."),
        ("platforms.together-ai.response_format", "`text`, `json_object`."),
        ("platforms.together-ai.image", "Image-generation parameters."),
    ],
    "platform_fields": {
        "model": "Together catalogue model id.",
        "surface": "`chat`, `images`, or `embeddings`.",
        "tools": "Function tools (chat surface only).",
        "response_format": "`text` or `json_object`.",
        "image": "Image-generation parameters (size, steps, guidance_scale).",
    },
    "schema_body": schema_object(
        required=["model", "surface"],
        properties={
            "model": str_prop(
                pattern=r"^[A-Za-z0-9./_-]+$",
                desc="Together catalogue id, e.g. meta-llama/Llama-3.3-70B-Instruct-Turbo.",
            ),
            "surface": enum(["chat", "images", "embeddings"]),
            "tools": tools_array(),
            "response_format": enum(["text", "json_object"]),
            "image": schema_object(
                properties={
                    "size": enum(["512x512", "1024x1024", "1024x1792", "1792x1024"]),
                    "steps": {"type": "integer", "minimum": 1, "maximum": 100},
                    "guidance_scale": {"type": "number", "minimum": 0, "maximum": 20},
                    "n": {"type": "integer", "minimum": 1, "maximum": 4},
                },
            ),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "max_tokens": {"type": "integer", "minimum": 1},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Together Template
type: ai-agent
description: Template for a Together-AI-targeted universal-spawn manifest.

platforms:
  together-ai:
    model: meta-llama/Llama-3.3-70B-Instruct-Turbo
    surface: chat
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    response_format: text
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.together.xyz]
  rate_limit_qps: 5

env_vars_required:
  - name: TOGETHER_API_KEY
    description: Together API key.
    secret: true

deployment:
  targets: [together-ai]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/together-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Catalogue resolver** — consumers resolve short model ids to "
        "the full catalogue path when the input is ambiguous.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Together Chat Helper
type: ai-agent
summary: Minimal Qwen-2.5-72B chat on Together AI.
description: Single-shot chat using the Qwen instruct turbo endpoint. No tools.

platforms:
  together-ai:
    model: Qwen/Qwen2.5-72B-Instruct-Turbo
    surface: chat
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.together.xyz]
  safe_for_auto_spawn: true

env_vars_required:
  - name: TOGETHER_API_KEY
    description: Together API key.
    secret: true

deployment:
  targets: [together-ai]

metadata:
  license: Apache-2.0
  author: { name: Helper Co., handle: helper-co }
  source: { type: git, url: https://github.com/helper-co/together-chat }
  id: com.helper-co.together-chat
"""},
        {"yaml": """
version: \"1.0\"
name: Together DeepSeek Router
type: ai-agent
summary: Full DeepSeek-V3 agent with tool router and JSON output.
description: >
  Uses DeepSeek-V3 on Together for an enterprise tool router. Four
  tools, strict JSON, and a workspace spend cap.

platforms:
  together-ai:
    model: deepseek-ai/DeepSeek-V3
    surface: chat
    tools:
      - name: create_ticket
        function_ref: tools/create_ticket.json
        strict: true
      - name: search_kb
        function_ref: tools/search_kb.json
        strict: true
      - name: escalate
        function_ref: tools/escalate.json
        strict: true
      - name: close_ticket
        function_ref: tools/close_ticket.json
        strict: true
    response_format: json_object
    temperature: 0
    max_tokens: 2048
    system_prompt_file: prompts/router.md

safety:
  min_permissions: [network:outbound:api.together.xyz]
  rate_limit_qps: 10
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: TOGETHER_API_KEY
    description: Together API key.
    secret: true

deployment:
  targets: [together-ai]

metadata:
  license: proprietary
  author: { name: Support Co., handle: support-co, org: Support }
  source: { type: git, url: https://github.com/support-co/together-router }
  id: com.support-co.together-router
"""},
        {"yaml": """
version: \"1.0\"
name: FLUX Plate Generator
type: ai-skill
summary: Creative FLUX image generator for Residual Frequencies plates.
description: >
  Image-generation skill that produces parchment-style plate sketches
  at 1024x1024. Uses FLUX.1-schnell on Together AI.

platforms:
  together-ai:
    model: black-forest-labs/FLUX.1-schnell
    surface: images
    image:
      size: 1024x1024
      steps: 8
      guidance_scale: 3.5
      n: 1

safety:
  min_permissions: [network:outbound:api.together.xyz]
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: true

env_vars_required:
  - name: TOGETHER_API_KEY
    description: Together API key.
    secret: true

deployment:
  targets: [together-ai]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/flux-plate-generator }
  categories: [ai, graphics]
  id: com.plate-studio.flux-plate-generator
"""},
    ],
}

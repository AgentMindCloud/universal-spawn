"""Fireworks AI — inference + function calling + FireFunction."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "fireworks",
    "title": "Fireworks AI",
    "location": ".",
    "lede": (
        "Fireworks AI runs open models behind an OpenAI-compatible API "
        "and adds FireFunction — a family of models fine-tuned for "
        "function calling. The extension covers both chat and "
        "FireFunction surfaces, plus Fireworks's `response_format` "
        "JSON-schema enforcement."
    ),
    "cares": (
        "The Fireworks catalogue path (starts with `accounts/fireworks/`), "
        "whether the model is a FireFunction variant, and response-"
        "format schema validation."
    ),
    "extras": (
        "`fire_function: true` signals a FireFunction model; the "
        "Fireworks console wires function calling automatically. "
        "`response_schema_ref` enables JSON Schema enforcement."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Fireworks console card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.cost_limit_usd_daily", "Enforced via Fireworks spend cap."),
        ("env_vars_required", "Fireworks secret store."),
        ("platforms.fireworks", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Console card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory; cost cap enforced."),
        ("env_vars_required", "Secret store."),
        ("platforms.fireworks.model", "Fireworks catalogue path."),
        ("platforms.fireworks.fire_function", "FireFunction flag."),
        ("platforms.fireworks.tools", "Function tools."),
        ("platforms.fireworks.response_format", "`text`, `json_object`, `json_schema`."),
        ("platforms.fireworks.response_schema_ref", "JSON Schema path."),
    ],
    "platform_fields": {
        "model": "Fireworks catalogue path (accounts/fireworks/...).",
        "fire_function": "Flag that this model is a FireFunction variant.",
        "tools": "Function tools.",
        "response_format": "`text`, `json_object`, or `json_schema`.",
        "response_schema_ref": "Relative path to JSON Schema for strict output.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": str_prop(
                pattern=r"^accounts/[a-z0-9-]+/models/[A-Za-z0-9._-]+$",
                desc="Fireworks catalogue path.",
            ),
            "fire_function": bool_prop(False),
            "tools": tools_array(),
            "response_format": enum(["text", "json_object", "json_schema"]),
            "response_schema_ref": str_prop(),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "max_tokens": {"type": "integer", "minimum": 1},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Fireworks Template
type: ai-agent
description: Template for a Fireworks-targeted universal-spawn manifest.

platforms:
  fireworks:
    model: accounts/fireworks/models/llama-v3p3-70b-instruct
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    response_format: text
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.fireworks.ai]
  rate_limit_qps: 5

env_vars_required:
  - name: FIREWORKS_API_KEY
    description: Fireworks API key.
    secret: true

deployment:
  targets: [fireworks]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/fireworks-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**FireFunction hint** — `fire_function: true` signals to the "
        "console that function calling is first-class for this model.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Fireworks Chat
type: ai-agent
summary: Minimal Llama-3.3-70B chat on Fireworks.
description: Single-shot chat on Fireworks's Llama-3.3-70B instruct model.

platforms:
  fireworks:
    model: accounts/fireworks/models/llama-v3p3-70b-instruct
    response_format: text
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.fireworks.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: FIREWORKS_API_KEY
    description: Fireworks API key.
    secret: true

deployment:
  targets: [fireworks]

metadata:
  license: Apache-2.0
  author: { name: Chat Co., handle: chat-co }
  source: { type: git, url: https://github.com/chat-co/fireworks-chat }
  id: com.chat-co.fireworks-chat
"""},
        {"yaml": """
version: \"1.0\"
name: FireFunction Router
type: ai-agent
summary: Full FireFunction-V2 router with strict JSON Schema output.
description: >
  Uses a FireFunction-V2 model to route incoming API calls to one of
  five internal tools. Enforces response shape via JSON Schema.

platforms:
  fireworks:
    model: accounts/fireworks/models/firefunction-v2
    fire_function: true
    tools:
      - name: create_order
        function_ref: tools/create_order.json
        strict: true
      - name: cancel_order
        function_ref: tools/cancel_order.json
        strict: true
      - name: refund_order
        function_ref: tools/refund_order.json
        strict: true
      - name: lookup_sku
        function_ref: tools/lookup_sku.json
        strict: true
      - name: escalate
        function_ref: tools/escalate.json
        strict: true
    response_format: json_schema
    response_schema_ref: schemas/response.json
    temperature: 0
    max_tokens: 1024

safety:
  min_permissions: [network:outbound:api.fireworks.ai]
  rate_limit_qps: 10
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: FIREWORKS_API_KEY
    description: Fireworks API key.
    secret: true

deployment:
  targets: [fireworks]

metadata:
  license: proprietary
  author: { name: Commerce Co., handle: commerce-co, org: Commerce }
  source: { type: git, url: https://github.com/commerce-co/firefunction-router }
  id: com.commerce-co.firefunction-router
"""},
        {"yaml": """
version: \"1.0\"
name: DeepSeek Plate Critic
type: ai-skill
summary: Creative DeepSeek-R1 critic that analyzes parchment plates.
description: >
  Uses DeepSeek-R1 on Fireworks to produce a one-paragraph critical
  reading of a Residual Frequencies plate, scored against the visual
  system's grammar (frame, ticks, accent usage).

platforms:
  fireworks:
    model: accounts/fireworks/models/deepseek-r1
    response_format: text
    temperature: 0.4

safety:
  min_permissions: [network:outbound:api.fireworks.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: FIREWORKS_API_KEY
    description: Fireworks API key.
    secret: true

deployment:
  targets: [fireworks]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Critic, handle: plate-critic }
  source: { type: git, url: https://github.com/plate-critic/deepseek-plate-critic }
  categories: [ai, graphics, writing]
  id: com.plate-critic.deepseek-plate-critic
"""},
    ],
}

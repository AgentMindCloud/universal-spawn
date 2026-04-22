"""Llama (Meta) — Llama Stack + Llama Guard."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "llama",
    "title": "Llama (Meta)",
    "location": "",  # directly under platforms/ai/

    "lede": (
        "Meta's Llama family (Llama 3.3, Llama 4) is distributed through "
        "Llama Stack — a reference set of inference APIs that any vendor "
        "can host. This extension covers a manifest that targets a Llama "
        "Stack endpoint (self-hosted, Together, Groq, Fireworks, and so "
        "on) and optionally engages Llama Guard for input/output safety "
        "classification."
    ),
    "cares": (
        "Llama Stack consumers care about three things: the model "
        "variant (`llama-3.3-70b-instruct`, `llama-4-scout`, "
        "`llama-4-maverick`), the Llama-Stack-compatible endpoint URL, "
        "and the Llama Guard policy file if content moderation is on. "
        "The declared `min_permissions` are enforced only when the "
        "consumer runs its own sandbox; many Llama Stack deployments "
        "delegate that to the hosting vendor."
    ),
    "extras": (
        "`llama_guard.policy_ref` points at a policy document that "
        "Llama Guard loads before the first turn. `endpoint_url` "
        "pins a specific Llama Stack server; omit it to let the "
        "consumer pick."
    ),

    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Shown on the Llama Stack server's model card."),
        ("type", "Accepts `ai-agent`, `ai-skill`, `ai-model`."),
        ("safety.min_permissions", "Enforced when the consumer sandboxes its own inference host."),
        ("safety.cost_limit_usd_daily", "Informational; most Llama Stack deployments bill through the hosting vendor."),
        ("env_vars_required", "Staged into the consumer's credential store."),
        ("platforms.llama", "Strict; see table below."),
    ],
    "compat_table_full": [
        ("version", "Required literal `\"1.0\"`."),
        ("metadata.id", "Stable key across Llama Stack consumers."),
        ("name, description", "Model card + listings."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Enforced on self-hosted sandboxes."),
        ("safety.rate_limit_qps", "Advisory."),
        ("safety.cost_limit_usd_daily", "Informational."),
        ("safety.safe_for_auto_spawn", "First-run confirmation gate."),
        ("env_vars_required", "Credential store staging."),
        ("platforms.llama.model", "Llama variant id."),
        ("platforms.llama.endpoint_url", "Llama Stack endpoint URL override."),
        ("platforms.llama.tools", "OpenAI-shaped function tools."),
        ("platforms.llama.llama_guard", "Policy file + enforcement level."),
        ("platforms.llama.quantization", "`int4`, `int8`, `fp16`, `bf16`."),
    ],
    "platform_fields": {
        "model": "Llama variant (`llama-3.3-70b-instruct`, `llama-4-scout`, …).",
        "endpoint_url": "Pin a specific Llama Stack server.",
        "tools": "OpenAI-shaped function tools.",
        "llama_guard": "Policy file + enforcement level.",
        "quantization": "Weight quantization hint.",
    },

    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "llama-3.3-70b-instruct",
                "llama-3.3-405b-instruct",
                "llama-4-scout",
                "llama-4-maverick",
                "llama-guard-4",
            ]),
            "endpoint_url": str_prop(desc="Llama Stack endpoint URL. Omit to use the consumer default."),
            "tools": tools_array(),
            "system_prompt_file": str_prop(),
            "llama_guard": schema_object(
                required=["policy_ref"],
                properties={
                    "policy_ref": str_prop(desc="Relative path to the Llama Guard policy file."),
                    "enforcement": enum(["advisory", "block"]),
                },
            ),
            "quantization": enum(["int4", "int8", "fp16", "bf16"]),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Llama Template
type: ai-agent
description: Template for a Llama-Stack-targeted universal-spawn manifest.

platforms:
  llama:
    model: llama-3.3-70b-instruct
    endpoint_url: https://llama-stack.example.com/v1
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    llama_guard:
      policy_ref: policies/default.yaml
      enforcement: block
    quantization: bf16
    temperature: 0.2

safety:
  min_permissions:
    - network:outbound:llama-stack.example.com
    - model:call:llama-3.3-70b-instruct
  rate_limit_qps: 3
  cost_limit_usd_daily: 5

env_vars_required:
  - name: LLAMA_STACK_TOKEN
    description: Bearer token for the Llama Stack endpoint.
    secret: true

deployment:
  targets: [llama]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/llama-template }
""",

    "compatibility_extras": (
        "## Endpoint portability\n\n"
        "`endpoint_url` lets the same manifest run on Meta's reference "
        "server, Together, Groq, Fireworks, or a private deployment. "
        "The Llama Stack wire protocol is identical across hosts; only "
        "the model catalogue differs."
    ),

    "perks": STANDARD_PERKS + [
        "**Llama Guard prefill** — `llama_guard.policy_ref` pre-loads "
        "the safety policy file on the server.",
        "**Endpoint auto-pick** — consumers may inspect `safety.data_residency` "
        "and route to the nearest Llama Stack host.",
    ],

    "examples": [
        {"yaml": """
version: \"1.0\"
name: Llama Classifier
type: ai-skill
summary: Minimal Llama-3.3 classifier with Llama Guard advisory mode.
description: >
  Single prompt, no tools, Llama Guard runs in advisory mode so
  responses include a safety score but are not blocked.

platforms:
  llama:
    model: llama-3.3-70b-instruct
    endpoint_url: https://llama-stack.example.com/v1
    llama_guard:
      policy_ref: policies/advisory.yaml
      enforcement: advisory
    temperature: 0

safety:
  min_permissions: [network:outbound:llama-stack.example.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: LLAMA_STACK_TOKEN
    description: Bearer token for the endpoint.
    secret: true

deployment:
  targets: [llama]

metadata:
  license: Apache-2.0
  author: { name: Classifier Co., handle: classifier-co }
  source: { type: git, url: https://github.com/classifier-co/llama-classifier }
  id: com.classifier-co.llama-classifier
"""},
        {"yaml": """
version: \"1.0\"
name: Llama Research Agent
type: ai-agent
summary: Full-featured Llama-4-Maverick research agent with tools and guard-blocked output.
description: >
  Uses Llama-4-Maverick via a self-hosted Llama Stack endpoint. Two
  function tools (search + extract), Llama Guard runs in block mode
  to reject unsafe outputs before they reach the user.

platforms:
  llama:
    model: llama-4-maverick
    endpoint_url: https://llama.internal.acme.com/v1
    tools:
      - name: search
        function_ref: tools/search.json
        strict: true
      - name: extract
        function_ref: tools/extract.json
        strict: true
    system_prompt_file: prompts/system.md
    llama_guard:
      policy_ref: policies/strict.yaml
      enforcement: block
    quantization: bf16
    temperature: 0.3

safety:
  min_permissions:
    - network:outbound:llama.internal.acme.com
    - network:outbound:api.openalex.org
    - model:call:llama-4-maverick
  rate_limit_qps: 5
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false
  data_residency: [us]

env_vars_required:
  - name: LLAMA_STACK_TOKEN
    description: Bearer token for the internal Llama Stack.
    secret: true

deployment:
  targets: [llama]

metadata:
  license: proprietary
  author: { name: Acme Research, handle: acme-research, org: Acme }
  source: { type: git, url: https://github.com/acme-research/llama-research-agent }
  id: com.acme-research.llama-research-agent
"""},
        {"yaml": """
version: \"1.0\"
name: Parchment Voice
type: ai-skill
summary: Creative Llama skill that narrates in Residual Frequencies voice.
description: >
  Takes an input paragraph and rewrites it in lab-notebook voice
  matching the Residual Frequencies design system. Unusual: uses
  an int4 quantization for edge deployment speed.

platforms:
  llama:
    model: llama-3.3-70b-instruct
    quantization: int4
    temperature: 0.9
    llama_guard:
      policy_ref: policies/creative.yaml
      enforcement: advisory

safety:
  min_permissions: [network:outbound:llama.edge.example]
  safe_for_auto_spawn: true

env_vars_required:
  - name: LLAMA_STACK_TOKEN
    description: Bearer token for the edge server.
    secret: true

deployment:
  targets: [llama]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-voice }
  categories: [ai, writing, graphics]
  id: com.plate-studio.parchment-voice
"""},
    ],
}

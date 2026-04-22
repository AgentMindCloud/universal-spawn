"""GroqCloud — fast inference (distinct from xAI Grok)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "groq-cloud",
    "title": "GroqCloud",
    "location": ".",
    "lede": (
        "GroqCloud (note: NOT xAI Grok; see `../grok/`) is an "
        "inference-only host for a set of open models — Llama 3.3, "
        "Mixtral, Gemma 2, Whisper. The extension targets the OpenAI-"
        "compatible Chat Completions endpoint Groq exposes, with one "
        "Groq-specific detail: the model id is the full Groq catalogue "
        "string."
    ),
    "cares": (
        "GroqCloud cares about the exact model id from its catalogue "
        "(`llama-3.3-70b-versatile`, `mixtral-8x7b-32768`, …), whether "
        "function calling is on, and the streaming mode."
    ),
    "extras": (
        "`response_format` enables JSON mode. `parallel_tool_calls` "
        "toggles Groq's batched tool-call support."
    ),
    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Shown on the GroqCloud console job list."),
        ("type", "Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Informational; Groq runs inference in its own sandbox."),
        ("safety.cost_limit_usd_daily", "Advisory; GroqCloud's spend cap is set on the org."),
        ("env_vars_required", "Staged into the GroqCloud secret store."),
        ("platforms.groq-cloud", "Strict; see below."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Console card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory across the board."),
        ("env_vars_required", "Secret store."),
        ("platforms.groq-cloud.model", "GroqCloud catalogue id."),
        ("platforms.groq-cloud.tools", "OpenAI-compatible function tools."),
        ("platforms.groq-cloud.response_format", "`text`, `json_object`."),
        ("platforms.groq-cloud.parallel_tool_calls", "Batched tool-call mode."),
        ("platforms.groq-cloud.streaming", "SSE streaming toggle."),
    ],
    "platform_fields": {
        "model": "GroqCloud catalogue model id.",
        "tools": "OpenAI-shaped function tools.",
        "response_format": "`text` or `json_object`.",
        "parallel_tool_calls": "Groq batched tool-call mode.",
        "streaming": "Server-sent events streaming toggle.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
                "mixtral-8x7b-32768",
                "gemma2-9b-it",
                "whisper-large-v3",
            ]),
            "tools": tools_array(),
            "response_format": enum(["text", "json_object"]),
            "parallel_tool_calls": bool_prop(True),
            "streaming": bool_prop(True),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "max_tokens": {"type": "integer", "minimum": 1},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: GroqCloud Template
type: ai-agent
description: Template for a GroqCloud-targeted universal-spawn manifest.

platforms:
  groq-cloud:
    model: llama-3.3-70b-versatile
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    response_format: text
    parallel_tool_calls: true
    streaming: true

safety:
  min_permissions: [network:outbound:api.groq.com]
  rate_limit_qps: 5

env_vars_required:
  - name: GROQ_API_KEY
    description: GroqCloud API key.
    secret: true

deployment:
  targets: [groq-cloud]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/groq-template }
""",
    "compatibility_extras": (
        "## Not to be confused with `grok/`\n\n"
        "GroqCloud is Groq's **inference** platform for open models. "
        "xAI's **Grok** model lives in `../grok/`. The spelling "
        "difference is intentional."
    ),
    "perks": STANDARD_PERKS + [
        "**Catalogue auto-resolve** — consumers pick the closest "
        "catalogue id when `model` matches a family rather than an "
        "exact id.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Groq Summarizer
type: ai-skill
summary: Minimal Llama-3.1-8b-instant summarizer on GroqCloud.
description: Single-shot summarizer using Groq's lowest-latency model. No tools.

platforms:
  groq-cloud:
    model: llama-3.1-8b-instant
    response_format: text
    streaming: true
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.groq.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: GROQ_API_KEY
    description: GroqCloud API key.
    secret: true

deployment:
  targets: [groq-cloud]

metadata:
  license: Apache-2.0
  author: { name: Summary Co., handle: summary-co }
  source: { type: git, url: https://github.com/summary-co/groq-summarizer }
  id: com.summary-co.groq-summarizer
"""},
        {"yaml": """
version: \"1.0\"
name: Groq Tool Router
type: ai-agent
summary: Full-featured Llama-3.3-70b-versatile agent with parallel tools and JSON output.
description: >
  Routes incoming requests to one of three tools based on intent.
  Uses parallel tool calls, JSON mode, and a long context window.

platforms:
  groq-cloud:
    model: llama-3.3-70b-versatile
    tools:
      - name: lookup_order
        function_ref: tools/lookup_order.json
        strict: true
      - name: file_return
        function_ref: tools/file_return.json
        strict: true
      - name: escalate
        function_ref: tools/escalate.json
        strict: true
    response_format: json_object
    parallel_tool_calls: true
    streaming: true
    temperature: 0
    max_tokens: 2048

safety:
  min_permissions: [network:outbound:api.groq.com]
  rate_limit_qps: 10
  cost_limit_usd_daily: 15
  safe_for_auto_spawn: false

env_vars_required:
  - name: GROQ_API_KEY
    description: GroqCloud API key.
    secret: true

deployment:
  targets: [groq-cloud]

metadata:
  license: proprietary
  author: { name: Retail Co., handle: retail-co, org: Retail }
  source: { type: git, url: https://github.com/retail-co/groq-router }
  id: com.retail-co.groq-router
"""},
        {"yaml": """
version: \"1.0\"
name: Whisper-Groq Transcriber
type: ai-skill
summary: Whisper-Large-v3 on GroqCloud for live-caption pipelines.
description: >
  Uses Whisper-large-v3 for audio transcription with streaming tokens.
  Pairs well with a downstream summarizer; this manifest is only the
  transcription step.

platforms:
  groq-cloud:
    model: whisper-large-v3
    streaming: true

safety:
  min_permissions:
    - network:outbound:api.groq.com
    - audio:capture
  safe_for_auto_spawn: false

env_vars_required:
  - name: GROQ_API_KEY
    description: GroqCloud API key.
    secret: true

deployment:
  targets: [groq-cloud]

metadata:
  license: MIT
  author: { name: Caption Team, handle: caption-team }
  source: { type: git, url: https://github.com/caption-team/whisper-groq }
  categories: [ai, audio]
  id: com.caption-team.whisper-groq
"""},
    ],
}

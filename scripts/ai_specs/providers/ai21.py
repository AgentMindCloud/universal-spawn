"""AI21 — Jamba + Maestro."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "ai21",
    "title": "AI21",
    "location": ".",
    "lede": (
        "AI21 ships the Jamba family of long-context hybrid-Mamba models "
        "plus Maestro, their orchestration layer. The extension handles "
        "both: Jamba for inference, Maestro for plan-then-execute "
        "workflows."
    ),
    "cares": (
        "The Jamba model id, the context-window target (Jamba goes to "
        "256k), whether Maestro orchestration is on, and the Maestro "
        "plan-level cost cap."
    ),
    "extras": (
        "`maestro.plan_file` points at a declarative plan; `maestro.max_steps` "
        "bounds the plan-execute loop."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Shown on the AI21 Studio card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.cost_limit_usd_daily", "Advisory; AI21 enforces at workspace."),
        ("env_vars_required", "AI21 secret store."),
        ("platforms.ai21", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Studio card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory."),
        ("env_vars_required", "Secret store."),
        ("platforms.ai21.model", "Jamba variant id."),
        ("platforms.ai21.tools", "Function tools."),
        ("platforms.ai21.maestro", "Maestro plan registration."),
        ("platforms.ai21.context_tokens", "Target context window."),
        ("platforms.ai21.response_format", "`text`, `json_object`."),
    ],
    "platform_fields": {
        "model": "Jamba variant id.",
        "tools": "Function tools.",
        "maestro": "Maestro plan registration.",
        "context_tokens": "Target context-window length.",
        "response_format": "`text` or `json_object`.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "jamba-1.5-large",
                "jamba-1.5-mini",
                "jamba-instruct",
            ]),
            "tools": tools_array(),
            "maestro": schema_object(
                properties={
                    "plan_file": str_prop(desc="Relative path to the Maestro plan YAML."),
                    "max_steps": {"type": "integer", "minimum": 1, "maximum": 50},
                },
            ),
            "context_tokens": {"type": "integer", "minimum": 1024, "maximum": 262144},
            "response_format": enum(["text", "json_object"]),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: AI21 Template
type: ai-agent
description: Template for an AI21-targeted universal-spawn manifest.

platforms:
  ai21:
    model: jamba-1.5-large
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    context_tokens: 65536
    response_format: text
    temperature: 0.3

safety:
  min_permissions: [network:outbound:api.ai21.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 5

env_vars_required:
  - name: AI21_API_KEY
    description: AI21 Studio API key.
    secret: true

deployment:
  targets: [ai21]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/ai21-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Maestro plan upload** — `maestro.plan_file` uploads the "
        "declarative plan to AI21 Studio on first spawn.",
        "**Context budget guard** — consumers refuse a manifest whose "
        "`context_tokens` exceeds the model's native window.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Jamba Long-doc Summarizer
type: ai-skill
summary: Minimal Jamba-1.5-mini summarizer tuned for 64k-token documents.
description: >
  One-shot summary of a long document. Uses Jamba's long context to
  avoid chunking. No tools, no Maestro.

platforms:
  ai21:
    model: jamba-1.5-mini
    context_tokens: 65536
    response_format: text
    temperature: 0.1

safety:
  min_permissions: [network:outbound:api.ai21.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: AI21_API_KEY
    description: AI21 Studio API key.
    secret: true

deployment:
  targets: [ai21]

metadata:
  license: Apache-2.0
  author: { name: Doc Co., handle: doc-co }
  source: { type: git, url: https://github.com/doc-co/jamba-summarizer }
  id: com.doc-co.jamba-summarizer
"""},
        {"yaml": """
version: \"1.0\"
name: AI21 Research Maestro
type: ai-agent
summary: Full Jamba-1.5-large agent with Maestro plan-then-execute orchestration.
description: >
  Uses Maestro to plan a three-phase research task (gather → verify →
  summarize), then executes each step with Jamba-1.5-large. 256k
  context window. JSON output.

platforms:
  ai21:
    model: jamba-1.5-large
    tools:
      - name: search_papers
        function_ref: tools/search_papers.json
        strict: true
      - name: fetch_url
        function_ref: tools/fetch_url.json
        strict: true
    maestro:
      plan_file: maestro/research-plan.yaml
      max_steps: 12
    context_tokens: 262144
    response_format: json_object
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.ai21.com]
  rate_limit_qps: 4
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: AI21_API_KEY
    description: AI21 Studio API key with Maestro access.
    secret: true

deployment:
  targets: [ai21]

metadata:
  license: proprietary
  author: { name: Research Lab, handle: research-lab, org: Lab }
  source: { type: git, url: https://github.com/research-lab/ai21-research-maestro }
  id: com.research-lab.ai21-research-maestro
"""},
        {"yaml": """
version: \"1.0\"
name: Jamba Plate Captioner
type: ai-skill
summary: Creative Jamba skill that captions Residual Frequencies plates.
description: >
  Takes a plate id and the archetype letter, returns a single caption
  in lab-notebook voice. Small model, short context.

platforms:
  ai21:
    model: jamba-instruct
    context_tokens: 4096
    response_format: text
    temperature: 0.9

safety:
  min_permissions: [network:outbound:api.ai21.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: AI21_API_KEY
    description: AI21 Studio API key.
    secret: true

deployment:
  targets: [ai21]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/jamba-captioner }
  categories: [ai, graphics, writing]
  id: com.plate-studio.jamba-captioner
"""},
    ],
}

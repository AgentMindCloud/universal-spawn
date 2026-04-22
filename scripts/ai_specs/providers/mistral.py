"""Mistral — La Plateforme + agents, function calling."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "mistral",
    "title": "Mistral",
    "location": ".",
    "lede": (
        "Mistral's La Plateforme hosts Large, Medium, Small, and the "
        "Ministraux models; the Agents surface wraps them with tool "
        "calling, JSON mode, and RAG connectors. This extension models "
        "both."
    ),
    "cares": (
        "La Plateforme cares about the model id, whether JSON mode is "
        "on, which connectors the Agent uses (web_search, "
        "document_library, code_interpreter), and the safety prompt."
    ),
    "extras": (
        "`agent.connectors[]` enables a built-in connector on the "
        "Mistral Agents surface. `json_mode: true` forces JSON output."
    ),
    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Shown on the Agents console."),
        ("type", "Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Informational; Mistral runs inference in its own sandbox."),
        ("safety.cost_limit_usd_daily", "Enforced via workspace spend cap."),
        ("env_vars_required", "Staged into workspace secrets."),
        ("platforms.mistral", "Strict; see below."),
    ],
    "compat_table_full": [
        ("version", "Required `\"1.0\"`."),
        ("metadata.id", "Stable key in the workspace."),
        ("name, description", "Agent card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Informational."),
        ("safety.rate_limit_qps", "Advisory; workspace quotas apply."),
        ("safety.cost_limit_usd_daily", "Enforced."),
        ("env_vars_required", "Workspace secret store."),
        ("platforms.mistral.model", "Mistral model id."),
        ("platforms.mistral.tools", "Function tools."),
        ("platforms.mistral.agent", "Agents-API registration."),
        ("platforms.mistral.json_mode", "Force JSON output."),
        ("platforms.mistral.safe_prompt", "Mistral safety prompt toggle."),
    ],
    "platform_fields": {
        "model": "Mistral model id.",
        "tools": "Function tools.",
        "agent": "Agents-API registration with connectors.",
        "json_mode": "Force JSON output.",
        "safe_prompt": "Mistral built-in safety prompt toggle.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "mistral-large-latest",
                "mistral-medium-latest",
                "mistral-small-latest",
                "ministral-8b-latest",
                "ministral-3b-latest",
                "codestral-latest",
                "pixtral-large-latest",
            ]),
            "tools": tools_array(),
            "agent": schema_object(
                properties={
                    "name": str_prop(),
                    "instructions_file": str_prop(),
                    "connectors": {
                        "type": "array",
                        "items": enum(["web_search", "document_library", "code_interpreter", "image_generation"]),
                    },
                },
            ),
            "json_mode": bool_prop(False),
            "safe_prompt": bool_prop(True),
            "temperature": {"type": "number", "minimum": 0, "maximum": 1.5},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Mistral Template
type: ai-agent
description: Template for a Mistral-targeted universal-spawn manifest.

platforms:
  mistral:
    model: mistral-large-latest
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    json_mode: false
    safe_prompt: true
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  rate_limit_qps: 3
  cost_limit_usd_daily: 5

env_vars_required:
  - name: MISTRAL_API_KEY
    description: La Plateforme API key.
    secret: true

deployment:
  targets: [mistral]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/mistral-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Connector prefill** — `agent.connectors[]` pre-populates the "
        "Agents-console connector picker.",
        "**JSON-mode preview** — consoles that support JSON mode "
        "preview the validated output shape from `response_format`.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Mistral SQL Helper
type: ai-agent
summary: Minimal Mistral function tool that proposes SQL for a data warehouse.
description: >
  One function tool. Takes a natural-language question and the schema
  id, returns a proposed SQL query with notes. JSON mode on.

platforms:
  mistral:
    model: mistral-medium-latest
    tools:
      - name: propose_sql
        function_ref: tools/propose_sql.json
        strict: true
    json_mode: true
    safe_prompt: true
    temperature: 0

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  rate_limit_qps: 3
  cost_limit_usd_daily: 2
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: La Plateforme API key.
    secret: true

deployment:
  targets: [mistral]

metadata:
  license: Apache-2.0
  author: { name: SQL Co., handle: sql-co }
  source: { type: git, url: https://github.com/sql-co/mistral-sql-helper }
  id: com.sql-co.mistral-sql-helper
"""},
        {"yaml": """
version: \"1.0\"
name: Mistral Research Agent
type: ai-agent
summary: Full Mistral Agent with web-search, document-library, and code-interpreter connectors.
description: >
  Research agent built on Mistral Agents. Uses web_search for fresh
  information, document_library grounded on a private corpus, and
  code_interpreter for inline analysis. Mistral-large-latest.

platforms:
  mistral:
    model: mistral-large-latest
    agent:
      name: research-agent
      instructions_file: prompts/instructions.md
      connectors: [web_search, document_library, code_interpreter]
    json_mode: false
    safe_prompt: true
    temperature: 0.3
    system_prompt_file: prompts/system.md

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  rate_limit_qps: 5
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: MISTRAL_API_KEY
    description: La Plateforme API key with Agents access.
    secret: true

deployment:
  targets: [mistral]

metadata:
  license: proprietary
  author: { name: Research Lab, handle: research-lab, org: Lab }
  source: { type: git, url: https://github.com/research-lab/mistral-research }
  id: com.research-lab.mistral-research
"""},
        {"yaml": """
version: \"1.0\"
name: Codestral Pair
type: ai-skill
summary: Codestral-based pair-programmer focused on Rust refactors.
description: >
  Creative: uses Codestral-latest for a single narrow pair-prog task —
  suggesting Rust refactors for idiomatic borrow-checker usage. No
  tools, pure system prompt.

platforms:
  mistral:
    model: codestral-latest
    system_prompt_file: prompts/rust-refactor.md
    json_mode: false
    safe_prompt: true
    temperature: 0.1

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: La Plateforme API key.
    secret: true

deployment:
  targets: [mistral]

metadata:
  license: Apache-2.0
  author: { name: Rust Tools, handle: rust-tools }
  source: { type: git, url: https://github.com/rust-tools/codestral-pair }
  categories: [ai, code, devtools]
  id: com.rust-tools.codestral-pair
"""},
    ],
}

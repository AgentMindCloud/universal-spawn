"""Cohere — Command R family + Compass."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "cohere",
    "title": "Cohere",
    "location": ".",
    "lede": (
        "Cohere's Command R / Command R+ / Command A models focus on "
        "enterprise RAG and tool use. This extension adds the Compass "
        "retrieval front end and Cohere's strict mode for JSON output."
    ),
    "cares": (
        "The model id, whether RAG is engaged via Compass, the set of "
        "connectors (`web-search`, `database`, `document`), and "
        "grounded-generation options."
    ),
    "extras": (
        "`compass.index_id` names a Compass index for retrieval. "
        "`connectors[]` lists built-in connectors to enable on every "
        "turn."
    ),
    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("name, description", "Shown on the Cohere dashboard card."),
        ("type", "Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Informational; Cohere sandboxes inference."),
        ("safety.cost_limit_usd_daily", "Enforced via workspace spend cap."),
        ("env_vars_required", "Cohere secret store."),
        ("platforms.cohere", "Strict; see below."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Dashboard card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory."),
        ("env_vars_required", "Secret store."),
        ("platforms.cohere.model", "Command model id."),
        ("platforms.cohere.tools", "Function tools."),
        ("platforms.cohere.compass", "Compass index reference."),
        ("platforms.cohere.connectors", "Built-in connector list."),
        ("platforms.cohere.grounded_generations", "Grounded-generation toggle."),
        ("platforms.cohere.safety_mode", "`CONTEXTUAL`, `STRICT`, `NONE`."),
    ],
    "platform_fields": {
        "model": "Command model id.",
        "tools": "Function tools.",
        "compass": "Compass index reference for RAG.",
        "connectors": "Built-in connector list (`web-search`, `database`, `document`).",
        "grounded_generations": "Enable grounded-generations mode.",
        "safety_mode": "Cohere safety mode preset.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "command-a-03-2025",
                "command-r-plus-08-2024",
                "command-r-08-2024",
                "command-r7b-12-2024",
            ]),
            "tools": tools_array(),
            "compass": schema_object(
                required=["index_id"],
                properties={
                    "index_id": str_prop(),
                    "top_k": {"type": "integer", "minimum": 1, "maximum": 50},
                },
            ),
            "connectors": {
                "type": "array",
                "items": enum(["web-search", "database", "document"]),
            },
            "grounded_generations": bool_prop(False),
            "safety_mode": enum(["CONTEXTUAL", "STRICT", "NONE"]),
            "system_prompt_file": str_prop(),
            "temperature": {"type": "number", "minimum": 0, "maximum": 1},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Cohere Template
type: ai-agent
description: Template for a Cohere-targeted universal-spawn manifest.

platforms:
  cohere:
    model: command-a-03-2025
    tools:
      - name: do_work
        function_ref: tools/do_work.json
        strict: true
    grounded_generations: true
    safety_mode: CONTEXTUAL
    temperature: 0.3

safety:
  min_permissions: [network:outbound:api.cohere.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 5

env_vars_required:
  - name: COHERE_API_KEY
    description: Cohere API key.
    secret: true

deployment:
  targets: [cohere]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/cohere-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Compass prefill** — `compass.index_id` pre-selects the "
        "retrieval index in the Cohere dashboard.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Cohere Support Triage
type: ai-agent
summary: Minimal Command-R ticket classifier with grounded generations.
description: >
  Classifies a ticket into three priority buckets with citations to the
  knowledge base. One function tool.

platforms:
  cohere:
    model: command-r-08-2024
    tools:
      - name: classify
        function_ref: tools/classify.json
        strict: true
    grounded_generations: true
    safety_mode: STRICT
    temperature: 0

safety:
  min_permissions: [network:outbound:api.cohere.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 2
  safe_for_auto_spawn: true

env_vars_required:
  - name: COHERE_API_KEY
    description: Cohere API key.
    secret: true

deployment:
  targets: [cohere]

metadata:
  license: Apache-2.0
  author: { name: Support Co., handle: support-co }
  source: { type: git, url: https://github.com/support-co/cohere-triage }
  id: com.support-co.cohere-triage
"""},
        {"yaml": """
version: \"1.0\"
name: Cohere Research Agent
type: ai-agent
summary: Full Command-A + Compass research agent with web-search and database connectors.
description: >
  Research agent that pulls from a Compass index of internal papers,
  augments with web-search, and queries a database connector for
  structured context. Grounded generations required.

platforms:
  cohere:
    model: command-a-03-2025
    system_prompt_file: prompts/system.md
    tools:
      - name: analyze
        function_ref: tools/analyze.json
        strict: true
    compass:
      index_id: projects/acme/indexes/papers
      top_k: 10
    connectors: [web-search, database, document]
    grounded_generations: true
    safety_mode: CONTEXTUAL
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.cohere.com]
  rate_limit_qps: 5
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false
  data_residency: [us]

env_vars_required:
  - name: COHERE_API_KEY
    description: Cohere API key.
    secret: true
  - name: COMPASS_API_KEY
    description: Compass access key.
    secret: true

deployment:
  targets: [cohere]

metadata:
  license: proprietary
  author: { name: Acme Research, handle: acme-research, org: Acme }
  source: { type: git, url: https://github.com/acme-research/cohere-research }
  id: com.acme-research.cohere-research
"""},
        {"yaml": """
version: \"1.0\"
name: Rerank Sidecar
type: ai-skill
summary: Creative Cohere skill that reranks a user search via grounded generations.
description: >
  Takes a set of candidate search results and reranks them using
  Command-R7B, then asks for a single-sentence editorial summary.
  Low-cost, no tools.

platforms:
  cohere:
    model: command-r7b-12-2024
    grounded_generations: true
    safety_mode: CONTEXTUAL
    temperature: 0.1

safety:
  min_permissions: [network:outbound:api.cohere.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: COHERE_API_KEY
    description: Cohere API key.
    secret: true

deployment:
  targets: [cohere]

metadata:
  license: MIT
  author: { name: Search Lab, handle: search-lab }
  source: { type: git, url: https://github.com/search-lab/rerank-sidecar }
  categories: [ai]
  id: com.search-lab.rerank-sidecar
"""},
    ],
}

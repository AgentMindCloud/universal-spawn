"""Perplexity — Pplx API + Sonar models."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, tools_array, schema_object,
)

SPEC = {
    "id": "perplexity",
    "title": "Perplexity",
    "location": ".",
    "lede": (
        "Perplexity's Pplx API exposes the Sonar family of "
        "search-augmented models. Every response comes with citations "
        "back to the web pages the model used, which changes how "
        "prompts and system messages are written. The extension "
        "captures that citation shape."
    ),
    "cares": (
        "The Sonar model id (`sonar`, `sonar-pro`, `sonar-reasoning`, "
        "`sonar-reasoning-pro`), the search domain allow/deny list, "
        "and recency filters."
    ),
    "extras": (
        "`search_domain_filter[]` narrows or excludes source domains; "
        "`search_recency_filter` limits to recent results "
        "(`hour`, `day`, `week`, `month`)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Shown on Perplexity's dashboard."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.min_permissions", "Informational; Perplexity runs its own sandbox."),
        ("env_vars_required", "Perplexity secret store."),
        ("platforms.perplexity", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Dashboard card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`."),
        ("safety.*", "Advisory."),
        ("env_vars_required", "Secret store."),
        ("platforms.perplexity.model", "Sonar model id."),
        ("platforms.perplexity.tools", "Function tools."),
        ("platforms.perplexity.search_domain_filter", "Domain allow/deny list."),
        ("platforms.perplexity.search_recency_filter", "Recency window."),
        ("platforms.perplexity.return_citations", "Citation-return toggle."),
        ("platforms.perplexity.return_images", "Image-return toggle."),
    ],
    "platform_fields": {
        "model": "Sonar model id.",
        "tools": "Function tools.",
        "search_domain_filter": "Domain allow or deny list (prefix with `-` for deny).",
        "search_recency_filter": "Recency window.",
        "return_citations": "Include citations in the response.",
        "return_images": "Include inline images where present.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": enum([
                "sonar",
                "sonar-pro",
                "sonar-reasoning",
                "sonar-reasoning-pro",
                "sonar-deep-research",
            ]),
            "tools": tools_array(),
            "search_domain_filter": {
                "type": "array",
                "maxItems": 10,
                "items": str_prop(),
            },
            "search_recency_filter": enum(["hour", "day", "week", "month"]),
            "return_citations": bool_prop(True),
            "return_images": bool_prop(False),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Perplexity Template
type: ai-agent
description: Template for a Perplexity Sonar-targeted universal-spawn manifest.

platforms:
  perplexity:
    model: sonar-pro
    return_citations: true
    return_images: false
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.perplexity.ai]
  rate_limit_qps: 3

env_vars_required:
  - name: PPLX_API_KEY
    description: Perplexity API key.
    secret: true

deployment:
  targets: [perplexity]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/perplexity-template }
""",
    "compatibility_extras": (
        "## Citation rendering\n\n"
        "When `return_citations: true` (the default) every response "
        "includes a `citations` array alongside the answer. Consumers "
        "that do not render these citations SHOULD disable the flag "
        "so user surface matches manifest intent."
    ),
    "perks": STANDARD_PERKS + [
        "**Domain-filter preview** — consoles preview which domains "
        "Pplx will allow before the first spawn.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Perplexity Fact Check
type: ai-skill
summary: Minimal Sonar-pro fact-check skill.
description: >
  Takes a claim, returns true/false/unclear with citations.
  Domain filter excludes two noisy sources.

platforms:
  perplexity:
    model: sonar-pro
    search_domain_filter: [\"-reddit.com\", \"-twitter.com\"]
    return_citations: true
    temperature: 0

safety:
  min_permissions: [network:outbound:api.perplexity.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: PPLX_API_KEY
    description: Perplexity API key.
    secret: true

deployment:
  targets: [perplexity]

metadata:
  license: Apache-2.0
  author: { name: Fact Co., handle: fact-co }
  source: { type: git, url: https://github.com/fact-co/pplx-fact-check }
  id: com.fact-co.pplx-fact-check
"""},
        {"yaml": """
version: \"1.0\"
name: Perplexity Deep Research
type: ai-agent
summary: Full Sonar deep-research agent with domain filter and recency window.
description: >
  Uses sonar-deep-research for multi-step research. Domain filter
  limits to three whitelisted sources, recency set to the last
  month. Returns citations and images.

platforms:
  perplexity:
    model: sonar-deep-research
    search_domain_filter:
      - arxiv.org
      - nature.com
      - science.org
    search_recency_filter: month
    return_citations: true
    return_images: true
    temperature: 0.1
    system_prompt_file: prompts/system.md

safety:
  min_permissions: [network:outbound:api.perplexity.ai]
  rate_limit_qps: 2
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false

env_vars_required:
  - name: PPLX_API_KEY
    description: Perplexity API key with deep-research access.
    secret: true

deployment:
  targets: [perplexity]

metadata:
  license: proprietary
  author: { name: Research Lab, handle: research-lab, org: Lab }
  source: { type: git, url: https://github.com/research-lab/pplx-deep-research }
  id: com.research-lab.pplx-deep-research
"""},
        {"yaml": """
version: \"1.0\"
name: Parchment News Digest
type: ai-skill
summary: Creative Pplx skill that digests parchment-style plate news daily.
description: >
  Queries Sonar for generative-art plate news from the last day,
  returns a three-line digest in lab-notebook voice. No tools.

platforms:
  perplexity:
    model: sonar
    search_recency_filter: day
    return_citations: true
    return_images: false
    temperature: 0.7

safety:
  min_permissions: [network:outbound:api.perplexity.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: PPLX_API_KEY
    description: Perplexity API key.
    secret: true

deployment:
  targets: [perplexity]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-news }
  categories: [ai, writing, graphics]
  id: com.plate-studio.parchment-news
"""},
    ],
}

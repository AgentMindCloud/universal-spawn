"""LiteLLM — provider-agnostic router (Python)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "litellm",
    "title": "LiteLLM",
    "location": "multi-agent",

    "lede": (
        "LiteLLM normalizes calls across 100+ model providers behind "
        "the OpenAI API shape. A manifest declares the router's model "
        "list, the fallback chain, and any caching or budget policy. "
        "The runtime is the LiteLLM Proxy or the in-process library."
    ),
    "cares": (
        "The model list (each entry names a provider-prefixed model id "
        "like `openai/gpt-5` or `anthropic/claude-opus-4-7`), the "
        "fallback chain, and router-level rate limits."
    ),
    "extras": (
        "`router.routing_strategy` picks among `simple-shuffle`, "
        "`least-busy`, `usage-based-routing`. `cache.type` is "
        "`redis`, `memory`, `disk`, or `none`."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `workflow`, `library`."),
        ("safety.*", "Informational; LiteLLM enforces per-model rate limits instead."),
        ("env_vars_required", "Router secret store (one key per provider)."),
        ("platforms.litellm", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Router metadata."),
        ("type", "`ai-agent`, `workflow`, `library`."),
        ("safety.rate_limit_qps", "Enforced by the router."),
        ("safety.cost_limit_usd_daily", "Enforced by the router budget."),
        ("env_vars_required", "Provider keys."),
        ("platforms.litellm.mode", "`proxy`, `library`."),
        ("platforms.litellm.model_list", "Routed model list."),
        ("platforms.litellm.fallbacks", "Per-model fallback chain."),
        ("platforms.litellm.router.routing_strategy", "Routing strategy."),
        ("platforms.litellm.cache", "Response cache settings."),
        ("platforms.litellm.budget", "Daily budget settings."),
    ],
    "platform_fields": {
        "mode": "`proxy` or `library`.",
        "model_list": "Routed model list (`{model_name, litellm_params}`).",
        "fallbacks": "`{model: [fallback, ...]}` map.",
        "router": "Routing strategy.",
        "cache": "Response cache.",
        "budget": "Daily budget.",
    },
    "schema_body": schema_object(
        required=["mode", "model_list"],
        properties={
            "mode": enum(["proxy", "library"]),
            "model_list": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["model_name", "litellm_params"],
                    properties={
                        "model_name": str_prop(),
                        "litellm_params": schema_object(
                            required=["model"],
                            properties={
                                "model": str_prop(),
                                "api_base": str_prop(),
                                "api_key_env": str_prop(pattern=r"^[A-Z][A-Z0-9_]*$"),
                                "rpm": {"type": "integer", "minimum": 1},
                            },
                            additional=True,
                        ),
                    },
                ),
            },
            "fallbacks": {
                "type": "object",
                "additionalProperties": {"type": "array", "items": str_prop()},
            },
            "router": schema_object(
                properties={
                    "routing_strategy": enum(["simple-shuffle", "least-busy", "usage-based-routing"]),
                    "allowed_fails": {"type": "integer", "minimum": 0},
                },
            ),
            "cache": schema_object(
                properties={
                    "type": enum(["redis", "memory", "disk", "none"]),
                    "redis_url_env": str_prop(pattern=r"^[A-Z][A-Z0-9_]*$"),
                    "ttl_seconds": {"type": "integer", "minimum": 1},
                },
            ),
            "budget": schema_object(
                properties={
                    "max_budget_usd": {"type": "number", "minimum": 0},
                    "reset_period": enum(["daily", "weekly", "monthly"]),
                },
            ),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: LiteLLM Template
type: workflow
description: Template for a LiteLLM-targeted universal-spawn manifest.

platforms:
  litellm:
    mode: proxy
    model_list:
      - model_name: default
        litellm_params:
          model: anthropic/claude-sonnet-4-6
          api_key_env: ANTHROPIC_API_KEY
          rpm: 60
      - model_name: fast
        litellm_params:
          model: openai/gpt-5-nano
          api_key_env: OPENAI_API_KEY
    fallbacks:
      default: [fast]
    router:
      routing_strategy: simple-shuffle
      allowed_fails: 3
    cache:
      type: redis
      redis_url_env: LITELLM_REDIS_URL
      ttl_seconds: 3600
    budget:
      max_budget_usd: 20
      reset_period: daily

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openai.com
  rate_limit_qps: 10
  cost_limit_usd_daily: 20

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI key.
    secret: true
  - name: LITELLM_REDIS_URL
    description: Redis URL for response cache.
    secret: true

deployment:
  targets: [litellm]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/litellm-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Model list preview** — consoles preview the routed model "
        "list with health check indicators.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: LiteLLM Library
type: library
summary: Minimal LiteLLM library-mode router with one model.
description: In-process router, one model (Claude Haiku), no cache, no budget.

platforms:
  litellm:
    mode: library
    model_list:
      - model_name: default
        litellm_params:
          model: anthropic/claude-haiku-4-5-20251001
          api_key_env: ANTHROPIC_API_KEY

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [litellm]

metadata:
  license: MIT
  author: { name: Router Co., handle: router-co }
  source: { type: git, url: https://github.com/router-co/litellm-library }
  id: com.router-co.litellm-library
"""},
        {"yaml": """
version: \"1.0\"
name: LiteLLM Proxy Cluster
type: workflow
summary: Full LiteLLM proxy with six providers, fallbacks, Redis cache, and daily budget.
description: >
  Proxy-mode LiteLLM with Anthropic, OpenAI, Gemini, Mistral, Together,
  and a local Ollama. Each family has a fallback chain. Redis cache
  with 1-hour TTL. $50 daily budget.

platforms:
  litellm:
    mode: proxy
    model_list:
      - { model_name: reasoning, litellm_params: { model: anthropic/claude-opus-4-7, api_key_env: ANTHROPIC_API_KEY, rpm: 60 } }
      - { model_name: reasoning-backup, litellm_params: { model: openai/gpt-5, api_key_env: OPENAI_API_KEY, rpm: 60 } }
      - { model_name: fast, litellm_params: { model: anthropic/claude-haiku-4-5-20251001, api_key_env: ANTHROPIC_API_KEY, rpm: 120 } }
      - { model_name: fast-backup, litellm_params: { model: gemini/gemini-2-5-flash, api_key_env: GOOGLE_API_KEY, rpm: 120 } }
      - { model_name: cheap, litellm_params: { model: mistral/mistral-small-latest, api_key_env: MISTRAL_API_KEY, rpm: 60 } }
      - { model_name: local, litellm_params: { model: ollama/llama3.3, api_base: http://ollama:11434 } }
    fallbacks:
      reasoning: [reasoning-backup, fast]
      fast: [fast-backup, cheap, local]
    router:
      routing_strategy: least-busy
      allowed_fails: 2
    cache:
      type: redis
      redis_url_env: LITELLM_REDIS_URL
      ttl_seconds: 3600
    budget:
      max_budget_usd: 50
      reset_period: daily

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openai.com
    - network:outbound:generativelanguage.googleapis.com
    - network:outbound:api.mistral.ai
    - network:outbound:ollama
  rate_limit_qps: 20
  cost_limit_usd_daily: 50
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI key.
    secret: true
  - name: GOOGLE_API_KEY
    description: Google key.
    secret: true
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true
  - name: LITELLM_REDIS_URL
    description: Redis URL.
    secret: true

deployment:
  targets: [litellm]

metadata:
  license: MIT
  author: { name: Platform Team, handle: platform-team, org: Platform }
  source: { type: git, url: https://github.com/platform-team/litellm-cluster }
  id: com.platform-team.litellm-cluster
"""},
        {"yaml": """
version: \"1.0\"
name: Parchment Router
type: workflow
summary: Creative LiteLLM router switching between three models by plate archetype.
description: >
  One route per plate archetype (A..F). Each archetype prefers a
  different model by creative fit — Opus for F (Module Constellation),
  Sonnet for A, Haiku for D. Demonstrates custom routing by user
  metadata.

platforms:
  litellm:
    mode: library
    model_list:
      - { model_name: f-archetype, litellm_params: { model: anthropic/claude-opus-4-7, api_key_env: ANTHROPIC_API_KEY } }
      - { model_name: a-archetype, litellm_params: { model: anthropic/claude-sonnet-4-6, api_key_env: ANTHROPIC_API_KEY } }
      - { model_name: d-archetype, litellm_params: { model: anthropic/claude-haiku-4-5-20251001, api_key_env: ANTHROPIC_API_KEY } }
    router:
      routing_strategy: usage-based-routing
      allowed_fails: 1
    cache: { type: memory, ttl_seconds: 600 }

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [litellm]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-router }
  categories: [ai, graphics]
  id: com.plate-studio.parchment-router
"""},
    ],
}

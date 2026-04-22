# LiteLLM compatibility — field-by-field

| universal-spawn v1.0 field | LiteLLM behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Router metadata. |
| `type` | `ai-agent`, `workflow`, `library`. |
| `safety.rate_limit_qps` | Enforced by the router. |
| `safety.cost_limit_usd_daily` | Enforced by the router budget. |
| `env_vars_required` | Provider keys. |
| `platforms.litellm.mode` | `proxy`, `library`. |
| `platforms.litellm.model_list` | Routed model list. |
| `platforms.litellm.fallbacks` | Per-model fallback chain. |
| `platforms.litellm.router.routing_strategy` | Routing strategy. |
| `platforms.litellm.cache` | Response cache settings. |
| `platforms.litellm.budget` | Daily budget settings. |



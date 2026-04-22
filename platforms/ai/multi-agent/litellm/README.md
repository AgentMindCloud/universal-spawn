# LiteLLM — universal-spawn platform extension

LiteLLM normalizes calls across 100+ model providers behind the OpenAI API shape. A manifest declares the router's model list, the fallback chain, and any caching or budget policy. The runtime is the LiteLLM Proxy or the in-process library.

## What this platform cares about

The model list (each entry names a provider-prefixed model id like `openai/gpt-5` or `anthropic/claude-opus-4-7`), the fallback chain, and router-level rate limits.

## What platform-specific extras unlock

`router.routing_strategy` picks among `simple-shuffle`, `least-busy`, `usage-based-routing`. `cache.type` is `redis`, `memory`, `disk`, or `none`.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | LiteLLM behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `workflow`, `library`. |
| `safety.*` | Informational; LiteLLM enforces per-model rate limits instead. |
| `env_vars_required` | Router secret store (one key per provider). |
| `platforms.litellm` | Strict. |

### `platforms.litellm` fields

| Field | Purpose |
|---|---|
| `platforms.litellm.mode` | `proxy` or `library`. |
| `platforms.litellm.model_list` | Routed model list (`{model_name, litellm_params}`). |
| `platforms.litellm.fallbacks` | `{model: [fallback, ...]}` map. |
| `platforms.litellm.router` | Routing strategy. |
| `platforms.litellm.cache` | Response cache. |
| `platforms.litellm.budget` | Daily budget. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

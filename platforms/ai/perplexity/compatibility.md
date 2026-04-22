# Perplexity compatibility — field-by-field

| universal-spawn v1.0 field | Perplexity behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Dashboard card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory. |
| `env_vars_required` | Secret store. |
| `platforms.perplexity.model` | Sonar model id. |
| `platforms.perplexity.tools` | Function tools. |
| `platforms.perplexity.search_domain_filter` | Domain allow/deny list. |
| `platforms.perplexity.search_recency_filter` | Recency window. |
| `platforms.perplexity.return_citations` | Citation-return toggle. |
| `platforms.perplexity.return_images` | Image-return toggle. |

## Citation rendering

When `return_citations: true` (the default) every response includes a `citations` array alongside the answer. Consumers that do not render these citations SHOULD disable the flag so user surface matches manifest intent.

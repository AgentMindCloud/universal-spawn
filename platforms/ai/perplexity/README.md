# Perplexity — universal-spawn platform extension

Perplexity's Pplx API exposes the Sonar family of search-augmented models. Every response comes with citations back to the web pages the model used, which changes how prompts and system messages are written. The extension captures that citation shape.

## What this platform cares about

The Sonar model id (`sonar`, `sonar-pro`, `sonar-reasoning`, `sonar-reasoning-pro`), the search domain allow/deny list, and recency filters.

## What platform-specific extras unlock

`search_domain_filter[]` narrows or excludes source domains; `search_recency_filter` limits to recent results (`hour`, `day`, `week`, `month`).

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Perplexity behavior |
|---|---|
| `version` | Required. |
| `name, description` | Shown on Perplexity's dashboard. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Informational; Perplexity runs its own sandbox. |
| `env_vars_required` | Perplexity secret store. |
| `platforms.perplexity` | Strict. |

### `platforms.perplexity` fields

| Field | Purpose |
|---|---|
| `platforms.perplexity.model` | Sonar model id. |
| `platforms.perplexity.tools` | Function tools. |
| `platforms.perplexity.search_domain_filter` | Domain allow or deny list (prefix with `-` for deny). |
| `platforms.perplexity.search_recency_filter` | Recency window. |
| `platforms.perplexity.return_citations` | Include citations in the response. |
| `platforms.perplexity.return_images` | Include inline images where present. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

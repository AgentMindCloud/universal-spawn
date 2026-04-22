# Cohere — universal-spawn platform extension

Cohere's Command R / Command R+ / Command A models focus on enterprise RAG and tool use. This extension adds the Compass retrieval front end and Cohere's strict mode for JSON output.

## What this platform cares about

The model id, whether RAG is engaged via Compass, the set of connectors (`web-search`, `database`, `document`), and grounded-generation options.

## What platform-specific extras unlock

`compass.index_id` names a Compass index for retrieval. `connectors[]` lists built-in connectors to enable on every turn.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Cohere behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Shown on the Cohere dashboard card. |
| `type` | Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Informational; Cohere sandboxes inference. |
| `safety.cost_limit_usd_daily` | Enforced via workspace spend cap. |
| `env_vars_required` | Cohere secret store. |
| `platforms.cohere` | Strict; see below. |

### `platforms.cohere` fields

| Field | Purpose |
|---|---|
| `platforms.cohere.model` | Command model id. |
| `platforms.cohere.tools` | Function tools. |
| `platforms.cohere.compass` | Compass index reference for RAG. |
| `platforms.cohere.connectors` | Built-in connector list (`web-search`, `database`, `document`). |
| `platforms.cohere.grounded_generations` | Enable grounded-generations mode. |
| `platforms.cohere.safety_mode` | Cohere safety mode preset. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

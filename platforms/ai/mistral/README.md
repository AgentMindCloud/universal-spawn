# Mistral — universal-spawn platform extension

Mistral's La Plateforme hosts Large, Medium, Small, and the Ministraux models; the Agents surface wraps them with tool calling, JSON mode, and RAG connectors. This extension models both.

## What this platform cares about

La Plateforme cares about the model id, whether JSON mode is on, which connectors the Agent uses (web_search, document_library, code_interpreter), and the safety prompt.

## What platform-specific extras unlock

`agent.connectors[]` enables a built-in connector on the Mistral Agents surface. `json_mode: true` forces JSON output.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Mistral behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Shown on the Agents console. |
| `type` | Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Informational; Mistral runs inference in its own sandbox. |
| `safety.cost_limit_usd_daily` | Enforced via workspace spend cap. |
| `env_vars_required` | Staged into workspace secrets. |
| `platforms.mistral` | Strict; see below. |

### `platforms.mistral` fields

| Field | Purpose |
|---|---|
| `platforms.mistral.model` | Mistral model id. |
| `platforms.mistral.tools` | Function tools. |
| `platforms.mistral.agent` | Agents-API registration with connectors. |
| `platforms.mistral.json_mode` | Force JSON output. |
| `platforms.mistral.safe_prompt` | Mistral built-in safety prompt toggle. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

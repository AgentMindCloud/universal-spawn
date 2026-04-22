# Fireworks AI — universal-spawn platform extension

Fireworks AI runs open models behind an OpenAI-compatible API and adds FireFunction — a family of models fine-tuned for function calling. The extension covers both chat and FireFunction surfaces, plus Fireworks's `response_format` JSON-schema enforcement.

## What this platform cares about

The Fireworks catalogue path (starts with `accounts/fireworks/`), whether the model is a FireFunction variant, and response-format schema validation.

## What platform-specific extras unlock

`fire_function: true` signals a FireFunction model; the Fireworks console wires function calling automatically. `response_schema_ref` enables JSON Schema enforcement.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Fireworks AI behavior |
|---|---|
| `version` | Required. |
| `name, description` | Fireworks console card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.cost_limit_usd_daily` | Enforced via Fireworks spend cap. |
| `env_vars_required` | Fireworks secret store. |
| `platforms.fireworks` | Strict. |

### `platforms.fireworks` fields

| Field | Purpose |
|---|---|
| `platforms.fireworks.model` | Fireworks catalogue path (accounts/fireworks/...). |
| `platforms.fireworks.fire_function` | Flag that this model is a FireFunction variant. |
| `platforms.fireworks.tools` | Function tools. |
| `platforms.fireworks.response_format` | `text`, `json_object`, or `json_schema`. |
| `platforms.fireworks.response_schema_ref` | Relative path to JSON Schema for strict output. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

# Fireworks AI compatibility — field-by-field

| universal-spawn v1.0 field | Fireworks AI behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Console card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory; cost cap enforced. |
| `env_vars_required` | Secret store. |
| `platforms.fireworks.model` | Fireworks catalogue path. |
| `platforms.fireworks.fire_function` | FireFunction flag. |
| `platforms.fireworks.tools` | Function tools. |
| `platforms.fireworks.response_format` | `text`, `json_object`, `json_schema`. |
| `platforms.fireworks.response_schema_ref` | JSON Schema path. |



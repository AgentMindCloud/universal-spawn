# AI21 compatibility — field-by-field

| universal-spawn v1.0 field | AI21 behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Studio card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory. |
| `env_vars_required` | Secret store. |
| `platforms.ai21.model` | Jamba variant id. |
| `platforms.ai21.tools` | Function tools. |
| `platforms.ai21.maestro` | Maestro plan registration. |
| `platforms.ai21.context_tokens` | Target context window. |
| `platforms.ai21.response_format` | `text`, `json_object`. |



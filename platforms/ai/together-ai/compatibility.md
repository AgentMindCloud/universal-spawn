# Together AI compatibility — field-by-field

| universal-spawn v1.0 field | Together AI behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Dashboard card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory; cost cap enforced. |
| `env_vars_required` | Secret store. |
| `platforms.together-ai.model` | Together catalogue id. |
| `platforms.together-ai.surface` | `chat`, `images`, `embeddings`. |
| `platforms.together-ai.tools` | Function tools (chat surface only). |
| `platforms.together-ai.response_format` | `text`, `json_object`. |
| `platforms.together-ai.image` | Image-generation parameters. |



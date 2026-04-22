# Cohere compatibility — field-by-field

| universal-spawn v1.0 field | Cohere behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Dashboard card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory. |
| `env_vars_required` | Secret store. |
| `platforms.cohere.model` | Command model id. |
| `platforms.cohere.tools` | Function tools. |
| `platforms.cohere.compass` | Compass index reference. |
| `platforms.cohere.connectors` | Built-in connector list. |
| `platforms.cohere.grounded_generations` | Grounded-generation toggle. |
| `platforms.cohere.safety_mode` | `CONTEXTUAL`, `STRICT`, `NONE`. |



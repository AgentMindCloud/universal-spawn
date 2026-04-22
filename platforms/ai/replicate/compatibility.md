# Replicate compatibility — field-by-field

| universal-spawn v1.0 field | Replicate behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Model card. |
| `type` | `ai-model`, `ai-skill`, `creative-tool`. |
| `safety.*` | Advisory. |
| `env_vars_required` | Secret store. |
| `platforms.replicate.model` | Model slug (`owner/name`). |
| `platforms.replicate.version` | Model version hash. |
| `platforms.replicate.input_schema_ref` | Replicate input schema JSON. |
| `platforms.replicate.hardware` | GPU class hint. |
| `platforms.replicate.webhook_ref` | Completion webhook spec. |

## Pinning versions

A Replicate manifest **MUST** pin `version` so every spawn runs the exact model snapshot the author validated. Consumers refuse a manifest whose `version` does not exist on Replicate.

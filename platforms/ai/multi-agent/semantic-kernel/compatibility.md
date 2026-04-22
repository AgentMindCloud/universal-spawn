# Semantic Kernel (Microsoft) compatibility — field-by-field

| universal-spawn v1.0 field | Semantic Kernel (Microsoft) behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Kernel metadata. |
| `type` | `ai-agent`, `workflow`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secret store. |
| `platforms.semantic-kernel.language` | `csharp`, `python`, `java`. |
| `platforms.semantic-kernel.connector` | Kernel connector. |
| `platforms.semantic-kernel.model` | Model id passed to the connector. |
| `platforms.semantic-kernel.skills` | Array of skill definitions. |
| `platforms.semantic-kernel.planner` | Planner kind. |



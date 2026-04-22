# Mastra compatibility — field-by-field

| universal-spawn v1.0 field | Mastra behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Mastra card. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secret store. |
| `platforms.mastra.agents` | Agents array. |
| `platforms.mastra.workflows` | Workflows array. |
| `platforms.mastra.memory` | Memory backend. |
| `platforms.mastra.telemetry` | OTLP telemetry. |
| `platforms.mastra.deploy` | Deployment runtime. |



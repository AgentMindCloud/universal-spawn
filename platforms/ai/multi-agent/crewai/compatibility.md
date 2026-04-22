# CrewAI compatibility — field-by-field

| universal-spawn v1.0 field | CrewAI behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Crew metadata. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational; CrewAI delegates to the model providers. |
| `env_vars_required` | Secret store. |
| `platforms.crewai.process` | `sequential`, `hierarchical`, `parallel`. |
| `platforms.crewai.roles` | Array of role definitions. |
| `platforms.crewai.tasks` | Array of task definitions. |
| `platforms.crewai.verbose` | Verbose logging toggle. |

## Declarative → programmatic

CrewAI scaffolding reads this manifest and emits the equivalent `Agent`, `Task`, and `Crew` definitions in Python. Each role maps to an `Agent`; each task to a `Task`; the crew wraps them with the declared `process`. Declarative fields round-trip to programmatic symbols by name.

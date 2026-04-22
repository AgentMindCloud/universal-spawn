# Semantic Kernel (Microsoft) — universal-spawn platform extension

Semantic Kernel is Microsoft's orchestration framework organized around skills (collections of native or prompt functions) and planners (auto-invoked via function calling). A manifest declares the language runtime, the connector, the skills that get loaded at boot, and the planner kind.

## What this platform cares about

The language (`csharp`, `python`, `java`), the connector (OpenAI / Azure OpenAI / HuggingFace / local), the skills array, and which planner runs the show.

## What platform-specific extras unlock

`skills[].kind` is `native`, `prompt`, or `openapi`. `planner` picks `function-calling`, `handlebars`, `sequential`, or `none`.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Semantic Kernel (Microsoft) behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `workflow`, `library`. |
| `safety.*` | Informational; enforced at the connector. |
| `env_vars_required` | Runtime host secret store. |
| `platforms.semantic-kernel` | Strict. |

### `platforms.semantic-kernel` fields

| Field | Purpose |
|---|---|
| `platforms.semantic-kernel.language` | `csharp`, `python`, or `java`. |
| `platforms.semantic-kernel.connector` | `openai`, `azure-openai`, `huggingface`, `ollama`, `local`. |
| `platforms.semantic-kernel.model` | Model id for the connector. |
| `platforms.semantic-kernel.skills` | Array of `{name, kind, path}` skill definitions. |
| `platforms.semantic-kernel.planner` | `function-calling`, `handlebars`, `sequential`, `none`. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

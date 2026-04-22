# Continue — universal-spawn platform extension

Continue is an open-source IDE extension for VS Code and JetBrains. Configuration lives in `~/.continue/config.yaml`. A universal-spawn manifest targets Continue by declaring the provider list, system prompts, context providers, and rule files.

## What this platform cares about

The model list (one entry per role — chat, edit, apply, autocomplete, embed, rerank), context providers, and rule files.

## What platform-specific extras unlock

`context_providers[]` lists Continue context providers (`codebase`, `docs`, `diff`, `currentFile`, etc.).

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Continue behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `ai-skill`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | User env. |
| `platforms.continue` | Strict. |

### `platforms.continue` fields

| Field | Purpose |
|---|---|
| `platforms.continue.models` | Model list by role. |
| `platforms.continue.system_prompt_file` | System prompt. |
| `platforms.continue.context_providers` | Context providers. |
| `platforms.continue.rules_files` | Rule files. |
| `platforms.continue.ide` | Target IDEs. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

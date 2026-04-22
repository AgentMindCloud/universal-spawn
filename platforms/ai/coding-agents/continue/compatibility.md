# Continue compatibility — field-by-field

| universal-spawn v1.0 field | Continue behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Shown in Continue's assistant picker. |
| `type` | `extension`, `plugin`, `ai-skill`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | User env. |
| `platforms.continue.models` | Model list keyed by role. |
| `platforms.continue.system_prompt_file` | Path to the system prompt. |
| `platforms.continue.context_providers` | Context providers. |
| `platforms.continue.rules_files` | Rule files (`.continuerules`). |
| `platforms.continue.ide` | Target IDEs (`vscode`, `jetbrains`). |



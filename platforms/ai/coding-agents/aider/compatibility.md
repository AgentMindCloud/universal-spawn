# Aider compatibility — field-by-field

| universal-spawn v1.0 field | Aider behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Shown in `aider --install <name>` listings. |
| `type` | `cli-tool`, `extension`, `ai-skill`. |
| `safety.*` | Enforced via wrapper. |
| `env_vars_required` | Shell env. |
| `platforms.aider.provider` | Model provider. |
| `platforms.aider.model` | Model id. |
| `platforms.aider.edit_format` | Edit format. |
| `platforms.aider.auto_commits` | Commit-per-edit toggle. |
| `platforms.aider.map_tokens` | Repo-map context window size. |
| `platforms.aider.read` | Read allowlist. |
| `platforms.aider.config_file` | Path to the .aider.conf.yml. |



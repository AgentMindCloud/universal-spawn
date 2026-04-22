# Aider — universal-spawn platform extension

Aider is a CLI pair-programmer that edits a git repository directly, committing as it goes. Creations targeting Aider are typically rule files in `.aider.conf.yml` or task-specific wrappers around the CLI.

## What this platform cares about

The model selection, edit format (`diff`, `whole`, `udiff`, `editor-diff`), the auto-commit toggle, and the read/write file allowlist.

## What platform-specific extras unlock

`auto_commits` toggles git commits per edit. `map_tokens` sizes the repo-map context window.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Aider behavior |
|---|---|
| `version` | Required. |
| `type` | `cli-tool`, `extension`, `ai-skill`. |
| `safety.min_permissions` | Enforced when Aider runs under a sandboxed wrapper; Aider itself does not sandbox. |
| `env_vars_required` | User shell env. |
| `platforms.aider` | Strict. |

### `platforms.aider` fields

| Field | Purpose |
|---|---|
| `platforms.aider.provider` | Model provider. |
| `platforms.aider.model` | Model id. |
| `platforms.aider.edit_format` | `diff`, `whole`, `udiff`, `editor-diff`. |
| `platforms.aider.auto_commits` | Commit per edit toggle. |
| `platforms.aider.map_tokens` | Repo-map context window size. |
| `platforms.aider.read` | Read allowlist (relative paths). |
| `platforms.aider.config_file` | Path to the .aider.conf.yml. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

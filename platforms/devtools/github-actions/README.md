# GitHub Actions — universal-spawn platform extension

GitHub Actions are either workflow files (`.github/workflows/*.yaml`) or reusable actions (`action.yml` at repo root). A universal-spawn manifest picks one and records the events it listens for, the runner, and the publication channel (Actions Marketplace).

## What this platform cares about

The `kind` (`workflow`, `reusable-action`), triggers, runner images, and the Marketplace category.

## Compatibility table

| Manifest field | GitHub Actions behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `library`, `cli-tool`. |
| `platforms.github-actions` | Strict. |

### `platforms.github-actions` fields

| Field | Purpose |
|---|---|
| `platforms.github-actions.kind` | `workflow` or `reusable-action`. |
| `platforms.github-actions.workflow_file` | Workflow file path. |
| `platforms.github-actions.action_type` | `docker`, `composite`, `javascript`. |
| `platforms.github-actions.runs_on` | Runner labels. |
| `platforms.github-actions.triggers` | Workflow triggers. |
| `platforms.github-actions.marketplace_category` | Marketplace category. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

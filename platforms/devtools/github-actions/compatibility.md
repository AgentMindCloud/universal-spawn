# GitHub Actions compatibility — field-by-field

| universal-spawn v1.0 field | GitHub Actions behavior |
|---|---|
| `version` | Required. |
| `platforms.github-actions.kind` | `workflow`, `reusable-action`. |
| `platforms.github-actions.workflow_file` | Workflow file path. |
| `platforms.github-actions.action_type` | `docker`, `composite`, `javascript`. |
| `platforms.github-actions.runs_on` | Runner list. |
| `platforms.github-actions.triggers` | Events. |
| `platforms.github-actions.marketplace_category` | Marketplace category. |

## Coexistence with `.github/workflows/*.yaml / action.yml`

universal-spawn does NOT replace .github/workflows/*.yaml / action.yml. Both files coexist; consumers read both and warn on conflicts.

### `.github/workflows/*.yaml / action.yml` (provider-native)

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo ok
```

### `universal-spawn.yaml` (platforms.github-actions block)

```yaml
platforms:
  github-actions:
    kind: workflow
    workflow_file: .github/workflows/ci.yaml
    runs_on: [ubuntu-latest]
    triggers: [push, pull_request]
```

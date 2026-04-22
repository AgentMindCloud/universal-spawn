# Paperspace compatibility — field-by-field

| universal-spawn v1.0 field | Paperspace behavior |
|---|---|
| `version` | Required. |
| `platforms.paperspace.surface` | `gradient-notebook`, `gradient-deployment`, `machine`. |
| `platforms.paperspace.gpu` | GPU class. |
| `platforms.paperspace.team_id` | Paperspace team id. |
| `platforms.paperspace.project_id` | Paperspace project id. |
| `platforms.paperspace.image` | Container image (deployment / notebook). |

## Coexistence with `Paperspace dashboard / Gradient project`

universal-spawn does NOT replace Paperspace dashboard / Gradient project. Both files coexist; consumers read both and warn on conflicts.

### `Paperspace dashboard / Gradient project` (provider-native)

```text
# Paperspace stores resource state in the Gradient project; this manifest mirrors it.
```

### `universal-spawn.yaml` (platforms.paperspace block)

```yaml
platforms:
  paperspace:
    surface: gradient-notebook
    gpu: A4000
```

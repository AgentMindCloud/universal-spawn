# Weights & Biases compatibility — field-by-field

| universal-spawn v1.0 field | Weights & Biases behavior |
|---|---|
| `version` | Required. |
| `platforms.weights-and-biases.entity` | W&B entity. |
| `platforms.weights-and-biases.project` | W&B project. |
| `platforms.weights-and-biases.sweep_file` | Sweep config YAML path. |
| `platforms.weights-and-biases.artifact_registry` | Artifact registry name. |
| `platforms.weights-and-biases.visibility` | `public` or `private`. |

## Coexistence with `wandb/config.yaml + sweep.yaml`

universal-spawn does NOT replace wandb/config.yaml + sweep.yaml. Both files coexist; consumers read both and warn on conflicts.

### `wandb/config.yaml + sweep.yaml` (provider-native)

```yaml
program: train.py
method: bayes
metric: { name: val_loss, goal: minimize }
parameters:
  learning_rate:
    min: 0.0001
    max: 0.1
```

### `universal-spawn.yaml` (platforms.weights-and-biases block)

```yaml
platforms:
  weights-and-biases:
    entity: your-entity
    project: your-project
    sweep_file: sweep.yaml
```

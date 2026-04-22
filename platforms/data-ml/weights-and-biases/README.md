# Weights & Biases — universal-spawn platform extension

W&B tracks experiments, runs hyperparameter sweeps, and stores artifacts. A universal-spawn manifest declares the entity / project, the optional sweep config, and the artifact registry.

## What this platform cares about

The entity, project, sweep config path, artifact registry, and whether runs are public.

## Compatibility table

| Manifest field | Weights & Biases behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `library`, `notebook`. |
| `platforms.weights-and-biases` | Strict. |

### `platforms.weights-and-biases` fields

| Field | Purpose |
|---|---|
| `platforms.weights-and-biases.entity` | W&B entity. |
| `platforms.weights-and-biases.project` | W&B project. |
| `platforms.weights-and-biases.sweep_file` | Sweep YAML. |
| `platforms.weights-and-biases.artifact_registry` | Artifact registry. |
| `platforms.weights-and-biases.visibility` | `public` or `private`. |

See [`compatibility.md`](./compatibility.md) for more.

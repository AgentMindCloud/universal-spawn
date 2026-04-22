# Replicate (data-ml) compatibility — field-by-field

| universal-spawn v1.0 field | Replicate (data-ml) behavior |
|---|---|
| `version` | Required. |
| `platforms.replicate.cog_file` | Path to cog.yaml. |
| `platforms.replicate.training` | Training config. |
| `platforms.replicate.notebook_url` | Companion notebook URL. |
| `platforms.replicate.dataset_slug` | Bundled dataset slug. |

## Coexistence with `cog.yaml (shared with the AI track)`

universal-spawn does NOT replace cog.yaml (shared with the AI track). Both files coexist; consumers read both and warn on conflicts.

### `cog.yaml (shared with the AI track)` (provider-native)

```yaml
build:
  python_version: "3.11"
  python_packages: [torch, accelerate]
predict: predict.py:Predictor
train: train.py:trainer
```

### `universal-spawn.yaml` (platforms.replicate block)

```yaml
platforms:
  replicate:
    cog_file: cog.yaml
    training: { command: "cog train", hardware: a40, max_run_time_minutes: 60 }
```

## Why two folders

`../../ai/replicate/` owns the inference (model + version + input_schema_ref) shape. This folder owns the training + notebook ergonomics on top of the same Cog format. Both are thin extensions that compose with the master schema; their fields do not overlap.

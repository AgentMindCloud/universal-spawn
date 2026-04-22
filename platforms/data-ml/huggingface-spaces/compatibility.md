# Hugging Face Spaces compatibility — field-by-field

| universal-spawn v1.0 field | Hugging Face Spaces behavior |
|---|---|
| `version` | Required. |
| `platforms.huggingface-spaces.sdk` | `gradio`, `streamlit`, `docker`, `static`. |
| `platforms.huggingface-spaces.hardware` | Hardware tier. |
| `platforms.huggingface-spaces.visibility` | `public` or `private`. |
| `platforms.huggingface-spaces.front_matter` | README front-matter fields. |

## Coexistence with `README.md front-matter (HF Spaces convention)`

universal-spawn does NOT replace README.md front-matter (HF Spaces convention). Both files coexist; consumers read both and warn on conflicts.

### `README.md front-matter (HF Spaces convention)` (provider-native)

```yaml
title: Your Demo
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
```

### `universal-spawn.yaml` (platforms.huggingface-spaces block)

```yaml
platforms:
  huggingface-spaces:
    sdk: gradio
    visibility: public
    hardware: zero-gpu
    front_matter:
      title: Your Demo
      license: apache-2.0
```

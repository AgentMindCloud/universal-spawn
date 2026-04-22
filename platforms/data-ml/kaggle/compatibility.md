# Kaggle compatibility — field-by-field

| universal-spawn v1.0 field | Kaggle behavior |
|---|---|
| `version` | Required. |
| `platforms.kaggle.kind` | `notebook` or `dataset`. |
| `platforms.kaggle.slug` | Kaggle slug (`username/title`). |
| `platforms.kaggle.language` | Notebook language. |
| `platforms.kaggle.kernel_type` | `notebook` or `script`. |
| `platforms.kaggle.enable_gpu` | GPU toggle. |
| `platforms.kaggle.enable_internet` | Internet toggle. |
| `platforms.kaggle.dataset_sources` | Input datasets. |
| `platforms.kaggle.competition` | Competition slug if entered. |

## Coexistence with `kernel-metadata.json`

universal-spawn does NOT replace kernel-metadata.json. Both files coexist; consumers read both and warn on conflicts.

### `kernel-metadata.json` (provider-native)

```json
{
  "id": "yourhandle/your-notebook",
  "title": "Your Notebook",
  "code_file": "notebook.ipynb",
  "language": "python",
  "kernel_type": "notebook",
  "enable_gpu": false,
  "enable_internet": false
}
```

### `universal-spawn.yaml` (platforms.kaggle block)

```yaml
platforms:
  kaggle:
    kind: notebook
    slug: yourhandle/your-notebook
    language: python
    kernel_type: notebook
```

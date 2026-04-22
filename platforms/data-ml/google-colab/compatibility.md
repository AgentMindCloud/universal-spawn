# Google Colab compatibility — field-by-field

| universal-spawn v1.0 field | Google Colab behavior |
|---|---|
| `version` | Required. |
| `platforms.google-colab.notebook_url` | Drive or GitHub notebook URL. |
| `platforms.google-colab.runtime` | `cpu`, `gpu`, `tpu`. |
| `platforms.google-colab.machine_type` | Machine type. |
| `platforms.google-colab.runtime_version` | Python runtime version. |
| `platforms.google-colab.requires_drive` | True if the notebook mounts Drive. |

## Coexistence with `.ipynb hosted on Drive or GitHub`

universal-spawn does NOT replace .ipynb hosted on Drive or GitHub. Both files coexist; consumers read both and warn on conflicts.

### `.ipynb hosted on Drive or GitHub` (provider-native)

```json
// Notebook .ipynb file; no separate config file by convention.
```

### `universal-spawn.yaml` (platforms.google-colab block)

```yaml
platforms:
  google-colab:
    notebook_url: "https://colab.research.google.com/github/yourhandle/your-repo/blob/main/notebook.ipynb"
    runtime: cpu
```

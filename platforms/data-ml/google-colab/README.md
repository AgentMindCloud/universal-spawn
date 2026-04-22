# Google Colab — universal-spawn platform extension

Colab runs Drive-hosted .ipynb notebooks with a Python runtime. A universal-spawn manifest pins the notebook URL, the runtime kind (CPU / GPU / TPU), and the recommended machine type.

## What this platform cares about

The notebook URL or GitHub path, the runtime kind, machine type, and required Drive scopes.

## Compatibility table

| Manifest field | Google Colab behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `workflow`. |
| `platforms.google-colab` | Strict. |

### `platforms.google-colab` fields

| Field | Purpose |
|---|---|
| `platforms.google-colab.notebook_url` | Notebook URL. |
| `platforms.google-colab.runtime` | `cpu`, `gpu`, `tpu`. |
| `platforms.google-colab.machine_type` | Machine type. |
| `platforms.google-colab.runtime_version` | Python runtime version. |
| `platforms.google-colab.requires_drive` | Mounts Drive. |

See [`compatibility.md`](./compatibility.md) for more.

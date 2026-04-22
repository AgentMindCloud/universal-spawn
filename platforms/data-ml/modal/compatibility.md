# Modal compatibility — field-by-field

| universal-spawn v1.0 field | Modal behavior |
|---|---|
| `version` | Required. |
| `platforms.modal.entry_file` | Modal app entry file. |
| `platforms.modal.app_name` | Modal App name. |
| `platforms.modal.gpu` | GPU class (if any). |
| `platforms.modal.image_kind` | `debian-slim`, `from-registry`, `dockerfile`. |
| `platforms.modal.volumes` | Persistent volume names. |
| `platforms.modal.secrets` | Modal Secret names. |

## Coexistence with `modal app.py + modal CLI`

universal-spawn does NOT replace modal app.py + modal CLI. Both files coexist; consumers read both and warn on conflicts.

### `modal app.py + modal CLI` (provider-native)

```python
import modal
app = modal.App("your-app")
@app.function()
def hello():
    return "ok"
```

### `universal-spawn.yaml` (platforms.modal block)

```yaml
platforms:
  modal:
    entry_file: app.py
    app_name: your-app
    gpu: none
```

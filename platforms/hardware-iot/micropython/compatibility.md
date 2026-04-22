# MicroPython compatibility — field-by-field

| universal-spawn v1.0 field | MicroPython behavior |
|---|---|
| `version` | Required. |
| `platforms.micropython.port` | MicroPython port. |
| `platforms.micropython.entry_script` | Entry script. |
| `platforms.micropython.frozen_modules` | Frozen modules. |
| `platforms.micropython.libraries` | mip-installable libraries. |

## Coexistence with `main.py + boot.py + (optional) manifest.py`

universal-spawn does NOT replace main.py + boot.py + (optional) manifest.py. Both files coexist; consumers read both and warn on conflicts.

### `main.py + boot.py + (optional) manifest.py` (provider-native)

```python
# main.py runs on every boot.
print("hello from MicroPython")
```

### `universal-spawn.yaml` (platforms.micropython block)

```yaml
platforms:
  micropython:
    port: rp2
    entry_script: src/main.py
```

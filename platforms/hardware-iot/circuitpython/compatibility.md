# CircuitPython compatibility — field-by-field

| universal-spawn v1.0 field | CircuitPython behavior |
|---|---|
| `version` | Required. |
| `platforms.circuitpython.board` | Board id. |
| `platforms.circuitpython.entry_script` | Entry script (`code.py`). |
| `platforms.circuitpython.bundle_libraries` | Adafruit Bundle libraries. |

## Coexistence with `code.py + lib/`

universal-spawn does NOT replace code.py + lib/. Both files coexist; consumers read both and warn on conflicts.

### `code.py + lib/` (provider-native)

```python
# code.py — runs on every boot
import board, time
print("hello from CircuitPython on", board.board_id)
```

### `universal-spawn.yaml` (platforms.circuitpython block)

```yaml
platforms:
  circuitpython:
    board: adafruit_qtpy_esp32s3_n4r2
    entry_script: code.py
    bundle_libraries: [adafruit_bus_device, adafruit_dht]
```

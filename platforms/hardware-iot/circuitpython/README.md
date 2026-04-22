# CircuitPython — universal-spawn platform extension

CircuitPython runs `code.py` from the device's USB drive. A universal-spawn manifest pins the board, the entry script, and any community-bundle libraries needed.

## What this platform cares about

The board id, entry script, and required Adafruit Bundle libraries.

## Compatibility table

| Manifest field | CircuitPython behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `library`, `cli-tool`. |
| `platforms.circuitpython` | Strict. |

### `platforms.circuitpython` fields

| Field | Purpose |
|---|---|
| `platforms.circuitpython.board` | Board id. |
| `platforms.circuitpython.entry_script` | Entry script. |
| `platforms.circuitpython.bundle_libraries` | Adafruit Bundle libraries. |

See [`compatibility.md`](./compatibility.md) for more.

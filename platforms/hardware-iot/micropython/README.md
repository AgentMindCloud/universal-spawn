# MicroPython — universal-spawn platform extension

MicroPython runs `main.py` on first boot. A universal-spawn manifest pins the target port, the entry script, and the frozen module list.

## What this platform cares about

Target MicroPython port, entry script, frozen modules, and required libraries.

## Compatibility table

| Manifest field | MicroPython behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `library`, `cli-tool`. |
| `platforms.micropython` | Strict. |

### `platforms.micropython` fields

| Field | Purpose |
|---|---|
| `platforms.micropython.port` | MicroPython port. |
| `platforms.micropython.entry_script` | Entry script. |
| `platforms.micropython.frozen_modules` | Frozen modules. |
| `platforms.micropython.libraries` | mip-installable libraries. |

See [`compatibility.md`](./compatibility.md) for more.

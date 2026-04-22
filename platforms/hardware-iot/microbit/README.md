# micro:bit — universal-spawn platform extension

BBC micro:bit ships projects via the MakeCode JSON format or as MicroPython scripts. A universal-spawn manifest pins the board variant (V1 / V2) and the toolchain.

## What this platform cares about

The board variant, toolchain (`makecode`, `micropython`), and the entry file.

## Compatibility table

| Manifest field | micro:bit behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `cli-tool`, `library`. |
| `platforms.microbit` | Strict. |

### `platforms.microbit` fields

| Field | Purpose |
|---|---|
| `platforms.microbit.variant` | Board variant. |
| `platforms.microbit.toolchain` | MakeCode or MicroPython. |
| `platforms.microbit.entry_file` | Entry file. |
| `platforms.microbit.makecode_share_url` | MakeCode share URL. |

See [`compatibility.md`](./compatibility.md) for more.

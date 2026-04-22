# Arduino — universal-spawn platform extension

Arduino creations are sketches (`.ino`) or libraries (`library.properties`). A universal-spawn manifest pins the `kind`, the target boards, and (for `flash-via-companion`) the prebuilt binary URL that a companion app like Arduino Lab can flash directly via WebUSB.

## What this platform cares about

The `kind` (`sketch`, `library`, `flash-via-companion`), the FQBN board id, the required libraries, and the prebuilt binary URL when applicable.

## Compatibility table

| Manifest field | Arduino behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `library`, `hardware-device`, `cli-tool`. |
| `platforms.arduino` | Strict. |

### `platforms.arduino` fields

| Field | Purpose |
|---|---|
| `platforms.arduino.kind` | `sketch`, `library`, `flash-via-companion`. |
| `platforms.arduino.fqbn` | Fully-Qualified Board Name. |
| `platforms.arduino.entry_ino` | Sketch entry .ino. |
| `platforms.arduino.libraries` | Required Arduino libraries. |
| `platforms.arduino.prebuilt_binary_url` | Prebuilt binary URL. |

See [`compatibility.md`](./compatibility.md) for more.

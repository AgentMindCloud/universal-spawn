# Raspberry Pi — universal-spawn platform extension

Raspberry Pi creations are SD-card images, dt-overlays, or first-boot scripts. A universal-spawn manifest pins the Pi model, OS image, and the install method.

## What this platform cares about

The Pi model, OS image, the install method (`image-flash`, `overlay`, `script`), and the entry file.

## Compatibility table

| Manifest field | Raspberry Pi behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `hardware-device`, `cli-tool`. |
| `platforms.raspberry-pi` | Strict. |

### `platforms.raspberry-pi` fields

| Field | Purpose |
|---|---|
| `platforms.raspberry-pi.model` | Pi model. |
| `platforms.raspberry-pi.os` | OS image. |
| `platforms.raspberry-pi.install_method` | Install method. |
| `platforms.raspberry-pi.image_url` | Image URL. |
| `platforms.raspberry-pi.entry_file` | Entry file. |

See [`compatibility.md`](./compatibility.md) for more.

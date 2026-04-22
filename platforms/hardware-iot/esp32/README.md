# ESP32 — universal-spawn platform extension

ESP32 firmware ships with a partition table and (often) an OTA channel. A universal-spawn manifest pins the chip variant, the partition CSV, and (for `flash-via-companion`) the prebuilt binary URL that esptool-js can flash via WebSerial.

## What this platform cares about

The chip variant, partition CSV, framework (`arduino`, `esp-idf`, `nuttx`), the OTA channel, and the prebuilt binary URL when applicable.

## Compatibility table

| Manifest field | ESP32 behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `hardware-device`. |
| `platforms.esp32` | Strict. |

### `platforms.esp32` fields

| Field | Purpose |
|---|---|
| `platforms.esp32.kind` | `firmware` or `flash-via-companion`. |
| `platforms.esp32.chip` | Chip variant (`esp32`, `esp32-c3`, `esp32-s3`, `esp32-c6`, `esp32-h2`). |
| `platforms.esp32.framework` | `arduino`, `esp-idf`, `nuttx`. |
| `platforms.esp32.partitions_csv` | Partition CSV. |
| `platforms.esp32.ota_channel` | OTA channel. |
| `platforms.esp32.prebuilt_binary_url` | Prebuilt binary URL. |

See [`compatibility.md`](./compatibility.md) for more.

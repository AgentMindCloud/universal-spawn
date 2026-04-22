# ESP32 compatibility — field-by-field

| universal-spawn v1.0 field | ESP32 behavior |
|---|---|
| `version` | Required. |
| `platforms.esp32.kind` | `firmware` or `flash-via-companion`. |
| `platforms.esp32.chip` | Chip variant. |
| `platforms.esp32.framework` | Build framework. |
| `platforms.esp32.partitions_csv` | Partition CSV path. |
| `platforms.esp32.ota_channel` | OTA channel name. |
| `platforms.esp32.prebuilt_binary_url` | Prebuilt .bin URL. |

## Coexistence with `platformio.ini + partitions.csv + sdkconfig`

universal-spawn does NOT replace platformio.ini + partitions.csv + sdkconfig. Both files coexist; consumers read both and warn on conflicts.

### `platformio.ini + partitions.csv + sdkconfig` (provider-native)

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = espidf
board_build.partitions = partitions.csv
```

### `universal-spawn.yaml` (platforms.esp32 block)

```yaml
platforms:
  esp32:
    kind: firmware
    chip: esp32-s3
    framework: esp-idf
    partitions_csv: partitions.csv
    ota_channel: stable
```

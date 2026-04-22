# PlatformIO compatibility — field-by-field

| universal-spawn v1.0 field | PlatformIO behavior |
|---|---|
| `version` | Required. |
| `platforms.platform-io.entry_env` | platformio.ini env name. |
| `platforms.platform-io.board` | Board id. |
| `platforms.platform-io.framework` | Framework. |
| `platforms.platform-io.libraries` | Library deps. |

## Coexistence with `platformio.ini`

universal-spawn does NOT replace platformio.ini. Both files coexist; consumers read both and warn on conflicts.

### `platformio.ini` (provider-native)

```ini
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
```

### `universal-spawn.yaml` (platforms.platform-io block)

```yaml
platforms:
  platform-io:
    entry_env: esp32-s3-devkitc-1
    board: esp32-s3-devkitc-1
    framework: arduino
```

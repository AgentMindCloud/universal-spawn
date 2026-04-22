# Arduino compatibility — field-by-field

| universal-spawn v1.0 field | Arduino behavior |
|---|---|
| `version` | Required. |
| `platforms.arduino.kind` | `sketch`, `library`, `flash-via-companion`. |
| `platforms.arduino.fqbn` | Fully-Qualified Board Name. |
| `platforms.arduino.entry_ino` | Sketch entry .ino (sketch). |
| `platforms.arduino.libraries` | Required Arduino libraries. |
| `platforms.arduino.prebuilt_binary_url` | Prebuilt .bin / .hex URL (flash-via-companion). |

## Coexistence with `library.properties + .ino`

universal-spawn does NOT replace library.properties + .ino. Both files coexist; consumers read both and warn on conflicts.

### `library.properties + .ino` (provider-native)

```properties
name=YourLibrary
version=0.1.0
author=yourhandle
sentence=Short description.
paragraph=Longer description.
architectures=avr,esp32,esp8266
```

### `universal-spawn.yaml` (platforms.arduino block)

```yaml
platforms:
  arduino:
    kind: sketch
    fqbn: "arduino:avr:uno"
    entry_ino: src/main.ino
```

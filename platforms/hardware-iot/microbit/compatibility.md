# micro:bit compatibility — field-by-field

| universal-spawn v1.0 field | micro:bit behavior |
|---|---|
| `version` | Required. |
| `platforms.microbit.variant` | `v1` or `v2`. |
| `platforms.microbit.toolchain` | `makecode` or `micropython`. |
| `platforms.microbit.entry_file` | Entry .json (MakeCode) or .py (MicroPython). |
| `platforms.microbit.makecode_share_url` | MakeCode share URL. |

## Coexistence with `MakeCode JSON / .py file`

universal-spawn does NOT replace MakeCode JSON / .py file. Both files coexist; consumers read both and warn on conflicts.

### `MakeCode JSON / .py file` (provider-native)

```json
{ "name": "Your Project", "main": "main.ts", "files": ["main.ts"] }
```

### `universal-spawn.yaml` (platforms.microbit block)

```yaml
platforms:
  microbit:
    variant: v2
    toolchain: makecode
    entry_file: src/project.json
```

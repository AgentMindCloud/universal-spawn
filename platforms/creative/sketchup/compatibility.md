# SketchUp compatibility — field-by-field

| universal-spawn v1.0 field | SketchUp behavior |
|---|---|
| `version` | Required. |
| `platforms.sketchup.kind` | `rbz-extension`, `component`. |
| `platforms.sketchup.min_year` | Minimum SketchUp year version. |
| `platforms.sketchup.entry_file` | Entry file path. |
| `platforms.sketchup.extension_warehouse` | Warehouse publication settings. |

## Coexistence with `*.rbz (zip of ruby extension)`

universal-spawn does NOT replace *.rbz (zip of ruby extension). Both files coexist; consumers read both and warn on conflicts.

### `*.rbz (zip of ruby extension)` (provider-native)

```text
# SketchUp extensions are zipped ruby trees renamed to .rbz.
```

### `universal-spawn.yaml` (platforms.sketchup block)

```yaml
platforms:
  sketchup:
    kind: rbz-extension
    min_year: 2024
    entry_file: dist/parchment-studio.rbz
```

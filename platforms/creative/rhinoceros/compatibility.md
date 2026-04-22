# Rhinoceros 3D compatibility — field-by-field

| universal-spawn v1.0 field | Rhinoceros 3D behavior |
|---|---|
| `version` | Required. |
| `platforms.rhinoceros.kind` | `rhp-plugin`, `grasshopper`, `yak-package`. |
| `platforms.rhinoceros.min_version` | Minimum Rhino version. |
| `platforms.rhinoceros.entry_file` | Entry file path. |
| `platforms.rhinoceros.yak` | Yak manifest settings (for `yak-package`). |

## Coexistence with `Yak package manifest (.yml)`

universal-spawn does NOT replace Yak package manifest (.yml). Both files coexist; consumers read both and warn on conflicts.

### `Yak package manifest (.yml)` (provider-native)

```yaml
name: your-plugin
version: 0.1.0
authors: [yourhandle]
description: Your description
```

### `universal-spawn.yaml` (platforms.rhinoceros block)

```yaml
platforms:
  rhinoceros:
    kind: yak-package
    min_version: "8"
    yak:
      yak_file: yak.yml
      category: Grasshopper
```

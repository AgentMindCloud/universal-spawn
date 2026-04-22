# Cinema 4D compatibility — field-by-field

| universal-spawn v1.0 field | Cinema 4D behavior |
|---|---|
| `version` | Required. |
| `platforms.cinema4d.kind` | `plugin`, `scene`, `asset-library`. |
| `platforms.cinema4d.min_version` | Minimum C4D version. |
| `platforms.cinema4d.entry_file` | Entry file (plugin `.pyp` or scene `.c4d` or `.lib4d`). |

## Coexistence with `plugin .pyp file + optional res/description/`

universal-spawn does NOT replace plugin .pyp file + optional res/description/. Both files coexist; consumers read both and warn on conflicts.

### `plugin .pyp file + optional res/description/` (provider-native)

```python
# Python plugin metadata lives at the top of the .pyp file.
PLUGIN_ID = 1000000
```

### `universal-spawn.yaml` (platforms.cinema4d block)

```yaml
platforms:
  cinema4d:
    kind: plugin
    min_version: "2025"
    entry_file: src/plugin.pyp
```

# Blender compatibility — field-by-field

| universal-spawn v1.0 field | Blender behavior |
|---|---|
| `version` | Required. |
| `platforms.blender.kind` | `addon`, `project`, `asset-library`. |
| `platforms.blender.blender_version` | Minimum Blender version. |
| `platforms.blender.entry_module` | `__init__.py` path for add-ons. |
| `platforms.blender.entry_blend` | `.blend` file for projects. |
| `platforms.blender.asset_library_path` | Directory for asset libraries. |
| `platforms.blender.render_engine` | Preferred render engine. |

## Coexistence with `addon __init__.py bl_info`

universal-spawn does NOT replace addon __init__.py bl_info. Both files coexist; consumers read both and warn on conflicts.

### `addon __init__.py bl_info` (provider-native)

```python
bl_info = {
    "name": "Your Addon",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "category": "Object",
}
```

### `universal-spawn.yaml` (platforms.blender block)

```yaml
platforms:
  blender:
    kind: addon
    blender_version: "4.2"
    entry_module: addons/your_addon/__init__.py
```

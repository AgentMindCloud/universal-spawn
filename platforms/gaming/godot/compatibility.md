# Godot compatibility — field-by-field

| universal-spawn v1.0 field | Godot behavior |
|---|---|
| `version` | Required. |
| `platforms.godot.kind` | `addon` or `project`. |
| `platforms.godot.engine_series` | Engine series (3 or 4). |
| `platforms.godot.renderer` | Renderer. |
| `platforms.godot.entry_scene` | Entry scene path. |

## Coexistence with `project.godot + addons/<id>/plugin.cfg`

universal-spawn does NOT replace `project.godot` + `addons/<id>/plugin.cfg`. Both files coexist; consumers read both and warn on conflicts.

### `project.godot + addons/<id>/plugin.cfg` (provider-native)

```ini
[application]
config/name="Your Project"
run/main_scene="res://scenes/main.tscn"

[rendering]
renderer/rendering_method="forward_plus"
```

### `universal-spawn.yaml` (platforms.godot block)

```yaml
platforms:
  godot:
    kind: project
    engine_series: "4"
    renderer: forward+
    entry_scene: scenes/main.tscn
```

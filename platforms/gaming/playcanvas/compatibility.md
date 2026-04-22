# PlayCanvas compatibility — field-by-field

| universal-spawn v1.0 field | PlayCanvas behavior |
|---|---|
| `version` | Required. |
| `platforms.playcanvas.project_id` | PlayCanvas project id. |
| `platforms.playcanvas.scene_id` | Default scene id. |
| `platforms.playcanvas.engine_version` | PlayCanvas engine version. |
| `platforms.playcanvas.editor_url` | Editor URL. |

## Coexistence with `PlayCanvas cloud project (no repo file by convention)`

universal-spawn does NOT replace PlayCanvas cloud project (no repo file by convention). Both files coexist; consumers read both and warn on conflicts.

### `PlayCanvas cloud project (no repo file by convention)` (provider-native)

```text
# Cloud-native; project state lives on PlayCanvas servers.
```

### `universal-spawn.yaml` (platforms.playcanvas block)

```yaml
platforms:
  playcanvas:
    project_id: "1234567"
    scene_id: "987654"
```

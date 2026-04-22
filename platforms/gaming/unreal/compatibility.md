# Unreal Engine compatibility — field-by-field

| universal-spawn v1.0 field | Unreal Engine behavior |
|---|---|
| `version` | Required. |
| `platforms.unreal.kind` | `marketplace-plugin` or `project-template`. |
| `platforms.unreal.engine_version` | Engine version. |
| `platforms.unreal.target_platforms` | Target build platforms. |
| `platforms.unreal.marketplace_category` | Marketplace category. |
| `platforms.unreal.entry_uproject` | Entry .uproject file (project-template). |

## Coexistence with `.uplugin / .uproject`

universal-spawn does NOT replace .uplugin / .uproject. Both files coexist; consumers read both and warn on conflicts.

### `.uplugin / .uproject` (provider-native)

```json
{
  "FileVersion": 3,
  "Version": 1,
  "VersionName": "1.0",
  "FriendlyName": "Your Plugin",
  "Description": "Your plugin description",
  "Category": "Other",
  "EngineVersion": "5.4.0"
}
```

### `universal-spawn.yaml` (platforms.unreal block)

```yaml
platforms:
  unreal:
    kind: marketplace-plugin
    engine_version: "5.4"
    target_platforms: [windows, macos]
```

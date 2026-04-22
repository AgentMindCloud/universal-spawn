# Roblox compatibility — field-by-field

| universal-spawn v1.0 field | Roblox behavior |
|---|---|
| `version` | Required. |
| `platforms.roblox.kind` | `experience` or `creator-asset`. |
| `platforms.roblox.universe_id` | Universe id. |
| `platforms.roblox.place_id` | Place id. |
| `platforms.roblox.rojo_project` | Rojo `default.project.json` path. |
| `platforms.roblox.asset_kind` | Asset kind (creator-asset). |
| `platforms.roblox.creator_hub_id` | Creator Hub asset id. |

## Coexistence with `default.project.json (Rojo)`

universal-spawn does NOT replace default.project.json (Rojo). Both files coexist; consumers read both and warn on conflicts.

### `default.project.json (Rojo)` (provider-native)

```json
{
  "name": "Your Game",
  "tree": {
    "$className": "DataModel",
    "ServerScriptService": { "$path": "src/server" }
  }
}
```

### `universal-spawn.yaml` (platforms.roblox block)

```yaml
platforms:
  roblox:
    kind: experience
    universe_id: "1234567890"
    place_id: "9876543210"
    rojo_project: default.project.json
```

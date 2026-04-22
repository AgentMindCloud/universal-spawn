# Steam compatibility — field-by-field

| universal-spawn v1.0 field | Steam behavior |
|---|---|
| `version` | Required. |
| `platforms.steam.kind` | `workshop-item` or `direct-title`. |
| `platforms.steam.host_appid` | Host appid for Workshop items. |
| `platforms.steam.workshop_id` | Workshop file id. |
| `platforms.steam.appid` | Steamworks appid for Direct titles. |
| `platforms.steam.depots` | Depot configuration. |
| `platforms.steam.steampipe_vdf` | Steampipe build VDF path. |

## Coexistence with `steampipe build VDF + Workshop API`

universal-spawn does NOT replace steampipe build VDF + Workshop API. Both files coexist; consumers read both and warn on conflicts.

### `steampipe build VDF + Workshop API` (provider-native)

```vdf
"appbuild"
{
  "appid" "1234567"
  "desc" "Your build"
  "depots"
  {
    "1234568" "depot_build_windows.vdf"
  }
}
```

### `universal-spawn.yaml` (platforms.steam block)

```yaml
platforms:
  steam:
    kind: direct-title
    appid: "1234567"
    depots:
      - { depot_id: "1234568", platform: windows }
    steampipe_vdf: build/app_build.vdf
```

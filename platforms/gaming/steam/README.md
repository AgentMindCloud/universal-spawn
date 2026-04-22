# Steam — universal-spawn platform extension

Steam ships two distribution paths: Steam Workshop items (uploaded via the Workshop API into a host game) and Steamworks Direct titles (Steam-published games). A universal-spawn manifest picks one with `kind`.

## What this platform cares about

The `kind` (`workshop-item`, `direct-title`), the host appid for Workshop items, and the depot configuration for Direct titles.

## Compatibility table

| Manifest field | Steam behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `game-mod`, `creative-tool`. |
| `platforms.steam` | Strict. |

### `platforms.steam` fields

| Field | Purpose |
|---|---|
| `platforms.steam.kind` | `workshop-item` or `direct-title`. |
| `platforms.steam.host_appid` | Host appid (Workshop). |
| `platforms.steam.workshop_id` | Workshop file id. |
| `platforms.steam.appid` | Steamworks appid (Direct). |
| `platforms.steam.depots` | Depot configuration. |
| `platforms.steam.steampipe_vdf` | Steampipe build VDF. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

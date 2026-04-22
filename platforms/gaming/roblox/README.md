# Roblox — universal-spawn platform extension

Roblox publishes experiences (places) plus Creator Hub assets (models, plugins, audio). A universal-spawn manifest picks one with `kind` and pins the universe + place ids.

## What this platform cares about

The `kind` (`experience`, `creator-asset`), the universe / place ids, and the Rojo `default.project.json` path.

## Compatibility table

| Manifest field | Roblox behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `creative-tool`, `extension`. |
| `platforms.roblox` | Strict. |

### `platforms.roblox` fields

| Field | Purpose |
|---|---|
| `platforms.roblox.kind` | `experience` or `creator-asset`. |
| `platforms.roblox.universe_id` | Universe id. |
| `platforms.roblox.place_id` | Place id. |
| `platforms.roblox.rojo_project` | Rojo project file. |
| `platforms.roblox.asset_kind` | Asset kind. |
| `platforms.roblox.creator_hub_id` | Creator Hub asset id. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

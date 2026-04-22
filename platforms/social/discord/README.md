# Discord — universal-spawn platform extension

Discord is the v1.0 successor to the v1.0.0 legacy `platforms/discord/` extension. It covers Application + Bot + slash commands + Activities (embedded apps), with strict OAuth2 scope and Gateway intent declarations. Includes a canonical one-click 'Add to server' URL recipe.

## What this platform cares about

OAuth2 scopes, Gateway intents, slash commands, message commands, Activity config, and the application id used to build the canonical install URL.

## Compatibility table

| Manifest field | Discord behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `extension`, `creative-tool`. |
| `platforms.discord` | Strict. |

### `platforms.discord` fields

| Field | Purpose |
|---|---|
| `platforms.discord.application_id` | Application id. |
| `platforms.discord.scopes` | OAuth2 scopes. |
| `platforms.discord.intents` | Gateway intents. |
| `platforms.discord.permissions` | Permissions integer. |
| `platforms.discord.slash_commands` | Slash command JSON files. |
| `platforms.discord.message_commands` | Message command JSON files. |
| `platforms.discord.activity` | Activity config. |

See [`compatibility.md`](./compatibility.md) for more.

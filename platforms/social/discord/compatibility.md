# Discord compatibility — field-by-field

| universal-spawn v1.0 field | Discord behavior |
|---|---|
| `version` | Required. |
| `platforms.discord.application_id` | Application id (snowflake). |
| `platforms.discord.scopes` | OAuth2 scopes. |
| `platforms.discord.intents` | Gateway intents. |
| `platforms.discord.permissions` | Bot install permissions integer. |
| `platforms.discord.slash_commands` | Slash command JSON files. |
| `platforms.discord.message_commands` | Message command JSON files. |
| `platforms.discord.activity` | Activity / embedded app config. |

## Coexistence with `Discord Application + bot.json`

universal-spawn does NOT replace Discord Application + bot.json. Both files coexist; consumers read both and warn on conflicts.

### `Discord Application + bot.json` (provider-native)

```json
{
  "id": "111111111111111111",
  "name": "Your Bot",
  "scopes": ["bot", "applications.commands"],
  "intents": ["guilds"]
}
```

### `universal-spawn.yaml` (platforms.discord block)

```yaml
platforms:
  discord:
    application_id: "111111111111111111"
    scopes: [bot, applications.commands]
    intents: [guilds]
    slash_commands: [commands/ping.json]
```

## One-click 'Add to server' URL

The canonical install URL is:

```
https://discord.com/oauth2/authorize?
  client_id={application_id}&
  scope={scopes joined with `+`}&
  permissions={permissions integer}
```

Generators MAY render a 'Add to your server' button on any registry card from those four fields alone.

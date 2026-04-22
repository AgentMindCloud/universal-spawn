# Slack compatibility — field-by-field

| universal-spawn v1.0 field | Slack behavior |
|---|---|
| `version` | Required. |
| `platforms.slack.manifest_file` | Slack `manifest.json` file path. |
| `platforms.slack.bot_scopes` | Bot OAuth scopes. |
| `platforms.slack.user_scopes` | User OAuth scopes (optional). |
| `platforms.slack.slash_commands` | Slash commands. |
| `platforms.slack.event_subscriptions` | Subscribed events. |
| `platforms.slack.socket_mode` | True for Socket Mode. |

## Coexistence with `slack manifest.json`

universal-spawn does NOT replace slack manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `slack manifest.json` (provider-native)

```json
{
  "display_information": { "name": "Your App" },
  "features": {
    "bot_user": { "display_name": "Your App", "always_online": true },
    "slash_commands": [{ "command": "/ping", "url": "https://api.example/slack" }]
  },
  "oauth_config": { "scopes": { "bot": ["chat:write", "commands"] } }
}
```

### `universal-spawn.yaml` (platforms.slack block)

```yaml
platforms:
  slack:
    manifest_file: slack.manifest.json
    bot_scopes: [chat:write, commands]
    slash_commands:
      - { command: "/ping", description: "Ping the bot." }
```

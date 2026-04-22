# Telegram compatibility — field-by-field

| universal-spawn v1.0 field | Telegram behavior |
|---|---|
| `version` | Required. |
| `platforms.telegram.bot_username` | Bot @-handle. |
| `platforms.telegram.transport` | `long-poll` or `webhook`. |
| `platforms.telegram.webhook_url` | Webhook URL when transport is webhook. |
| `platforms.telegram.commands` | Registered commands. |
| `platforms.telegram.web_app_url` | Telegram Web App entry URL. |

## Coexistence with `BotFather + setMyCommands`

universal-spawn does NOT replace BotFather + setMyCommands. Both files coexist; consumers read both and warn on conflicts.

### `BotFather + setMyCommands` (provider-native)

```text
# Configure via @BotFather; commands registered with the setMyCommands API.
```

### `universal-spawn.yaml` (platforms.telegram block)

```yaml
platforms:
  telegram:
    bot_username: yourname_bot
    transport: long-poll
    commands:
      - { command: start, description: "Start the bot." }
```

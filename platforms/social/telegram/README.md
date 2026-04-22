# Telegram — universal-spawn platform extension

Telegram exposes the Bot API (long-poll or webhook) and Telegram Web Apps. A universal-spawn manifest captures the bot username, the registered commands, and (optionally) the Web App entry URL.

## What this platform cares about

The bot username, transport (`long-poll` or `webhook`), registered commands (for `setMyCommands`), and Web App URL.

## Compatibility table

| Manifest field | Telegram behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `web-app`. |
| `platforms.telegram` | Strict. |

### `platforms.telegram` fields

| Field | Purpose |
|---|---|
| `platforms.telegram.bot_username` | Bot @-handle. |
| `platforms.telegram.transport` | `long-poll` or `webhook`. |
| `platforms.telegram.webhook_url` | Webhook URL. |
| `platforms.telegram.commands` | Registered commands. |
| `platforms.telegram.web_app_url` | Telegram Web App entry URL. |

See [`compatibility.md`](./compatibility.md) for more.

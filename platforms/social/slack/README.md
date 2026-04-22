# Slack — universal-spawn platform extension

Slack apps ship via a `manifest.json` that declares OAuth scopes, slash commands, event subscriptions, and interactive shortcuts. A universal-spawn manifest captures those fields plus the canonical 'Add to Slack' URL inputs.

## What this platform cares about

Bot + user OAuth scopes, slash commands, event subscriptions, and the Slack manifest.json file.

## Compatibility table

| Manifest field | Slack behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `extension`, `web-app`. |
| `platforms.slack` | Strict. |

### `platforms.slack` fields

| Field | Purpose |
|---|---|
| `platforms.slack.manifest_file` | Slack manifest.json. |
| `platforms.slack.bot_scopes` | Bot OAuth scopes. |
| `platforms.slack.user_scopes` | User OAuth scopes. |
| `platforms.slack.slash_commands` | Slash commands. |
| `platforms.slack.event_subscriptions` | Subscribed events. |
| `platforms.slack.socket_mode` | Socket Mode flag. |

See [`compatibility.md`](./compatibility.md) for more.

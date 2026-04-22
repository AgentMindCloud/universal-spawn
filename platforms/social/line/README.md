# LINE — universal-spawn platform extension

LINE bots use the Messaging API; LINE Mini Apps use LIFF (LINE Front-end Framework). A universal-spawn manifest captures the channel id, rich-menu configuration, and LIFF endpoint.

## What this platform cares about

The channel id, channel kind (`messaging-api`, `liff`), the rich-menu image, and the LIFF endpoint URL.

## Compatibility table

| Manifest field | LINE behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `web-app`. |
| `platforms.line` | Strict. |

### `platforms.line` fields

| Field | Purpose |
|---|---|
| `platforms.line.channel_id` | LINE channel id. |
| `platforms.line.channel_kind` | `messaging-api` or `liff`. |
| `platforms.line.webhook_url` | Messaging API webhook URL. |
| `platforms.line.rich_menu_image` | Rich-menu image path. |
| `platforms.line.liff_endpoint_url` | LIFF endpoint URL. |
| `platforms.line.scopes` | LIFF scopes. |

See [`compatibility.md`](./compatibility.md) for more.

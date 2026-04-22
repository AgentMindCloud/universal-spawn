# LINE compatibility — field-by-field

| universal-spawn v1.0 field | LINE behavior |
|---|---|
| `version` | Required. |
| `platforms.line.channel_id` | LINE channel id. |
| `platforms.line.channel_kind` | `messaging-api` or `liff`. |
| `platforms.line.webhook_url` | Messaging-API webhook URL. |
| `platforms.line.rich_menu_image` | Rich menu image path. |
| `platforms.line.liff_endpoint_url` | LIFF endpoint URL. |
| `platforms.line.scopes` | LIFF scopes. |

## Coexistence with `LINE Developers Console + (optional) liff.config.json`

universal-spawn does NOT replace LINE Developers Console + (optional) liff.config.json. Both files coexist; consumers read both and warn on conflicts.

### `LINE Developers Console + (optional) liff.config.json` (provider-native)

```text
# Configured in the LINE Developers Console; secrets via the channel.
```

### `universal-spawn.yaml` (platforms.line block)

```yaml
platforms:
  line:
    channel_id: "1111111111"
    channel_kind: messaging-api
    webhook_url: "https://api.yourapp.example/line/webhook"
```

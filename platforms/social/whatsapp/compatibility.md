# WhatsApp compatibility — field-by-field

| universal-spawn v1.0 field | WhatsApp behavior |
|---|---|
| `version` | Required. |
| `platforms.whatsapp.phone_number_id` | Phone number id. |
| `platforms.whatsapp.business_account_id` | WABA id. |
| `platforms.whatsapp.webhook_url` | Webhook receiver URL. |
| `platforms.whatsapp.templates` | Registered message templates. |
| `platforms.whatsapp.api_kind` | `cloud` or `on-premise`. |

## Coexistence with `Meta WhatsApp Business Platform settings`

universal-spawn does NOT replace Meta WhatsApp Business Platform settings. Both files coexist; consumers read both and warn on conflicts.

### `Meta WhatsApp Business Platform settings` (provider-native)

```text
# Configured in the Meta Business Suite + Cloud API console.
```

### `universal-spawn.yaml` (platforms.whatsapp block)

```yaml
platforms:
  whatsapp:
    phone_number_id: "111111111111111"
    api_kind: cloud
    templates:
      - { name: hello_world, language: en_US }
```

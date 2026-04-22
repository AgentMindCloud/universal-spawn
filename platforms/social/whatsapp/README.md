# WhatsApp — universal-spawn platform extension

WhatsApp bots use the WhatsApp Business API (Cloud or On-Premise). A universal-spawn manifest declares the phone number id, the message templates, and the webhook receiver.

## What this platform cares about

The phone number id, registered message templates, the webhook receiver URL, and the messaging tier.

## Compatibility table

| Manifest field | WhatsApp behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `api-service`, `workflow`. |
| `platforms.whatsapp` | Strict. |

### `platforms.whatsapp` fields

| Field | Purpose |
|---|---|
| `platforms.whatsapp.phone_number_id` | Phone number id. |
| `platforms.whatsapp.business_account_id` | WhatsApp Business Account id. |
| `platforms.whatsapp.webhook_url` | Webhook receiver URL. |
| `platforms.whatsapp.templates` | Registered message templates. |
| `platforms.whatsapp.api_kind` | `cloud` or `on-premise`. |

See [`compatibility.md`](./compatibility.md) for more.

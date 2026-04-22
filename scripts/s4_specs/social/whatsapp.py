"""WhatsApp — Business API + message templates."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "whatsapp",
    "title": "WhatsApp",
    "lede": (
        "WhatsApp bots use the WhatsApp Business API (Cloud or "
        "On-Premise). A universal-spawn manifest declares the phone "
        "number id, the message templates, and the webhook receiver."
    ),
    "cares": (
        "The phone number id, registered message templates, the "
        "webhook receiver URL, and the messaging tier."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `api-service`, `workflow`."),
        ("platforms.whatsapp", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.whatsapp.phone_number_id", "Phone number id."),
        ("platforms.whatsapp.business_account_id", "WABA id."),
        ("platforms.whatsapp.webhook_url", "Webhook receiver URL."),
        ("platforms.whatsapp.templates", "Registered message templates."),
        ("platforms.whatsapp.api_kind", "`cloud` or `on-premise`."),
    ],
    "platform_fields": {
        "phone_number_id": "Phone number id.",
        "business_account_id": "WhatsApp Business Account id.",
        "webhook_url": "Webhook receiver URL.",
        "templates": "Registered message templates.",
        "api_kind": "`cloud` or `on-premise`.",
    },
    "schema_body": schema_object(
        required=["phone_number_id", "api_kind"],
        properties={
            "phone_number_id": str_prop(pattern=r"^[0-9]{8,20}$"),
            "business_account_id": str_prop(pattern=r"^[0-9]{8,20}$"),
            "webhook_url": {"type": "string", "format": "uri"},
            "templates": {
                "type": "array",
                "items": schema_object(
                    required=["name", "language"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_]{0,63}$"),
                        "language": str_prop(pattern=r"^[a-z]{2}(_[A-Z]{2})?$"),
                    },
                ),
            },
            "api_kind": enum(["cloud", "on-premise"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: WhatsApp Template
type: bot
description: Template for a WhatsApp-targeted universal-spawn manifest.

platforms:
  whatsapp:
    phone_number_id: "111111111111111"
    business_account_id: "222222222222222"
    webhook_url: "https://api.yourapp.example/whatsapp/webhook"
    api_kind: cloud
    templates:
      - { name: hello_world, language: en_US }

safety:
  min_permissions: [network:inbound, network:outbound:graph.facebook.com]

env_vars_required:
  - name: WHATSAPP_ACCESS_TOKEN
    description: Cloud API access token.
    secret: true
  - name: WHATSAPP_VERIFY_TOKEN
    description: Webhook verify token.
    secret: true

deployment:
  targets: [whatsapp]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/whatsapp-template }
""",
    "native_config_name": "Meta WhatsApp Business Platform settings",
    "native_config_lang": "text",
    "native_config": "# Configured in the Meta Business Suite + Cloud API console.\n",
    "universal_excerpt": """
platforms:
  whatsapp:
    phone_number_id: "111111111111111"
    api_kind: cloud
    templates:
      - { name: hello_world, language: en_US }
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate WhatsApp Bot
type: bot
summary: Minimal WhatsApp Cloud API bot answering plate queries.
description: Cloud API. Webhook receiver. One template registered.

platforms:
  whatsapp:
    phone_number_id: "123456789012345"
    business_account_id: "987654321098765"
    webhook_url: "https://api.plate.example/whatsapp/webhook"
    api_kind: cloud
    templates:
      - { name: plate_of_day, language: en_US }

safety:
  min_permissions: [network:inbound, network:outbound:graph.facebook.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: WHATSAPP_ACCESS_TOKEN
    description: Cloud API token.
    secret: true
  - name: WHATSAPP_VERIFY_TOKEN
    description: Webhook verify token.
    secret: true

deployment:
  targets: [whatsapp]

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/whatsapp-plate-bot }
  id: com.plate-studio.whatsapp-plate-bot
""",
        "example-2": """
version: "1.0"
name: Acme Support WhatsApp
type: bot
summary: Full WhatsApp Business bot with five templates and on-premise transport.
description: On-premise WhatsApp Business with five message templates and an internal webhook receiver.

platforms:
  whatsapp:
    phone_number_id: "555555555555555"
    business_account_id: "666666666666666"
    webhook_url: "https://internal.acme.com/whatsapp/webhook"
    api_kind: on-premise
    templates:
      - { name: order_confirmation, language: en_US }
      - { name: order_shipped,      language: en_US }
      - { name: order_delivered,    language: en_US }
      - { name: support_followup,   language: en_US }
      - { name: feedback_request,   language: en_US }

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: WHATSAPP_ACCESS_TOKEN
    description: On-premise client token.
    secret: true

deployment:
  targets: [whatsapp]

metadata:
  license: proprietary
  author: { name: Acme Support, handle: acme-support, org: Acme }
  source: { type: git, url: https://github.com/acme-support/whatsapp-business }
  id: com.acme-support.whatsapp-business
""",
    },
}

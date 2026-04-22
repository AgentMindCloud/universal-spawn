"""LINE — Messaging API + LIFF apps."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "line",
    "title": "LINE",
    "lede": (
        "LINE bots use the Messaging API; LINE Mini Apps use LIFF "
        "(LINE Front-end Framework). A universal-spawn manifest "
        "captures the channel id, rich-menu configuration, and LIFF "
        "endpoint."
    ),
    "cares": (
        "The channel id, channel kind (`messaging-api`, `liff`), the "
        "rich-menu image, and the LIFF endpoint URL."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `web-app`."),
        ("platforms.line", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.line.channel_id", "LINE channel id."),
        ("platforms.line.channel_kind", "`messaging-api` or `liff`."),
        ("platforms.line.webhook_url", "Messaging-API webhook URL."),
        ("platforms.line.rich_menu_image", "Rich menu image path."),
        ("platforms.line.liff_endpoint_url", "LIFF endpoint URL."),
        ("platforms.line.scopes", "LIFF scopes."),
    ],
    "platform_fields": {
        "channel_id": "LINE channel id.",
        "channel_kind": "`messaging-api` or `liff`.",
        "webhook_url": "Messaging API webhook URL.",
        "rich_menu_image": "Rich-menu image path.",
        "liff_endpoint_url": "LIFF endpoint URL.",
        "scopes": "LIFF scopes.",
    },
    "schema_body": schema_object(
        required=["channel_id", "channel_kind"],
        properties={
            "channel_id": str_prop(pattern=r"^[0-9]{8,20}$"),
            "channel_kind": enum(["messaging-api", "liff"]),
            "webhook_url": {"type": "string", "format": "uri"},
            "rich_menu_image": str_prop(),
            "liff_endpoint_url": {"type": "string", "format": "uri"},
            "scopes": {
                "type": "array",
                "items": enum(["profile", "openid", "email", "chat_message.write"]),
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: LINE Template
type: bot
description: Template for a LINE-targeted universal-spawn manifest.

platforms:
  line:
    channel_id: "1111111111"
    channel_kind: messaging-api
    webhook_url: "https://api.yourapp.example/line/webhook"

safety:
  min_permissions: [network:inbound, network:outbound:api.line.me]

env_vars_required:
  - name: LINE_CHANNEL_ACCESS_TOKEN
    description: Channel access token.
    secret: true
  - name: LINE_CHANNEL_SECRET
    description: Channel secret.
    secret: true

deployment:
  targets: [line]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/line-template }
""",
    "native_config_name": "LINE Developers Console + (optional) liff.config.json",
    "native_config_lang": "text",
    "native_config": "# Configured in the LINE Developers Console; secrets via the channel.\n",
    "universal_excerpt": """
platforms:
  line:
    channel_id: "1111111111"
    channel_kind: messaging-api
    webhook_url: "https://api.yourapp.example/line/webhook"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate LINE Bot
type: bot
summary: Minimal LINE Messaging API bot replying with the plate of the day.
description: Webhook receiver. Rich menu image. No LIFF surface.

platforms:
  line:
    channel_id: "2222222222"
    channel_kind: messaging-api
    webhook_url: "https://api.plate.example/line/webhook"
    rich_menu_image: assets/rich-menu.png

safety:
  min_permissions: [network:inbound, network:outbound:api.line.me]
  safe_for_auto_spawn: false

env_vars_required:
  - name: LINE_CHANNEL_ACCESS_TOKEN
    description: Channel access token.
    secret: true
  - name: LINE_CHANNEL_SECRET
    description: Channel secret.
    secret: true

deployment:
  targets: [line]

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/line-plate-bot }
  id: com.plate-studio.line-plate-bot
""",
        "example-2": """
version: "1.0"
name: Plate LIFF App
type: web-app
summary: Full LINE Mini App (LIFF) for browsing parchment plates.
description: LIFF endpoint URL. Profile + email scopes. Pairs with the messaging-api bot above.

platforms:
  line:
    channel_id: "3333333333"
    channel_kind: liff
    liff_endpoint_url: "https://liff.plate.example/"
    scopes: [profile, openid, email]

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [line]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/line-plate-liff }
  id: com.plate-studio.line-plate-liff
""",
    },
}

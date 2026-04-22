"""Telegram — Bot API + WebApp + setMyCommands."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "telegram",
    "title": "Telegram",
    "lede": (
        "Telegram exposes the Bot API (long-poll or webhook) and "
        "Telegram Web Apps. A universal-spawn manifest captures the "
        "bot username, the registered commands, and (optionally) the "
        "Web App entry URL."
    ),
    "cares": (
        "The bot username, transport (`long-poll` or `webhook`), "
        "registered commands (for `setMyCommands`), and Web App URL."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `web-app`."),
        ("platforms.telegram", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.telegram.bot_username", "Bot @-handle."),
        ("platforms.telegram.transport", "`long-poll` or `webhook`."),
        ("platforms.telegram.webhook_url", "Webhook URL when transport is webhook."),
        ("platforms.telegram.commands", "Registered commands."),
        ("platforms.telegram.web_app_url", "Telegram Web App entry URL."),
    ],
    "platform_fields": {
        "bot_username": "Bot @-handle.",
        "transport": "`long-poll` or `webhook`.",
        "webhook_url": "Webhook URL.",
        "commands": "Registered commands.",
        "web_app_url": "Telegram Web App entry URL.",
    },
    "schema_body": schema_object(
        required=["bot_username", "transport"],
        properties={
            "bot_username": str_prop(pattern=r"^[A-Za-z0-9_]{5,32}_?bot$"),
            "transport": enum(["long-poll", "webhook"]),
            "webhook_url": {"type": "string", "format": "uri"},
            "commands": {
                "type": "array",
                "items": schema_object(
                    required=["command", "description"],
                    properties={
                        "command": str_prop(pattern=r"^[a-z][a-z0-9_]{0,31}$"),
                        "description": str_prop(),
                    },
                ),
            },
            "web_app_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Telegram Template
type: bot
description: Template for a Telegram-targeted universal-spawn manifest.

platforms:
  telegram:
    bot_username: yourname_bot
    transport: long-poll
    commands:
      - { command: start, description: "Start the bot." }
      - { command: help,  description: "Show help." }

safety:
  min_permissions: [network:outbound:api.telegram.org]

env_vars_required:
  - name: TELEGRAM_BOT_TOKEN
    description: Bot token from @BotFather.
    secret: true

deployment:
  targets: [telegram]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/telegram-template }
""",
    "native_config_name": "BotFather + setMyCommands",
    "native_config_lang": "text",
    "native_config": "# Configure via @BotFather; commands registered with the setMyCommands API.\n",
    "universal_excerpt": """
platforms:
  telegram:
    bot_username: yourname_bot
    transport: long-poll
    commands:
      - { command: start, description: "Start the bot." }
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Telegram Bot
type: bot
summary: Minimal Telegram long-poll bot with two commands.
description: /start and /help. No Web App.

platforms:
  telegram:
    bot_username: plate_studio_bot
    transport: long-poll
    commands:
      - { command: start, description: "Start the plate bot." }
      - { command: help,  description: "Show help." }

safety:
  min_permissions: [network:outbound:api.telegram.org]
  safe_for_auto_spawn: false

env_vars_required:
  - name: TELEGRAM_BOT_TOKEN
    description: Bot token.
    secret: true

deployment:
  targets: [telegram]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/telegram-plate-bot }
  id: com.plate-studio.telegram-plate-bot
""",
        "one-click-add": """
version: "1.0"
name: Plate Studio Web App
type: bot
summary: Full Telegram Web App with a one-click Telegram URL to add the bot.
description: >
  Webhook-driven Telegram bot that opens a Telegram Web App for
  plate browsing. A consumer renders a `https://t.me/{bot_username}`
  link that adds the bot in one click.

platforms:
  telegram:
    bot_username: plate_explore_bot
    transport: webhook
    webhook_url: "https://api.plate.example/telegram/webhook"
    commands:
      - { command: start, description: "Open the plate gallery." }
    web_app_url: "https://app.plate.example/telegram"

safety:
  min_permissions: [network:inbound, network:outbound:api.telegram.org]
  safe_for_auto_spawn: false

env_vars_required:
  - name: TELEGRAM_BOT_TOKEN
    description: Bot token.
    secret: true
  - name: WEBHOOK_SECRET
    description: Webhook signing secret.
    secret: true

deployment:
  targets: [telegram]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/telegram-plate-webapp }
  id: com.plate-studio.telegram-plate-webapp
""",
    },
}

"""Slack — Bolt apps + slash commands + manifest.json."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "slack",
    "title": "Slack",
    "lede": (
        "Slack apps ship via a `manifest.json` that declares OAuth "
        "scopes, slash commands, event subscriptions, and "
        "interactive shortcuts. A universal-spawn manifest captures "
        "those fields plus the canonical 'Add to Slack' URL inputs."
    ),
    "cares": (
        "Bot + user OAuth scopes, slash commands, event subscriptions, "
        "and the Slack manifest.json file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `extension`, `web-app`."),
        ("platforms.slack", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.slack.manifest_file", "Slack `manifest.json` file path."),
        ("platforms.slack.bot_scopes", "Bot OAuth scopes."),
        ("platforms.slack.user_scopes", "User OAuth scopes (optional)."),
        ("platforms.slack.slash_commands", "Slash commands."),
        ("platforms.slack.event_subscriptions", "Subscribed events."),
        ("platforms.slack.socket_mode", "True for Socket Mode."),
    ],
    "platform_fields": {
        "manifest_file": "Slack manifest.json.",
        "bot_scopes": "Bot OAuth scopes.",
        "user_scopes": "User OAuth scopes.",
        "slash_commands": "Slash commands.",
        "event_subscriptions": "Subscribed events.",
        "socket_mode": "Socket Mode flag.",
    },
    "schema_body": schema_object(
        properties={
            "manifest_file": str_prop(),
            "bot_scopes": {"type": "array", "items": str_prop()},
            "user_scopes": {"type": "array", "items": str_prop()},
            "slash_commands": {
                "type": "array",
                "items": schema_object(
                    required=["command"],
                    properties={
                        "command": str_prop(pattern=r"^/[a-z][a-z0-9_-]{0,31}$"),
                        "description": str_prop(),
                    },
                ),
            },
            "event_subscriptions": {"type": "array", "items": str_prop()},
            "socket_mode": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Slack Template
type: bot
description: Template for a Slack-targeted universal-spawn manifest.

platforms:
  slack:
    manifest_file: slack.manifest.json
    bot_scopes: [chat:write, commands]
    slash_commands:
      - { command: "/ping", description: "Ping the bot." }
    socket_mode: false

safety:
  min_permissions: [network:outbound:slack.com]

env_vars_required:
  - name: SLACK_BOT_TOKEN
    description: Bot xoxb token.
    secret: true
  - name: SLACK_SIGNING_SECRET
    description: Signing secret for incoming requests.
    secret: true

deployment:
  targets: [slack]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/slack-template }
""",
    "native_config_name": "slack manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "display_information": { "name": "Your App" },
  "features": {
    "bot_user": { "display_name": "Your App", "always_online": true },
    "slash_commands": [{ "command": "/ping", "url": "https://api.example/slack" }]
  },
  "oauth_config": { "scopes": { "bot": ["chat:write", "commands"] } }
}
""",
    "universal_excerpt": """
platforms:
  slack:
    manifest_file: slack.manifest.json
    bot_scopes: [chat:write, commands]
    slash_commands:
      - { command: "/ping", description: "Ping the bot." }
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Slack Bot
type: bot
summary: Minimal Bolt app — single /plate slash command.
description: HTTP transport. One slash command. Two scopes.

platforms:
  slack:
    manifest_file: slack.manifest.json
    bot_scopes: [chat:write, commands]
    slash_commands:
      - { command: "/plate", description: "Show the plate of the day." }

safety:
  min_permissions: [network:outbound:slack.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: SLACK_BOT_TOKEN
    description: xoxb token.
    secret: true
  - name: SLACK_SIGNING_SECRET
    description: Signing secret.
    secret: true

deployment:
  targets: [slack]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/slack-plate-bot }
  id: com.plate-studio.slack-plate-bot
""",
        "one-click-add": """
version: "1.0"
name: Plate Studio Slack App
type: bot
summary: Full Slack app with a one-click 'Add to Slack' URL.
description: >
  Bolt app shipped with a `slack.manifest.json` and rich event
  subscriptions. A consumer renders an "Add to Slack" button from
  the manifest's `client_id` (stored in a sibling secret).

platforms:
  slack:
    manifest_file: slack.manifest.json
    bot_scopes: [chat:write, commands, channels:history, im:history, files:read]
    user_scopes: [users:read.email]
    slash_commands:
      - { command: "/plate", description: "Browse plates." }
      - { command: "/critique", description: "Critique a posted plate." }
    event_subscriptions: [message.channels, app_mention, reaction_added]
    socket_mode: false

safety:
  min_permissions: [network:outbound:slack.com]
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false

env_vars_required:
  - name: SLACK_BOT_TOKEN
    description: xoxb token.
    secret: true
  - name: SLACK_SIGNING_SECRET
    description: Signing secret.
    secret: true
  - name: SLACK_CLIENT_ID
    description: OAuth client id used to build the install URL.

deployment:
  targets: [slack]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/slack-plate-app }
  id: com.plate-studio.slack-plate-app
""",
    },
}

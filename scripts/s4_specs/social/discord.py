"""Discord — bots, slash commands, Activities, one-click add."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "discord",
    "title": "Discord",
    "lede": (
        "Discord is the v1.0 successor to the v1.0.0 legacy "
        "`platforms/discord/` extension. It covers Application + Bot "
        "+ slash commands + Activities (embedded apps), with strict "
        "OAuth2 scope and Gateway intent declarations. Includes a "
        "canonical one-click 'Add to server' URL recipe."
    ),
    "cares": (
        "OAuth2 scopes, Gateway intents, slash commands, message "
        "commands, Activity config, and the application id used to "
        "build the canonical install URL."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `extension`, `creative-tool`."),
        ("platforms.discord", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.discord.application_id", "Application id (snowflake)."),
        ("platforms.discord.scopes", "OAuth2 scopes."),
        ("platforms.discord.intents", "Gateway intents."),
        ("platforms.discord.permissions", "Bot install permissions integer."),
        ("platforms.discord.slash_commands", "Slash command JSON files."),
        ("platforms.discord.message_commands", "Message command JSON files."),
        ("platforms.discord.activity", "Activity / embedded app config."),
    ],
    "platform_fields": {
        "application_id": "Application id.",
        "scopes": "OAuth2 scopes.",
        "intents": "Gateway intents.",
        "permissions": "Permissions integer.",
        "slash_commands": "Slash command JSON files.",
        "message_commands": "Message command JSON files.",
        "activity": "Activity config.",
    },
    "schema_body": schema_object(
        required=["application_id", "scopes"],
        properties={
            "application_id": str_prop(pattern=r"^[0-9]{17,20}$"),
            "scopes": {
                "type": "array",
                "minItems": 1,
                "items": enum(["bot", "applications.commands", "applications.commands.update", "applications.entitlements", "identify", "email", "guilds", "guilds.members.read", "messages.read", "webhook.incoming"]),
            },
            "intents": {
                "type": "array",
                "items": enum(["guilds", "guild_members", "guild_messages", "message_content", "guild_voice_states", "direct_messages", "auto_moderation_execution"]),
            },
            "permissions": str_prop(pattern=r"^[0-9]+$"),
            "slash_commands": {
                "type": "array",
                "items": str_prop(),
            },
            "message_commands": {
                "type": "array",
                "items": str_prop(),
            },
            "activity": schema_object(
                properties={
                    "supported_platforms": {
                        "type": "array",
                        "items": enum(["web", "ios", "android"]),
                    },
                    "orientation_lock_state": enum(["unlocked", "portrait", "landscape"]),
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Discord Template
type: bot
description: Template for a Discord-targeted universal-spawn manifest.

platforms:
  discord:
    application_id: "111111111111111111"
    scopes: [bot, applications.commands]
    intents: [guilds]
    permissions: "274877910016"
    slash_commands: [commands/ping.json]

safety:
  min_permissions: [network:outbound:discord.com, network:outbound:gateway.discord.gg]

env_vars_required:
  - name: DISCORD_BOT_TOKEN
    description: Discord bot token.
    secret: true

deployment:
  targets: [discord]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/discord-template }
""",
    "native_config_name": "Discord Application + bot.json",
    "native_config_lang": "json",
    "native_config": """
{
  "id": "111111111111111111",
  "name": "Your Bot",
  "scopes": ["bot", "applications.commands"],
  "intents": ["guilds"]
}
""",
    "universal_excerpt": """
platforms:
  discord:
    application_id: "111111111111111111"
    scopes: [bot, applications.commands]
    intents: [guilds]
    slash_commands: [commands/ping.json]
""",
    "compatibility_extras": (
        "## One-click 'Add to server' URL\n\n"
        "The canonical install URL is:\n\n"
        "```\n"
        "https://discord.com/oauth2/authorize?\n"
        "  client_id={application_id}&\n"
        "  scope={scopes joined with `+`}&\n"
        "  permissions={permissions integer}\n"
        "```\n\n"
        "Generators MAY render a 'Add to your server' button on any "
        "registry card from those four fields alone."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Discord Ping Bot
type: bot
summary: Minimal Discord bot — one /ping slash command.
description: Smallest useful bot; safe_for_auto_spawn so the install URL works without confirmation.

platforms:
  discord:
    application_id: "222222222222222222"
    scopes: [bot, applications.commands]
    intents: [guilds]
    permissions: "2147483648"
    slash_commands: [commands/ping.json]

safety:
  min_permissions: [network:outbound:discord.com, network:outbound:gateway.discord.gg]
  safe_for_auto_spawn: true

env_vars_required:
  - name: DISCORD_BOT_TOKEN
    description: Bot token.
    secret: true

deployment:
  targets: [discord]

metadata:
  license: Apache-2.0
  author: { name: Ping Co., handle: ping-co }
  source: { type: git, url: https://github.com/ping-co/discord-ping }
  id: com.ping-co.discord-ping
""",
        "one-click-add": """
version: "1.0"
name: Plate Studio Bot
type: bot
summary: Full Discord bot with slash + message commands and a 'one-click add to server' install URL.
description: >
  Full-shape Discord bot. Generators read this manifest and render a
  Discord install URL using `application_id` + `scopes` + `permissions`.

platforms:
  discord:
    application_id: "333333333333333333"
    scopes: [bot, applications.commands, messages.read]
    intents: [guilds, guild_messages, message_content]
    permissions: "274877910016"
    slash_commands: [commands/plate.json, commands/critique.json]
    message_commands: [commands/flag-message.json]

safety:
  min_permissions: [network:outbound:discord.com, network:outbound:gateway.discord.gg, messages:read]
  rate_limit_qps: 10
  safe_for_auto_spawn: false

env_vars_required:
  - name: DISCORD_BOT_TOKEN
    description: Bot token.
    secret: true

deployment:
  targets: [discord]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/discord-plate-bot }
  id: com.plate-studio.discord-plate-bot
""",
    },
}

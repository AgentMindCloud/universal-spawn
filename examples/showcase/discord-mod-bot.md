# Showcase · `mod-helper` — a Discord moderation bot

**Use case.** A Discord moderation bot that classifies messages
against a server-specific banned-pattern list, integrates with
AutoMod, and surfaces /report + /flag-message commands.

## The manifest

```yaml
version: "1.0"
name: Mod Helper
description: >
  Discord moderation bot. Listens to guild messages for banned
  patterns, integrates with AutoMod, exposes /report (slash) and
  Flag Message (context menu) commands.
type: bot
platforms:
  discord:
    application_id: "111122223333444455"
    scopes: [bot, applications.commands, messages.read]
    intents: [guilds, guild_messages, message_content, auto_moderation_execution]
    permissions: "274877910016"
    slash_commands: [commands/report.json]
    message_commands: [commands/flag-message.json]
safety:
  min_permissions:
    - network:outbound:discord.com
    - network:outbound:gateway.discord.gg
    - messages:read
  rate_limit_qps: 20
  safe_for_auto_spawn: false
env_vars_required:
  - { name: DISCORD_BOT_TOKEN, secret: true, description: Bot token }
deployment: { targets: [discord] }
metadata:
  license: Apache-2.0
  id: com.mod-helper.bot
  author: { name: Mod Helper Team, handle: mod-helper }
  source: { type: git, url: https://github.com/mod-helper/discord-bot }
  categories: [social, security]
```

## Platforms targeted, and why

- **`discord`** — the surface. AutoMod intent + message-content
  intent are why the bot exists.

## How discovery happens

The bot's website renders an "Add to your server" button derived
from `application_id` + `scopes` + `permissions`. A Discord
moderation directory crawls the manifest to populate its catalog.

# `ai-agent-discord-bot` template

Discord bot built on an LLM. One slash command (`/ask`) that the bot
replies to with an LLM-generated answer.

## What ships

- `universal-spawn.yaml` — Discord application + Claude subagent.
- `commands/ask.json` — slash-command definition.

## Change before shipping

1. `platforms.discord.application_id` → your Discord app id.
2. `platforms.discord.permissions` → recompute via Discord's
   permission calculator.
3. `metadata.author` and `metadata.source.url`.

## Validate

```bash
universal-spawn validate
```

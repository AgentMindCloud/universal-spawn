# `ai-agent-x-reply-bot` template

Production-shaped X (Twitter) reply bot powered by an LLM. Defaults
target Claude Opus; swap to Grok via `platforms.grok` for the
Grok-native variant (see `templates/x-native-agent-grok-compat/`).

## What ships

- `universal-spawn.yaml` — bot manifest with X scopes, daily cost cap,
  rate limit, no-emoji system-prompt slot.
- `tools/reply.json` — function-tool definition.

## Change before shipping

1. `platforms.x-twitter.account` → your bot @-handle.
2. `metadata.author` and `metadata.source.url`.
3. `safety.cost_limit_usd_daily` if your traffic is heavier.

## Validate

```bash
universal-spawn validate
```

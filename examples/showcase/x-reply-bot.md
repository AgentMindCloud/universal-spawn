# Showcase · `signal-scout` — an X reply bot powered by Grok

**Use case.** Tracks mentions of niche keywords in machine-learning
research conversations on X, uses Grok-4-fast to compose a one-tweet
reply pointing at a relevant paper, and posts. Operated by a single
researcher.

## The manifest

```yaml
version: "1.0"
name: Signal Scout
description: >
  X reply bot that watches a curated keyword stream, drafts a paper-
  citation reply with Grok-4-fast, and posts. Operated by one
  researcher; budget capped at $20 / day.
type: ai-agent
platforms:
  x-twitter:
    account: signal_scout
    scopes: [tweet.read, tweet.write, users.read, offline.access]
    tier: pro
    streams: [streams/keywords.json]
    uses_grok: true
  grok:
    model: grok-4-fast
    surface: [grok-api, grok-x-integration]
    system_prompt_file: prompts/system.md
    tools:
      - { name: cite, function_ref: tools/cite.json }
    streaming: true
    real_time_data: true
    grok_install_compat: { version: "2.14", x_handle: signal_scout }
safety:
  min_permissions:
    - network:outbound:api.x.ai
    - network:outbound:api.twitter.com
    - network:outbound:api.x.com
    - model:call:grok-4-fast
  rate_limit_qps: 5
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false
env_vars_required:
  - { name: XAI_API_KEY,             secret: true, description: xAI key }
  - { name: X_OAUTH_CLIENT_ID,       description: X client id }
  - { name: X_OAUTH_CLIENT_SECRET,   secret: true, description: X client secret }
deployment: { targets: [grok, x-twitter] }
metadata:
  license: Apache-2.0
  id: com.signal-scout.bot
  author: { name: Signal Scout, handle: signal-scout }
  source: { type: git, url: https://github.com/signal-scout/x-reply-bot }
```

## Platforms targeted, and why

- **`x-twitter`** — the bot's primary surface; without it there's no
  reply to post.
- **`grok`** — the model behind the reply. Grok's real-time data
  lets the bot react to fresh conversation, and the cross-link to
  `platforms.grok` keeps the bot Grok-native rather than a generic
  LLM bot.
- A `grok-install.yaml` ships alongside (per the flagship template's
  pattern) so existing Grok consumers keep working.

## How discovery happens

A user finds Signal Scout by reading the X bio, clicks through to
the GitHub repo, sees the `universal-spawn.yaml` at the root, and
the universal-spawn registry's `Spawn it` page renders a one-click
"Add to your X account" button derived from `platforms.x-twitter`
plus the scopes / tier / stream rules.

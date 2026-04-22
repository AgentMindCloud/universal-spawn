# `x-native-agent-grok-compat` — flagship template

The headline universal-spawn template: an X (Twitter) reply bot
powered by Grok-4, shipped with **both** a `grok-install.yaml`
(legacy, AgentMindCloud/grok-install v2.14) and a
`universal-spawn.yaml` (cross-platform). The two files coexist; one
manifest does not replace the other.

This template exists because the question "do I have to delete
`grok-install.yaml`?" has come up enough that the answer needs to
live in code, not in a wiki page.

## The compat story in one diagram

```
                ┌─────────────────────────────────────────┐
                │         your bot's git repo             │
                ├─────────────────────────────────────────┤
                │  grok-install.yaml      ← legacy v2.14   │
                │  universal-spawn.yaml   ← v1.0 standard  │
                │  tools/reply.json                        │
                │  prompts/system.md                       │
                └────────┬─────────────────────┬──────────┘
                         │                     │
                Grok consumer            Universal-spawn consumer
                (reads grok-install.yaml)  (reads universal-spawn.yaml)
                         │                     │
                         └────────────┬────────┘
                                      ▼
                            same bot, two front doors
```

Both files describe the same bot. The Grok host reads
`grok-install.yaml` for backward compatibility. Any other consumer —
Claude, OpenAI, a generic registry — reads `universal-spawn.yaml`
and looks at `platforms.grok` for the Grok-specific fields.

## What ships in this template

| File | Purpose |
|---|---|
| `universal-spawn.yaml` | The cross-platform manifest. Contains a `platforms.grok` block with all fields the legacy v2.14 file needs. |
| `grok-install.yaml` | The legacy AgentMindCloud/grok-install v2.14 manifest, unchanged. |
| `tools/reply.json` | Function-tool definition (xAI tool-use schema). |
| `prompts/system.md` | System prompt loaded by both surfaces. |

## What to change before you ship

1. Both manifests' `name`, `description`, and `metadata.author` /
   `author.x_handle` (in the legacy file).
2. The X bot account handle inside `platforms.x-twitter.account`
   (universal) and `account` (legacy).
3. `metadata.source.url` to your real repo URL once you push.
4. Replace placeholders in `prompts/system.md` with your actual
   system prompt.

## Validate

```bash
universal-spawn validate          # checks universal-spawn.yaml
# Optional: validate the legacy file with the v1.0.0 legacy validator.
```

## Round-trip invariant

For any universal-spawn manifest `u` with `compat.grok_install`
declared, the lowering tool produces a `grok-install.yaml` `g` such
that lifting `g` back yields `u` modulo field ordering and the fields
listed as "dropped" in `docs/grok-compat.md`.

This template is the canonical exercise of that invariant: edit one
side, regenerate the other, diff to confirm the round-trip holds.

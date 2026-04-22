# Canonical schema sources

Authoritative URLs for every published schema. These are the same
URLs the schemas declare in their `$id`. Cache them; never re-host
without updating the `$id`.

## Master spec

| Schema | URL |
|---|---|
| v1.0 master | `https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json` |
| v1.0.0 legacy (draft 2020-12) | `https://universal-spawn.org/spec/v1.0.0/manifest.schema.json` |

## Platform extensions (v1.0 track)

All v1.0 platform extensions are draft-07 and `allOf` against the v1.0
master. URL pattern:

```
https://universal-spawn.dev/platforms/<subtree>/<id>/<id>-spawn.schema.json
```

### AI

| Id | URL suffix |
|---|---|
| grok | `platforms/ai/grok/grok-spawn.schema.json` |
| claude | `platforms/ai/claude/claude-spawn.schema.json` |
| openai | `platforms/ai/openai/openai-spawn.schema.json` |
| gemini | `platforms/ai/gemini/gemini-spawn.schema.json` |
| llama | `platforms/ai/llama/llama-spawn.schema.json` |
| mistral | `platforms/ai/mistral/mistral-spawn.schema.json` |
| groq-cloud | `platforms/ai/groq-cloud/groq-cloud-spawn.schema.json` |
| cohere | `platforms/ai/cohere/cohere-spawn.schema.json` |
| ai21 | `platforms/ai/ai21/ai21-spawn.schema.json` |
| perplexity | `platforms/ai/perplexity/perplexity-spawn.schema.json` |
| together-ai | `platforms/ai/together-ai/together-ai-spawn.schema.json` |
| fireworks | `platforms/ai/fireworks/fireworks-spawn.schema.json` |
| replicate | `platforms/ai/replicate/replicate-spawn.schema.json` |
| huggingface | `platforms/ai/huggingface/huggingface-spawn.schema.json` |
| anthropic-mcp | `platforms/ai/anthropic-mcp/anthropic-mcp-spawn.schema.json` |
| multi-agent/* | `platforms/ai/multi-agent/<id>/<id>-spawn.schema.json` (8 frameworks) |
| coding-agents/* | `platforms/ai/coding-agents/<id>/<id>-spawn.schema.json` (6 agents) |
| local/* | `platforms/ai/local/<id>/<id>-spawn.schema.json` (4 runtimes) |

### Hosting (20)

URL pattern: `platforms/hosting/<id>/<id>-spawn.schema.json`. Ids:
vercel, netlify, cloudflare, deno-deploy, railway, fly-io, render,
heroku, aws, gcp, azure, supabase, firebase, digitalocean, koyeb,
northflank, pythonanywhere, hetzner, linode, vultr.

### Creative (12), Devtools (20), Social (9), Data-ML (11), Gaming (13), Hardware-IoT (9)

URL pattern: `platforms/<subtree>/<id>/<id>-spawn.schema.json`. See
each subtree's `README.md` for the id list.

## Wiring autocomplete

See [`README.md`](./README.md) for editor-by-editor setup.

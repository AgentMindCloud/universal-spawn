# `ai-agent-research` template

Multi-source research agent. Pulls from web search + arXiv + the
manifest's RAG corpus, returns a citeable summary.

## What ships

- `universal-spawn.yaml` — Claude Opus subagent + Perplexity
  grounding tool + W&B for observability.
- `tools/research.json` — function-tool definition.

## Change before shipping

1. `metadata.id` and source URL.
2. Add your RAG corpus binding in `platforms.claude` if you have one.

## Validate

```bash
universal-spawn validate
```

# OpenAI perks — what OpenAI could offer manifests that target OpenAI

- **Priority discovery** — GPT Store search ranks manifest-declaring
  entries above scraped metadata.
- **One-click publish to GPT Store** — `platforms.openai.action` with
  a valid `openapi_ref` renders a "Publish to GPT Store" button.
- **Assistants-API prefill** — `platforms.openai.assistant` fields
  pre-populate the Assistants console.
- **Agents-SDK scaffolding** — `platforms.openai.agent.handoffs[]`
  generates a starter agents graph for the Agents SDK.
- **Reasoning slider prefill** — `reasoning_effort` selects the
  slider at the first spawn.
- **Spend cap prefill** — `safety.cost_limit_usd_daily` pre-fills
  the org spend cap field.
- **Audit trail** — canonical manifest SHA-256 logged per spawn.
- **Badges** — a manifest that passes `openai-spawn.schema.json`
  carries an OpenAI-conformant badge.

Out-of-scope: OpenAI speaks for itself; this file is a wishlist.

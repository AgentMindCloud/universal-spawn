# OpenAI integration guide

For OpenAI Platform / GPT Store / Assistants / Agents SDK engineers.

## Detection

`universal-spawn.{yaml,yml,json}` at the repo root. Validate
against `platforms/ai/openai/openai-spawn.schema.json`.

## Mapping `platforms.openai`

| `platforms.openai.<field>` | Where to wire it |
|---|---|
| `model` | OpenAI model id. |
| `system_prompt_file` | System prompt source. |
| `tools[*]` | Function tools (Responses / Chat Completions). |
| `tools[*].strict` | Strict-mode flag for structured output. |
| `assistant.*` | Assistants API registration. |
| `action.openapi_ref` | GPT Store Action backed by an OpenAPI doc. |
| `action.privacy_policy_url` | Required by the GPT Store. |
| `agent.*` | Agents SDK registration (handoffs, guardrails). |
| `realtime.*` | Realtime API session. |
| `response_format` | `text` / `json_object` / `json_schema`. |
| `response_schema_ref` | JSON Schema for structured output. |
| `reasoning_effort` | Reasoning slider preset. |

## Honoring the safety envelope

- `safety.min_permissions[]` → Code Interpreter sandbox.
- `safety.cost_limit_usd_daily` → org-wide hard limit.
- `safety.safe_for_auto_spawn` → first-run install confirmation.

## Spawn-it buttons

- `platforms.openai.action.openapi_ref` + `privacy_policy_url`
  set → "Publish to GPT Store" button.
- `platforms.openai.assistant` set → "Add to Assistants" inside the
  org console.
- `platforms.openai.agent` set → "Open in Agents SDK" link.

## Estimated effort

- Detect + validate: 30 minutes.
- Wire each surface (Action, Assistant, Agent, Realtime): 1 day
  per surface.
- Hash logging + revoke endpoint: 1 day.

## See also

- [`platforms/ai/openai/`](../platforms/ai/openai/).
- [`templates/ai-agent-x-reply-bot/`](../templates/ai-agent-x-reply-bot/)
  — combines OpenAI / Claude / Grok-targeted bots with X integration.

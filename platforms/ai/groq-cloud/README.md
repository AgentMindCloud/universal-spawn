# GroqCloud — universal-spawn platform extension

GroqCloud (note: NOT xAI Grok; see `../grok/`) is an inference-only host for a set of open models — Llama 3.3, Mixtral, Gemma 2, Whisper. The extension targets the OpenAI-compatible Chat Completions endpoint Groq exposes, with one Groq-specific detail: the model id is the full Groq catalogue string.

## What this platform cares about

GroqCloud cares about the exact model id from its catalogue (`llama-3.3-70b-versatile`, `mixtral-8x7b-32768`, …), whether function calling is on, and the streaming mode.

## What platform-specific extras unlock

`response_format` enables JSON mode. `parallel_tool_calls` toggles Groq's batched tool-call support.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | GroqCloud behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Shown on the GroqCloud console job list. |
| `type` | Accepts `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Informational; Groq runs inference in its own sandbox. |
| `safety.cost_limit_usd_daily` | Advisory; GroqCloud's spend cap is set on the org. |
| `env_vars_required` | Staged into the GroqCloud secret store. |
| `platforms.groq-cloud` | Strict; see below. |

### `platforms.groq-cloud` fields

| Field | Purpose |
|---|---|
| `platforms.groq-cloud.model` | GroqCloud catalogue model id. |
| `platforms.groq-cloud.tools` | OpenAI-shaped function tools. |
| `platforms.groq-cloud.response_format` | `text` or `json_object`. |
| `platforms.groq-cloud.parallel_tool_calls` | Groq batched tool-call mode. |
| `platforms.groq-cloud.streaming` | Server-sent events streaming toggle. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

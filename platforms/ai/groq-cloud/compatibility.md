# GroqCloud compatibility — field-by-field

| universal-spawn v1.0 field | GroqCloud behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Console card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.*` | Advisory across the board. |
| `env_vars_required` | Secret store. |
| `platforms.groq-cloud.model` | GroqCloud catalogue id. |
| `platforms.groq-cloud.tools` | OpenAI-compatible function tools. |
| `platforms.groq-cloud.response_format` | `text`, `json_object`. |
| `platforms.groq-cloud.parallel_tool_calls` | Batched tool-call mode. |
| `platforms.groq-cloud.streaming` | SSE streaming toggle. |

## Not to be confused with `grok/`

GroqCloud is Groq's **inference** platform for open models. xAI's **Grok** model lives in `../grok/`. The spelling difference is intentional.

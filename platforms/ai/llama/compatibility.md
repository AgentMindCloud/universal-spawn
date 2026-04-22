# Llama (Meta) compatibility — field-by-field

| universal-spawn v1.0 field | Llama (Meta) behavior |
|---|---|
| `version` | Required literal `"1.0"`. |
| `metadata.id` | Stable key across Llama Stack consumers. |
| `name, description` | Model card + listings. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Enforced on self-hosted sandboxes. |
| `safety.rate_limit_qps` | Advisory. |
| `safety.cost_limit_usd_daily` | Informational. |
| `safety.safe_for_auto_spawn` | First-run confirmation gate. |
| `env_vars_required` | Credential store staging. |
| `platforms.llama.model` | Llama variant id. |
| `platforms.llama.endpoint_url` | Llama Stack endpoint URL override. |
| `platforms.llama.tools` | OpenAI-shaped function tools. |
| `platforms.llama.llama_guard` | Policy file + enforcement level. |
| `platforms.llama.quantization` | `int4`, `int8`, `fp16`, `bf16`. |

## Endpoint portability

`endpoint_url` lets the same manifest run on Meta's reference server, Together, Groq, Fireworks, or a private deployment. The Llama Stack wire protocol is identical across hosts; only the model catalogue differs.

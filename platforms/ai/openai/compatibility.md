# OpenAI compatibility — universal-spawn ↔ OpenAI surfaces

| Manifest field                      | OpenAI behavior                                       |
|-------------------------------------|--------------------------------------------------------|
| `version`                           | Required `"1.0"`.                                     |
| `metadata.id`                       | Stable key in GPT Store / org.                        |
| `name`, `description`               | Card text on GPT Store / Assistants.                  |
| `type`                              | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`. |
| `safety.min_permissions`            | Enforced on Code Interpreter / tool sandbox.          |
| `safety.rate_limit_qps`             | Advisory; org-level quotas apply.                     |
| `safety.cost_limit_usd_daily`       | Enforced as org hard limit.                           |
| `env_vars_required`                 | Staged into org secret store.                         |
| `platforms.openai.tools[*]`         | Responses / Chat Completions `tools`.                 |
| `platforms.openai.assistant`        | Registered via Assistants API.                        |
| `platforms.openai.action`           | GPT Store Action (public). Requires `openapi_ref` + `privacy_policy_url`. |
| `platforms.openai.agent`            | Registered via Agents SDK (handoffs, guardrails).    |
| `platforms.openai.realtime`         | Realtime API session.                                 |
| `platforms.openai.response_format`  | Forces text / json_object / json_schema.              |
| `platforms.openai.response_schema_ref` | Path to JSON Schema for structured output.         |
| `platforms.openai.reasoning_effort` | Reasoning slider preset.                              |
| `compat.openapi` (master)           | Used when `action.openapi_ref` is unset.              |

## Strict function tools

Setting `platforms.openai.tools[*].strict: true` constrains the model
to produce arguments matching the declared JSON schema exactly.
Recommended for production Actions.

## Realtime limits

A Realtime session ignores `rate_limit_qps` — the limit is latency,
not throughput. `cost_limit_usd_daily` still applies at the key
scope.

## GPT Store vs Assistants vs Agents

These are three different product surfaces; the manifest can target
any combination:

- `action` → public on the GPT Store. Must have privacy policy URL.
- `assistant` → org-internal Assistants-API assistant.
- `agent` → Agents-SDK agent with handoffs.

A manifest that sets all three describes the same creation across
all three surfaces; a consumer picks the one it can spawn.

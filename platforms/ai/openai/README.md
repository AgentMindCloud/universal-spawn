# OpenAI — universal-spawn platform extension

Covers the OpenAI surfaces a creator is most likely to target: the
Responses API, Chat Completions, the Agents SDK, the Assistants API,
the GPT Store (Custom GPTs / Actions), and the new Realtime surface.
The extension is strict (`additionalProperties: false`) and composes
with the master v1.0 schema via `allOf`.

## Five primary shapes

1. **Function tool** — a tool registered via Responses / Chat
   Completions `tools` parameter.
2. **Custom GPT (Action)** — a public GPT Store entry backed by an
   OpenAPI document with OAuth or API-key auth.
3. **Assistant** — an Assistants-API assistant with tool list,
   instructions file, and optional file search.
4. **Agent** — an Agents SDK agent (handoffs, guardrails, tracing).
5. **Realtime** — a Realtime-API endpoint for voice or low-latency
   multimodal.

Each shape lives under `platforms.openai.<shape>` and is optional. A
manifest typically uses one shape; `tools[]` are compatible with
any of the first four.

## Structured output

Set `platforms.openai.response_format` to `json_schema` and point
`response_schema_ref` at the schema file. Consumers enforce strict
JSON matching when supported.

## Reasoning effort

`platforms.openai.reasoning_effort` pre-selects the slider:
`minimal`, `low`, `medium`, `high`. Consumers honor it; users may
override in the UI.

## Custom GPT — special handling

A manifest that declares `platforms.openai.action` is a GPT Store
candidate. The `openapi_ref` MUST point at a valid OpenAPI 3.1
document. Auth is `none`, `api_key`, or `oauth`. A
`privacy_policy_url` is required by the store and by this schema.

## Compatibility table

| Manifest field                 | OpenAI behavior                                   |
|--------------------------------|----------------------------------------------------|
| `version`                      | Required literal `"1.0"`.                         |
| `metadata.id`                  | Stable key; clashes rejected on upload.           |
| `name`, `description`          | Shown on GPT Store / Assistants cards.            |
| `type`                         | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`. |
| `safety.min_permissions`       | Enforced on Code Interpreter sandbox.             |
| `safety.cost_limit_usd_daily`  | Enforced as org hard limit.                       |
| `env_vars_required`            | Staged into the org secret store.                 |
| `platforms.openai.tools[*]`    | Function tools on Responses / Chat Completions.   |
| `platforms.openai.assistant`   | Registered via Assistants API.                    |
| `platforms.openai.action`      | GPT Store Action (public).                        |
| `platforms.openai.agent`       | Registered via Agents SDK.                        |
| `platforms.openai.realtime`    | Registered via Realtime API.                      |
| `platforms.openai.response_format` | Enforced JSON mode.                            |
| `platforms.openai.reasoning_effort` | Slider preset.                               |

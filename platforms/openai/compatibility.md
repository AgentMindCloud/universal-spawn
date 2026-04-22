# OpenAI — compatibility notes

| Field                  | Behavior on OpenAI                                                       |
|------------------------|---------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                         |
| `id`                   | Used as the stable key in the OpenAI registry; clashes are rejected.     |
| `name`, `description`  | Shown on GPT Store / Assistants cards.                                   |
| `kind`                 | `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`.              |
| `license`              | `proprietary` OK for private Assistants; blocked on the public GPT Store.|
| `author`, `source`     | Required.                                                                |
| `runtime`              | Informational.                                                           |
| `entrypoints`          | At least one of `tool-call`, `http`, `websocket`, or `cli`.              |
| `env_vars_required`    | Surfaced at install; stored in the organization's secret store.          |
| `min_permissions`      | Enforced on the Code Interpreter sandbox.                                |
| `rate_limit_qps`       | Advisory — organization quotas apply.                                    |
| `cost_limit_usd_daily` | Enforced as an organization hard limit.                                  |
| `safe_for_auto_spawn`  | If false, a human must approve first use.                                |
| `data_residency`       | Used to pick an EU / US endpoint where available.                        |
| `compat.openapi`       | Used verbatim when `action.openapi_ref` is unset.                        |
| `signatures`           | Verified when present; advisory in v1.0.0.                               |

## Entrypoint kinds

- `tool-call` → `function` tool in Responses / Chat Completions.
- `http`, `websocket` → GPT Store Action or Assistants tool.
- `cli` → OpenAI CLI command.
- Others: ignored.

## Strict mode

Set `tools[].strict: true` to have the consumer force JSON-schema-only
arguments.

## Structured output

When `response_format` is `json_schema`, the schema lives at
`response_schema_ref` relative to the repository root.

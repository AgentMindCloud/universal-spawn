# Gemini — compatibility notes

| Field                  | Behavior on Gemini                                                           |
|------------------------|-------------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                             |
| `id`                   | Used as the extension id inside a Google Cloud project.                      |
| `name`, `description`  | Shown in the Vertex AI Extensions UI and the Gemini picker.                  |
| `kind`                 | `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`.                  |
| `license`              | `proprietary` OK inside a private project; blocked on the public registry.   |
| `author`, `source`     | Required. The extension card links to `source.url`.                          |
| `runtime`              | Informational. Gemini does not install local runtimes.                       |
| `entrypoints`          | At least one of kind `tool-call`, `http`, `webhook`, `websocket`, or `cli`. |
| `env_vars_required`    | Surfaced to the caller at extension registration.                            |
| `min_permissions`      | Enforced on the Gemini code-execution sandbox.                               |
| `rate_limit_qps`       | Advisory — enforced by Google's quota system at project scope.               |
| `cost_limit_usd_daily` | Enforced as a daily spend cap on the project.                                |
| `safe_for_auto_spawn`  | If false, the Gemini consumer requires explicit install.                     |
| `data_residency`       | Used to pick a regional Vertex endpoint.                                     |
| `compat.openapi`       | Used verbatim as the extension's OpenAPI when `extension.openapi_ref` is unset.|
| `signatures`           | Verified when present; advisory in v1.0.0.                                   |

## Entrypoint kinds

- `tool-call` → `FunctionDeclaration`.
- `http`, `webhook`, `websocket` → Vertex AI Extension backed by OpenAPI.
- `cli` → Gemini CLI command.
- `slash-command`, `scene`, `ui-panel`, `stdio` → ignored.

## Grounding and search

Enable `grounding.google_search: true` or set
`grounding.vertex_search_corpus` to opt into retrieval. Grounded
responses include citations; consumers MUST render them.

## Safety settings

Gemini applies its own safety filtering on top of `min_permissions`.
The `safety_settings` block lets the author record recommended
thresholds; the consumer MAY override.

# Gemini compatibility — universal-spawn ↔ Google surfaces

| Manifest field                              | Gemini behavior                                   |
|---------------------------------------------|----------------------------------------------------|
| `version`                                   | Required `"1.0"`.                                 |
| `metadata.id`                               | Extension id inside a Google Cloud project.       |
| `name`, `description`                       | Vertex Extensions UI + Gem card.                  |
| `type`                                      | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`. |
| `safety.min_permissions`                    | Enforced on code-execution sandbox.               |
| `safety.rate_limit_qps`                     | Advisory; Google project quotas apply.            |
| `safety.cost_limit_usd_daily`               | Enforced as project-level daily cap.              |
| `env_vars_required`                         | Surfaced at extension registration.               |
| `platforms.gemini.model`                    | Recommended model id; consumer may override.      |
| `platforms.gemini.tools[*]`                 | `FunctionDeclaration`.                            |
| `platforms.gemini.extension.openapi_ref`    | Vertex AI Extension OpenAPI path.                 |
| `platforms.gemini.extension.auth`           | `none`, `api_key`, `oauth`, `gcp_service_account`.|
| `platforms.gemini.gem.*`                    | Gem publication inside Gemini app.                |
| `platforms.gemini.grounding.google_search`  | Enables Google Search grounding.                  |
| `platforms.gemini.grounding.vertex_search_corpus` | Named Vertex Search corpus grounding.       |
| `platforms.gemini.safety_settings`          | Harm thresholds per category.                     |
| `platforms.gemini.code_execution`           | Toggle built-in code-execution tool.              |
| `platforms.gemini.thinking.budget_tokens`   | Extended-thinking budget (Gemini 2.5-pro).        |
| `compat.openapi` (master)                   | Used when `extension.openapi_ref` unset.          |

## Gem visibility

- `private` — owner only.
- `workspace` — the Google Workspace org.
- `public` — listed on the Gemini Gems directory.

`public` gems **MUST** have a `license` field and a
`metadata.source.url`. The Gemini directory refuses publication
otherwise.

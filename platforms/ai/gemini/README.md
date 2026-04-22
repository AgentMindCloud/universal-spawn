# Gemini (Google) — universal-spawn platform extension

Gemini's surfaces are plural: the Gemini API
(`generativelanguage.googleapis.com`), the Vertex AI endpoint
(`aiplatform.googleapis.com`), Gems inside Gemini app, Gemini CLI,
and Vertex AI Extensions (OpenAPI-backed). This extension maps a
universal-spawn manifest onto all four.

The extension declares:

- `model` — one of the current Gemini models.
- `tools[]` — Gemini function declarations.
- `system_instruction_file` — system instruction source.
- `extension` — Vertex AI Extension backed by OpenAPI.
- `gem` — a Gem published in the Gemini app.
- `grounding` — Google Search or Vertex Search corpus grounding.
- `safety_settings` — per-category harm thresholds.
- `code_execution` — toggle the built-in code-execution tool.
- `thinking` — extended thinking for 2.5-pro.

The extension is strict (`additionalProperties: false`) and composes
with the master v1.0 schema via `allOf`.

## Vertex vs Gemini API

Both surfaces share the manifest shape. The consumer chooses which
endpoint to call based on the calling credential (API key → Gemini
API; service account → Vertex). `data_residency` routes to a regional
Vertex endpoint when available.

## Grounding

- `grounding.google_search: true` enables Google Search grounding on
  every turn.
- `grounding.vertex_search_corpus` names a Vertex AI Search corpus;
  responses include citations back into the corpus. Consumers MUST
  render citations.

## Compatibility table

| Manifest field                          | Gemini behavior                                 |
|-----------------------------------------|--------------------------------------------------|
| `version`                               | Required literal `"1.0"`.                       |
| `name`, `description`                   | Shown on Vertex AI Extensions UI and Gem card.   |
| `type`                                  | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`. |
| `safety.min_permissions`                | Enforced on the Gemini code-execution sandbox.   |
| `safety.rate_limit_qps`                 | Advisory — Google quotas apply.                  |
| `safety.cost_limit_usd_daily`           | Enforced as project-level daily cap.             |
| `env_vars_required`                     | Surfaced at extension registration.              |
| `platforms.gemini.model`                | Recommended model id.                            |
| `platforms.gemini.tools[*]`             | FunctionDeclarations.                            |
| `platforms.gemini.extension`            | Vertex AI Extension registration (OpenAPI).      |
| `platforms.gemini.gem`                  | Gem published inside Gemini app.                 |
| `platforms.gemini.grounding`            | Search / corpus grounding.                       |
| `platforms.gemini.safety_settings`      | Harm thresholds.                                 |
| `platforms.gemini.code_execution`       | Code-execution tool toggle.                      |
| `platforms.gemini.thinking`             | Extended-thinking budget (Gemini 2.5-pro).       |
| `compat.openapi` (master)               | Used verbatim when `extension.openapi_ref` unset.|

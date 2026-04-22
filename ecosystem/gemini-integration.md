# Gemini integration guide

For Google Vertex AI / Gemini engineers wiring universal-spawn
into the Gemini API, Vertex AI Extensions, and Gems.

## Detection

Add `universal-spawn.{yaml,yml,json}` to the repo crawler. Validate
against `platforms/ai/gemini/gemini-spawn.schema.json` plus the v1.0
master.

## Mapping `platforms.gemini`

| `platforms.gemini.<field>` | Where to wire it |
|---|---|
| `model` | The Gemini model to invoke. |
| `system_instruction_file` | Read into the Gemini system instruction. |
| `tools[*]` | `FunctionDeclaration` entries. |
| `extension.openapi_ref` | Vertex AI Extension registration. |
| `gem.*` | Gem registration in the Gemini app. |
| `grounding.google_search` | Enable Google Search grounding. |
| `grounding.vertex_search_corpus` | Vertex Search corpus name. |
| `safety_settings.*` | Per-category harm thresholds. |
| `code_execution` | Enable the built-in code-execution tool. |
| `thinking.budget_tokens` | Extended-thinking budget (2.5-pro). |

## Honoring the safety envelope

- `safety.min_permissions[]` → enforced on the code-execution
  sandbox.
- `safety.cost_limit_usd_daily` → daily spend cap at the GCP
  project scope.
- `safety.data_residency[]` → pick a regional Vertex endpoint when
  multi-region is offered.

## Spawn-it button

For Gem manifests with `platforms.gemini.gem.visibility: public`,
render a "Publish to Gemini Gems" button. For Extension manifests
with a valid `extension.openapi_ref`, render a "Deploy to Vertex"
button.

## Estimated effort

- Detect + validate: 30 minutes.
- Wire `platforms.gemini` to your provisioning paths: 1–2 days
  (one path per surface: Gemini API, Vertex Extensions, Gems).
- Spawn-it buttons + canonical-hash logging: 1 day.

## See also

- [`platforms/ai/gemini/`](../platforms/ai/gemini/).
- [`templates/ai-agent-research/`](../templates/ai-agent-research/)
  — example research-agent manifest that targets Gemini.

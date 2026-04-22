# Gemini platform extension

**Id**: `gemini`
**Vendor**: Google
**Surfaces**: Gemini API (`generativelanguage.googleapis.com` and
`aiplatform.googleapis.com`), Gemini CLI, Gemini Extensions for
Workspace.

A conformant Gemini consumer:

1. Validates the core manifest against
   `spec/v1.0.0/manifest.schema.json`.
2. Validates `platforms.gemini` against
   [`schema.extension.json`](./schema.extension.json).
3. Maps `entrypoints[*]` onto Gemini surfaces:
   - `tool-call` → a `FunctionDeclaration` in the Gemini function
     calling API.
   - `http` / `webhook` / `websocket` → a Vertex AI Extension.
   - `cli` → a Gemini CLI command.
4. Applies `min_permissions` to the code-execution tool sandbox
   (`code_execution` in the Gemini API).
5. Honors `cost_limit_usd_daily` via a daily spend cap scoped to the
   caller's project.

## Supported `kind`s

`ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`.

## Notable fields (`platforms.gemini`)

- `model` — one of the current Gemini models.
- `system_instruction_file` — path to a file whose contents form the
  system instruction.
- `tools[]` — function declarations.
- `grounding` — whether to enable Google Search or Vertex AI Search
  grounding, and the retrieval corpus if any.
- `safety_settings` — per-category harm thresholds.

See [`gemini-spawn.yaml`](./gemini-spawn.yaml) and two complete examples
in [`examples/`](./examples).

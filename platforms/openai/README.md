# OpenAI platform extension

**Id**: `openai`
**Vendor**: OpenAI
**Surfaces**: OpenAI API (Responses, Chat Completions, Assistants,
Realtime), GPT Store entries, OpenAI Apps/Actions.

A conformant OpenAI consumer:

1. Validates the core manifest against
   `spec/v1.0.0/manifest.schema.json`.
2. Validates `platforms.openai` against
   [`schema.extension.json`](./schema.extension.json).
3. Maps `entrypoints[*]` onto OpenAI surfaces:
   - `tool-call` → a `function` tool in the Responses / Chat
     Completions API.
   - `http` / `websocket` → an Action or an Assistants tool.
   - `cli` → an OpenAI CLI command.
4. Applies `min_permissions` to the Code Interpreter sandbox.
5. Honors `cost_limit_usd_daily` via an organization hard limit.

## Notable fields

- `model` — recommended OpenAI model id.
- `tools[]` — function tools.
- `system_prompt_file` — path to the system prompt.
- `assistant` — optional Assistants-API registration block.
- `action` — optional GPT Store action (OpenAPI-backed).
- `response_format` — `text` | `json_object` | `json_schema`.

See [`openai-spawn.yaml`](./openai-spawn.yaml) and two complete examples
in [`examples/`](./examples).

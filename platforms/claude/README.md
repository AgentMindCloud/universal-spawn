# Claude platform extension

**Id**: `claude`
**Vendor**: Anthropic
**Current models**: Opus 4.7 (`claude-opus-4-7`), Sonnet 4.6
(`claude-sonnet-4-6`), Haiku 4.5 (`claude-haiku-4-5-20251001`).

This folder describes how Anthropic's Claude surfaces consume a
universal-spawn manifest.

A conformant Claude consumer (Claude API, Claude Code, Claude.ai
Skills, Claude MCP host) will:

1. Read the **core** manifest and validate it against
   `spec/v1.0.0/manifest.schema.json`.
2. Read `platforms.claude` and validate it against
   [`schema.extension.json`](./schema.extension.json).
3. Map the declared `entrypoints` onto Claude's surfaces:
   - `tool-call` → a tool exposed via the Messages API's `tools`
     parameter.
   - `slash-command` → a Claude Code slash command.
   - `stdio` → an MCP server launched over stdio.
   - `http` / `websocket` → an MCP server reachable over the wire.
4. Enforce `min_permissions` on the tool-calling / code-execution
   sandbox.
5. Enforce `cost_limit_usd_daily` as a hard ceiling at the API key
   scope.

## Supported `kind`s

- `ai-agent`, `ai-skill`, `ai-model` (primary).
- `cli-tool`, `library`, `workflow` — only exposed via tool-calls.

## Required core fields (beyond the schema baseline)

- `min_permissions` MUST be present, even if empty, so the sandbox has
  an envelope.
- At least one `entrypoints[*]` with one of the kinds above.

## Surfaces

The `surface` array inside `platforms.claude` enumerates which Claude
surfaces are allowed to spawn this manifest:

- `claude-api` — the Messages API and the Claude Agent SDK.
- `claude-code` — the CLI tool; also enables slash-command ingestion.
- `claude-app` — the Claude.ai web/mobile app (Skills, Projects).
- `claude-mcp` — any MCP host.

If `surface` is omitted, the platform MUST NOT spawn.

## Tooling

- **Tool-call entrypoints** generate an entry in the `tools` parameter.
  The `function_ref` inside `platforms.claude.tools` points at a JSON
  file that follows the Claude tool-use schema (name, description,
  input_schema).
- **Skills** are declared via `skill_type: skill` with an optional
  `skill_file` path.
- **MCP servers** are declared via `mcp_server` with a transport.

See [`claude-spawn.yaml`](./claude-spawn.yaml) for the full template
and [`examples/`](./examples) for two complete worked manifests.

## Model selection

Set `platforms.claude.model` to the model id you recommend. Consumers
MAY ignore this if the user has a default. When targeting Opus 4.7
specifically, use `claude-opus-4-7`.

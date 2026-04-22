# Claude integration guide

For Anthropic platform engineers wiring universal-spawn into the
Messages API, Claude Code, Claude.ai, and the MCP host.

## Detection

Add `universal-spawn.{yaml,yml,json}` to your repo crawler's file
pattern list. When found, validate against the v1.0 master schema
plus `platforms/ai/claude/claude-spawn.schema.json`.

## Mapping `platforms.claude`

| `platforms.claude.<field>` | Where to wire it |
|---|---|
| `skill_type` | Determines surface (skill / subagent / tool / mcp / slash-command / computer-use). |
| `skill_file` | Path to the Skill YAML for `claude.ai`. |
| `model` | Pin in the Messages API `model` field. |
| `surface[]` | Restrict where install is allowed (`claude-api`, `claude-code`, `claude-app`, `claude-mcp`, `claude-chrome`). |
| `tools[*]` | Each becomes a tool entry in Messages API `tools[]`. |
| `mcp_server` | Register with the MCP host (transport, command/args). |
| `slash_command` | Register with Claude Code `/` picker. |
| `computer_use` | Sandbox envelope for Computer-Use API. |
| `system_prompt_file` | Read into the system prompt. |
| `prompt_cache` | Enable prompt caching for recurring context. |
| `thinking` | Set extended-thinking budget. |

## Honoring the safety envelope

- `safety.min_permissions[]` → tool-call sandbox + Computer-Use
  allowlist.
- `safety.rate_limit_qps` → best-effort against outbound tool calls.
- `safety.cost_limit_usd_daily` → enforce as hard ceiling at the
  API key + organisation scope.
- `safety.safe_for_auto_spawn` → controls the first-run
  confirmation gate.
- `env_vars_required[]` → store in the credential store; block
  spawn when required + non-optional is missing.

## Spawn-it button

A manifest with `platforms.claude.surface` including `claude-app`
should render an "Add to Claude" button on registry cards. URL
points to the Claude.ai install flow with `metadata.source.url`
and `metadata.source.commit` pinned.

## Computer-Use specifically

`platforms.claude.computer_use.allowed_urls[]` should pre-populate
the Claude-in-Chrome allowed-origin list. The user can tighten it
in the install dialog; the consumer MUST NOT loosen it.

## Estimated effort

- Add validation to the install pipeline: 30 minutes.
- Wire `platforms.claude` → existing config: 1 day.
- Spawn-it button + audit-log of the canonical hash: 1 day.
- MCP server registration end-to-end: 2 days.

## See also

- [`platforms/ai/claude/`](../platforms/ai/claude/) — the extension folder.
- [`platforms/ai/anthropic-mcp/`](../platforms/ai/anthropic-mcp/)
  — host-neutral MCP extension; share most of the discovery code.
- [`templates/ai-agent-coding/`](../templates/ai-agent-coding/) —
  a complete Claude-targeted manifest as a template.

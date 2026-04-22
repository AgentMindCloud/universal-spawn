# Claude Code — universal-spawn platform extension

Claude Code is Anthropic's official CLI — it runs under a conversational loop with slash commands, hooks, subagents, and MCP connections. A manifest targeted at Claude Code declares which surfaces the creation uses. This is distinct from `platforms/ai/claude/` (the API surface) — Claude Code is the CLI.

## What this platform cares about

The surface kind (`slash-command`, `subagent`, `hook`, `mcp-server`, `skill`), the file location inside `.claude/`, and the model choice.

## What platform-specific extras unlock

`hook.event` registers a hook on one of the Claude Code hook events (`PreToolUse`, `PostToolUse`, `Stop`, etc.). `subagent.file` points at a subagent definition.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Claude Code behavior |
|---|---|
| `version` | Required. |
| `type` | `cli-tool`, `extension`, `ai-skill`, `ai-agent`. |
| `safety.*` | Informational. |
| `env_vars_required` | Shell env. |
| `platforms.claude-code` | Strict. |

### `platforms.claude-code` fields

| Field | Purpose |
|---|---|
| `platforms.claude-code.kind` | `slash-command`, `subagent`, `hook`, `mcp-server`, `skill`. |
| `platforms.claude-code.file` | Relative path inside `.claude/`. |
| `platforms.claude-code.model` | Claude model (optional pin). |
| `platforms.claude-code.hook` | Hook registration block. |
| `platforms.claude-code.subagent` | Subagent definition block. |
| `platforms.claude-code.mcp_ref` | Cross-link to an MCP server manifest. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

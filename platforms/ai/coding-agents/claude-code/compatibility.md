# Claude Code compatibility — field-by-field

| universal-spawn v1.0 field | Claude Code behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Surfaced in Claude Code's listing commands. |
| `type` | `cli-tool`, `extension`, `ai-skill`, `ai-agent`. |
| `safety.*` | Informational. |
| `env_vars_required` | Shell env. |
| `platforms.claude-code.kind` | `slash-command`, `subagent`, `hook`, `mcp-server`, `skill`. |
| `platforms.claude-code.file` | Relative path inside `.claude/` where the creation installs. |
| `platforms.claude-code.model` | Claude model (when the creation pins one). |
| `platforms.claude-code.hook` | Hook registration (kind+event+matcher). |
| `platforms.claude-code.subagent` | Subagent definition. |
| `platforms.claude-code.mcp_ref` | Cross-link to an MCP server manifest. |

## Relation to `platforms/ai/claude/`

`platforms/ai/claude/` describes how a creation appears to the Claude **API** (Messages API, Skills, Agents SDK). `platforms/ai/coding-agents/claude-code/` describes how a creation appears to the **Claude Code CLI** (slash commands, hooks, subagents, MCP bindings). A creation MAY target both; most target only one.

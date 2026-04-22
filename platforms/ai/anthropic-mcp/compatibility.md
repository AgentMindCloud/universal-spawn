# Anthropic MCP compatibility — field-by-field

| universal-spawn v1.0 field | Anthropic MCP behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key across MCP registries. |
| `name, description` | Card text. |
| `type` | `extension`, `plugin`, `cli-tool`, `library`. |
| `safety.min_permissions` | Enforced by the host. |
| `env_vars_required` | Host credential store. |
| `platforms.anthropic-mcp.transport` | `stdio`, `http`, `websocket`. |
| `platforms.anthropic-mcp.command` | stdio command to launch the server. |
| `platforms.anthropic-mcp.args` | stdio command arguments. |
| `platforms.anthropic-mcp.url` | http/websocket endpoint URL. |
| `platforms.anthropic-mcp.resources` | Declared resources. |
| `platforms.anthropic-mcp.prompts` | Declared prompts. |
| `platforms.anthropic-mcp.tools` | Declared tools. |
| `platforms.anthropic-mcp.hosts` | Compatible host list. |

## Relation to `platforms/ai/claude/`

`platforms.claude.mcp_server` and `platforms.anthropic-mcp` overlap in spirit. The `claude` extension wires an MCP server specifically into Claude. The `anthropic-mcp` extension describes a server that happens to speak MCP, regardless of host. A manifest that ships both describes the same server from two vantage points.


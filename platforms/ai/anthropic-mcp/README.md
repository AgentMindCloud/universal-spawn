# Anthropic MCP — universal-spawn platform extension

MCP (Model Context Protocol) is an open wire protocol for model-to-tool communication. Servers expose resources, prompts, and tools; hosts (Claude Desktop, Claude Code, Cursor, Windsurf, Zed, any future host) connect to them. This extension describes a manifest whose creation IS an MCP server — independent of whether Claude is the host.

## What this platform cares about

The MCP transport (`stdio`, `http`, `websocket`), the command or URL that starts the server, the declared set of resources, prompts, and tools the server exposes.

## What platform-specific extras unlock

`resources[]`, `prompts[]`, `tools[]` list what the server advertises to its host. Purely declarative — the host does discovery at runtime; the manifest lets a registry index the server.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Anthropic MCP behavior |
|---|---|
| `version` | Required. |
| `name, description` | MCP registry card. |
| `type` | `extension`, `plugin`, `cli-tool`, `library`. |
| `safety.min_permissions` | Enforced at the host sandbox boundary. |
| `env_vars_required` | Host credential store. |
| `platforms.anthropic-mcp` | Strict. |

### `platforms.anthropic-mcp` fields

| Field | Purpose |
|---|---|
| `platforms.anthropic-mcp.transport` | MCP transport kind. |
| `platforms.anthropic-mcp.command` | stdio launch command. |
| `platforms.anthropic-mcp.args` | stdio arguments. |
| `platforms.anthropic-mcp.url` | http/websocket endpoint URL. |
| `platforms.anthropic-mcp.resources` | Declared resources. |
| `platforms.anthropic-mcp.prompts` | Declared prompts. |
| `platforms.anthropic-mcp.tools` | Declared tools. |
| `platforms.anthropic-mcp.hosts` | Compatible MCP host list. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

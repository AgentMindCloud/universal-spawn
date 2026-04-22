# Cursor — universal-spawn platform extension

Cursor is a VS Code fork with built-in AI agents (Tab, Chat, Agent, Composer). Creations that target Cursor are either MCP servers it can connect to, rule files (`.cursor/rules/*.mdc`) that shape its behavior in a repo, or extensions delivered via the VS Code Marketplace. This extension covers all three.

## What this platform cares about

The kind (`rules`, `mcp-server`, `extension`), the rule scope, the MCP binding if applicable, and which Cursor features the creation expects (agent, composer, tab).

## What platform-specific extras unlock

`rules.files[]` lists `.mdc` rule files to install under `.cursor/rules/`. `mcp_ref` references an entry in `platforms/ai/anthropic-mcp/`.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Cursor behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `ai-skill`. |
| `safety.*` | Inherited from the underlying provider (Claude, OpenAI, etc.). |
| `env_vars_required` | User-level Cursor settings. |
| `platforms.cursor` | Strict. |

### `platforms.cursor` fields

| Field | Purpose |
|---|---|
| `platforms.cursor.kind` | `rules`, `mcp-server`, or `extension`. |
| `platforms.cursor.rules` | Rule files + scope. |
| `platforms.cursor.mcp_ref` | Cross-link to an MCP server manifest. |
| `platforms.cursor.features` | Cursor features the creation uses (`agent`, `composer`, `tab`, `chat`). |
| `platforms.cursor.min_cursor_version` | Minimum Cursor editor version. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

# Windsurf — universal-spawn platform extension

Windsurf is Codeium's IDE, centered on the Cascade agent and Flows (persistent task contexts). Creations target Windsurf as rules files, MCP servers, or extensions.

## What this platform cares about

The kind (`rules`, `mcp-server`, `extension`), Flow metadata when the creation is a Flow template, and Cascade feature flags.

## What platform-specific extras unlock

`flow.template_file` points at a reusable Flow template. `cascade.auto_memory` pre-enables Cascade's auto-memory.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Windsurf behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `ai-skill`. |
| `safety.*` | Informational. |
| `env_vars_required` | User-level Windsurf settings. |
| `platforms.windsurf` | Strict. |

### `platforms.windsurf` fields

| Field | Purpose |
|---|---|
| `platforms.windsurf.kind` | `rules`, `mcp-server`, `extension`, `flow-template`. |
| `platforms.windsurf.rules` | `.windsurfrules` file + scope. |
| `platforms.windsurf.mcp_ref` | Cross-link to an MCP server manifest. |
| `platforms.windsurf.flow` | Flow template metadata. |
| `platforms.windsurf.cascade` | Cascade feature flags. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

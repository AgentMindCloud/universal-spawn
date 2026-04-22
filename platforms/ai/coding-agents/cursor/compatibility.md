# Cursor compatibility — field-by-field

| universal-spawn v1.0 field | Cursor behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key for extension publication. |
| `name, description` | Marketplace card. |
| `type` | `extension`, `plugin`, `ai-skill`. |
| `safety.*` | Informational. |
| `env_vars_required` | Cursor settings. |
| `platforms.cursor.kind` | `rules`, `mcp-server`, `extension`. |
| `platforms.cursor.rules` | Rule files + scope. |
| `platforms.cursor.mcp_ref` | Relative path into platforms/ai/anthropic-mcp. |
| `platforms.cursor.features` | Cursor features the creation uses. |
| `platforms.cursor.min_cursor_version` | Minimum Cursor editor version. |



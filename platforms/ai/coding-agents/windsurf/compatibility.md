# Windsurf compatibility — field-by-field

| universal-spawn v1.0 field | Windsurf behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Marketplace card. |
| `type` | `extension`, `plugin`, `ai-skill`. |
| `safety.*` | Informational. |
| `env_vars_required` | Windsurf settings. |
| `platforms.windsurf.kind` | `rules`, `mcp-server`, `extension`, `flow-template`. |
| `platforms.windsurf.rules` | `.windsurfrules` path + scope. |
| `platforms.windsurf.mcp_ref` | Cross-link to an MCP server. |
| `platforms.windsurf.flow` | Flow template metadata. |
| `platforms.windsurf.cascade` | Cascade feature flags. |



# Mistral compatibility — field-by-field

| universal-spawn v1.0 field | Mistral behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `metadata.id` | Stable key in the workspace. |
| `name, description` | Agent card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.min_permissions` | Informational. |
| `safety.rate_limit_qps` | Advisory; workspace quotas apply. |
| `safety.cost_limit_usd_daily` | Enforced. |
| `env_vars_required` | Workspace secret store. |
| `platforms.mistral.model` | Mistral model id. |
| `platforms.mistral.tools` | Function tools. |
| `platforms.mistral.agent` | Agents-API registration. |
| `platforms.mistral.json_mode` | Force JSON output. |
| `platforms.mistral.safe_prompt` | Mistral safety prompt toggle. |



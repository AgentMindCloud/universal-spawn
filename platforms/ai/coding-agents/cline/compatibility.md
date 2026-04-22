# Cline compatibility — field-by-field

| universal-spawn v1.0 field | Cline behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Shown in Cline's workspace profile picker. |
| `type` | `extension`, `ai-agent`. |
| `safety.min_permissions` | Mapped to auto_approve_tools. |
| `env_vars_required` | VS Code secret store. |
| `platforms.cline.provider` | Model provider. |
| `platforms.cline.model` | Model id. |
| `platforms.cline.mode` | `plan` or `act`. |
| `platforms.cline.auto_approve_tools` | Tools pre-authorised per turn. |
| `platforms.cline.max_requests_per_task` | Upper bound on per-task requests. |



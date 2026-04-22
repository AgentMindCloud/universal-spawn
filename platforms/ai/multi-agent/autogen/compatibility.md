# AutoGen (Microsoft) compatibility — field-by-field

| universal-spawn v1.0 field | AutoGen (Microsoft) behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Chat metadata. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secret store. |
| `platforms.autogen.pattern` | `round-robin`, `selector`, `swarm`, `nested-chat`. |
| `platforms.autogen.agents` | Typed agent roster. |
| `platforms.autogen.user_proxy` | User-proxy agent config. |
| `platforms.autogen.termination` | Termination condition. |



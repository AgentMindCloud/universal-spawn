# llama.cpp compatibility — field-by-field

| universal-spawn v1.0 field | llama.cpp behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Server card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `library`, `cli-tool`. |
| `safety.*` | Informational. |
| `env_vars_required` | Shell env. |
| `platforms.llamacpp.model_path` | Local GGUF path. |
| `platforms.llamacpp.model_url` | GGUF download URL. |
| `platforms.llamacpp.host` | Server host. |
| `platforms.llamacpp.port` | Server port. |
| `platforms.llamacpp.ngl` | GPU layer count. |
| `platforms.llamacpp.threads` | CPU thread count. |
| `platforms.llamacpp.context_length` | Context window. |
| `platforms.llamacpp.mlock` | Pin model in RAM. |



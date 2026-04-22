# Ollama compatibility — field-by-field

| universal-spawn v1.0 field | Ollama behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Shown in the consumer's Ollama integration. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | Shell env. |
| `platforms.ollama.model` | Ollama model tag. |
| `platforms.ollama.server_url` | Endpoint URL (default `http://localhost:11434`). |
| `platforms.ollama.modelfile` | Path to a custom Modelfile. |
| `platforms.ollama.quantization` | Quantisation tag. |
| `platforms.ollama.keep_alive` | Keep-alive window. |
| `platforms.ollama.pre_pull` | Pre-pull on first spawn. |



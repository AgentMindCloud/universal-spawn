# LM Studio compatibility — field-by-field

| universal-spawn v1.0 field | LM Studio behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Shown in LM Studio's chat preset picker. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | Usually none. |
| `platforms.lm-studio.model` | HF repo slug loaded in LM Studio. |
| `platforms.lm-studio.server_url` | Default `http://localhost:1234/v1`. |
| `platforms.lm-studio.preset_file` | Preset JSON. |
| `platforms.lm-studio.gpu_offload` | GPU offload level. |
| `platforms.lm-studio.context_length` | Context length override. |



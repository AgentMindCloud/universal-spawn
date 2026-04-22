# vLLM compatibility — field-by-field

| universal-spawn v1.0 field | vLLM behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Server card. |
| `type` | `ai-model`, `api-service`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Host env. |
| `platforms.vllm.model` | HF repo slug. |
| `platforms.vllm.host` | Server host. |
| `platforms.vllm.port` | Server port. |
| `platforms.vllm.tensor_parallel_size` | TP degree. |
| `platforms.vllm.pipeline_parallel_size` | PP degree. |
| `platforms.vllm.quantization` | Quant method. |
| `platforms.vllm.kv_cache_dtype` | KV-cache dtype. |
| `platforms.vllm.max_model_len` | Max context length served. |
| `platforms.vllm.enable_prefix_caching` | Prefix cache toggle. |



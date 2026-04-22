# vLLM — universal-spawn platform extension

vLLM is a high-throughput inference server with an OpenAI-compatible API. A manifest targeting vLLM captures the model (an HF repo slug), the tensor-parallel degree, and the KV-cache / quantisation settings that drive the throughput.

## What this platform cares about

The model id, tensor-parallel and pipeline-parallel degrees, the quantisation method, and the KV-cache dtype.

## What platform-specific extras unlock

`enable_prefix_caching` is almost always worth it. `max_model_len` is a hard cap on the context window served.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | vLLM behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-model`, `api-service`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Host env. |
| `platforms.vllm` | Strict. |

### `platforms.vllm` fields

| Field | Purpose |
|---|---|
| `platforms.vllm.model` | HF repo slug. |
| `platforms.vllm.host` | Server host. |
| `platforms.vllm.port` | Server port. |
| `platforms.vllm.tensor_parallel_size` | TP degree. |
| `platforms.vllm.pipeline_parallel_size` | PP degree. |
| `platforms.vllm.quantization` | Quant method (`awq`, `gptq`, `fp8`, `bnb`, `none`). |
| `platforms.vllm.kv_cache_dtype` | KV-cache dtype. |
| `platforms.vllm.max_model_len` | Max context length served. |
| `platforms.vllm.enable_prefix_caching` | Prefix cache toggle. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

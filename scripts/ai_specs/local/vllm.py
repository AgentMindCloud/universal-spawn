"""vLLM — OpenAI-compatible inference server."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "vllm",
    "title": "vLLM",
    "location": "local",
    "lede": (
        "vLLM is a high-throughput inference server with an OpenAI-"
        "compatible API. A manifest targeting vLLM captures the model "
        "(an HF repo slug), the tensor-parallel degree, and the KV-"
        "cache / quantisation settings that drive the throughput."
    ),
    "cares": (
        "The model id, tensor-parallel and pipeline-parallel degrees, "
        "the quantisation method, and the KV-cache dtype."
    ),
    "extras": (
        "`enable_prefix_caching` is almost always worth it. "
        "`max_model_len` is a hard cap on the context window served."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-model`, `api-service`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Host env."),
        ("platforms.vllm", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Server card."),
        ("type", "`ai-model`, `api-service`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Host env."),
        ("platforms.vllm.model", "HF repo slug."),
        ("platforms.vllm.host", "Server host."),
        ("platforms.vllm.port", "Server port."),
        ("platforms.vllm.tensor_parallel_size", "TP degree."),
        ("platforms.vllm.pipeline_parallel_size", "PP degree."),
        ("platforms.vllm.quantization", "Quant method."),
        ("platforms.vllm.kv_cache_dtype", "KV-cache dtype."),
        ("platforms.vllm.max_model_len", "Max context length served."),
        ("platforms.vllm.enable_prefix_caching", "Prefix cache toggle."),
    ],
    "platform_fields": {
        "model": "HF repo slug.",
        "host": "Server host.",
        "port": "Server port.",
        "tensor_parallel_size": "TP degree.",
        "pipeline_parallel_size": "PP degree.",
        "quantization": "Quant method (`awq`, `gptq`, `fp8`, `bnb`, `none`).",
        "kv_cache_dtype": "KV-cache dtype.",
        "max_model_len": "Max context length served.",
        "enable_prefix_caching": "Prefix cache toggle.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": str_prop(pattern=r"^[^/\s]+/[^/\s]+$"),
            "host": str_prop(),
            "port": {"type": "integer", "minimum": 1, "maximum": 65535},
            "tensor_parallel_size": {"type": "integer", "minimum": 1, "maximum": 64},
            "pipeline_parallel_size": {"type": "integer", "minimum": 1, "maximum": 64},
            "quantization": enum(["awq", "gptq", "fp8", "bnb", "none"]),
            "kv_cache_dtype": enum(["auto", "fp8", "fp16", "bf16"]),
            "max_model_len": {"type": "integer", "minimum": 512, "maximum": 1048576},
            "enable_prefix_caching": bool_prop(True),
            "dtype": enum(["auto", "fp16", "bf16", "fp32"]),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: vLLM Template
type: api-service
description: Template for a vLLM-targeted universal-spawn manifest.

platforms:
  vllm:
    model: meta-llama/Llama-3.3-70B-Instruct
    host: 0.0.0.0
    port: 8000
    tensor_parallel_size: 4
    quantization: fp8
    kv_cache_dtype: fp8
    max_model_len: 32768
    enable_prefix_caching: true
    dtype: bf16

safety:
  min_permissions: [network:inbound, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required:
  - name: HF_TOKEN
    description: HuggingFace token for gated model access.
    secret: true

deployment:
  targets: [vllm]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/vllm-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: vLLM Minimal
type: api-service
summary: Minimal vLLM server on one GPU with bf16 Qwen-7B.
description: Single GPU, no tensor parallel, short context. Starter shape.

platforms:
  vllm:
    model: Qwen/Qwen2.5-7B-Instruct
    host: 0.0.0.0
    port: 8000
    tensor_parallel_size: 1
    quantization: none
    kv_cache_dtype: auto
    max_model_len: 8192
    enable_prefix_caching: true
    dtype: bf16

safety:
  min_permissions: [network:inbound, gpu:compute]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [vllm]

metadata:
  license: Apache-2.0
  author: { name: Infra Co., handle: infra-co }
  source: { type: git, url: https://github.com/infra-co/vllm-minimal }
  id: com.infra-co.vllm-minimal
"""},
        {"yaml": """
version: \"1.0\"
name: vLLM 8xA100 Cluster
type: api-service
summary: Full vLLM deployment on an 8xA100 cluster with tensor parallel 8 and FP8 KV cache.
description: >
  Production deployment of Llama-3.3-405B-Instruct-FP8 across 8xA100.
  Tensor parallel 8, FP8 weights, FP8 KV cache, prefix caching on,
  128k context length.

platforms:
  vllm:
    model: meta-llama/Llama-3.3-405B-Instruct-FP8
    host: 0.0.0.0
    port: 8000
    tensor_parallel_size: 8
    pipeline_parallel_size: 1
    quantization: fp8
    kv_cache_dtype: fp8
    max_model_len: 131072
    enable_prefix_caching: true
    dtype: bf16

safety:
  min_permissions: [network:inbound, network:outbound:huggingface.co, gpu:compute, fs:read, fs:write]
  safe_for_auto_spawn: false
  data_residency: [us]

env_vars_required:
  - name: HF_TOKEN
    description: HuggingFace token with access to the gated model.
    secret: true

deployment:
  targets: [vllm]

metadata:
  license: proprietary
  author: { name: Infra Team, handle: infra-team, org: Acme }
  source: { type: git, url: https://github.com/acme-infra/vllm-405b }
  id: com.acme-infra.vllm-405b
"""},
        {"yaml": """
version: \"1.0\"
name: vLLM Edge Embedder
type: api-service
summary: Creative vLLM deployment serving only embeddings on a T4 edge box.
description: >
  Serves a sentence-transformer embeddings model on a single T4 via
  vLLM. Max model length 512 tokens, no prefix cache, FP16.

platforms:
  vllm:
    model: sentence-transformers/all-mpnet-base-v2
    host: 0.0.0.0
    port: 8000
    tensor_parallel_size: 1
    quantization: none
    kv_cache_dtype: fp16
    max_model_len: 512
    enable_prefix_caching: false
    dtype: fp16

safety:
  min_permissions: [network:inbound, gpu:compute]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [vllm]

metadata:
  license: Apache-2.0
  author: { name: Edge Team, handle: edge-team }
  source: { type: git, url: https://github.com/edge-team/vllm-embedder }
  categories: [ai, hardware]
  id: com.edge-team.vllm-embedder
"""},
    ],
}

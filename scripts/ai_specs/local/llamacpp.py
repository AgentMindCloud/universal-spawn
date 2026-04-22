"""llama.cpp — library + llama-server CLI."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "llamacpp",
    "title": "llama.cpp",
    "location": "local",
    "lede": (
        "llama.cpp is the reference C/C++ inference library for GGUF "
        "models, shipping both a library and a `llama-server` CLI "
        "that exposes OpenAI-compatible endpoints. A manifest targets "
        "`llama-server` directly."
    ),
    "cares": (
        "The GGUF model path (or download URL), the server host/port, "
        "GPU offload flags, and the context length."
    ),
    "extras": (
        "`ngl` sets `--n-gpu-layers`. `threads` sets `--threads`. "
        "`mlock` pins the model in RAM."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `library`, `cli-tool`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Shell env."),
        ("platforms.llamacpp", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Server card."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `library`, `cli-tool`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Shell env."),
        ("platforms.llamacpp.model_path", "Local GGUF path."),
        ("platforms.llamacpp.model_url", "GGUF download URL."),
        ("platforms.llamacpp.host", "Server host."),
        ("platforms.llamacpp.port", "Server port."),
        ("platforms.llamacpp.ngl", "GPU layer count."),
        ("platforms.llamacpp.threads", "CPU thread count."),
        ("platforms.llamacpp.context_length", "Context window."),
        ("platforms.llamacpp.mlock", "Pin model in RAM."),
    ],
    "platform_fields": {
        "model_path": "Local GGUF path.",
        "model_url": "GGUF download URL (alternative to `model_path`).",
        "host": "Server host.",
        "port": "Server port.",
        "ngl": "`--n-gpu-layers` value.",
        "threads": "`--threads` value.",
        "context_length": "`--ctx-size` value.",
        "mlock": "`--mlock` flag.",
    },
    "schema_body": schema_object(
        properties={
            "model_path": str_prop(),
            "model_url": str_prop(pattern=r"^https?://"),
            "host": str_prop(),
            "port": {"type": "integer", "minimum": 1, "maximum": 65535},
            "ngl": {"type": "integer", "minimum": 0, "maximum": 999},
            "threads": {"type": "integer", "minimum": 1, "maximum": 256},
            "context_length": {"type": "integer", "minimum": 512, "maximum": 1048576},
            "mlock": bool_prop(False),
            "batch_size": {"type": "integer", "minimum": 1, "maximum": 8192},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: llama.cpp Template
type: ai-model
description: Template for a llama.cpp-server-targeted universal-spawn manifest.

platforms:
  llamacpp:
    model_path: /srv/models/llama-3.3-70b-q5_k_m.gguf
    host: 0.0.0.0
    port: 8080
    ngl: 99
    threads: 16
    context_length: 8192
    mlock: true
    batch_size: 512

safety:
  min_permissions: [network:inbound, fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [llamacpp]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/llamacpp-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: llama-server Local
type: ai-model
summary: Minimal llama.cpp server binding one GGUF file at localhost:8080.
description: One model, CPU only, small context window.

platforms:
  llamacpp:
    model_path: ./models/qwen2.5-7b-instruct-q5_k_m.gguf
    host: 127.0.0.1
    port: 8080
    ngl: 0
    threads: 8
    context_length: 4096

safety:
  min_permissions: [network:inbound, fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [llamacpp]

metadata:
  license: Apache-2.0
  author: { name: Local Co., handle: local-co }
  source: { type: git, url: https://github.com/local-co/llama-server-local }
  id: com.local-co.llama-server-local
"""},
        {"yaml": """
version: \"1.0\"
name: llama-server GPU Host
type: ai-model
summary: Full llama.cpp server on a GPU host with remote downloads, mlock, and big context.
description: >
  Downloads a 70B model on first spawn. Pins it in RAM. Offloads all
  layers to GPU. Exposes a 32k context server on port 8080.

platforms:
  llamacpp:
    model_url: https://huggingface.co/lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q5_K_M.gguf
    host: 0.0.0.0
    port: 8080
    ngl: 99
    threads: 24
    context_length: 32768
    mlock: true
    batch_size: 1024

safety:
  min_permissions: [network:inbound, network:outbound:huggingface.co, fs:read, fs:write, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [llamacpp]

metadata:
  license: Apache-2.0
  author: { name: GPU Host Co., handle: gpu-host-co }
  source: { type: git, url: https://github.com/gpu-host-co/llama-server-gpu }
  id: com.gpu-host-co.llama-server-gpu
"""},
        {"yaml": """
version: \"1.0\"
name: llama-server Raspberry Pi
type: ai-model
summary: Creative llama.cpp manifest for a tiny on-device Pi 5 deployment.
description: >
  Runs a 3B model on a Raspberry Pi 5. CPU only, aggressively small
  context to fit in 8GB. Serves locally; no outbound network.

platforms:
  llamacpp:
    model_path: /home/pi/models/llama-3.2-3b-q4_k_m.gguf
    host: 127.0.0.1
    port: 8080
    ngl: 0
    threads: 4
    context_length: 2048
    mlock: false
    batch_size: 128

safety:
  min_permissions: [network:inbound, fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [llamacpp]

metadata:
  license: Apache-2.0
  author: { name: Pi Co., handle: pi-co }
  source: { type: git, url: https://github.com/pi-co/llama-server-pi5 }
  categories: [ai, hardware]
  id: com.pi-co.llama-server-pi5
"""},
    ],
}

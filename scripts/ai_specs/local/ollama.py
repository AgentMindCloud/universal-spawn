"""Ollama — local model daemon."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "ollama",
    "title": "Ollama",
    "location": "local",
    "lede": (
        "Ollama runs open models as a local daemon exposing an "
        "OpenAI-compatible API at `http://localhost:11434`. A manifest "
        "that targets Ollama pins the model tag (which becomes a "
        "`Modelfile` pull on first spawn) and the quantisation."
    ),
    "cares": (
        "The model tag (`llama3.3`, `qwen2.5-coder:7b`, `gemma3:27b`), "
        "the server URL (default `localhost:11434`), and whether the "
        "consumer should pre-pull the model."
    ),
    "extras": (
        "`modelfile` points at a custom `Modelfile` the consumer should "
        "`ollama create` from. `keep_alive` tunes how long Ollama keeps "
        "the model resident in VRAM."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`."),
        ("safety.*", "Informational; Ollama does not sandbox."),
        ("env_vars_required", "Shell env."),
        ("platforms.ollama", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Shown in the consumer's Ollama integration."),
        ("type", "`ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Shell env."),
        ("platforms.ollama.model", "Ollama model tag."),
        ("platforms.ollama.server_url", "Endpoint URL (default `http://localhost:11434`)."),
        ("platforms.ollama.modelfile", "Path to a custom Modelfile."),
        ("platforms.ollama.quantization", "Quantisation tag."),
        ("platforms.ollama.keep_alive", "Keep-alive window."),
        ("platforms.ollama.pre_pull", "Pre-pull on first spawn."),
    ],
    "platform_fields": {
        "model": "Ollama model tag.",
        "server_url": "Endpoint URL.",
        "modelfile": "Path to a custom Modelfile.",
        "quantization": "Quantisation tag (`Q4_K_M`, `Q5_K_M`, `Q8_0`, `fp16`).",
        "keep_alive": "Keep-alive window (e.g. `5m`, `-1`).",
        "pre_pull": "Pre-pull the model on first spawn.",
    },
    "schema_body": schema_object(
        required=["model"],
        properties={
            "model": str_prop(pattern=r"^[a-zA-Z0-9][a-zA-Z0-9._-]*(:[a-zA-Z0-9._-]+)?$"),
            "server_url": str_prop(pattern=r"^https?://[A-Za-z0-9._:/-]+$"),
            "modelfile": str_prop(),
            "quantization": enum(["Q4_K_M", "Q5_K_M", "Q5_K_S", "Q6_K", "Q8_0", "fp16", "bf16"]),
            "keep_alive": str_prop(pattern=r"^-1$|^[0-9]+(s|m|h)$"),
            "pre_pull": bool_prop(True),
            "num_ctx": {"type": "integer", "minimum": 512, "maximum": 1048576},
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Ollama Template
type: ai-agent
description: Template for an Ollama-targeted universal-spawn manifest.

platforms:
  ollama:
    model: llama3.3
    server_url: http://localhost:11434
    quantization: Q5_K_M
    keep_alive: 5m
    pre_pull: true
    num_ctx: 8192
    temperature: 0.2

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [ollama]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/ollama-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Ollama Local Chat
type: ai-agent
summary: Minimal Ollama chat on llama3.3 at default localhost URL.
description: Single-model chat, Q5_K_M quant, 5-minute keep-alive.

platforms:
  ollama:
    model: llama3.3
    quantization: Q5_K_M
    keep_alive: 5m
    pre_pull: true
    num_ctx: 8192

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [ollama]

metadata:
  license: Apache-2.0
  author: { name: Local Co., handle: local-co }
  source: { type: git, url: https://github.com/local-co/ollama-chat }
  id: com.local-co.ollama-chat
"""},
        {"yaml": """
version: \"1.0\"
name: Ollama Custom Modelfile
type: ai-skill
summary: Full Ollama manifest that builds a custom parchment-tuned Modelfile.
description: >
  Builds a custom Ollama model from a local Modelfile that sets the
  system prompt to enforce Residual Frequencies voice. Keeps the
  model resident indefinitely.

platforms:
  ollama:
    model: parchment-llama:latest
    modelfile: Modelfile
    quantization: Q5_K_M
    keep_alive: \"-1\"
    pre_pull: false
    num_ctx: 16384
    temperature: 0.7

safety:
  min_permissions: [network:outbound:localhost, fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [ollama]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/ollama-parchment }
  id: com.plate-studio.ollama-parchment
"""},
        {"yaml": """
version: \"1.0\"
name: Ollama GPU Workstation
type: ai-agent
summary: Creative manifest that targets an Ollama daemon on a GPU workstation at a fixed LAN IP.
description: >
  Targets a shared Ollama server at `ollama.lan:11434`. Runs
  qwen2.5-coder:32b at bf16 quantisation for coding tasks. Consumers
  on the LAN share the same resident model.

platforms:
  ollama:
    model: qwen2.5-coder:32b
    server_url: http://ollama.lan:11434
    quantization: bf16
    keep_alive: 1h
    pre_pull: true
    num_ctx: 32768

safety:
  min_permissions: [network:outbound:ollama.lan]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [ollama]

metadata:
  license: Apache-2.0
  author: { name: Workstation Team, handle: workstation-team }
  source: { type: git, url: https://github.com/workstation-team/ollama-shared }
  id: com.workstation-team.ollama-shared
"""},
    ],
}

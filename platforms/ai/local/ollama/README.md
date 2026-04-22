# Ollama — universal-spawn platform extension

Ollama runs open models as a local daemon exposing an OpenAI-compatible API at `http://localhost:11434`. A manifest that targets Ollama pins the model tag (which becomes a `Modelfile` pull on first spawn) and the quantisation.

## What this platform cares about

The model tag (`llama3.3`, `qwen2.5-coder:7b`, `gemma3:27b`), the server URL (default `localhost:11434`), and whether the consumer should pre-pull the model.

## What platform-specific extras unlock

`modelfile` points at a custom `Modelfile` the consumer should `ollama create` from. `keep_alive` tunes how long Ollama keeps the model resident in VRAM.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Ollama behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`. |
| `safety.*` | Informational; Ollama does not sandbox. |
| `env_vars_required` | Shell env. |
| `platforms.ollama` | Strict. |

### `platforms.ollama` fields

| Field | Purpose |
|---|---|
| `platforms.ollama.model` | Ollama model tag. |
| `platforms.ollama.server_url` | Endpoint URL. |
| `platforms.ollama.modelfile` | Path to a custom Modelfile. |
| `platforms.ollama.quantization` | Quantisation tag (`Q4_K_M`, `Q5_K_M`, `Q8_0`, `fp16`). |
| `platforms.ollama.keep_alive` | Keep-alive window (e.g. `5m`, `-1`). |
| `platforms.ollama.pre_pull` | Pre-pull the model on first spawn. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

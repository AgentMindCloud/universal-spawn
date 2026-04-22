# llama.cpp — universal-spawn platform extension

llama.cpp is the reference C/C++ inference library for GGUF models, shipping both a library and a `llama-server` CLI that exposes OpenAI-compatible endpoints. A manifest targets `llama-server` directly.

## What this platform cares about

The GGUF model path (or download URL), the server host/port, GPU offload flags, and the context length.

## What platform-specific extras unlock

`ngl` sets `--n-gpu-layers`. `threads` sets `--threads`. `mlock` pins the model in RAM.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | llama.cpp behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `library`, `cli-tool`. |
| `safety.*` | Informational. |
| `env_vars_required` | Shell env. |
| `platforms.llamacpp` | Strict. |

### `platforms.llamacpp` fields

| Field | Purpose |
|---|---|
| `platforms.llamacpp.model_path` | Local GGUF path. |
| `platforms.llamacpp.model_url` | GGUF download URL (alternative to `model_path`). |
| `platforms.llamacpp.host` | Server host. |
| `platforms.llamacpp.port` | Server port. |
| `platforms.llamacpp.ngl` | `--n-gpu-layers` value. |
| `platforms.llamacpp.threads` | `--threads` value. |
| `platforms.llamacpp.context_length` | `--ctx-size` value. |
| `platforms.llamacpp.mlock` | `--mlock` flag. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

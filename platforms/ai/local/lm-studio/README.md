# LM Studio — universal-spawn platform extension

LM Studio is a desktop app with a built-in model library and a local HTTP server at `http://localhost:1234/v1`. A manifest targets LM Studio's server surface (OpenAI-compatible) plus the desktop-specific preset metadata.

## What this platform cares about

The model id (a huggingface repo slug once loaded in LM Studio), the preset file that captures inference settings, and whether GPU offload is engaged.

## What platform-specific extras unlock

`preset_file` points at an LM Studio preset JSON. `gpu_offload` is `max`, `auto`, or an integer layer count.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | LM Studio behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`, `library`. |
| `safety.*` | Informational. |
| `env_vars_required` | Usually none — LM Studio runs locally. |
| `platforms.lm-studio` | Strict. |

### `platforms.lm-studio` fields

| Field | Purpose |
|---|---|
| `platforms.lm-studio.model` | HF repo slug. |
| `platforms.lm-studio.server_url` | LM Studio server URL. |
| `platforms.lm-studio.preset_file` | Preset JSON. |
| `platforms.lm-studio.gpu_offload` | `max`, `auto`, or layer count. |
| `platforms.lm-studio.context_length` | Context length override. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

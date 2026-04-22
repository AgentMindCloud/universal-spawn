# Together AI — universal-spawn platform extension

Together AI hosts hundreds of open-weight models (Llama, Qwen, DeepSeek, Mixtral, FLUX) behind a single OpenAI-compatible endpoint plus dedicated endpoints for fine-tuning and image generation. This extension targets the Chat + Images + Embeddings surfaces.

## What this platform cares about

The model id (the exact Together catalogue string), which surface is being called (chat, images, embeddings), and whether JSON mode is engaged.

## What platform-specific extras unlock

`surface` selects the endpoint family. `image.size` and `image.steps` control the image-generation request shape.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Together AI behavior |
|---|---|
| `version` | Required. |
| `name, description` | Dashboard card text. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.cost_limit_usd_daily` | Enforced at the workspace budget level. |
| `env_vars_required` | Together secret store. |
| `platforms.together-ai` | Strict. |

### `platforms.together-ai` fields

| Field | Purpose |
|---|---|
| `platforms.together-ai.model` | Together catalogue model id. |
| `platforms.together-ai.surface` | `chat`, `images`, or `embeddings`. |
| `platforms.together-ai.tools` | Function tools (chat surface only). |
| `platforms.together-ai.response_format` | `text` or `json_object`. |
| `platforms.together-ai.image` | Image-generation parameters (size, steps, guidance_scale). |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

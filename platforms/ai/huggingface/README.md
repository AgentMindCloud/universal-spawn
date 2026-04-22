# Hugging Face — universal-spawn platform extension

Hugging Face is three surfaces in one: Model repositories, Dataset repositories, and Spaces (Gradio, Streamlit, Docker, static). This extension covers all three, plus Inference Endpoints deployment.

## What this platform cares about

`repo_kind` (model / dataset / space), visibility, the card README, and — for Spaces — the SDK and hardware tier.

## What platform-specific extras unlock

`inference.endpoints[]` describes Inference Endpoints deployments. `base_model` links a finetune to its origin.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Hugging Face behavior |
|---|---|
| `version` | Required. |
| `license` | Required by HF for publication. |
| `name, description` | Repo card. |
| `type` | Mapped to `repo_kind`. |
| `safety.*` | Informational. |
| `env_vars_required` | HF Space secrets. |
| `platforms.huggingface` | Strict. |

### `platforms.huggingface` fields

| Field | Purpose |
|---|---|
| `platforms.huggingface.repo_kind` | `model`, `dataset`, or `space`. |
| `platforms.huggingface.visibility` | `public` or `private`. |
| `platforms.huggingface.card_file` | Repo card README path. |
| `platforms.huggingface.tags` | HF-specific tags. |
| `platforms.huggingface.space_sdk` | Space SDK (`docker`, `gradio`, `streamlit`, `static`). |
| `platforms.huggingface.hardware` | Space hardware tier. |
| `platforms.huggingface.inference` | Inference Endpoints deployment block. |
| `platforms.huggingface.base_model` | Base model HF repo id (for finetunes). |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

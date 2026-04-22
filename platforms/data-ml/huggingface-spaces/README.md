# Hugging Face Spaces — universal-spawn platform extension

HF Spaces hosts notebook-style demos in four flavors: Gradio, Streamlit, Docker, or static. A universal-spawn manifest declares the SDK + hardware tier + visibility + the README-frontmatter fields HF reads.

## What this platform cares about

The space SDK, hardware tier, visibility, and the README front-matter fields (`title`, `emoji`, `colorFrom`, `colorTo`, `pinned`).

## Compatibility table

| Manifest field | Hugging Face Spaces behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `notebook`, `creative-tool`. |
| `platforms.huggingface-spaces` | Strict. |

### `platforms.huggingface-spaces` fields

| Field | Purpose |
|---|---|
| `platforms.huggingface-spaces.sdk` | `gradio`, `streamlit`, `docker`, `static`. |
| `platforms.huggingface-spaces.hardware` | Hardware tier. |
| `platforms.huggingface-spaces.visibility` | `public` or `private`. |
| `platforms.huggingface-spaces.front_matter` | README front-matter (title, emoji, colorFrom/To, pinned). |

See [`compatibility.md`](./compatibility.md) for more.

## See also

Complementary to `../../ai/huggingface/` (models + datasets). A creation that ships a model AND a Space targets both.

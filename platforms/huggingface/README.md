# Hugging Face platform extension

**Id**: `huggingface`
**Vendor**: Hugging Face
**Surfaces**: Model repositories, Dataset repositories, Spaces.

A conformant Hugging Face consumer:

1. Validates core + extension.
2. Provisions a repository of the declared `repo_kind` (model /
   dataset / space) and pushes the creation's files.
3. Uses `license` as the publication gate — a repository cannot be
   published without a license.
4. Honors `card_file` when building the model / dataset / space card.

## Notable fields

- `repo_kind` — `model`, `dataset`, or `space`.
- `visibility` — `public` or `private`.
- `card_file` — relative path to the README used as the repository
  card.
- `space_sdk` — when `repo_kind` is `space`: `docker`, `gradio`,
  `streamlit`, or `static`.
- `hardware` — when hosting a Space: `cpu-basic`, `cpu-upgrade`,
  `t4-small`, `a10g-small`, …
- `tags[]` — HF-specific tags surfaced on the repo card.
- `inference` — optional Inference Endpoints / Inference API settings.

See [`huggingface-spawn.yaml`](./huggingface-spawn.yaml) and
[`examples/`](./examples).

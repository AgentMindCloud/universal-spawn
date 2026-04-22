# Hugging Face compatibility — field-by-field

| universal-spawn v1.0 field | Hugging Face behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `metadata.license` | Required for HF publication. |
| `name, description` | Repo card header. |
| `type` | `ai-model` → model; `dataset` → dataset; `web-app`/`notebook`/`creative-tool` → space. |
| `safety.*` | Informational. |
| `env_vars_required` | Space secrets. |
| `platforms.huggingface.repo_kind` | `model`, `dataset`, `space`. |
| `platforms.huggingface.visibility` | `public`, `private`. |
| `platforms.huggingface.card_file` | Repo card README path. |
| `platforms.huggingface.tags` | HF-specific tags. |
| `platforms.huggingface.space_sdk` | Space SDK (when `repo_kind: space`). |
| `platforms.huggingface.hardware` | Space hardware tier. |
| `platforms.huggingface.inference` | Inference Endpoints deployment. |
| `platforms.huggingface.base_model` | Base model id (for finetunes). |



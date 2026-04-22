# Kaggle — universal-spawn platform extension

Kaggle hosts notebooks ('kernels') and datasets. A universal-spawn manifest declares the kernel id, the source language, the GPU class, the input datasets, and the competition link if any.

## What this platform cares about

The kernel slug, language, GPU/Internet enablement, the input datasets, and the competition link.

## Compatibility table

| Manifest field | Kaggle behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `dataset`, `workflow`. |
| `platforms.kaggle` | Strict. |

### `platforms.kaggle` fields

| Field | Purpose |
|---|---|
| `platforms.kaggle.kind` | `notebook` or `dataset`. |
| `platforms.kaggle.slug` | Kaggle slug. |
| `platforms.kaggle.language` | Notebook language. |
| `platforms.kaggle.kernel_type` | `notebook` or `script`. |
| `platforms.kaggle.enable_gpu` | GPU toggle. |
| `platforms.kaggle.enable_internet` | Internet toggle. |
| `platforms.kaggle.dataset_sources` | Input datasets. |
| `platforms.kaggle.competition` | Competition slug. |

See [`compatibility.md`](./compatibility.md) for more.

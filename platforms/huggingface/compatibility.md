# Hugging Face — compatibility notes

| Field                  | Behavior on Hugging Face                                                |
|------------------------|--------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                        |
| `id`                   | Used as the HF repo id suggestion; the user may rename to `<org>/<repo>`.|
| `name`, `description`  | Used in the repo card header.                                           |
| `kind`                 | Maps to `repo_kind`: `ai-model` → `model`, `dataset` → `dataset`, `notebook`/`web-app` → `space`. |
| `license`              | Required. HF refuses publication without a license.                     |
| `author`, `source`     | Required. `source.url` links back to the canonical repo.                |
| `runtime`              | `gpu_required` and `memory_mb_min` inform default hardware selection.   |
| `entrypoints`          | Informational for Spaces; each HTTP entrypoint becomes a documented API.|
| `env_vars_required`    | Surfaced as HF Space secrets.                                           |
| `min_permissions`      | Informational.                                                          |
| `rate_limit_qps`       | Ignored.                                                                |
| `cost_limit_usd_daily` | Ignored.                                                                |
| `safe_for_auto_spawn`  | Gates Space auto-deploy on push.                                        |
| `data_residency`       | Informational.                                                          |
| `compat.dockerfile`    | Used automatically when `space_sdk: docker`.                            |
| `signatures`           | Verified when present; advisory in v1.0.0.                              |

## Kind → repo_kind

- `ai-model` → `model`.
- `dataset` → `dataset`.
- `web-app`, `notebook`, `creative-tool` → `space`.
- Other kinds are rejected.

## Spaces hardware selection

When `runtime.gpu_required` is true and `hardware` is unset, the HF
consumer SHOULD suggest `t4-small` or better. When false, it defaults
to `cpu-basic`.

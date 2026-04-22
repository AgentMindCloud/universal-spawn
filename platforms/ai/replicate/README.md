# Replicate — universal-spawn platform extension

Replicate hosts models behind a pinned-version URL. Every request is `POST /predictions` with the model's declared input schema. This extension models that shape: each manifest pins one model + version + input-schema.

## What this platform cares about

The model slug (`stability-ai/sdxl`), the version hash, and the path to the input-schema JSON that Replicate generates for each model.

## What platform-specific extras unlock

`hardware` pins a GPU class when the model supports it; `webhook_ref` points to a relative spec file describing the completion webhook.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Replicate behavior |
|---|---|
| `version` | Required. |
| `name, description` | Replicate model card. |
| `type` | `ai-model`, `ai-skill`, `creative-tool`. |
| `safety.cost_limit_usd_daily` | Advisory; Replicate bills per-prediction. |
| `env_vars_required` | Replicate secret store. |
| `platforms.replicate` | Strict. |

### `platforms.replicate` fields

| Field | Purpose |
|---|---|
| `platforms.replicate.model` | Replicate model slug (`owner/name`). |
| `platforms.replicate.version` | Model version hash (64 hex chars). |
| `platforms.replicate.input_schema_ref` | Relative path to the Replicate-generated input schema. |
| `platforms.replicate.hardware` | GPU class hint (`cpu`, `t4`, `a40`, `a100-80gb`). |
| `platforms.replicate.webhook_ref` | Relative path to the completion webhook spec. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

# Replicate (data-ml) — universal-spawn platform extension

This is the data-ml view of Replicate — a thin extension covering training and notebook ergonomics. The inference side (`model`, `version`, `input_schema_ref`) lives in `../../ai/replicate/`; ship both when a creation does both.

## What this platform cares about

The Cog file path, training config, the notebook link, and the bundled dataset slug.

## Compatibility table

| Manifest field | Replicate (data-ml) behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `notebook`, `library`. |
| `platforms.replicate` | Strict. |

### `platforms.replicate` fields

| Field | Purpose |
|---|---|
| `platforms.replicate.cog_file` | cog.yaml path. |
| `platforms.replicate.training` | Training config block. |
| `platforms.replicate.notebook_url` | Companion notebook URL. |
| `platforms.replicate.dataset_slug` | Bundled dataset slug. |

See [`compatibility.md`](./compatibility.md) for more.

## See also

Inference + version pinning live at [`../../ai/replicate/`](../../ai/replicate/). A single creation typically declares both `platforms.replicate` blocks — one in each subtree.

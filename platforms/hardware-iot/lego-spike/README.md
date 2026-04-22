# LEGO SPIKE — universal-spawn platform extension

LEGO Education's SPIKE App exports projects you can re-import. A universal-spawn manifest pins the SPIKE generation, language (icon-blocks vs Python), and the exported project.

## What this platform cares about

The SPIKE generation (Prime/Essential, App 3.x), the language, and the exported project file.

## Compatibility table

| Manifest field | LEGO SPIKE behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `cli-tool`, `library`. |
| `platforms.lego-spike` | Strict. |

### `platforms.lego-spike` fields

| Field | Purpose |
|---|---|
| `platforms.lego-spike.generation` | `spike-prime` or `spike-essential`. |
| `platforms.lego-spike.language` | `icon-blocks` or `python`. |
| `platforms.lego-spike.entry_file` | Exported project file. |
| `platforms.lego-spike.app_version` | Min SPIKE App version. |

See [`compatibility.md`](./compatibility.md) for more.

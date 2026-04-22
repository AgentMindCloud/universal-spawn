# Houdini — universal-spawn platform extension

SideFX Houdini packages reusable nodes as Houdini Digital Assets (HDAs), saves projects as .hip files, and ships toolbars as Python shelves. A universal-spawn manifest picks the `kind` and points at the entry artifact.

## What this platform cares about

The `kind` (`hda`, `hip`, `shelf`), the Houdini build version, the context (`sop`, `dop`, `cop2`, `obj`), and the entry file.

## Compatibility table

| Manifest field | Houdini behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `plugin`, `design-template`. |
| `platforms.houdini` | Strict. |

### `platforms.houdini` fields

| Field | Purpose |
|---|---|
| `platforms.houdini.kind` | `hda`, `hip`, or `shelf`. |
| `platforms.houdini.min_build` | Minimum Houdini build. |
| `platforms.houdini.context` | Network context. |
| `platforms.houdini.entry_file` | Entry file. |

See [`compatibility.md`](./compatibility.md) for more.

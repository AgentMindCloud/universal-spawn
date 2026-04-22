# Godot — universal-spawn platform extension

Godot ships projects (project.godot) and addons (Asset Library). A universal-spawn manifest picks one with `kind` and pins the engine series + renderer.

## What this platform cares about

The `kind` (`addon`, `project`), engine series (3 or 4), and renderer (`forward+`, `mobile`, `compatibility`).

## Compatibility table

| Manifest field | Godot behavior |
|---|---|
| `version` | Required. |
| `type` | `game-mod`, `game-world`, `extension`. |
| `platforms.godot` | Strict. |

### `platforms.godot` fields

| Field | Purpose |
|---|---|
| `platforms.godot.kind` | `addon` or `project`. |
| `platforms.godot.engine_series` | Engine series. |
| `platforms.godot.renderer` | Renderer. |
| `platforms.godot.entry_scene` | Entry scene path. |

See [`compatibility.md`](./compatibility.md) for more.

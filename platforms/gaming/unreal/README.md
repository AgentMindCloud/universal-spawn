# Unreal Engine — universal-spawn platform extension

Unreal Engine has Marketplace plugins (`.uplugin`) and full project templates (`.uproject`). A universal-spawn manifest picks one with `kind` and pins the engine version + target platforms.

## What this platform cares about

The `kind` (`marketplace-plugin`, `project-template`), the engine version, target platforms, and Marketplace category.

## Compatibility table

| Manifest field | Unreal Engine behavior |
|---|---|
| `version` | Required. |
| `type` | `game-mod`, `game-world`, `creative-tool`, `extension`. |
| `platforms.unreal` | Strict. |

### `platforms.unreal` fields

| Field | Purpose |
|---|---|
| `platforms.unreal.kind` | `marketplace-plugin` or `project-template`. |
| `platforms.unreal.engine_version` | Engine version. |
| `platforms.unreal.target_platforms` | Target build platforms. |
| `platforms.unreal.marketplace_category` | Marketplace category. |
| `platforms.unreal.entry_uproject` | Entry .uproject file. |

See [`compatibility.md`](./compatibility.md) for more.

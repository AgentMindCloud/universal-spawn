# Fortnite UEFN — universal-spawn platform extension

UEFN (Unreal Editor for Fortnite) ships published islands into Fortnite via the Discover system. A universal-spawn manifest pins the island code, the UEFN project file, and the Verse module.

## What this platform cares about

The island code, the .uefnproject file, the Verse main module, and the discover category.

## Compatibility table

| Manifest field | Fortnite UEFN behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`. |
| `platforms.fortnite-uefn` | Strict. |

### `platforms.fortnite-uefn` fields

| Field | Purpose |
|---|---|
| `platforms.fortnite-uefn.island_code` | Island code. |
| `platforms.fortnite-uefn.uefnproject` | UEFN project file. |
| `platforms.fortnite-uefn.verse_main` | Verse main module. |
| `platforms.fortnite-uefn.discover_category` | Discover category. |

See [`compatibility.md`](./compatibility.md) for more.

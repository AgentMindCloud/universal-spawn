# Minecraft — universal-spawn platform extension

Minecraft creations split cleanly into datapacks (data-only, vanilla-compatible) and mods (Java code via Fabric / Forge / NeoForge). A universal-spawn manifest forces exactly one via `kind` and pins the Minecraft version + loader + distribution platform.

## What this platform cares about

The `kind` (`datapack` or `mod`), the Minecraft version, the mod loader (mods only), and the distribution platform (CurseForge / Modrinth).

## Compatibility table

| Manifest field | Minecraft behavior |
|---|---|
| `version` | Required. |
| `type` | `game-mod`, `game-world`. |
| `platforms.minecraft` | Strict. |

### `platforms.minecraft` fields

| Field | Purpose |
|---|---|
| `platforms.minecraft.kind` | `datapack` or `mod`. |
| `platforms.minecraft.minecraft_version` | Minecraft version range. |
| `platforms.minecraft.loader` | Mod loader (mods only). |
| `platforms.minecraft.pack_format` | Datapack pack_format. |
| `platforms.minecraft.distribution` | Distribution platform. |
| `platforms.minecraft.curseforge_id` | CurseForge project id. |
| `platforms.minecraft.modrinth_id` | Modrinth project id. |

See [`compatibility.md`](./compatibility.md) for more.

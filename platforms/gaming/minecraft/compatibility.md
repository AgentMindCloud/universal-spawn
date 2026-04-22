# Minecraft compatibility — field-by-field

| universal-spawn v1.0 field | Minecraft behavior |
|---|---|
| `version` | Required. |
| `platforms.minecraft.kind` | `datapack` or `mod`. |
| `platforms.minecraft.minecraft_version` | Minecraft version range. |
| `platforms.minecraft.loader` | Mod loader (mods only). |
| `platforms.minecraft.pack_format` | Datapack pack_format integer. |
| `platforms.minecraft.distribution` | `curseforge`, `modrinth`, `both`. |
| `platforms.minecraft.curseforge_id` | CurseForge project id. |
| `platforms.minecraft.modrinth_id` | Modrinth project id. |

## Coexistence with `pack.mcmeta (datapack) / fabric.mod.json / mods.toml (mod)`

universal-spawn does NOT replace pack.mcmeta (datapack) / fabric.mod.json / mods.toml (mod). Both files coexist; consumers read both and warn on conflicts.

### `pack.mcmeta (datapack) / fabric.mod.json / mods.toml (mod)` (provider-native)

```json
{
  "pack": {
    "pack_format": 48,
    "description": "Your datapack"
  }
}
```

### `universal-spawn.yaml` (platforms.minecraft block)

```yaml
platforms:
  minecraft:
    kind: datapack
    minecraft_version: "1.21"
    pack_format: 48
    distribution: modrinth
```

## Datapacks vs mods

Datapacks are data-only — vanilla Minecraft loads them with no mod loader. Mods require Fabric / Forge / NeoForge / Quilt and ship Java code. A consumer that targets vanilla Minecraft MUST refuse to install a `kind: mod` manifest.

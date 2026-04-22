"""Minecraft — datapacks vs mods (CurseForge + Modrinth)."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "minecraft",
    "title": "Minecraft",
    "lede": (
        "Minecraft creations split cleanly into datapacks (data-only, "
        "vanilla-compatible) and mods (Java code via Fabric / Forge / "
        "NeoForge). A universal-spawn manifest forces exactly one via "
        "`kind` and pins the Minecraft version + loader + distribution "
        "platform."
    ),
    "cares": (
        "The `kind` (`datapack` or `mod`), the Minecraft version, "
        "the mod loader (mods only), and the distribution platform "
        "(CurseForge / Modrinth)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-mod`, `game-world`."),
        ("platforms.minecraft", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.minecraft.kind", "`datapack` or `mod`."),
        ("platforms.minecraft.minecraft_version", "Minecraft version range."),
        ("platforms.minecraft.loader", "Mod loader (mods only)."),
        ("platforms.minecraft.pack_format", "Datapack pack_format integer."),
        ("platforms.minecraft.distribution", "`curseforge`, `modrinth`, `both`."),
        ("platforms.minecraft.curseforge_id", "CurseForge project id."),
        ("platforms.minecraft.modrinth_id", "Modrinth project id."),
    ],
    "platform_fields": {
        "kind": "`datapack` or `mod`.",
        "minecraft_version": "Minecraft version range.",
        "loader": "Mod loader (mods only).",
        "pack_format": "Datapack pack_format.",
        "distribution": "Distribution platform.",
        "curseforge_id": "CurseForge project id.",
        "modrinth_id": "Modrinth project id.",
    },
    "schema_body": schema_object(
        required=["kind", "minecraft_version"],
        properties={
            "kind": enum(["datapack", "mod"]),
            "minecraft_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+(-[a-z0-9.]+)?(,[ ]*[0-9]+(\.[0-9]+)+)?$"),
            "loader": enum(["fabric", "forge", "neoforge", "quilt"]),
            "pack_format": {"type": "integer", "minimum": 1, "maximum": 99},
            "distribution": enum(["curseforge", "modrinth", "both"]),
            "curseforge_id": str_prop(pattern=r"^[0-9]{4,10}$"),
            "modrinth_id": str_prop(pattern=r"^[A-Za-z0-9]{6,16}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Minecraft Template
type: game-mod
description: Template for a Minecraft-targeted universal-spawn manifest.

platforms:
  minecraft:
    kind: datapack
    minecraft_version: "1.21"
    pack_format: 48
    distribution: modrinth

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [minecraft]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/minecraft-template }
""",
    "native_config_name": "pack.mcmeta (datapack) / fabric.mod.json / mods.toml (mod)",
    "native_config_lang": "json",
    "native_config": """
{
  "pack": {
    "pack_format": 48,
    "description": "Your datapack"
  }
}
""",
    "universal_excerpt": """
platforms:
  minecraft:
    kind: datapack
    minecraft_version: "1.21"
    pack_format: 48
    distribution: modrinth
""",
    "compatibility_extras": (
        "## Datapacks vs mods\n\n"
        "Datapacks are data-only — vanilla Minecraft loads them with "
        "no mod loader. Mods require Fabric / Forge / NeoForge / "
        "Quilt and ship Java code. A consumer that targets vanilla "
        "Minecraft MUST refuse to install a `kind: mod` manifest."
    ),
    "examples": {
        "datapack": """
version: "1.0"
name: Plate Datapack
type: game-mod
summary: Minimal Minecraft datapack adding parchment-themed advancements.
description: Vanilla 1.21. pack_format 48. Modrinth distribution.

platforms:
  minecraft:
    kind: datapack
    minecraft_version: "1.21"
    pack_format: 48
    distribution: modrinth
    modrinth_id: "abc123"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [minecraft]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/minecraft-plate-datapack }
  id: com.plate-studio.minecraft-plate-datapack
""",
        "mod": """
version: "1.0"
name: Plate Mod
type: game-mod
summary: Full Fabric mod adding a parchment biome (Java code).
description: Fabric mod for 1.21. Distributed on both CurseForge and Modrinth.

platforms:
  minecraft:
    kind: mod
    minecraft_version: "1.21"
    loader: fabric
    distribution: both
    curseforge_id: "1234567"
    modrinth_id: "ABCdef12"

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [minecraft]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/minecraft-plate-mod }
  id: com.plate-studio.minecraft-plate-mod
""",
    },
}

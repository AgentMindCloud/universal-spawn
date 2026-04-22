"""Fortnite UEFN — published islands."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "fortnite-uefn",
    "title": "Fortnite UEFN",
    "lede": (
        "UEFN (Unreal Editor for Fortnite) ships published islands "
        "into Fortnite via the Discover system. A universal-spawn "
        "manifest pins the island code, the UEFN project file, and "
        "the Verse module."
    ),
    "cares": (
        "The island code, the .uefnproject file, the Verse main "
        "module, and the discover category."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`."),
        ("platforms.fortnite-uefn", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.fortnite-uefn.island_code", "Island code (XXXX-XXXX-XXXX)."),
        ("platforms.fortnite-uefn.uefnproject", "UEFN project file path."),
        ("platforms.fortnite-uefn.verse_main", "Verse main module."),
        ("platforms.fortnite-uefn.discover_category", "Discover category."),
    ],
    "platform_fields": {
        "island_code": "Island code.",
        "uefnproject": "UEFN project file.",
        "verse_main": "Verse main module.",
        "discover_category": "Discover category.",
    },
    "schema_body": schema_object(
        required=["uefnproject"],
        properties={
            "island_code": str_prop(pattern=r"^[0-9]{4}-[0-9]{4}-[0-9]{4}$"),
            "uefnproject": str_prop(),
            "verse_main": str_prop(),
            "discover_category": enum(["adventure", "combat", "escape", "discovery", "creative", "horror", "music", "experimental"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Fortnite UEFN Template
type: game-world
description: Template for a Fortnite UEFN-targeted universal-spawn manifest.

platforms:
  fortnite-uefn:
    uefnproject: YourIsland.uefnproject
    verse_main: src/main.verse

safety:
  min_permissions: [fs:read, gpu:compute]

env_vars_required: []

deployment:
  targets: [fortnite-uefn]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/uefn-template }
""",
    "native_config_name": ".uefnproject + Verse module tree",
    "native_config_lang": "text",
    "native_config": "# UEFN project files + Verse modules.\n",
    "universal_excerpt": """
platforms:
  fortnite-uefn:
    uefnproject: YourIsland.uefnproject
    verse_main: src/main.verse
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Lab Island
type: game-world
summary: Minimal UEFN island showcasing the Residual Frequencies design.
description: One island. Verse main module. Adventure category.

platforms:
  fortnite-uefn:
    uefnproject: PlateLab.uefnproject
    verse_main: src/lab.verse
    discover_category: adventure

safety:
  min_permissions: [fs:read, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [fortnite-uefn]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/uefn-plate-lab }
  id: com.plate-studio.uefn-plate-lab
""",
        "example-2": """
version: "1.0"
name: Plate Studio Music Island
type: game-world
summary: Full UEFN music-experience island with a published code.
description: Released island with code 1234-5678-9012; music category.

platforms:
  fortnite-uefn:
    island_code: "1234-5678-9012"
    uefnproject: MusicIsland.uefnproject
    verse_main: src/music.verse
    discover_category: music

safety:
  min_permissions: [fs:read, fs:write, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [fortnite-uefn]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/uefn-music-island }
  id: com.plate-studio.uefn-music-island
""",
    },
}

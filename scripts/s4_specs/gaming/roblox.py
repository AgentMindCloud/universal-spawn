"""Roblox — experiences + Creator Hub assets."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "roblox",
    "title": "Roblox",
    "lede": (
        "Roblox publishes experiences (places) plus Creator Hub "
        "assets (models, plugins, audio). A universal-spawn manifest "
        "picks one with `kind` and pins the universe + place ids."
    ),
    "cares": (
        "The `kind` (`experience`, `creator-asset`), the universe / "
        "place ids, and the Rojo `default.project.json` path."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `creative-tool`, `extension`."),
        ("platforms.roblox", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.roblox.kind", "`experience` or `creator-asset`."),
        ("platforms.roblox.universe_id", "Universe id."),
        ("platforms.roblox.place_id", "Place id."),
        ("platforms.roblox.rojo_project", "Rojo `default.project.json` path."),
        ("platforms.roblox.asset_kind", "Asset kind (creator-asset)."),
        ("platforms.roblox.creator_hub_id", "Creator Hub asset id."),
    ],
    "platform_fields": {
        "kind": "`experience` or `creator-asset`.",
        "universe_id": "Universe id.",
        "place_id": "Place id.",
        "rojo_project": "Rojo project file.",
        "asset_kind": "Asset kind.",
        "creator_hub_id": "Creator Hub asset id.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["experience", "creator-asset"]),
            "universe_id": str_prop(pattern=r"^[0-9]{6,32}$"),
            "place_id": str_prop(pattern=r"^[0-9]{6,32}$"),
            "rojo_project": str_prop(),
            "asset_kind": enum(["model", "plugin", "audio", "image", "ui"]),
            "creator_hub_id": str_prop(pattern=r"^[0-9]{6,32}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Roblox Template
type: game-world
description: Template for a Roblox-targeted universal-spawn manifest.

platforms:
  roblox:
    kind: experience
    universe_id: "1234567890"
    place_id: "9876543210"
    rojo_project: default.project.json

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [roblox]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/roblox-template }
""",
    "native_config_name": "default.project.json (Rojo)",
    "native_config_lang": "json",
    "native_config": """
{
  "name": "Your Game",
  "tree": {
    "$className": "DataModel",
    "ServerScriptService": { "$path": "src/server" }
  }
}
""",
    "universal_excerpt": """
platforms:
  roblox:
    kind: experience
    universe_id: "1234567890"
    place_id: "9876543210"
    rojo_project: default.project.json
""",
    "compatibility_extras": "",
    "perks": ["**Creator Hub badge** — manifest-declared experiences carry a 'spawns on Roblox' badge on the registry card."],
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Studio Place
type: game-world
summary: Minimal Roblox experience deploying a parchment-themed place via Rojo.
description: Single place id; Rojo project at the repo root.

platforms:
  roblox:
    kind: experience
    universe_id: "1111111111"
    place_id: "2222222222"
    rojo_project: default.project.json

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ROBLOX_API_KEY
    description: Roblox Open Cloud API key.
    secret: true

deployment:
  targets: [roblox]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/roblox-plate-place }
  id: com.plate-studio.roblox-plate-place
""",
        "example-2": """
version: "1.0"
name: Parchment Plugin Asset
type: extension
summary: Full Roblox Studio plugin published as a Creator Hub asset.
description: Roblox Studio plugin asset id; pairs with the experience above.

platforms:
  roblox:
    kind: creator-asset
    asset_kind: plugin
    creator_hub_id: "3333333333"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [roblox]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/roblox-parchment-plugin }
  id: com.plate-studio.roblox-parchment-plugin
""",
    },
}

"""Steam — Workshop items + Steamworks Direct."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "steam",
    "title": "Steam",
    "lede": (
        "Steam ships two distribution paths: Steam Workshop items "
        "(uploaded via the Workshop API into a host game) and "
        "Steamworks Direct titles (Steam-published games). A "
        "universal-spawn manifest picks one with `kind`."
    ),
    "cares": (
        "The `kind` (`workshop-item`, `direct-title`), the host "
        "appid for Workshop items, and the depot configuration for "
        "Direct titles."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `game-mod`, `creative-tool`."),
        ("platforms.steam", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.steam.kind", "`workshop-item` or `direct-title`."),
        ("platforms.steam.host_appid", "Host appid for Workshop items."),
        ("platforms.steam.workshop_id", "Workshop file id."),
        ("platforms.steam.appid", "Steamworks appid for Direct titles."),
        ("platforms.steam.depots", "Depot configuration."),
        ("platforms.steam.steampipe_vdf", "Steampipe build VDF path."),
    ],
    "platform_fields": {
        "kind": "`workshop-item` or `direct-title`.",
        "host_appid": "Host appid (Workshop).",
        "workshop_id": "Workshop file id.",
        "appid": "Steamworks appid (Direct).",
        "depots": "Depot configuration.",
        "steampipe_vdf": "Steampipe build VDF.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["workshop-item", "direct-title"]),
            "host_appid": str_prop(pattern=r"^[0-9]{4,10}$"),
            "workshop_id": str_prop(pattern=r"^[0-9]{6,20}$"),
            "appid": str_prop(pattern=r"^[0-9]{4,10}$"),
            "depots": {
                "type": "array",
                "items": schema_object(
                    required=["depot_id"],
                    properties={
                        "depot_id": str_prop(pattern=r"^[0-9]{4,10}$"),
                        "platform": enum(["windows", "macos", "linux"]),
                    },
                ),
            },
            "steampipe_vdf": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Steam Template
type: game-world
description: Template for a Steam-targeted universal-spawn manifest.

platforms:
  steam:
    kind: workshop-item
    host_appid: "108600"
    workshop_id: "1234567890"

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [steam]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/steam-template }
""",
    "native_config_name": "steampipe build VDF + Workshop API",
    "native_config_lang": "vdf",
    "native_config": """
"appbuild"
{
  "appid" "1234567"
  "desc" "Your build"
  "depots"
  {
    "1234568" "depot_build_windows.vdf"
  }
}
""",
    "universal_excerpt": """
platforms:
  steam:
    kind: direct-title
    appid: "1234567"
    depots:
      - { depot_id: "1234568", platform: windows }
    steampipe_vdf: build/app_build.vdf
""",
    "compatibility_extras": "",
    "perks": ["**Steam Workshop badge** — Workshop-item manifests carry a 'Subscribe on Workshop' link rendered from `host_appid` + `workshop_id`."],
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Workshop Mod
type: game-mod
summary: Minimal Steam Workshop item for a host game (appid 108600).
description: Single Workshop item id; subscriber-installable.

platforms:
  steam:
    kind: workshop-item
    host_appid: "108600"
    workshop_id: "9999988887"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [steam]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/steam-plate-workshop }
  id: com.plate-studio.steam-plate-workshop
""",
        "example-2": """
version: "1.0"
name: Plate Lab Steam Title
type: game-world
summary: Full Steamworks Direct title with three platform depots.
description: Direct-published Steam title across Windows + macOS + Linux depots.

platforms:
  steam:
    kind: direct-title
    appid: "5555555"
    depots:
      - { depot_id: "5555556", platform: windows }
      - { depot_id: "5555557", platform: macos }
      - { depot_id: "5555558", platform: linux }
    steampipe_vdf: build/app_build.vdf

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required:
  - name: STEAM_USERNAME
    description: Steamworks publisher account.
  - name: STEAM_PASSWORD
    description: Steamworks publisher password.
    secret: true

deployment:
  targets: [steam]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/steam-plate-lab }
  id: com.plate-studio.steam-plate-lab
""",
    },
}

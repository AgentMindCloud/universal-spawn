"""RPG Maker — MV/MZ data/ tree + plugins."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "rpg-maker",
    "title": "RPG Maker",
    "lede": (
        "RPG Maker projects (MV / MZ) ship a `data/` tree plus "
        "optional plugins (`js/plugins/`). A universal-spawn manifest "
        "picks the engine generation and the kind."
    ),
    "cares": (
        "The engine (`mv`, `mz`, `unite`), the `kind` (`project` or "
        "`plugin`), and the JS-engine target."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `extension`, `creative-tool`."),
        ("platforms.rpg-maker", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.rpg-maker.engine", "`mv`, `mz`, `unite`."),
        ("platforms.rpg-maker.kind", "`project` or `plugin`."),
        ("platforms.rpg-maker.entry_data_dir", "data/ directory path."),
        ("platforms.rpg-maker.plugin_file", "Plugin JS file (`kind: plugin`)."),
    ],
    "platform_fields": {
        "engine": "`mv`, `mz`, `unite`.",
        "kind": "`project` or `plugin`.",
        "entry_data_dir": "data/ directory.",
        "plugin_file": "Plugin JS file.",
    },
    "schema_body": schema_object(
        required=["engine", "kind"],
        properties={
            "engine": enum(["mv", "mz", "unite"]),
            "kind": enum(["project", "plugin"]),
            "entry_data_dir": str_prop(),
            "plugin_file": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: RPG Maker Template
type: game-world
description: Template for an RPG-Maker-targeted universal-spawn manifest.

platforms:
  rpg-maker:
    engine: mz
    kind: project
    entry_data_dir: data

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [rpg-maker]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/rpg-maker-template }
""",
    "native_config_name": "data/ tree (MV/MZ) or rpgmaker_unite project",
    "native_config_lang": "text",
    "native_config": "# RPG Maker MV/MZ projects expose state as JSON files inside data/.\n",
    "universal_excerpt": """
platforms:
  rpg-maker:
    engine: mz
    kind: project
    entry_data_dir: data
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Lab RPG Project
type: game-world
summary: Minimal RPG Maker MZ project — parchment-themed lab notebook RPG.
description: Whole project tree under data/.

platforms:
  rpg-maker:
    engine: mz
    kind: project
    entry_data_dir: data

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [rpg-maker]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rpgmaker-plate-lab }
  id: com.plate-studio.rpgmaker-plate-lab
""",
        "example-2": """
version: "1.0"
name: Parchment Battle System Plugin
type: extension
summary: Full RPG Maker MZ plugin replacing the default battle system.
description: Single .js file inside js/plugins/.

platforms:
  rpg-maker:
    engine: mz
    kind: plugin
    plugin_file: js/plugins/ParchmentBattleSystem.js

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [rpg-maker]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rpgmaker-parchment-battle-system }
  id: com.plate-studio.rpgmaker-parchment-battle-system
""",
    },
}

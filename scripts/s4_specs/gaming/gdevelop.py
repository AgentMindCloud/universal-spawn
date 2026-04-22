"""GDevelop — game.json projects."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "gdevelop",
    "title": "GDevelop",
    "lede": (
        "GDevelop projects ship as `game.json`. A universal-spawn "
        "manifest pins the project file and the export targets."
    ),
    "cares": ("game.json path and export targets."),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `creative-tool`."),
        ("platforms.gdevelop", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.gdevelop.project_file", "game.json path."),
        ("platforms.gdevelop.exports", "Export targets."),
        ("platforms.gdevelop.engine_version", "GDevelop engine version."),
    ],
    "platform_fields": {
        "project_file": "game.json path.",
        "exports": "Export targets.",
        "engine_version": "Engine version.",
    },
    "schema_body": schema_object(
        required=["project_file"],
        properties={
            "project_file": str_prop(),
            "exports": {
                "type": "array",
                "items": enum(["html5", "android", "ios", "windows", "macos", "linux"]),
            },
            "engine_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: GDevelop Template
type: game-world
description: Template for a GDevelop-targeted universal-spawn manifest.

platforms:
  gdevelop:
    project_file: game.json
    exports: [html5, android]
    engine_version: "5.4"

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [gdevelop]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/gdevelop-template }
""",
    "native_config_name": "game.json",
    "native_config_lang": "json",
    "native_config": """
{
  "properties": { "name": "Your Game", "version": "0.1.0" },
  "layouts": []
}
""",
    "universal_excerpt": """
platforms:
  gdevelop:
    project_file: game.json
    exports: [html5, android]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Mini Game
type: game-world
summary: Minimal GDevelop game exporting to HTML5.
description: One game.json. HTML5 export only.

platforms:
  gdevelop:
    project_file: game.json
    exports: [html5]
    engine_version: "5.4"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [gdevelop]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/gdevelop-plate-mini-game }
  id: com.plate-studio.gdevelop-plate-mini-game
""",
        "example-2": """
version: "1.0"
name: Plate Lab Game
type: game-world
summary: Full GDevelop game exporting to HTML5 + Android + Windows.
description: Same project, three platforms.

platforms:
  gdevelop:
    project_file: game.json
    exports: [html5, android, windows]
    engine_version: "5.4"

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [gdevelop]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/gdevelop-plate-lab }
  id: com.plate-studio.gdevelop-plate-lab
""",
    },
}

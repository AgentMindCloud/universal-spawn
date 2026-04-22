"""Construct — .c3p projects."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "construct",
    "title": "Construct",
    "lede": (
        "Construct (Construct 3) ships projects as `.c3p` archives. "
        "A universal-spawn manifest pins the project file and the "
        "export targets."
    ),
    "cares": (".c3p file path and export targets."),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `creative-tool`."),
        ("platforms.construct", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.construct.project_file", ".c3p file path."),
        ("platforms.construct.exports", "Export targets."),
    ],
    "platform_fields": {
        "project_file": ".c3p file.",
        "exports": "Export targets.",
    },
    "schema_body": schema_object(
        required=["project_file"],
        properties={
            "project_file": str_prop(),
            "exports": {
                "type": "array",
                "items": enum(["html5", "android", "ios", "windows", "macos", "linux"]),
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: Construct Template
type: game-world
description: Template for a Construct-targeted universal-spawn manifest.

platforms:
  construct:
    project_file: project.c3p
    exports: [html5, android]

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [construct]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/construct-template }
""",
    "native_config_name": "*.c3p (Construct project archive)",
    "native_config_lang": "text",
    "native_config": "# Construct projects are .c3p archives; no separate config file.\n",
    "universal_excerpt": """
platforms:
  construct:
    project_file: project.c3p
    exports: [html5, android]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Construct Demo
type: game-world
summary: Minimal Construct project exported to HTML5.
description: One .c3p; HTML5 only.

platforms:
  construct:
    project_file: plate-demo.c3p
    exports: [html5]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [construct]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/construct-plate-demo }
  id: com.plate-studio.construct-plate-demo
""",
        "example-2": """
version: "1.0"
name: Plate Lab Construct Game
type: game-world
summary: Full Construct game exporting across HTML5 + iOS + Android + Windows.
description: Same project, four targets.

platforms:
  construct:
    project_file: plate-lab.c3p
    exports: [html5, ios, android, windows]

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [construct]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/construct-plate-lab }
  id: com.plate-studio.construct-plate-lab
""",
    },
}

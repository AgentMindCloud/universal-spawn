"""Defold — game.project + native extensions."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "defold",
    "title": "Defold",
    "lede": (
        "Defold projects are described by `game.project`. Native "
        "extensions ship as separate manifests. A universal-spawn "
        "manifest picks `kind` and pins the engine version + target "
        "platforms."
    ),
    "cares": (
        "The `kind` (`project`, `extension`), engine version, and "
        "target platforms."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `extension`."),
        ("platforms.defold", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.defold.kind", "`project` or `extension`."),
        ("platforms.defold.engine_version", "Defold engine version."),
        ("platforms.defold.target_platforms", "Target platforms."),
        ("platforms.defold.entry_collection", "Entry collection (project)."),
    ],
    "platform_fields": {
        "kind": "`project` or `extension`.",
        "engine_version": "Defold engine version.",
        "target_platforms": "Target platforms.",
        "entry_collection": "Entry collection.",
    },
    "schema_body": schema_object(
        required=["kind", "engine_version"],
        properties={
            "kind": enum(["project", "extension"]),
            "engine_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "target_platforms": {
                "type": "array",
                "items": enum(["windows", "macos", "linux", "ios", "android", "html5", "switch"]),
            },
            "entry_collection": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Defold Template
type: game-world
description: Template for a Defold-targeted universal-spawn manifest.

platforms:
  defold:
    kind: project
    engine_version: "1.9"
    target_platforms: [windows, macos, linux, html5]
    entry_collection: main/main.collection

safety:
  min_permissions: [fs:read, gpu:compute]

env_vars_required: []

deployment:
  targets: [defold]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/defold-template }
""",
    "native_config_name": "game.project",
    "native_config_lang": "ini",
    "native_config": """
[project]
title = Your Game
version = 1.0

[bootstrap]
main_collection = /main/main.collectionc
""",
    "universal_excerpt": """
platforms:
  defold:
    kind: project
    engine_version: "1.9"
    entry_collection: main/main.collection
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Defold Project
type: game-world
summary: Minimal Defold 1.9 project for HTML5 + desktop.
description: Single collection entry; HTML5 + desktop targets.

platforms:
  defold:
    kind: project
    engine_version: "1.9"
    target_platforms: [windows, macos, linux, html5]
    entry_collection: main/main.collection

safety:
  min_permissions: [fs:read, gpu:compute]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [defold]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/defold-plate-project }
  id: com.plate-studio.defold-plate-project
""",
        "example-2": """
version: "1.0"
name: Parchment Native Extension
type: extension
summary: Full Defold native extension shading textures via the parchment palette.
description: Native extension for iOS + Android.

platforms:
  defold:
    kind: extension
    engine_version: "1.9"
    target_platforms: [ios, android]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [defold]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/defold-parchment-extension }
  id: com.plate-studio.defold-parchment-extension
""",
    },
}

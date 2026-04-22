"""PlayCanvas — cloud-native WebGL projects."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "playcanvas",
    "title": "PlayCanvas",
    "lede": (
        "PlayCanvas hosts WebGL projects in the cloud editor. A "
        "universal-spawn manifest pins the project id, the published "
        "scene, and the engine version."
    ),
    "cares": (
        "Project id, published scene id, engine version, and the "
        "Editor URL."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `creative-tool`, `web-app`."),
        ("platforms.playcanvas", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.playcanvas.project_id", "PlayCanvas project id."),
        ("platforms.playcanvas.scene_id", "Default scene id."),
        ("platforms.playcanvas.engine_version", "PlayCanvas engine version."),
        ("platforms.playcanvas.editor_url", "Editor URL."),
    ],
    "platform_fields": {
        "project_id": "PlayCanvas project id.",
        "scene_id": "Default scene id.",
        "engine_version": "Engine version.",
        "editor_url": "Editor URL.",
    },
    "schema_body": schema_object(
        required=["project_id"],
        properties={
            "project_id": str_prop(pattern=r"^[0-9]{4,12}$"),
            "scene_id": str_prop(pattern=r"^[0-9]{4,12}$"),
            "engine_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "editor_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: PlayCanvas Template
type: game-world
description: Template for a PlayCanvas-targeted universal-spawn manifest.

platforms:
  playcanvas:
    project_id: "1234567"
    scene_id: "987654"
    engine_version: "1.74"

safety:
  min_permissions: [network:inbound, gpu:compute]

env_vars_required: []

deployment:
  targets: [playcanvas]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/playcanvas-template }
""",
    "native_config_name": "PlayCanvas cloud project (no repo file by convention)",
    "native_config_lang": "text",
    "native_config": "# Cloud-native; project state lives on PlayCanvas servers.\n",
    "universal_excerpt": """
platforms:
  playcanvas:
    project_id: "1234567"
    scene_id: "987654"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Demo PlayCanvas
type: game-world
summary: Minimal PlayCanvas project showcasing parchment plates in 3D.
description: Single scene; engine 1.74.

platforms:
  playcanvas:
    project_id: "1111111"
    scene_id: "222222"
    engine_version: "1.74"

safety:
  min_permissions: [network:inbound, gpu:compute]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [playcanvas]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/playcanvas-plate-demo }
  id: com.plate-studio.playcanvas-plate-demo
""",
        "example-2": """
version: "1.0"
name: Plate Studio Showroom
type: web-app
summary: Full PlayCanvas WebGL project deployed as a public showroom.
description: Multi-scene WebGL build with shared editor URL.

platforms:
  playcanvas:
    project_id: "3333333"
    engine_version: "1.74"
    editor_url: "https://playcanvas.com/editor/scene/3333333"

safety:
  min_permissions: [network:inbound, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [playcanvas]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/playcanvas-showroom }
  id: com.plate-studio.playcanvas-showroom
""",
    },
}

"""Godot — projects + addons (Asset Library)."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "godot",
    "title": "Godot",
    "lede": (
        "Godot ships projects (project.godot) and addons (Asset "
        "Library). A universal-spawn manifest picks one with `kind` "
        "and pins the engine series + renderer."
    ),
    "cares": (
        "The `kind` (`addon`, `project`), engine series (3 or 4), and "
        "renderer (`forward+`, `mobile`, `compatibility`)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-mod`, `game-world`, `extension`."),
        ("platforms.godot", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.godot.kind", "`addon` or `project`."),
        ("platforms.godot.engine_series", "Engine series (3 or 4)."),
        ("platforms.godot.renderer", "Renderer."),
        ("platforms.godot.entry_scene", "Entry scene path."),
    ],
    "platform_fields": {
        "kind": "`addon` or `project`.",
        "engine_series": "Engine series.",
        "renderer": "Renderer.",
        "entry_scene": "Entry scene path.",
    },
    "schema_body": schema_object(
        required=["kind", "engine_series"],
        properties={
            "kind": enum(["addon", "project"]),
            "engine_series": enum(["3", "4"]),
            "renderer": enum(["forward+", "mobile", "compatibility"]),
            "entry_scene": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Godot Template
type: game-world
description: Template for a Godot-targeted universal-spawn manifest.

platforms:
  godot:
    kind: project
    engine_series: "4"
    renderer: forward+
    entry_scene: scenes/main.tscn

safety:
  min_permissions: [fs:read, gpu:compute]

env_vars_required: []

deployment:
  targets: [godot]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/godot-template }
""",
    "native_config_name": "project.godot + addons/<id>/plugin.cfg",
    "native_config_lang": "ini",
    "native_config": """
[application]
config/name="Your Project"
run/main_scene="res://scenes/main.tscn"

[rendering]
renderer/rendering_method="forward_plus"
""",
    "universal_excerpt": """
platforms:
  godot:
    kind: project
    engine_series: "4"
    renderer: forward+
    entry_scene: scenes/main.tscn
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Godot Project
type: game-world
summary: Minimal Godot 4 project running the parchment lab scene.
description: Forward+ renderer, single entry scene.

platforms:
  godot:
    kind: project
    engine_series: "4"
    renderer: forward+
    entry_scene: scenes/lab.tscn

safety:
  min_permissions: [fs:read, gpu:compute]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [godot]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/godot-plate-project }
  id: com.plate-studio.godot-plate-project
""",
        "example-2": """
version: "1.0"
name: Parchment Shader Addon
type: extension
summary: Full Godot Asset Library addon — parchment-tone shader pack.
description: GDScript + GLSL shader addon. Registers a small editor menu.

platforms:
  godot:
    kind: addon
    engine_series: "4"
    renderer: forward+

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [godot]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/godot-parchment-shader }
  id: com.plate-studio.godot-parchment-shader
""",
    },
}

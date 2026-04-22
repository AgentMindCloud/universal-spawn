"""Blender — add-ons + projects + asset libraries."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "blender",
    "title": "Blender",
    "lede": (
        "Blender ships a vast Python add-on ecosystem plus .blend files "
        "that act as projects and asset libraries. The extension "
        "captures the `kind`, the entry Python module (for add-ons), "
        "and the asset library path (for libraries)."
    ),
    "cares": (
        "The `kind` (`addon`, `project`, `asset-library`), the "
        "Blender version range, and the entry point for each kind."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `design-template`, `extension`."),
        ("platforms.blender", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.blender.kind", "`addon`, `project`, `asset-library`."),
        ("platforms.blender.blender_version", "Minimum Blender version."),
        ("platforms.blender.entry_module", "`__init__.py` path for add-ons."),
        ("platforms.blender.entry_blend", "`.blend` file for projects."),
        ("platforms.blender.asset_library_path", "Directory for asset libraries."),
        ("platforms.blender.render_engine", "Preferred render engine."),
    ],
    "platform_fields": {
        "kind": "`addon`, `project`, `asset-library`.",
        "blender_version": "Minimum Blender version.",
        "entry_module": "`__init__.py` for add-ons.",
        "entry_blend": "`.blend` file for projects.",
        "asset_library_path": "Directory for asset libraries.",
        "render_engine": "`cycles`, `eevee`, or `workbench`.",
    },
    "schema_body": schema_object(
        required=["kind", "blender_version"],
        properties={
            "kind": enum(["addon", "project", "asset-library"]),
            "blender_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
            "entry_module": str_prop(),
            "entry_blend": str_prop(),
            "asset_library_path": str_prop(),
            "render_engine": enum(["cycles", "eevee", "workbench"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Blender Template
type: creative-tool
description: Template for a Blender-targeted universal-spawn manifest.

platforms:
  blender:
    kind: addon
    blender_version: "4.2"
    entry_module: addons/your_addon/__init__.py

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [blender]

metadata:
  license: GPL-3.0-only
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/blender-template }
""",
    "native_config_name": "addon __init__.py bl_info",
    "native_config_lang": "python",
    "native_config": """
bl_info = {
    "name": "Your Addon",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "category": "Object",
}
""",
    "universal_excerpt": """
platforms:
  blender:
    kind: addon
    blender_version: "4.2"
    entry_module: addons/your_addon/__init__.py
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Shader Addon
type: creative-tool
summary: Minimal Blender addon adding a parchment-tone shader node.
description: Single-file addon registering one shader node group.

platforms:
  blender:
    kind: addon
    blender_version: "4.2"
    entry_module: addons/parchment_shader/__init__.py
    render_engine: cycles

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [blender]

visuals: { palette: parchment }

metadata:
  license: GPL-3.0-only
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/blender-parchment-shader }
  id: com.plate-studio.blender-parchment-shader
""",
        "example-2": """
version: "1.0"
name: Plate Asset Library
type: design-template
summary: Distributable asset library with 40 Residual Frequencies props.
description: Blender asset library (a directory full of .blend files) for drag-and-drop from the Asset Browser.

platforms:
  blender:
    kind: asset-library
    blender_version: "4.2"
    asset_library_path: lib/parchment-props

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [blender]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/blender-plate-asset-library }
  id: com.plate-studio.blender-plate-asset-library
""",
    },
}

"""SketchUp — Ruby extensions + RBZ packages + components."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "sketchup",
    "title": "SketchUp",
    "lede": (
        "SketchUp ships Ruby extensions (RBZ archives) and reusable "
        "components (.skp). A universal-spawn manifest points at one."
    ),
    "cares": (
        "The `kind` (`rbz-extension`, `component`), the minimum "
        "SketchUp year, and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `plugin`, `design-template`."),
        ("platforms.sketchup", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.sketchup.kind", "`rbz-extension`, `component`."),
        ("platforms.sketchup.min_year", "Minimum SketchUp year version."),
        ("platforms.sketchup.entry_file", "Entry file path."),
        ("platforms.sketchup.extension_warehouse", "Warehouse publication settings."),
    ],
    "platform_fields": {
        "kind": "`rbz-extension`, `component`.",
        "min_year": "Minimum SketchUp year (e.g. 2024).",
        "entry_file": "Entry file path.",
        "extension_warehouse": "Extension Warehouse settings.",
    },
    "schema_body": schema_object(
        required=["kind", "min_year"],
        properties={
            "kind": enum(["rbz-extension", "component"]),
            "min_year": {"type": "integer", "minimum": 2017, "maximum": 2099},
            "entry_file": str_prop(),
            "extension_warehouse": schema_object(
                properties={
                    "listed": bool_prop(False),
                    "category": str_prop(),
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: SketchUp Template
type: creative-tool
description: Template for a SketchUp-targeted universal-spawn manifest.

platforms:
  sketchup:
    kind: rbz-extension
    min_year: 2024
    entry_file: dist/your-extension.rbz

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [sketchup]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/sketchup-template }
""",
    "native_config_name": "*.rbz (zip of ruby extension)",
    "native_config_lang": "text",
    "native_config": "# SketchUp extensions are zipped ruby trees renamed to .rbz.\n",
    "universal_excerpt": """
platforms:
  sketchup:
    kind: rbz-extension
    min_year: 2024
    entry_file: dist/parchment-studio.rbz
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Palette Extension
type: creative-tool
summary: Minimal SketchUp extension that ships the Residual Frequencies palette.
description: Single RBZ. Applies the parchment palette to selected faces.

platforms:
  sketchup:
    kind: rbz-extension
    min_year: 2024
    entry_file: dist/parchment-palette.rbz

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [sketchup]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/sketchup-parchment-palette }
  id: com.plate-studio.sketchup-parchment-palette
""",
        "example-2": """
version: "1.0"
name: Plate Components Pack
type: design-template
summary: SketchUp component library with parchment-themed props, listed on the Warehouse.
description: Extension Warehouse-listed .skp component pack.

platforms:
  sketchup:
    kind: component
    min_year: 2023
    entry_file: components/plate-props.skp
    extension_warehouse:
      listed: true
      category: "Models"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [sketchup]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/sketchup-plate-components }
  id: com.plate-studio.sketchup-plate-components
""",
    },
}

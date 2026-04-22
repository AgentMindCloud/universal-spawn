"""Cinema 4D — Python generators, Python tags, .lib4d asset libraries."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "cinema4d",
    "title": "Cinema 4D",
    "lede": (
        "Cinema 4D runs Python-scripted generators, Python Tags, and "
        "ships asset libraries as `.lib4d` archives. A universal-spawn "
        "manifest targets one of those shapes plus the C4D version "
        "range."
    ),
    "cares": (
        "The `kind` (`plugin`, `scene`, `asset-library`), the minimum "
        "Cinema 4D version, and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `design-template`, `plugin`."),
        ("platforms.cinema4d", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.cinema4d.kind", "`plugin`, `scene`, `asset-library`."),
        ("platforms.cinema4d.min_version", "Minimum C4D version."),
        ("platforms.cinema4d.entry_file", "Entry file (plugin `.pyp` or scene `.c4d` or `.lib4d`)."),
    ],
    "platform_fields": {
        "kind": "`plugin`, `scene`, or `asset-library`.",
        "min_version": "Minimum Cinema 4D version.",
        "entry_file": "Entry file.",
    },
    "schema_body": schema_object(
        required=["kind", "min_version"],
        properties={
            "kind": enum(["plugin", "scene", "asset-library"]),
            "min_version": str_prop(pattern=r"^(R|S)?[0-9]+(\.[0-9]+)?$"),
            "entry_file": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Cinema 4D Template
type: creative-tool
description: Template for a Cinema-4D-targeted universal-spawn manifest.

platforms:
  cinema4d:
    kind: plugin
    min_version: "2025"
    entry_file: src/plugin.pyp

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [cinema4d]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/cinema4d-template }
""",
    "native_config_name": "plugin .pyp file + optional res/description/",
    "native_config_lang": "python",
    "native_config": "# Python plugin metadata lives at the top of the .pyp file.\nPLUGIN_ID = 1000000\n",
    "universal_excerpt": """
platforms:
  cinema4d:
    kind: plugin
    min_version: "2025"
    entry_file: src/plugin.pyp
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: C4D Parchment Procedural
type: creative-tool
summary: Minimal Cinema 4D Python generator producing a parchment-plate lattice.
description: Single .pyp plugin registering one Object generator.

platforms:
  cinema4d:
    kind: plugin
    min_version: "2024"
    entry_file: src/plate_lattice.pyp

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [cinema4d]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/c4d-parchment-procedural }
  id: com.plate-studio.c4d-parchment-procedural
""",
        "example-2": """
version: "1.0"
name: Plate Asset Library
type: design-template
summary: .lib4d asset library with 20 Residual Frequencies props.
description: Distributed as a Cinema 4D asset library archive.

platforms:
  cinema4d:
    kind: asset-library
    min_version: "2024"
    entry_file: dist/plate-props.lib4d

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [cinema4d]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/c4d-plate-asset-library }
  id: com.plate-studio.c4d-plate-asset-library
""",
    },
}

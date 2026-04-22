"""Houdini — HDA assets, hip files, Python shelves."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "houdini",
    "title": "Houdini",
    "lede": (
        "SideFX Houdini packages reusable nodes as Houdini Digital "
        "Assets (HDAs), saves projects as .hip files, and ships "
        "toolbars as Python shelves. A universal-spawn manifest picks "
        "the `kind` and points at the entry artifact."
    ),
    "cares": (
        "The `kind` (`hda`, `hip`, `shelf`), the Houdini build version, "
        "the context (`sop`, `dop`, `cop2`, `obj`), and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `plugin`, `design-template`."),
        ("platforms.houdini", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.houdini.kind", "`hda`, `hip`, `shelf`."),
        ("platforms.houdini.min_build", "Minimum Houdini build."),
        ("platforms.houdini.context", "Houdini network context."),
        ("platforms.houdini.entry_file", "Entry `.hda` / `.hip` / `.shelf` path."),
    ],
    "platform_fields": {
        "kind": "`hda`, `hip`, or `shelf`.",
        "min_build": "Minimum Houdini build.",
        "context": "Network context.",
        "entry_file": "Entry file.",
    },
    "schema_body": schema_object(
        required=["kind", "min_build", "entry_file"],
        properties={
            "kind": enum(["hda", "hip", "shelf"]),
            "min_build": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "context": enum(["obj", "sop", "dop", "cop2", "shop", "vop", "chop", "top", "lop"]),
            "entry_file": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Houdini Template
type: creative-tool
description: Template for a Houdini-targeted universal-spawn manifest.

platforms:
  houdini:
    kind: hda
    min_build: "20.5"
    context: sop
    entry_file: otls/your_hda.hda

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [houdini]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/houdini-template }
""",
    "native_config_name": ".hda + otls/ + shelves/*.shelf",
    "native_config_lang": "text",
    "native_config": "# HDAs contain their own metadata; no separate config file.\n",
    "universal_excerpt": """
platforms:
  houdini:
    kind: hda
    min_build: "20.5"
    context: sop
    entry_file: otls/plate_lattice.hda
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Lattice HDA
type: creative-tool
summary: Minimal Houdini HDA producing a parchment plate lattice.
description: Single SOP-context HDA.

platforms:
  houdini:
    kind: hda
    min_build: "20.5"
    context: sop
    entry_file: otls/plate_lattice.hda

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [houdini]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/houdini-plate-lattice }
  id: com.plate-studio.houdini-plate-lattice
""",
        "example-2": """
version: "1.0"
name: Plate Studio Shelf
type: creative-tool
summary: Houdini shelf bundling six Residual Frequencies quick-start tools.
description: Python shelf with shortcuts for plate setup, palette apply, and scene notes.

platforms:
  houdini:
    kind: shelf
    min_build: "20.0"
    entry_file: shelves/plate-studio.shelf

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [houdini]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/houdini-plate-shelf }
  id: com.plate-studio.houdini-plate-shelf
""",
    },
}

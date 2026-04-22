"""Rhinoceros 3D — Rhino plugins + Grasshopper definitions + Food4Rhino."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "rhinoceros",
    "title": "Rhinoceros 3D",
    "lede": (
        "Rhino ships .rhp plugins, Grasshopper `.gh` definitions, and "
        "Yak packages for Food4Rhino distribution. A universal-spawn "
        "manifest targets one of those shapes."
    ),
    "cares": (
        "The `kind` (`rhp-plugin`, `grasshopper`, `yak-package`), the "
        "Rhino version range, and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `plugin`, `design-template`."),
        ("platforms.rhinoceros", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.rhinoceros.kind", "`rhp-plugin`, `grasshopper`, `yak-package`."),
        ("platforms.rhinoceros.min_version", "Minimum Rhino version."),
        ("platforms.rhinoceros.entry_file", "Entry file path."),
        ("platforms.rhinoceros.yak", "Yak manifest settings (for `yak-package`)."),
    ],
    "platform_fields": {
        "kind": "`rhp-plugin`, `grasshopper`, `yak-package`.",
        "min_version": "Minimum Rhino version.",
        "entry_file": "Entry file path.",
        "yak": "Yak package manifest settings.",
    },
    "schema_body": schema_object(
        required=["kind", "min_version"],
        properties={
            "kind": enum(["rhp-plugin", "grasshopper", "yak-package"]),
            "min_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)?$"),
            "entry_file": str_prop(),
            "yak": schema_object(
                properties={
                    "yak_file": str_prop(),
                    "category": str_prop(),
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Rhinoceros Template
type: creative-tool
description: Template for a Rhinoceros-targeted universal-spawn manifest.

platforms:
  rhinoceros:
    kind: grasshopper
    min_version: "8"
    entry_file: gh/plate-lattice.gh

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [rhinoceros]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/rhino-template }
""",
    "native_config_name": "Yak package manifest (.yml)",
    "native_config_lang": "yaml",
    "native_config": """
name: your-plugin
version: 0.1.0
authors: [yourhandle]
description: Your description
""",
    "universal_excerpt": """
platforms:
  rhinoceros:
    kind: yak-package
    min_version: "8"
    yak:
      yak_file: yak.yml
      category: Grasshopper
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Lattice GH
type: creative-tool
summary: Minimal Grasshopper definition that draws a parchment plate lattice.
description: Single `.gh` file, Rhino 8+.

platforms:
  rhinoceros:
    kind: grasshopper
    min_version: "8"
    entry_file: gh/plate-lattice.gh

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [rhinoceros]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rhino-plate-lattice }
  id: com.plate-studio.rhino-plate-lattice
""",
        "example-2": """
version: "1.0"
name: Parchment Plugin Yak
type: plugin
summary: Food4Rhino-listed plugin distributed as a Yak package.
description: Rhino plugin published via Yak, listed under Grasshopper.

platforms:
  rhinoceros:
    kind: yak-package
    min_version: "8"
    yak:
      yak_file: yak.yml
      category: Grasshopper

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [rhinoceros]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rhino-parchment-yak }
  id: com.plate-studio.rhino-parchment-yak
""",
    },
}

"""LEGO SPIKE — exported SPIKE App projects."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "lego-spike",
    "title": "LEGO SPIKE",
    "lede": (
        "LEGO Education's SPIKE App exports projects you can re-import. "
        "A universal-spawn manifest pins the SPIKE generation, "
        "language (icon-blocks vs Python), and the exported project."
    ),
    "cares": (
        "The SPIKE generation (Prime/Essential, App 3.x), the "
        "language, and the exported project file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `cli-tool`, `library`."),
        ("platforms.lego-spike", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.lego-spike.generation", "`spike-prime`, `spike-essential`."),
        ("platforms.lego-spike.language", "`icon-blocks` or `python`."),
        ("platforms.lego-spike.entry_file", "Exported project file."),
        ("platforms.lego-spike.app_version", "Minimum SPIKE App version."),
    ],
    "platform_fields": {
        "generation": "`spike-prime` or `spike-essential`.",
        "language": "`icon-blocks` or `python`.",
        "entry_file": "Exported project file.",
        "app_version": "Min SPIKE App version.",
    },
    "schema_body": schema_object(
        required=["generation", "language"],
        properties={
            "generation": enum(["spike-prime", "spike-essential"]),
            "language": enum(["icon-blocks", "python"]),
            "entry_file": str_prop(),
            "app_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: LEGO SPIKE Template
type: firmware
description: Template for a LEGO-SPIKE-targeted universal-spawn manifest.

platforms:
  lego-spike:
    generation: spike-prime
    language: python
    entry_file: project/main.py
    app_version: "3.4"

safety:
  min_permissions: [usb:claim:vid=0x0694]

env_vars_required: []

deployment:
  targets: [lego-spike]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/lego-spike-template }
""",
    "native_config_name": "SPIKE App project export (.llsp3 / .py)",
    "native_config_lang": "text",
    "native_config": "# SPIKE App exports include the project metadata + code.\n",
    "universal_excerpt": """
platforms:
  lego-spike:
    generation: spike-prime
    language: python
    entry_file: project/main.py
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Lesson SPIKE Prime
type: firmware
summary: Minimal LEGO SPIKE Prime icon-blocks lesson.
description: One exported icon-blocks project.

platforms:
  lego-spike:
    generation: spike-prime
    language: icon-blocks
    entry_file: project/lesson.llsp3
    app_version: "3.4"

safety:
  min_permissions: [usb:claim:vid=0x0694]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [lego-spike]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/lego-spike-plate-lesson }
  id: com.plate-studio.lego-spike-plate-lesson
""",
        "example-2": """
version: "1.0"
name: Plate Lab SPIKE Python
type: firmware
summary: Full LEGO SPIKE Prime Python project — drives a small data logger.
description: Python-flavored SPIKE Prime project.

platforms:
  lego-spike:
    generation: spike-prime
    language: python
    entry_file: project/main.py
    app_version: "3.4"

safety:
  min_permissions: [usb:claim:vid=0x0694]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [lego-spike]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/lego-spike-plate-logger }
  id: com.plate-studio.lego-spike-plate-logger
""",
    },
}

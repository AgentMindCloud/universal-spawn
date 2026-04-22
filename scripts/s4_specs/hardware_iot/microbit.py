"""micro:bit — MakeCode JSON / MicroPython (V1, V2)."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "microbit",
    "title": "micro:bit",
    "lede": (
        "BBC micro:bit ships projects via the MakeCode JSON format "
        "or as MicroPython scripts. A universal-spawn manifest pins "
        "the board variant (V1 / V2) and the toolchain."
    ),
    "cares": (
        "The board variant, toolchain (`makecode`, `micropython`), "
        "and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `cli-tool`, `library`."),
        ("platforms.microbit", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.microbit.variant", "`v1` or `v2`."),
        ("platforms.microbit.toolchain", "`makecode` or `micropython`."),
        ("platforms.microbit.entry_file", "Entry .json (MakeCode) or .py (MicroPython)."),
        ("platforms.microbit.makecode_share_url", "MakeCode share URL."),
    ],
    "platform_fields": {
        "variant": "Board variant.",
        "toolchain": "MakeCode or MicroPython.",
        "entry_file": "Entry file.",
        "makecode_share_url": "MakeCode share URL.",
    },
    "schema_body": schema_object(
        required=["variant", "toolchain"],
        properties={
            "variant": enum(["v1", "v2"]),
            "toolchain": enum(["makecode", "micropython"]),
            "entry_file": str_prop(),
            "makecode_share_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: micro:bit Template
type: firmware
description: Template for a micro:bit-targeted universal-spawn manifest.

platforms:
  microbit:
    variant: v2
    toolchain: makecode
    entry_file: src/project.json
    makecode_share_url: "https://makecode.microbit.org/_aaaaaa"

safety:
  min_permissions: [usb:claim:vid=0x0d28]

env_vars_required: []

deployment:
  targets: [microbit]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/microbit-template }
""",
    "native_config_name": "MakeCode JSON / .py file",
    "native_config_lang": "json",
    "native_config": """
{ "name": "Your Project", "main": "main.ts", "files": ["main.ts"] }
""",
    "universal_excerpt": """
platforms:
  microbit:
    variant: v2
    toolchain: makecode
    entry_file: src/project.json
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Pixel Lesson
type: firmware
summary: Minimal micro:bit MakeCode lesson — animates the parchment palette on the LED grid.
description: V2 board. MakeCode share URL provided.

platforms:
  microbit:
    variant: v2
    toolchain: makecode
    entry_file: src/lesson.json
    makecode_share_url: "https://makecode.microbit.org/_xyz123abc"

safety:
  min_permissions: [usb:claim:vid=0x0d28]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [microbit]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/microbit-plate-lesson }
  id: com.plate-studio.microbit-plate-lesson
""",
        "example-2": """
version: "1.0"
name: Plate Lab MicroPython
type: firmware
summary: Full micro:bit MicroPython project building a small data logger.
description: V2 board, MicroPython toolchain.

platforms:
  microbit:
    variant: v2
    toolchain: micropython
    entry_file: src/main.py

safety:
  min_permissions: [usb:claim:vid=0x0d28]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [microbit]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/microbit-plate-logger }
  id: com.plate-studio.microbit-plate-logger
""",
    },
}

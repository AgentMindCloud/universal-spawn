"""Arduino — sketches + libraries + flash-via-companion."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "arduino",
    "title": "Arduino",
    "lede": (
        "Arduino creations are sketches (`.ino`) or libraries "
        "(`library.properties`). A universal-spawn manifest pins the "
        "`kind`, the target boards, and (for `flash-via-companion`) "
        "the prebuilt binary URL that a companion app like Arduino "
        "Lab can flash directly via WebUSB."
    ),
    "cares": (
        "The `kind` (`sketch`, `library`, `flash-via-companion`), the "
        "FQBN board id, the required libraries, and the prebuilt "
        "binary URL when applicable."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `library`, `hardware-device`, `cli-tool`."),
        ("platforms.arduino", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.arduino.kind", "`sketch`, `library`, `flash-via-companion`."),
        ("platforms.arduino.fqbn", "Fully-Qualified Board Name."),
        ("platforms.arduino.entry_ino", "Sketch entry .ino (sketch)."),
        ("platforms.arduino.libraries", "Required Arduino libraries."),
        ("platforms.arduino.prebuilt_binary_url", "Prebuilt .bin / .hex URL (flash-via-companion)."),
    ],
    "platform_fields": {
        "kind": "`sketch`, `library`, `flash-via-companion`.",
        "fqbn": "Fully-Qualified Board Name.",
        "entry_ino": "Sketch entry .ino.",
        "libraries": "Required Arduino libraries.",
        "prebuilt_binary_url": "Prebuilt binary URL.",
    },
    "schema_body": schema_object(
        required=["kind", "fqbn"],
        properties={
            "kind": enum(["sketch", "library", "flash-via-companion"]),
            "fqbn": str_prop(pattern=r"^[a-z][a-z0-9_-]*:[a-z][a-z0-9_-]*:[A-Za-z][A-Za-z0-9_-]*$"),
            "entry_ino": str_prop(),
            "libraries": {"type": "array", "items": str_prop()},
            "prebuilt_binary_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Arduino Template
type: firmware
description: Template for an Arduino-targeted universal-spawn manifest.

platforms:
  arduino:
    kind: sketch
    fqbn: "arduino:avr:uno"
    entry_ino: src/main.ino

safety:
  min_permissions: [usb:claim:vid=0x2341]

env_vars_required: []

deployment:
  targets: [arduino]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/arduino-template }
""",
    "native_config_name": "library.properties + .ino",
    "native_config_lang": "properties",
    "native_config": """
name=YourLibrary
version=0.1.0
author=yourhandle
sentence=Short description.
paragraph=Longer description.
architectures=avr,esp32,esp8266
""",
    "universal_excerpt": """
platforms:
  arduino:
    kind: sketch
    fqbn: "arduino:avr:uno"
    entry_ino: src/main.ino
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor Sketch
type: firmware
summary: Minimal Arduino sketch for an Uno reading a parchment-grade humidity sensor.
description: Uno target. Single .ino. One library dependency.

platforms:
  arduino:
    kind: sketch
    fqbn: "arduino:avr:uno"
    entry_ino: src/plate_sensor.ino
    libraries: [Adafruit_Sensor]

safety:
  min_permissions: [usb:claim:vid=0x2341]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [arduino]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/arduino-plate-sensor }
  id: com.plate-studio.arduino-plate-sensor
""",
        "flash-via-companion": """
version: "1.0"
name: Plate Sensor Flash-via-Companion
type: firmware
summary: Full Arduino flash-via-companion manifest — companion app pulls the prebuilt .hex and flashes via WebUSB.
description: >
  Companion installer (Arduino Lab, web flasher) reads this manifest,
  downloads the prebuilt binary from `prebuilt_binary_url`, and
  flashes it onto the target board over WebUSB. No local toolchain.

platforms:
  arduino:
    kind: flash-via-companion
    fqbn: "arduino:avr:uno"
    prebuilt_binary_url: "https://releases.plate.example/plate-sensor.hex"

safety:
  min_permissions: [usb:claim:vid=0x2341]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [arduino]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/arduino-plate-sensor-flash }
  id: com.plate-studio.arduino-plate-sensor-flash
""",
    },
}

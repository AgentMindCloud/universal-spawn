"""CircuitPython — code.py + lib/."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "circuitpython",
    "title": "CircuitPython",
    "lede": (
        "CircuitPython runs `code.py` from the device's USB drive. A "
        "universal-spawn manifest pins the board, the entry script, "
        "and any community-bundle libraries needed."
    ),
    "cares": (
        "The board id, entry script, and required Adafruit Bundle "
        "libraries."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `library`, `cli-tool`."),
        ("platforms.circuitpython", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.circuitpython.board", "Board id."),
        ("platforms.circuitpython.entry_script", "Entry script (`code.py`)."),
        ("platforms.circuitpython.bundle_libraries", "Adafruit Bundle libraries."),
    ],
    "platform_fields": {
        "board": "Board id.",
        "entry_script": "Entry script.",
        "bundle_libraries": "Adafruit Bundle libraries.",
    },
    "schema_body": schema_object(
        required=["board"],
        properties={
            "board": str_prop(pattern=r"^[a-z0-9][a-z0-9_-]+$"),
            "entry_script": str_prop(),
            "bundle_libraries": {"type": "array", "items": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: CircuitPython Template
type: firmware
description: Template for a CircuitPython-targeted universal-spawn manifest.

platforms:
  circuitpython:
    board: adafruit_qtpy_esp32s3_n4r2
    entry_script: code.py
    bundle_libraries: [adafruit_bus_device, adafruit_dht]

safety:
  min_permissions: [usb:claim]

env_vars_required: []

deployment:
  targets: [circuitpython]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/circuitpython-template }
""",
    "native_config_name": "code.py + lib/",
    "native_config_lang": "python",
    "native_config": """
# code.py — runs on every boot
import board, time
print("hello from CircuitPython on", board.board_id)
""",
    "universal_excerpt": """
platforms:
  circuitpython:
    board: adafruit_qtpy_esp32s3_n4r2
    entry_script: code.py
    bundle_libraries: [adafruit_bus_device, adafruit_dht]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor CircuitPython
type: firmware
summary: Minimal CircuitPython sketch reading a humidity sensor.
description: One code.py + two bundle libraries.

platforms:
  circuitpython:
    board: adafruit_qtpy_esp32s3_n4r2
    entry_script: code.py
    bundle_libraries: [adafruit_bus_device, adafruit_dht]

safety:
  min_permissions: [usb:claim]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [circuitpython]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/circuitpython-plate-sensor }
  id: com.plate-studio.circuitpython-plate-sensor
""",
        "example-2": """
version: "1.0"
name: Plate Pixel Frame
type: firmware
summary: Full CircuitPython project animating a NeoPixel parchment frame.
description: Pico W board + four bundle libraries.

platforms:
  circuitpython:
    board: raspberry_pi_pico_w
    entry_script: code.py
    bundle_libraries: [adafruit_bus_device, neopixel, adafruit_led_animation, adafruit_requests]

safety:
  min_permissions: [usb:claim, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [circuitpython]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/circuitpython-plate-pixel-frame }
  id: com.plate-studio.circuitpython-plate-pixel-frame
""",
    },
}

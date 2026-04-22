"""MicroPython — main.py + boot.py + frozen modules."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "micropython",
    "title": "MicroPython",
    "lede": (
        "MicroPython runs `main.py` on first boot. A universal-spawn "
        "manifest pins the target port, the entry script, and the "
        "frozen module list."
    ),
    "cares": (
        "Target MicroPython port, entry script, frozen modules, "
        "and required libraries."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `library`, `cli-tool`."),
        ("platforms.micropython", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.micropython.port", "MicroPython port."),
        ("platforms.micropython.entry_script", "Entry script."),
        ("platforms.micropython.frozen_modules", "Frozen modules."),
        ("platforms.micropython.libraries", "mip-installable libraries."),
    ],
    "platform_fields": {
        "port": "MicroPython port.",
        "entry_script": "Entry script.",
        "frozen_modules": "Frozen modules.",
        "libraries": "mip-installable libraries.",
    },
    "schema_body": schema_object(
        required=["port"],
        properties={
            "port": enum(["esp32", "esp8266", "rp2", "stm32", "samd", "nrf", "mimxrt", "renesas-ra", "unix"]),
            "entry_script": str_prop(),
            "frozen_modules": {"type": "array", "items": str_prop()},
            "libraries": {"type": "array", "items": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: MicroPython Template
type: firmware
description: Template for a MicroPython-targeted universal-spawn manifest.

platforms:
  micropython:
    port: rp2
    entry_script: src/main.py

safety:
  min_permissions: [usb:claim]

env_vars_required: []

deployment:
  targets: [micropython]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/micropython-template }
""",
    "native_config_name": "main.py + boot.py + (optional) manifest.py",
    "native_config_lang": "python",
    "native_config": """
# main.py runs on every boot.
print("hello from MicroPython")
""",
    "universal_excerpt": """
platforms:
  micropython:
    port: rp2
    entry_script: src/main.py
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor MicroPython
type: firmware
summary: Minimal MicroPython sensor sketch on a Pico (rp2 port).
description: Single main.py.

platforms:
  micropython:
    port: rp2
    entry_script: src/main.py
    libraries: ["github:peterhinch/micropython-async"]

safety:
  min_permissions: [usb:claim]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [micropython]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/micropython-plate-sensor }
  id: com.plate-studio.micropython-plate-sensor
""",
        "example-2": """
version: "1.0"
name: Plate Sensor Frozen Build
type: firmware
summary: Full MicroPython firmware build with frozen modules for an ESP32.
description: Custom-built firmware with two frozen modules.

platforms:
  micropython:
    port: esp32
    entry_script: src/main.py
    frozen_modules: [src/sensor, src/wifi_setup]

safety:
  min_permissions: [usb:claim:vid=0x303a]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [micropython]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/micropython-plate-frozen }
  id: com.plate-studio.micropython-plate-frozen
""",
    },
}

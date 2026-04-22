"""PlatformIO — platformio.ini build environments."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "platform-io",
    "title": "PlatformIO",
    "lede": (
        "PlatformIO drives embedded builds via `platformio.ini`. A "
        "universal-spawn manifest pins the entry environment, the "
        "board, and the framework."
    ),
    "cares": (
        "The active environment, board, framework, and library deps."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `library`, `cli-tool`."),
        ("platforms.platform-io", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.platform-io.entry_env", "platformio.ini env name."),
        ("platforms.platform-io.board", "Board id."),
        ("platforms.platform-io.framework", "Framework."),
        ("platforms.platform-io.libraries", "Library deps."),
    ],
    "platform_fields": {
        "entry_env": "platformio.ini env.",
        "board": "Board id.",
        "framework": "Framework.",
        "libraries": "Library deps.",
    },
    "schema_body": schema_object(
        required=["entry_env", "board"],
        properties={
            "entry_env": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "board": str_prop(pattern=r"^[a-z0-9][a-z0-9_-]+$"),
            "framework": enum(["arduino", "espidf", "mbed", "stm32cube", "zephyr", "nuttx"]),
            "libraries": {"type": "array", "items": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: PlatformIO Template
type: firmware
description: Template for a PlatformIO-targeted universal-spawn manifest.

platforms:
  platform-io:
    entry_env: esp32-s3-devkitc-1
    board: esp32-s3-devkitc-1
    framework: arduino

safety:
  min_permissions: [usb:claim:vid=0x303a]

env_vars_required: []

deployment:
  targets: [platform-io]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/platform-io-template }
""",
    "native_config_name": "platformio.ini",
    "native_config_lang": "ini",
    "native_config": """
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
""",
    "universal_excerpt": """
platforms:
  platform-io:
    entry_env: esp32-s3-devkitc-1
    board: esp32-s3-devkitc-1
    framework: arduino
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor PlatformIO
type: firmware
summary: Minimal PlatformIO manifest building plate-sensor firmware for an ESP32-S3.
description: Single env. Arduino framework.

platforms:
  platform-io:
    entry_env: esp32-s3-devkitc-1
    board: esp32-s3-devkitc-1
    framework: arduino
    libraries: ["adafruit/Adafruit Unified Sensor"]

safety:
  min_permissions: [usb:claim:vid=0x303a]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [platform-io]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/platformio-plate-sensor }
  id: com.plate-studio.platformio-plate-sensor
""",
        "example-2": """
version: "1.0"
name: Plate Logger PlatformIO STM32
type: firmware
summary: Full PlatformIO firmware for an STM32 logger via the stm32cube framework.
description: STM32 board with stm32cube framework.

platforms:
  platform-io:
    entry_env: stm32-logger
    board: nucleo_f767zi
    framework: stm32cube

safety:
  min_permissions: [usb:claim:vid=0x0483]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [platform-io]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/platformio-stm32-logger }
  id: com.plate-studio.platformio-stm32-logger
""",
    },
}

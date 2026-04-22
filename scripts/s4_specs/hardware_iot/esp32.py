"""ESP32 — partitions, OTA, esptool / esptool-js."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "esp32",
    "title": "ESP32",
    "lede": (
        "ESP32 firmware ships with a partition table and (often) an "
        "OTA channel. A universal-spawn manifest pins the chip "
        "variant, the partition CSV, and (for `flash-via-companion`) "
        "the prebuilt binary URL that esptool-js can flash via WebSerial."
    ),
    "cares": (
        "The chip variant, partition CSV, framework (`arduino`, "
        "`esp-idf`, `nuttx`), the OTA channel, and the prebuilt "
        "binary URL when applicable."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `hardware-device`."),
        ("platforms.esp32", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.esp32.kind", "`firmware` or `flash-via-companion`."),
        ("platforms.esp32.chip", "Chip variant."),
        ("platforms.esp32.framework", "Build framework."),
        ("platforms.esp32.partitions_csv", "Partition CSV path."),
        ("platforms.esp32.ota_channel", "OTA channel name."),
        ("platforms.esp32.prebuilt_binary_url", "Prebuilt .bin URL."),
    ],
    "platform_fields": {
        "kind": "`firmware` or `flash-via-companion`.",
        "chip": "Chip variant (`esp32`, `esp32-c3`, `esp32-s3`, `esp32-c6`, `esp32-h2`).",
        "framework": "`arduino`, `esp-idf`, `nuttx`.",
        "partitions_csv": "Partition CSV.",
        "ota_channel": "OTA channel.",
        "prebuilt_binary_url": "Prebuilt binary URL.",
    },
    "schema_body": schema_object(
        required=["kind", "chip"],
        properties={
            "kind": enum(["firmware", "flash-via-companion"]),
            "chip": enum(["esp32", "esp32-c3", "esp32-s2", "esp32-s3", "esp32-c6", "esp32-h2", "esp32-p4"]),
            "framework": enum(["arduino", "esp-idf", "nuttx", "zephyr"]),
            "partitions_csv": str_prop(),
            "ota_channel": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            "prebuilt_binary_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: ESP32 Template
type: firmware
description: Template for an ESP32-targeted universal-spawn manifest.

platforms:
  esp32:
    kind: firmware
    chip: esp32-s3
    framework: esp-idf
    partitions_csv: partitions.csv
    ota_channel: stable

safety:
  min_permissions: [usb:claim:vid=0x303a]

env_vars_required: []

deployment:
  targets: [esp32]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/esp32-template }
""",
    "native_config_name": "platformio.ini + partitions.csv + sdkconfig",
    "native_config_lang": "ini",
    "native_config": """
[env:esp32-s3-devkitc-1]
platform = espressif32
board = esp32-s3-devkitc-1
framework = espidf
board_build.partitions = partitions.csv
""",
    "universal_excerpt": """
platforms:
  esp32:
    kind: firmware
    chip: esp32-s3
    framework: esp-idf
    partitions_csv: partitions.csv
    ota_channel: stable
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor Firmware
type: firmware
summary: Minimal ESP32-C3 firmware reading a humidity sensor.
description: Arduino framework. Single partition CSV. Stable OTA channel.

platforms:
  esp32:
    kind: firmware
    chip: esp32-c3
    framework: arduino
    partitions_csv: partitions.csv
    ota_channel: stable

safety:
  min_permissions: [usb:claim:vid=0x303a]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [esp32]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/esp32-plate-sensor }
  id: com.plate-studio.esp32-plate-sensor
""",
        "flash-via-companion": """
version: "1.0"
name: Plate Sensor Web-Flasher
type: firmware
summary: Full ESP32-S3 flash-via-companion manifest — esptool-js flashes the prebuilt binary over WebSerial.
description: >
  Companion installer (esptool-js in browser) reads this manifest,
  downloads the prebuilt .bin, and flashes the device over WebSerial
  with no local toolchain required.

platforms:
  esp32:
    kind: flash-via-companion
    chip: esp32-s3
    prebuilt_binary_url: "https://releases.plate.example/plate-sensor-esp32s3.bin"

safety:
  min_permissions: [usb:claim:vid=0x303a]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [esp32]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/esp32-plate-sensor-flash }
  id: com.plate-studio.esp32-plate-sensor-flash
""",
    },
}

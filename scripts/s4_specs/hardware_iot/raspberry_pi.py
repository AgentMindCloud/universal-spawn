"""Raspberry Pi — images, overlays, scripts."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "raspberry-pi",
    "title": "Raspberry Pi",
    "lede": (
        "Raspberry Pi creations are SD-card images, dt-overlays, or "
        "first-boot scripts. A universal-spawn manifest pins the "
        "Pi model, OS image, and the install method."
    ),
    "cares": (
        "The Pi model, OS image, the install method (`image-flash`, "
        "`overlay`, `script`), and the entry file."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`firmware`, `hardware-device`, `cli-tool`."),
        ("platforms.raspberry-pi", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.raspberry-pi.model", "`pi-1`, `pi-2`, ..., `pi-5`, `compute-module-4`, `pico`, `pico-2`, `pico-w`."),
        ("platforms.raspberry-pi.os", "`raspberry-pi-os`, `raspberry-pi-os-lite`, `ubuntu`, `dietpi`, `none`."),
        ("platforms.raspberry-pi.install_method", "`image-flash`, `overlay`, `script`."),
        ("platforms.raspberry-pi.image_url", "Image URL for image-flash installs."),
        ("platforms.raspberry-pi.entry_file", "Entry file for overlay / script installs."),
    ],
    "platform_fields": {
        "model": "Pi model.",
        "os": "OS image.",
        "install_method": "Install method.",
        "image_url": "Image URL.",
        "entry_file": "Entry file.",
    },
    "schema_body": schema_object(
        required=["model", "install_method"],
        properties={
            "model": enum(["pi-1", "pi-2", "pi-3", "pi-4", "pi-5", "compute-module-4", "compute-module-5", "pico", "pico-2", "pico-w", "pico-2-w", "zero", "zero-2-w"]),
            "os": enum(["raspberry-pi-os", "raspberry-pi-os-lite", "ubuntu", "dietpi", "none"]),
            "install_method": enum(["image-flash", "overlay", "script"]),
            "image_url": {"type": "string", "format": "uri"},
            "entry_file": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Raspberry Pi Template
type: firmware
description: Template for a Raspberry-Pi-targeted universal-spawn manifest.

platforms:
  raspberry-pi:
    model: pi-5
    os: raspberry-pi-os
    install_method: script
    entry_file: install.sh

safety:
  min_permissions: [fs:write, network:outbound]

env_vars_required: []

deployment:
  targets: [raspberry-pi]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/raspberry-pi-template }
""",
    "native_config_name": "config.txt + cmdline.txt + cloud-init",
    "native_config_lang": "ini",
    "native_config": """
[all]
gpu_mem=128
dtparam=audio=on
""",
    "universal_excerpt": """
platforms:
  raspberry-pi:
    model: pi-5
    os: raspberry-pi-os
    install_method: script
    entry_file: install.sh
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Pi Install Script
type: cli-tool
summary: Minimal first-boot install script for a Pi 5.
description: Bash script run after first boot; installs the parchment dashboard.

platforms:
  raspberry-pi:
    model: pi-5
    os: raspberry-pi-os
    install_method: script
    entry_file: install.sh

safety:
  min_permissions: [fs:write, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [raspberry-pi]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/raspberry-pi-plate-install }
  id: com.plate-studio.raspberry-pi-plate-install
""",
        "example-2": """
version: "1.0"
name: Plate OS Image
type: firmware
summary: Full prebuilt SD-card image for a Pi Zero 2 W kiosk display.
description: Distributed as a flashable .img.xz at a hosted URL. dietpi base.

platforms:
  raspberry-pi:
    model: zero-2-w
    os: dietpi
    install_method: image-flash
    image_url: "https://releases.plate.example/plate-kiosk.img.xz"

safety:
  min_permissions: [fs:write, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [raspberry-pi]

visuals: { palette: parchment }

metadata:
  license: GPL-3.0-only
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/raspberry-pi-kiosk-image }
  id: com.plate-studio.raspberry-pi-kiosk-image
""",
    },
}

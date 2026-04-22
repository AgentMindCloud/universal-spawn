"""Home Assistant — integrations + blueprints."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "home-assistant",
    "title": "Home Assistant",
    "lede": (
        "Home Assistant integrations live in `custom_components/`; "
        "blueprints under `blueprints/`. A universal-spawn manifest "
        "maps onto either, and explicitly mirrors the integration's "
        "`manifest.json` fields (`domain`, `iot_class`, "
        "`requirements`, `dependencies`)."
    ),
    "cares": (
        "The `kind` (`integration`, `blueprint`), the integration "
        "domain, IoT class, and dependencies."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `workflow`, `hardware-device`."),
        ("platforms.home-assistant", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.home-assistant.kind", "`integration` or `blueprint`."),
        ("platforms.home-assistant.domain", "Integration domain."),
        ("platforms.home-assistant.iot_class", "Integration IoT class."),
        ("platforms.home-assistant.requirements", "Python requirements."),
        ("platforms.home-assistant.dependencies", "HA component dependencies."),
        ("platforms.home-assistant.blueprint_kind", "Blueprint kind (blueprint)."),
    ],
    "platform_fields": {
        "kind": "`integration` or `blueprint`.",
        "domain": "Integration domain.",
        "iot_class": "IoT class.",
        "requirements": "Python requirements.",
        "dependencies": "HA component dependencies.",
        "blueprint_kind": "Blueprint kind.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["integration", "blueprint"]),
            "domain": str_prop(pattern=r"^[a-z][a-z0-9_]{0,63}$"),
            "iot_class": enum(["assumed_state", "cloud_polling", "cloud_push", "local_polling", "local_push", "calculated"]),
            "requirements": {"type": "array", "items": str_prop()},
            "dependencies": {"type": "array", "items": str_prop()},
            "blueprint_kind": enum(["automation", "script", "template"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Home Assistant Template
type: extension
description: Template for a Home-Assistant-targeted universal-spawn manifest.

platforms:
  home-assistant:
    kind: integration
    domain: your_integration
    iot_class: local_push
    requirements: ["aiohttp>=3.9"]

safety:
  min_permissions: [network:outbound]

env_vars_required: []

deployment:
  targets: [home-assistant]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/home-assistant-template }
""",
    "native_config_name": "custom_components/<domain>/manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "domain": "your_integration",
  "name": "Your Integration",
  "version": "0.1.0",
  "iot_class": "local_push",
  "requirements": ["aiohttp>=3.9"],
  "dependencies": [],
  "codeowners": ["@yourhandle"]
}
""",
    "universal_excerpt": """
platforms:
  home-assistant:
    kind: integration
    domain: your_integration
    iot_class: local_push
    requirements: ["aiohttp>=3.9"]
    dependencies: []
""",
    "compatibility_extras": (
        "## Mapping to Home Assistant manifest.json\n\n"
        "| `platforms.home-assistant.*` | `custom_components/<domain>/manifest.json` |\n"
        "|---|---|\n"
        "| `domain`        | `domain`        |\n"
        "| `iot_class`     | `iot_class`     |\n"
        "| `requirements`  | `requirements`  |\n"
        "| `dependencies`  | `dependencies`  |\n"
        "\n"
        "A consumer SHOULD generate `manifest.json` from these fields "
        "if it is missing."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sensor Integration
type: extension
summary: Minimal Home Assistant integration for a parchment-grade humidity sensor.
description: Local-push IoT class. One Python requirement.

platforms:
  home-assistant:
    kind: integration
    domain: plate_sensor
    iot_class: local_push
    requirements: ["aiohttp>=3.9"]
    dependencies: []

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [home-assistant]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/home-assistant-plate-sensor }
  id: com.plate-studio.home-assistant-plate-sensor
""",
        "example-2": """
version: "1.0"
name: Plate Lab Automation Blueprint
type: workflow
summary: Full Home Assistant automation blueprint that flips the lab lights to parchment colors.
description: Automation blueprint imported via the blueprint URL.

platforms:
  home-assistant:
    kind: blueprint
    blueprint_kind: automation

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [home-assistant]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/home-assistant-plate-blueprint }
  id: com.plate-studio.home-assistant-plate-blueprint
""",
    },
}

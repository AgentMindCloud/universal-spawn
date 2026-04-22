"""JetBrains — IntelliJ platform plugins."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "jetbrains",
    "title": "JetBrains",
    "lede": (
        "JetBrains' Marketplace hosts plugins for the IntelliJ "
        "Platform (IDEA, PyCharm, WebStorm, GoLand, RustRover, Rider, "
        "CLion, etc). A universal-spawn manifest targets one plugin "
        "with its plugin id, compatible IDE set, and the compatibility "
        "range (`sinceBuild` / `untilBuild`)."
    ),
    "cares": (
        "The plugin id, the compatible IDEs, and the IntelliJ build "
        "range."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`."),
        ("platforms.jetbrains", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.jetbrains.plugin_id", "Plugin id."),
        ("platforms.jetbrains.ides", "Compatible IDEs."),
        ("platforms.jetbrains.since_build", "IntelliJ since-build."),
        ("platforms.jetbrains.until_build", "Optional until-build."),
        ("platforms.jetbrains.marketplace_id", "Numeric Marketplace id (if listed)."),
    ],
    "platform_fields": {
        "plugin_id": "Plugin id.",
        "ides": "Compatible IDEs.",
        "since_build": "sinceBuild.",
        "until_build": "untilBuild.",
        "marketplace_id": "Numeric Marketplace id.",
    },
    "schema_body": schema_object(
        required=["plugin_id", "ides", "since_build"],
        properties={
            "plugin_id": str_prop(pattern=r"^[a-z][a-z0-9.-]*\.[a-z][a-z0-9-]*$"),
            "ides": {
                "type": "array",
                "minItems": 1,
                "items": enum(["idea", "pycharm", "webstorm", "goland", "rustrover", "rider", "clion", "appcode", "rubymine", "phpstorm", "datagrip", "datasPell", "aqua", "writerside"]),
            },
            "since_build": str_prop(pattern=r"^[0-9]+(\.([0-9]+|\*))+$"),
            "until_build": str_prop(pattern=r"^[0-9]+(\.([0-9]+|\*))+$"),
            "marketplace_id": {"type": "integer", "minimum": 1},
        },
    ),
    "template_yaml": """
version: "1.0"
name: JetBrains Template
type: extension
description: Template for a JetBrains-targeted universal-spawn manifest.

platforms:
  jetbrains:
    plugin_id: com.yourhandle.yourplugin
    ides: [idea, pycharm, webstorm]
    since_build: "243.0"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [jetbrains]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/jetbrains-template }
""",
    "native_config_name": "plugin.xml",
    "native_config_lang": "xml",
    "native_config": """
<idea-plugin>
  <id>com.yourhandle.yourplugin</id>
  <name>Your Plugin</name>
  <vendor>Your Name</vendor>
  <idea-version since-build="243.0"/>
  <depends>com.intellij.modules.platform</depends>
</idea-plugin>
""",
    "universal_excerpt": """
platforms:
  jetbrains:
    plugin_id: com.yourhandle.yourplugin
    ides: [idea, pycharm, webstorm]
    since_build: "243.0"
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Color Scheme
type: extension
summary: Minimal JetBrains color scheme matching the Residual Frequencies palette.
description: Single plugin exposing one color scheme.

platforms:
  jetbrains:
    plugin_id: com.plate-studio.parchment-scheme
    ides: [idea, pycharm, webstorm, goland, rustrover, rider]
    since_build: "243.0"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [jetbrains]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/jetbrains-parchment-scheme }
  id: com.plate-studio.jetbrains-parchment-scheme
""",
        "example-2": """
version: "1.0"
name: Lab Notebook Inspector
type: plugin
summary: Full JetBrains plugin that inspects Markdown lab-notebooks in-editor.
description: >
  Plugin for IDEA + PyCharm + WebStorm that inspects Markdown files
  against the Residual Frequencies lab-notebook rubric. Listed on the
  Marketplace.

platforms:
  jetbrains:
    plugin_id: com.plate-studio.lab-notebook-inspector
    ides: [idea, pycharm, webstorm]
    since_build: "243.0"
    until_build: "252.*"
    marketplace_id: 24001

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [jetbrains]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/jetbrains-lab-notebook-inspector }
  id: com.plate-studio.jetbrains-lab-notebook-inspector
""",
    },
}

"""itch.io — html5 + downloadable + .itch.toml channel pinning."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "itch-io",
    "title": "itch.io",
    "lede": (
        "itch.io publishes html5, downloadable, and physical games. "
        "A universal-spawn manifest pins the kind, the butler "
        "channel, and the html5 frame settings (for in-browser games)."
    ),
    "cares": (
        "The `kind` (`html5`, `downloadable`, `physical`), the "
        "butler channel, and html5 frame settings."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-world`, `web-app`, `creative-tool`."),
        ("platforms.itch-io", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.itch-io.kind", "`html5`, `downloadable`, `physical`."),
        ("platforms.itch-io.butler_channel", "butler channel."),
        ("platforms.itch-io.html5_frame", "html5 frame size + fullscreen."),
        ("platforms.itch-io.payment", "Payment kind."),
    ],
    "platform_fields": {
        "kind": "`html5`, `downloadable`, or `physical`.",
        "butler_channel": "butler channel.",
        "html5_frame": "html5 frame settings.",
        "payment": "Payment kind.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["html5", "downloadable", "physical"]),
            "butler_channel": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            "html5_frame": schema_object(
                properties={
                    "width": {"type": "integer", "minimum": 320, "maximum": 3840},
                    "height": {"type": "integer", "minimum": 240, "maximum": 2160},
                    "fullscreen_button": bool_prop(True),
                    "mobile_friendly": bool_prop(False),
                },
            ),
            "payment": enum(["free", "name-your-price", "fixed", "hidden"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: itch.io Template
type: game-world
description: Template for an itch.io-targeted universal-spawn manifest.

platforms:
  itch-io:
    kind: html5
    butler_channel: web
    html5_frame: { width: 1280, height: 720, fullscreen_button: true, mobile_friendly: true }
    payment: free

safety:
  min_permissions: [network:inbound]

env_vars_required: []

deployment:
  targets: [itch-io]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/itch-io-template }
""",
    "native_config_name": ".itch.toml + butler push",
    "native_config_lang": "toml",
    "native_config": """
[[actions]]
name = "play"
path = "index.html"

[[prereqs]]
name = "webview"
""",
    "universal_excerpt": """
platforms:
  itch-io:
    kind: html5
    butler_channel: web
    html5_frame: { width: 1280, height: 720, fullscreen_button: true }
""",
    "compatibility_extras": "",
    "examples": {
        "web-build": """
version: "1.0"
name: Plate Lab Web Build
type: game-world
summary: Minimal itch.io HTML5 web build of the Parchment Lab demo.
description: Browser-playable build pushed to the `web` channel.

platforms:
  itch-io:
    kind: html5
    butler_channel: web
    html5_frame: { width: 1280, height: 720, fullscreen_button: true, mobile_friendly: true }
    payment: name-your-price

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [itch-io]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/itch-plate-web }
  id: com.plate-studio.itch-plate-web
""",
        "example-2": """
version: "1.0"
name: Plate Lab Native
type: game-world
summary: Full itch.io downloadable build for Windows + macOS + Linux.
description: Pushed via butler to three native channels.

platforms:
  itch-io:
    kind: downloadable
    butler_channel: stable
    payment: fixed

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required:
  - name: BUTLER_API_KEY
    description: butler API key.
    secret: true

deployment:
  targets: [itch-io]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/itch-plate-native }
  id: com.plate-studio.itch-plate-native
""",
    },
}

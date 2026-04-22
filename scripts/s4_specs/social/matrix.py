"""Matrix — appservice bridges + bots."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "matrix",
    "title": "Matrix",
    "lede": (
        "Matrix is the federated messaging protocol. A universal-spawn "
        "manifest declares a bot or an Application Service "
        "(appservice) bridge with its registration YAML."
    ),
    "cares": (
        "The `kind` (`bot`, `appservice`), the homeserver, the bot/"
        "appservice id, and (for appservice) the registration YAML "
        "path and namespaces."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `extension`, `workflow`."),
        ("platforms.matrix", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.matrix.kind", "`bot` or `appservice`."),
        ("platforms.matrix.homeserver", "Homeserver URL."),
        ("platforms.matrix.identifier", "MXID for bots, appservice id for bridges."),
        ("platforms.matrix.registration_file", "Appservice registration.yaml path."),
        ("platforms.matrix.namespaces", "Appservice user/alias/room namespaces."),
    ],
    "platform_fields": {
        "kind": "`bot` or `appservice`.",
        "homeserver": "Homeserver URL.",
        "identifier": "MXID or appservice id.",
        "registration_file": "Registration YAML path.",
        "namespaces": "Appservice namespaces.",
    },
    "schema_body": schema_object(
        required=["kind", "homeserver"],
        properties={
            "kind": enum(["bot", "appservice"]),
            "homeserver": {"type": "string", "format": "uri"},
            "identifier": str_prop(pattern=r"^[@!#][^:]+:[^/]+$|^[a-z][a-z0-9._-]*$"),
            "registration_file": str_prop(),
            "namespaces": schema_object(
                properties={
                    "users": {"type": "array", "items": str_prop()},
                    "aliases": {"type": "array", "items": str_prop()},
                    "rooms": {"type": "array", "items": str_prop()},
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Matrix Template
type: bot
description: Template for a Matrix-targeted universal-spawn manifest.

platforms:
  matrix:
    kind: bot
    homeserver: "https://matrix.org"
    identifier: "@yourbot:matrix.org"

safety:
  min_permissions: [network:outbound:matrix.org]

env_vars_required:
  - name: MATRIX_ACCESS_TOKEN
    description: Matrix access token.
    secret: true

deployment:
  targets: [matrix]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/matrix-template }
""",
    "native_config_name": "appservice registration.yaml",
    "native_config_lang": "yaml",
    "native_config": """
id: yourbridge
url: http://localhost:9000
as_token: REPLACE
hs_token: REPLACE
sender_localpart: bridgebot
namespaces:
  users:
    - { regex: "@_yourbridge_.*:matrix.org", exclusive: true }
""",
    "universal_excerpt": """
platforms:
  matrix:
    kind: appservice
    homeserver: "https://matrix.org"
    identifier: yourbridge
    registration_file: registration.yaml
    namespaces:
      users: ["@_yourbridge_.*:matrix.org"]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Matrix Bot
type: bot
summary: Minimal Matrix bot answering with the plate of the day.
description: Single bot account on matrix.org. Reads invites; replies in joined rooms.

platforms:
  matrix:
    kind: bot
    homeserver: "https://matrix.org"
    identifier: "@plate_studio:matrix.org"

safety:
  min_permissions: [network:outbound:matrix.org]
  safe_for_auto_spawn: false

env_vars_required:
  - name: MATRIX_ACCESS_TOKEN
    description: Bot access token.
    secret: true

deployment:
  targets: [matrix]

metadata:
  license: AGPL-3.0-only
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/matrix-plate-bot }
  id: com.plate-studio.matrix-plate-bot
""",
        "one-click-add": """
version: "1.0"
name: Discord Matrix Bridge
type: extension
summary: Full Matrix appservice bridge connecting Discord and Matrix.
description: >
  Appservice bridge with full namespace declaration. A consumer reads
  this manifest and renders a `matrix:r/discord-bridge` link that adds
  the bridge to a homeserver in one step.

platforms:
  matrix:
    kind: appservice
    homeserver: "https://matrix.example.org"
    identifier: discord-bridge
    registration_file: registration.yaml
    namespaces:
      users: ["@_discord_.*:matrix.example.org"]
      aliases: ["#_discord_.*:matrix.example.org"]

safety:
  min_permissions: [network:inbound, network:outbound:matrix.example.org, network:outbound:discord.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: AS_TOKEN
    description: Appservice token.
    secret: true
  - name: HS_TOKEN
    description: Homeserver token.
    secret: true
  - name: DISCORD_BOT_TOKEN
    description: Discord bot token.
    secret: true

deployment:
  targets: [matrix]

metadata:
  license: AGPL-3.0-only
  author: { name: Bridge Co., handle: bridge-co }
  source: { type: git, url: https://github.com/bridge-co/matrix-discord-bridge }
  id: com.bridge-co.matrix-discord-bridge
""",
    },
}

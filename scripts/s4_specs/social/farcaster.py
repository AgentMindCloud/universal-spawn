"""Farcaster — Frames v2 + mini-app manifest.json."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "farcaster",
    "title": "Farcaster",
    "lede": (
        "Farcaster ships Frames (interactive embeds) and mini-apps "
        "(`fc:miniapp` manifest). A universal-spawn manifest covers "
        "both and the bot account behind them."
    ),
    "cares": (
        "The `kind` (`frame`, `mini-app`, `bot`), the bot's FID, and "
        "the manifest URL for mini-apps."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `web-app`, `extension`."),
        ("platforms.farcaster", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.farcaster.kind", "`frame`, `mini-app`, `bot`."),
        ("platforms.farcaster.fid", "Farcaster FID."),
        ("platforms.farcaster.frame_url", "Frame entry URL."),
        ("platforms.farcaster.miniapp_url", "Mini-app manifest URL."),
        ("platforms.farcaster.signer_uuid", "Signer UUID for posting."),
    ],
    "platform_fields": {
        "kind": "`frame`, `mini-app`, `bot`.",
        "fid": "Farcaster FID.",
        "frame_url": "Frame entry URL.",
        "miniapp_url": "Mini-app manifest URL.",
        "signer_uuid": "Signer UUID.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["frame", "mini-app", "bot"]),
            "fid": {"type": "integer", "minimum": 1},
            "frame_url": {"type": "string", "format": "uri"},
            "miniapp_url": {"type": "string", "format": "uri"},
            "signer_uuid": str_prop(pattern=r"^[0-9a-fA-F-]{32,36}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Farcaster Template
type: bot
description: Template for a Farcaster-targeted universal-spawn manifest.

platforms:
  farcaster:
    kind: bot
    fid: 100000
    signer_uuid: "00000000-0000-0000-0000-000000000000"

safety:
  min_permissions: [network:outbound:hub.farcaster.xyz]

env_vars_required:
  - name: NEYNAR_API_KEY
    description: Neynar API key (or alternative Farcaster API).
    secret: true

deployment:
  targets: [farcaster]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/farcaster-template }
""",
    "native_config_name": "fc:miniapp manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "version": "1",
  "name": "Your Mini App",
  "iconUrl": "https://app.example/icon.png",
  "homeUrl": "https://app.example",
  "tags": ["miniapp"]
}
""",
    "universal_excerpt": """
platforms:
  farcaster:
    kind: mini-app
    miniapp_url: "https://app.example/.well-known/farcaster.json"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Frame
type: web-app
summary: Minimal Farcaster Frame that previews the plate of the day.
description: One Frame URL serving the plate-of-day preview.

platforms:
  farcaster:
    kind: frame
    frame_url: "https://frames.plate.example/today"

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [farcaster]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/farcaster-plate-frame }
  id: com.plate-studio.farcaster-plate-frame
""",
        "one-click-add": """
version: "1.0"
name: Plate Studio Mini App
type: web-app
summary: Full Farcaster mini-app with one-click add via the manifest URL.
description: >
  Full mini-app shipping a `.well-known/farcaster.json`. Clients pick
  up the manifest URL and offer a one-click "Add to Warpcast" flow.

platforms:
  farcaster:
    kind: mini-app
    miniapp_url: "https://miniapp.plate.example/.well-known/farcaster.json"

safety:
  min_permissions: [network:inbound, network:outbound:hub.farcaster.xyz]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [farcaster]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/farcaster-plate-miniapp }
  id: com.plate-studio.farcaster-plate-miniapp
""",
    },
}

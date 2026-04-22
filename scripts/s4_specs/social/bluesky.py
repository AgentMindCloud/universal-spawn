"""Bluesky — AT Protocol bots + custom feeds."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "bluesky",
    "title": "Bluesky",
    "lede": (
        "Bluesky runs on the AT Protocol. A universal-spawn manifest "
        "describes a bot account or a custom feed generator and pins "
        "the lexicon NSIDs the creation publishes."
    ),
    "cares": (
        "The `kind` (`bot`, `feed-generator`), the bot handle, the "
        "feed-generator service DID + record name, and the lexicon "
        "NSIDs the creation owns."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `extension`, `web-app`."),
        ("platforms.bluesky", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.bluesky.kind", "`bot` or `feed-generator`."),
        ("platforms.bluesky.handle", "Bluesky handle."),
        ("platforms.bluesky.service_did", "Service DID for feed-generators."),
        ("platforms.bluesky.feed_record", "Record name (rkey) for feed-generators."),
        ("platforms.bluesky.nsids", "Owned lexicon NSIDs."),
        ("platforms.bluesky.pds_url", "PDS URL (for self-hosted)."),
    ],
    "platform_fields": {
        "kind": "`bot` or `feed-generator`.",
        "handle": "Bluesky handle.",
        "service_did": "Service DID.",
        "feed_record": "Feed-generator record name.",
        "nsids": "Owned lexicon NSIDs.",
        "pds_url": "PDS URL.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["bot", "feed-generator"]),
            "handle": str_prop(pattern=r"^[a-z0-9][a-z0-9.-]+\.[a-z]+$"),
            "service_did": str_prop(pattern=r"^did:[a-z]+:[A-Za-z0-9._-]+$"),
            "feed_record": str_prop(pattern=r"^[a-z0-9][a-z0-9-]+$"),
            "nsids": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z][a-zA-Z0-9.-]+$"),
            },
            "pds_url": {"type": "string", "format": "uri"},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Bluesky Template
type: bot
description: Template for a Bluesky-targeted universal-spawn manifest.

platforms:
  bluesky:
    kind: bot
    handle: yourbot.bsky.social

safety:
  min_permissions: [network:outbound:bsky.social]

env_vars_required:
  - name: BLUESKY_APP_PASSWORD
    description: App password.
    secret: true

deployment:
  targets: [bluesky]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/bluesky-template }
""",
    "native_config_name": "AT Protocol lexicon JSON files",
    "native_config_lang": "json",
    "native_config": """
{
  "lexicon": 1,
  "id": "com.example.feed.getPlateFeed",
  "defs": {}
}
""",
    "universal_excerpt": """
platforms:
  bluesky:
    kind: feed-generator
    service_did: "did:web:feed.example.com"
    feed_record: plate-of-day
    nsids: ["com.example.feed.getPlateFeed"]
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Bluesky Bot
type: bot
summary: Minimal Bluesky bot posting the plate of the day.
description: One bot handle. Reads from a feed; posts daily.

platforms:
  bluesky:
    kind: bot
    handle: plate.bsky.social

safety:
  min_permissions: [network:outbound:bsky.social]
  safe_for_auto_spawn: false

env_vars_required:
  - name: BLUESKY_APP_PASSWORD
    description: App password.
    secret: true

deployment:
  targets: [bluesky]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/bluesky-plate-bot }
  id: com.plate-studio.bluesky-plate-bot
""",
        "example-2": """
version: "1.0"
name: Parchment Feed Generator
type: extension
summary: Full Bluesky feed generator surfacing parchment-style posts.
description: Custom feed generator with one record (`parchment-feed`) and an owned lexicon NSID.

platforms:
  bluesky:
    kind: feed-generator
    service_did: "did:web:feed.plate.example"
    feed_record: parchment-feed
    nsids: ["com.plate-studio.feed.getParchment"]
    pds_url: "https://bsky.social"

safety:
  min_permissions: [network:inbound, network:outbound:bsky.social]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [bluesky]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/bluesky-parchment-feed }
  id: com.plate-studio.bluesky-parchment-feed
""",
    },
}

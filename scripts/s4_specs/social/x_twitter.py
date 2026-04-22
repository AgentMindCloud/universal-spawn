"""X (Twitter) — bots via Grok + Developer Platform v2."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "x-twitter",
    "title": "X (Twitter)",
    "lede": (
        "X bots are built on the X Developer Platform v2 API and "
        "increasingly on Grok-for-X surfaces. A universal-spawn "
        "manifest declares the OAuth scopes, the bot account, and "
        "(when applicable) cross-links to the Grok extension that "
        "powers the AI side."
    ),
    "cares": (
        "The OAuth 2.0 scopes the bot needs, the X account handle, "
        "the API tier, and the optional Grok cross-link for AI-driven "
        "bots."
    ),
    "cross_links": (
        "AI-driven X bots typically pair `platforms.x-twitter` with "
        "`platforms.grok` from the AI subtree. See "
        "[`../../ai/grok/`](../../ai/grok/) for the model-side surface."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`bot`, `ai-agent`, `workflow`."),
        ("platforms.x-twitter", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.x-twitter.account", "Bot @-handle."),
        ("platforms.x-twitter.scopes", "OAuth 2.0 scopes."),
        ("platforms.x-twitter.tier", "API tier (`free`, `basic`, `pro`, `enterprise`)."),
        ("platforms.x-twitter.streams", "Filtered-stream rule files."),
        ("platforms.x-twitter.uses_grok", "True if the bot routes inference through Grok."),
    ],
    "platform_fields": {
        "account": "Bot @-handle.",
        "scopes": "OAuth 2.0 scopes.",
        "tier": "API tier.",
        "streams": "Filtered-stream rule files.",
        "uses_grok": "Routes inference through Grok.",
    },
    "schema_body": schema_object(
        required=["account", "scopes", "tier"],
        properties={
            "account": str_prop(pattern=r"^[A-Za-z0-9_]{1,15}$"),
            "scopes": {
                "type": "array",
                "minItems": 1,
                "items": enum(["tweet.read", "tweet.write", "users.read", "follows.read", "follows.write", "offline.access", "space.read", "mute.read", "mute.write", "like.read", "like.write", "list.read", "list.write", "block.read", "block.write", "bookmark.read", "bookmark.write", "dm.read", "dm.write"]),
            },
            "tier": enum(["free", "basic", "pro", "enterprise"]),
            "streams": {
                "type": "array",
                "items": str_prop(),
            },
            "uses_grok": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: X Bot Template
type: bot
description: Template for an X-targeted universal-spawn manifest.

platforms:
  x-twitter:
    account: yourbot
    scopes: [tweet.read, tweet.write, users.read, offline.access]
    tier: basic
    uses_grok: false

safety:
  min_permissions: [network:outbound:api.twitter.com, network:outbound:api.x.com]

env_vars_required:
  - name: X_OAUTH_CLIENT_ID
    description: X OAuth 2.0 client id.
    secret: false
  - name: X_OAUTH_CLIENT_SECRET
    description: X OAuth 2.0 client secret.
    secret: true

deployment:
  targets: [x-twitter]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/x-bot-template }
""",
    "native_config_name": "X Developer Portal app + OAuth 2.0 settings",
    "native_config_lang": "text",
    "native_config": "# Configured in the X Developer Portal; no repo-level config file by convention.\n",
    "universal_excerpt": """
platforms:
  x-twitter:
    account: yourbot
    scopes: [tweet.read, tweet.write]
    tier: basic
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Daily X Bot
type: bot
summary: Minimal X bot that posts the plate-of-the-day.
description: Pulls the daily plate from a feed and posts it. Basic API tier.

platforms:
  x-twitter:
    account: plateofday
    scopes: [tweet.write, users.read, offline.access]
    tier: basic

safety:
  min_permissions: [network:outbound:api.twitter.com, network:outbound:api.x.com]
  rate_limit_qps: 1
  safe_for_auto_spawn: false

env_vars_required:
  - name: X_OAUTH_CLIENT_ID
    description: OAuth client id.
  - name: X_OAUTH_CLIENT_SECRET
    description: OAuth client secret.
    secret: true

deployment:
  targets: [x-twitter]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/x-plate-daily }
  id: com.plate-studio.x-plate-daily
""",
        "example-2": """
version: "1.0"
name: Grok-Powered Reply Bot
type: ai-agent
summary: Full X bot that replies to mentions with Grok-generated answers.
description: >
  Listens to a filtered stream for mentions, generates replies through
  Grok-4-fast (see `../../ai/grok/`), and posts. Pro tier for the
  filtered-stream throughput.

platforms:
  x-twitter:
    account: gridreply
    scopes: [tweet.read, tweet.write, users.read, offline.access]
    tier: pro
    streams: [streams/mentions.json]
    uses_grok: true

safety:
  min_permissions:
    - network:outbound:api.twitter.com
    - network:outbound:api.x.com
    - network:outbound:api.x.ai
  rate_limit_qps: 5
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false

env_vars_required:
  - name: X_OAUTH_CLIENT_ID
    description: OAuth client id.
  - name: X_OAUTH_CLIENT_SECRET
    description: OAuth client secret.
    secret: true
  - name: XAI_API_KEY
    description: xAI API key for Grok.
    secret: true

deployment:
  targets: [x-twitter]

metadata:
  license: Apache-2.0
  author: { name: Reply Co., handle: reply-co }
  source: { type: git, url: https://github.com/reply-co/x-grok-reply-bot }
  id: com.reply-co.x-grok-reply-bot
""",
    },
}

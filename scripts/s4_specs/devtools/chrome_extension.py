"""Chrome extension — MV3 manifest + Web Store."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "chrome-extension",
    "title": "Chrome Extension",
    "lede": (
        "Chrome extensions use Manifest V3 (`manifest.json`). A "
        "universal-spawn manifest pins the declared permissions, "
        "host permissions, service-worker entry, and the Chrome Web "
        "Store id."
    ),
    "cares": (
        "The `manifest_version` (MV3 only), the declared "
        "`permissions[]` and `host_permissions[]`, the service-worker "
        "entry, and the Chrome Web Store id."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`."),
        ("platforms.chrome-extension", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.chrome-extension.manifest_version", "Must be 3."),
        ("platforms.chrome-extension.permissions", "Declared permissions."),
        ("platforms.chrome-extension.host_permissions", "Declared host permissions."),
        ("platforms.chrome-extension.service_worker", "Service-worker entry file."),
        ("platforms.chrome-extension.web_store_id", "Chrome Web Store id."),
        ("platforms.chrome-extension.min_chrome_version", "Minimum Chrome version."),
    ],
    "platform_fields": {
        "manifest_version": "MV3 (literal `3`).",
        "permissions": "Declared permissions.",
        "host_permissions": "Declared host permissions.",
        "service_worker": "Service-worker entry file.",
        "web_store_id": "Chrome Web Store id.",
        "min_chrome_version": "Minimum Chrome version.",
    },
    "schema_body": schema_object(
        required=["manifest_version"],
        properties={
            "manifest_version": {"const": 3},
            "permissions": {
                "type": "array",
                "items": enum(["activeTab", "alarms", "bookmarks", "clipboardRead", "clipboardWrite",
                               "contextMenus", "cookies", "downloads", "history", "identity",
                               "notifications", "scripting", "storage", "tabs", "webNavigation",
                               "webRequest", "offscreen", "sidePanel"]),
            },
            "host_permissions": {"type": "array", "items": str_prop()},
            "service_worker": str_prop(),
            "web_store_id": str_prop(pattern=r"^[a-p]{32}$"),
            "min_chrome_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)*$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Chrome Extension Template
type: extension
description: Template for a Chrome-extension-targeted universal-spawn manifest.

platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [storage, sidePanel]
    host_permissions: ["https://example.com/*"]
    service_worker: background.js
    min_chrome_version: "120"

safety:
  min_permissions: [network:outbound:example.com, clipboard:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [chrome-extension]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/chrome-extension-template }
""",
    "native_config_name": "manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "manifest_version": 3,
  "name": "Your Extension",
  "version": "0.1.0",
  "permissions": ["storage", "sidePanel"],
  "host_permissions": ["https://example.com/*"],
  "background": { "service_worker": "background.js" },
  "minimum_chrome_version": "120"
}
""",
    "universal_excerpt": """
platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [storage, sidePanel]
    host_permissions: ["https://example.com/*"]
    service_worker: background.js
    min_chrome_version: "120"
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Reader
type: extension
summary: Minimal Chrome extension recoloring readable pages to the parchment palette.
description: Side-panel button; no host permissions beyond content-script injection on the active tab.

platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [activeTab, sidePanel, storage]
    service_worker: background.js
    min_chrome_version: "120"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [chrome-extension]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/chrome-parchment-reader }
  id: com.plate-studio.chrome-parchment-reader
""",
        "example-2": """
version: "1.0"
name: Receipt Catcher
type: extension
summary: Full Chrome extension that catches receipts from three vendor sites and forwards them.
description: >
  Listed on the Web Store. Declares narrow host permissions for three
  vendor domains; forwards captured receipts to a private endpoint
  over HTTPS.

platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [activeTab, storage, scripting, webRequest]
    host_permissions:
      - "https://vendor-a.example.com/*"
      - "https://vendor-b.example.com/*"
      - "https://vendor-c.example.com/*"
    service_worker: dist/background.js
    web_store_id: "abcdefghijklmnopabcdefghijklmnop"
    min_chrome_version: "120"

safety:
  min_permissions:
    - network:outbound:vendor-a.example.com
    - network:outbound:vendor-b.example.com
    - network:outbound:vendor-c.example.com
    - network:outbound:api.receipts.example
  safe_for_auto_spawn: false

env_vars_required:
  - name: RECEIPTS_API_TOKEN
    description: API token stored via the identity permission.
    secret: true

deployment:
  targets: [chrome-extension]

metadata:
  license: proprietary
  author: { name: Receipts Co., handle: receipts-co }
  source: { type: git, url: https://github.com/receipts-co/chrome-receipt-catcher }
  id: com.receipts-co.chrome-receipt-catcher
""",
    },
}

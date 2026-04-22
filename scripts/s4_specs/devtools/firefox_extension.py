"""Firefox extension — WebExtensions + AMO (addons.mozilla.org)."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "firefox-extension",
    "title": "Firefox Extension",
    "lede": (
        "Firefox extensions use the WebExtensions API with `manifest.json`. "
        "Firefox supports both MV2 and MV3. A universal-spawn manifest "
        "pins the manifest version, permissions, and the AMO slug."
    ),
    "cares": (
        "`manifest_version` (2 or 3), `permissions[]`, "
        "`host_permissions[]`, the background script or service worker, "
        "and the AMO slug."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`."),
        ("platforms.firefox-extension", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.firefox-extension.manifest_version", "`2` or `3`."),
        ("platforms.firefox-extension.amo_slug", "AMO slug."),
        ("platforms.firefox-extension.gecko_id", "Firefox gecko id."),
        ("platforms.firefox-extension.permissions", "Declared permissions."),
        ("platforms.firefox-extension.host_permissions", "Declared host permissions."),
        ("platforms.firefox-extension.background_script", "Background script path."),
        ("platforms.firefox-extension.strict_min_version", "Minimum Firefox version."),
    ],
    "platform_fields": {
        "manifest_version": "`2` or `3`.",
        "amo_slug": "AMO slug.",
        "gecko_id": "Firefox gecko id.",
        "permissions": "Declared permissions.",
        "host_permissions": "Declared host permissions.",
        "background_script": "Background script path.",
        "strict_min_version": "Minimum Firefox version.",
    },
    "schema_body": schema_object(
        required=["manifest_version"],
        properties={
            "manifest_version": {"type": "integer", "enum": [2, 3]},
            "amo_slug": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "gecko_id": str_prop(pattern=r"^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+$"),
            "permissions": {"type": "array", "items": str_prop()},
            "host_permissions": {"type": "array", "items": str_prop()},
            "background_script": str_prop(),
            "strict_min_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)*$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Firefox Extension Template
type: extension
description: Template for a Firefox-extension-targeted universal-spawn manifest.

platforms:
  firefox-extension:
    manifest_version: 3
    gecko_id: "your-ext@yourhandle.example"
    permissions: [storage]
    background_script: background.js
    strict_min_version: "120.0"

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [firefox-extension]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/firefox-extension-template }
""",
    "native_config_name": "manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "manifest_version": 3,
  "name": "Your Extension",
  "version": "0.1.0",
  "browser_specific_settings": {
    "gecko": { "id": "your-ext@yourhandle.example", "strict_min_version": "120.0" }
  },
  "permissions": ["storage"],
  "background": { "scripts": ["background.js"] }
}
""",
    "universal_excerpt": """
platforms:
  firefox-extension:
    manifest_version: 3
    gecko_id: "your-ext@yourhandle.example"
    permissions: [storage]
    background_script: background.js
    strict_min_version: "120.0"
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Reader FF
type: extension
summary: Minimal Firefox extension recoloring pages to the parchment palette.
description: WebExtension MV3. Active-tab scoped.

platforms:
  firefox-extension:
    manifest_version: 3
    gecko_id: "parchment-reader@plate-studio.example"
    permissions: [activeTab, storage]
    background_script: background.js
    strict_min_version: "120.0"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [firefox-extension]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/firefox-parchment-reader }
  id: com.plate-studio.firefox-parchment-reader
""",
        "example-2": """
version: "1.0"
name: Privacy Proxy
type: extension
summary: Full Firefox extension routing outbound traffic through a declared proxy, listed on AMO.
description: Full MV2 extension (uses the historical proxy API). AMO-listed with a public slug.

platforms:
  firefox-extension:
    manifest_version: 2
    amo_slug: privacy-proxy
    gecko_id: "privacy-proxy@privacy.example"
    permissions: [proxy, storage, webRequest, webRequestBlocking]
    host_permissions: ["<all_urls>"]
    background_script: background.js
    strict_min_version: "115.0"

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: false

env_vars_required:
  - name: PROXY_URL
    description: Proxy endpoint.
    secret: true

deployment:
  targets: [firefox-extension]

metadata:
  license: MPL-2.0
  author: { name: Privacy Co., handle: privacy-co }
  source: { type: git, url: https://github.com/privacy-co/firefox-privacy-proxy }
  id: com.privacy-co.firefox-privacy-proxy
""",
    },
}

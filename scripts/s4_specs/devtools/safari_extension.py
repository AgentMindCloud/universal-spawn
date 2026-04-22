"""Safari extension — Xcode project + SafariWebExtensionHandler."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "safari-extension",
    "title": "Safari Extension",
    "lede": (
        "Safari extensions ship as part of a host macOS or iOS app "
        "built in Xcode. The universal-spawn manifest captures the "
        "Xcode project path, the bundle id, the entitlement file, "
        "and App Store distribution metadata."
    ),
    "cares": (
        "The Xcode project path, the bundle id, the host app kind "
        "(`macos`, `ios`, `universal`), the entitlements file, and "
        "the App Store app id."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`."),
        ("platforms.safari-extension", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.safari-extension.xcodeproj", "Path to the .xcodeproj."),
        ("platforms.safari-extension.bundle_id", "Extension bundle id."),
        ("platforms.safari-extension.host_app", "`macos`, `ios`, `universal`."),
        ("platforms.safari-extension.entitlements", "Entitlements file path."),
        ("platforms.safari-extension.app_store_id", "App Store app id."),
    ],
    "platform_fields": {
        "xcodeproj": "Xcode project path.",
        "bundle_id": "Extension bundle id.",
        "host_app": "`macos`, `ios`, or `universal`.",
        "entitlements": "Entitlements file path.",
        "app_store_id": "App Store app id.",
    },
    "schema_body": schema_object(
        required=["xcodeproj", "bundle_id", "host_app"],
        properties={
            "xcodeproj": str_prop(),
            "bundle_id": str_prop(pattern=r"^[A-Za-z0-9.-]+$"),
            "host_app": enum(["macos", "ios", "universal"]),
            "entitlements": str_prop(),
            "app_store_id": {"type": "integer", "minimum": 1},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Safari Extension Template
type: extension
description: Template for a Safari-extension-targeted universal-spawn manifest.

platforms:
  safari-extension:
    xcodeproj: SafariExt.xcodeproj
    bundle_id: com.yourhandle.safariext
    host_app: macos
    entitlements: SafariExt/SafariExt.entitlements

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [safari-extension]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/safari-extension-template }
""",
    "native_config_name": ".xcodeproj + Info.plist",
    "native_config_lang": "xml",
    "native_config": """
<!-- Info.plist excerpt -->
<key>CFBundleIdentifier</key>
<string>com.yourhandle.safariext</string>
<key>NSExtension</key>
<dict>
  <key>NSExtensionPointIdentifier</key>
  <string>com.apple.Safari.web-extension</string>
</dict>
""",
    "universal_excerpt": """
platforms:
  safari-extension:
    xcodeproj: SafariExt.xcodeproj
    bundle_id: com.yourhandle.safariext
    host_app: macos
""",
    "compatibility_extras": (
        "## Xcode is required\n\n"
        "Unlike Chrome / Firefox, Safari extensions cannot ship as a "
        "standalone zip. A universal-spawn consumer targeting Safari "
        "needs Xcode in the build pipeline; the manifest simply names "
        "the project and bundle."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Reader Safari
type: extension
summary: Minimal Safari extension packaged as a macOS host app.
description: Reader mode CSS injection. Single .xcodeproj; no host_permissions beyond activeTab-equivalent.

platforms:
  safari-extension:
    xcodeproj: ParchmentReader.xcodeproj
    bundle_id: com.plate-studio.safari-parchment-reader
    host_app: macos

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [safari-extension]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/safari-parchment-reader }
  id: com.plate-studio.safari-parchment-reader
""",
        "example-2": """
version: "1.0"
name: Universal Content Blocker
type: extension
summary: Full Safari content blocker spanning macOS + iOS with an App Store listing.
description: Content blocker shipping a universal host app. App Store id linked. Entitlements narrowly scoped.

platforms:
  safari-extension:
    xcodeproj: Blocker.xcodeproj
    bundle_id: com.privacy-co.blocker
    host_app: universal
    entitlements: Blocker/Blocker.entitlements
    app_store_id: 6700000000

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [safari-extension]

metadata:
  license: proprietary
  author: { name: Privacy Co., handle: privacy-co }
  source: { type: git, url: https://github.com/privacy-co/safari-universal-blocker }
  id: com.privacy-co.safari-universal-blocker
""",
    },
}

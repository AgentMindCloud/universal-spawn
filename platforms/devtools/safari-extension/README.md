# Safari Extension — universal-spawn platform extension

Safari extensions ship as part of a host macOS or iOS app built in Xcode. The universal-spawn manifest captures the Xcode project path, the bundle id, the entitlement file, and App Store distribution metadata.

## What this platform cares about

The Xcode project path, the bundle id, the host app kind (`macos`, `ios`, `universal`), the entitlements file, and the App Store app id.

## Compatibility table

| Manifest field | Safari Extension behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`. |
| `platforms.safari-extension` | Strict. |

### `platforms.safari-extension` fields

| Field | Purpose |
|---|---|
| `platforms.safari-extension.xcodeproj` | Xcode project path. |
| `platforms.safari-extension.bundle_id` | Extension bundle id. |
| `platforms.safari-extension.host_app` | `macos`, `ios`, or `universal`. |
| `platforms.safari-extension.entitlements` | Entitlements file path. |
| `platforms.safari-extension.app_store_id` | App Store app id. |

See [`compatibility.md`](./compatibility.md) for more.

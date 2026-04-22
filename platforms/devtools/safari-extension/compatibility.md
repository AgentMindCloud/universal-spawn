# Safari Extension compatibility — field-by-field

| universal-spawn v1.0 field | Safari Extension behavior |
|---|---|
| `version` | Required. |
| `platforms.safari-extension.xcodeproj` | Path to the .xcodeproj. |
| `platforms.safari-extension.bundle_id` | Extension bundle id. |
| `platforms.safari-extension.host_app` | `macos`, `ios`, `universal`. |
| `platforms.safari-extension.entitlements` | Entitlements file path. |
| `platforms.safari-extension.app_store_id` | App Store app id. |

## Coexistence with `.xcodeproj + Info.plist`

universal-spawn does NOT replace .xcodeproj + Info.plist. Both files coexist; consumers read both and warn on conflicts.

### `.xcodeproj + Info.plist` (provider-native)

```xml
<!-- Info.plist excerpt -->
<key>CFBundleIdentifier</key>
<string>com.yourhandle.safariext</string>
<key>NSExtension</key>
<dict>
  <key>NSExtensionPointIdentifier</key>
  <string>com.apple.Safari.web-extension</string>
</dict>
```

### `universal-spawn.yaml` (platforms.safari-extension block)

```yaml
platforms:
  safari-extension:
    xcodeproj: SafariExt.xcodeproj
    bundle_id: com.yourhandle.safariext
    host_app: macos
```

## Xcode is required

Unlike Chrome / Firefox, Safari extensions cannot ship as a standalone zip. A universal-spawn consumer targeting Safari needs Xcode in the build pipeline; the manifest simply names the project and bundle.

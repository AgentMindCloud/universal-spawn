# Chrome Extension compatibility — field-by-field

| universal-spawn v1.0 field | Chrome Extension behavior |
|---|---|
| `version` | Required. |
| `platforms.chrome-extension.manifest_version` | Must be 3. |
| `platforms.chrome-extension.permissions` | Declared permissions. |
| `platforms.chrome-extension.host_permissions` | Declared host permissions. |
| `platforms.chrome-extension.service_worker` | Service-worker entry file. |
| `platforms.chrome-extension.web_store_id` | Chrome Web Store id. |
| `platforms.chrome-extension.min_chrome_version` | Minimum Chrome version. |

## Coexistence with `manifest.json`

universal-spawn does NOT replace manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `manifest.json` (provider-native)

```json
{
  "manifest_version": 3,
  "name": "Your Extension",
  "version": "0.1.0",
  "permissions": ["storage", "sidePanel"],
  "host_permissions": ["https://example.com/*"],
  "background": { "service_worker": "background.js" },
  "minimum_chrome_version": "120"
}
```

### `universal-spawn.yaml` (platforms.chrome-extension block)

```yaml
platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [storage, sidePanel]
    host_permissions: ["https://example.com/*"]
    service_worker: background.js
    min_chrome_version: "120"
```

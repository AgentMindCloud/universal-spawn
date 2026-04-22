# Firefox Extension compatibility — field-by-field

| universal-spawn v1.0 field | Firefox Extension behavior |
|---|---|
| `version` | Required. |
| `platforms.firefox-extension.manifest_version` | `2` or `3`. |
| `platforms.firefox-extension.amo_slug` | AMO slug. |
| `platforms.firefox-extension.gecko_id` | Firefox gecko id. |
| `platforms.firefox-extension.permissions` | Declared permissions. |
| `platforms.firefox-extension.host_permissions` | Declared host permissions. |
| `platforms.firefox-extension.background_script` | Background script path. |
| `platforms.firefox-extension.strict_min_version` | Minimum Firefox version. |

## Coexistence with `manifest.json`

universal-spawn does NOT replace manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `manifest.json` (provider-native)

```json
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
```

### `universal-spawn.yaml` (platforms.firefox-extension block)

```yaml
platforms:
  firefox-extension:
    manifest_version: 3
    gecko_id: "your-ext@yourhandle.example"
    permissions: [storage]
    background_script: background.js
    strict_min_version: "120.0"
```

# Firefox Extension — universal-spawn platform extension

Firefox extensions use the WebExtensions API with `manifest.json`. Firefox supports both MV2 and MV3. A universal-spawn manifest pins the manifest version, permissions, and the AMO slug.

## What this platform cares about

`manifest_version` (2 or 3), `permissions[]`, `host_permissions[]`, the background script or service worker, and the AMO slug.

## Compatibility table

| Manifest field | Firefox Extension behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`. |
| `platforms.firefox-extension` | Strict. |

### `platforms.firefox-extension` fields

| Field | Purpose |
|---|---|
| `platforms.firefox-extension.manifest_version` | `2` or `3`. |
| `platforms.firefox-extension.amo_slug` | AMO slug. |
| `platforms.firefox-extension.gecko_id` | Firefox gecko id. |
| `platforms.firefox-extension.permissions` | Declared permissions. |
| `platforms.firefox-extension.host_permissions` | Declared host permissions. |
| `platforms.firefox-extension.background_script` | Background script path. |
| `platforms.firefox-extension.strict_min_version` | Minimum Firefox version. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

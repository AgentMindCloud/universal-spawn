# Chrome Extension — universal-spawn platform extension

Chrome extensions use Manifest V3 (`manifest.json`). A universal-spawn manifest pins the declared permissions, host permissions, service-worker entry, and the Chrome Web Store id.

## What this platform cares about

The `manifest_version` (MV3 only), the declared `permissions[]` and `host_permissions[]`, the service-worker entry, and the Chrome Web Store id.

## Compatibility table

| Manifest field | Chrome Extension behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`. |
| `platforms.chrome-extension` | Strict. |

### `platforms.chrome-extension` fields

| Field | Purpose |
|---|---|
| `platforms.chrome-extension.manifest_version` | MV3 (literal `3`). |
| `platforms.chrome-extension.permissions` | Declared permissions. |
| `platforms.chrome-extension.host_permissions` | Declared host permissions. |
| `platforms.chrome-extension.service_worker` | Service-worker entry file. |
| `platforms.chrome-extension.web_store_id` | Chrome Web Store id. |
| `platforms.chrome-extension.min_chrome_version` | Minimum Chrome version. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

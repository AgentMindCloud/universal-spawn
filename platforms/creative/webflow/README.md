# Webflow — universal-spawn platform extension

Webflow publishes visual-editor sites with optional CMS collections. The extension covers a site, a Webflow Libraries component pack, or a full data-collection schema.

## What this platform cares about

The `kind` (`site`, `library`, `collection`), the site id, optional CMS collection definitions, and the custom domain.

## Compatibility table

| Manifest field | Webflow behavior |
|---|---|
| `version` | Required. |
| `type` | `site`, `web-app`, `creative-tool`. |
| `deployment.targets` | Must include `webflow`. |
| `platforms.webflow` | Strict. |

### `platforms.webflow` fields

| Field | Purpose |
|---|---|
| `platforms.webflow.kind` | `site`, `library`, `collection`. |
| `platforms.webflow.site_id` | Webflow site id. |
| `platforms.webflow.custom_domain` | Custom domain. |
| `platforms.webflow.collections` | CMS collection schemas. |
| `platforms.webflow.localization` | Webflow Localization locales. |

See [`compatibility.md`](./compatibility.md) for more.

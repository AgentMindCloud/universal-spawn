# Canva — universal-spawn platform extension

Canva's extension surface is the Apps SDK (in-editor apps) and the Canva Templates gallery (duplicatable designs). The extension handles both, plus the canonical duplicate-to-workspace pattern that makes templates one-click shareable.

## What this platform cares about

The `kind` (`app`, `template`, `design`), the Canva `app.json` path for apps, and the public design URL for templates that drives the duplicate button.

## Compatibility table

| Manifest field | Canva behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `design-template`, `plugin`. |
| `platforms.canva` | Strict. |

### `platforms.canva` fields

| Field | Purpose |
|---|---|
| `platforms.canva.kind` | `app`, `template`, `design`. |
| `platforms.canva.app_json` | Canva Apps SDK `app.json` path. |
| `platforms.canva.design_url` | Public Canva design URL. |
| `platforms.canva.design_id` | Canva design id. |
| `platforms.canva.categories` | Canva category slugs. |
| `platforms.canva.surface` | In-editor surfaces the app runs on. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

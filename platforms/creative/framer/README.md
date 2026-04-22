# Framer — universal-spawn platform extension

Framer is a design tool that ships published websites + reusable code components. A universal-spawn manifest describes which shape is being published — a full site, a component pack, or a project duplicate.

## What this platform cares about

The `kind` (`site`, `component-pack`, `project`), the Framer project id, custom-domain metadata, and whether the project is opted into the marketplace.

## Compatibility table

| Manifest field | Framer behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `site`, `web-app`. |
| `deployment.targets` | Must include `framer`. |
| `platforms.framer` | Strict. |

### `platforms.framer` fields

| Field | Purpose |
|---|---|
| `platforms.framer.kind` | `site`, `component-pack`, or `project`. |
| `platforms.framer.project_id` | Framer project id. |
| `platforms.framer.custom_domain` | Optional custom domain. |
| `platforms.framer.marketplace` | Marketplace listing settings. |

See [`compatibility.md`](./compatibility.md) for more.

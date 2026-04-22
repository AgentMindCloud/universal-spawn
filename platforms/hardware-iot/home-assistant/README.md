# Home Assistant — universal-spawn platform extension

Home Assistant integrations live in `custom_components/`; blueprints under `blueprints/`. A universal-spawn manifest maps onto either, and explicitly mirrors the integration's `manifest.json` fields (`domain`, `iot_class`, `requirements`, `dependencies`).

## What this platform cares about

The `kind` (`integration`, `blueprint`), the integration domain, IoT class, and dependencies.

## Compatibility table

| Manifest field | Home Assistant behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `workflow`, `hardware-device`. |
| `platforms.home-assistant` | Strict. |

### `platforms.home-assistant` fields

| Field | Purpose |
|---|---|
| `platforms.home-assistant.kind` | `integration` or `blueprint`. |
| `platforms.home-assistant.domain` | Integration domain. |
| `platforms.home-assistant.iot_class` | IoT class. |
| `platforms.home-assistant.requirements` | Python requirements. |
| `platforms.home-assistant.dependencies` | HA component dependencies. |
| `platforms.home-assistant.blueprint_kind` | Blueprint kind. |

See [`compatibility.md`](./compatibility.md) for more.

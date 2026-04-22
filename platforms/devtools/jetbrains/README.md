# JetBrains — universal-spawn platform extension

JetBrains' Marketplace hosts plugins for the IntelliJ Platform (IDEA, PyCharm, WebStorm, GoLand, RustRover, Rider, CLion, etc). A universal-spawn manifest targets one plugin with its plugin id, compatible IDE set, and the compatibility range (`sinceBuild` / `untilBuild`).

## What this platform cares about

The plugin id, the compatible IDEs, and the IntelliJ build range.

## Compatibility table

| Manifest field | JetBrains behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`. |
| `platforms.jetbrains` | Strict. |

### `platforms.jetbrains` fields

| Field | Purpose |
|---|---|
| `platforms.jetbrains.plugin_id` | Plugin id. |
| `platforms.jetbrains.ides` | Compatible IDEs. |
| `platforms.jetbrains.since_build` | sinceBuild. |
| `platforms.jetbrains.until_build` | untilBuild. |
| `platforms.jetbrains.marketplace_id` | Numeric Marketplace id. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.

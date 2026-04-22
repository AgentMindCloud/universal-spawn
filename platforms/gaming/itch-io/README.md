# itch.io — universal-spawn platform extension

itch.io publishes html5, downloadable, and physical games. A universal-spawn manifest pins the kind, the butler channel, and the html5 frame settings (for in-browser games).

## What this platform cares about

The `kind` (`html5`, `downloadable`, `physical`), the butler channel, and html5 frame settings.

## Compatibility table

| Manifest field | itch.io behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `web-app`, `creative-tool`. |
| `platforms.itch-io` | Strict. |

### `platforms.itch-io` fields

| Field | Purpose |
|---|---|
| `platforms.itch-io.kind` | `html5`, `downloadable`, or `physical`. |
| `platforms.itch-io.butler_channel` | butler channel. |
| `platforms.itch-io.html5_frame` | html5 frame settings. |
| `platforms.itch-io.payment` | Payment kind. |

See [`compatibility.md`](./compatibility.md) for more.

# Farcaster — universal-spawn platform extension

Farcaster ships Frames (interactive embeds) and mini-apps (`fc:miniapp` manifest). A universal-spawn manifest covers both and the bot account behind them.

## What this platform cares about

The `kind` (`frame`, `mini-app`, `bot`), the bot's FID, and the manifest URL for mini-apps.

## Compatibility table

| Manifest field | Farcaster behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `web-app`, `extension`. |
| `platforms.farcaster` | Strict. |

### `platforms.farcaster` fields

| Field | Purpose |
|---|---|
| `platforms.farcaster.kind` | `frame`, `mini-app`, `bot`. |
| `platforms.farcaster.fid` | Farcaster FID. |
| `platforms.farcaster.frame_url` | Frame entry URL. |
| `platforms.farcaster.miniapp_url` | Mini-app manifest URL. |
| `platforms.farcaster.signer_uuid` | Signer UUID. |

See [`compatibility.md`](./compatibility.md) for more.

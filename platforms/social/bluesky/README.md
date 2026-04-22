# Bluesky — universal-spawn platform extension

Bluesky runs on the AT Protocol. A universal-spawn manifest describes a bot account or a custom feed generator and pins the lexicon NSIDs the creation publishes.

## What this platform cares about

The `kind` (`bot`, `feed-generator`), the bot handle, the feed-generator service DID + record name, and the lexicon NSIDs the creation owns.

## Compatibility table

| Manifest field | Bluesky behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `extension`, `web-app`. |
| `platforms.bluesky` | Strict. |

### `platforms.bluesky` fields

| Field | Purpose |
|---|---|
| `platforms.bluesky.kind` | `bot` or `feed-generator`. |
| `platforms.bluesky.handle` | Bluesky handle. |
| `platforms.bluesky.service_did` | Service DID. |
| `platforms.bluesky.feed_record` | Feed-generator record name. |
| `platforms.bluesky.nsids` | Owned lexicon NSIDs. |
| `platforms.bluesky.pds_url` | PDS URL. |

See [`compatibility.md`](./compatibility.md) for more.

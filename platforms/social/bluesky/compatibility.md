# Bluesky compatibility — field-by-field

| universal-spawn v1.0 field | Bluesky behavior |
|---|---|
| `version` | Required. |
| `platforms.bluesky.kind` | `bot` or `feed-generator`. |
| `platforms.bluesky.handle` | Bluesky handle. |
| `platforms.bluesky.service_did` | Service DID for feed-generators. |
| `platforms.bluesky.feed_record` | Record name (rkey) for feed-generators. |
| `platforms.bluesky.nsids` | Owned lexicon NSIDs. |
| `platforms.bluesky.pds_url` | PDS URL (for self-hosted). |

## Coexistence with `AT Protocol lexicon JSON files`

universal-spawn does NOT replace AT Protocol lexicon JSON files. Both files coexist; consumers read both and warn on conflicts.

### `AT Protocol lexicon JSON files` (provider-native)

```json
{
  "lexicon": 1,
  "id": "com.example.feed.getPlateFeed",
  "defs": {}
}
```

### `universal-spawn.yaml` (platforms.bluesky block)

```yaml
platforms:
  bluesky:
    kind: feed-generator
    service_did: "did:web:feed.example.com"
    feed_record: plate-of-day
    nsids: ["com.example.feed.getPlateFeed"]
```

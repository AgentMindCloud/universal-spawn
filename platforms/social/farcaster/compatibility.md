# Farcaster compatibility — field-by-field

| universal-spawn v1.0 field | Farcaster behavior |
|---|---|
| `version` | Required. |
| `platforms.farcaster.kind` | `frame`, `mini-app`, `bot`. |
| `platforms.farcaster.fid` | Farcaster FID. |
| `platforms.farcaster.frame_url` | Frame entry URL. |
| `platforms.farcaster.miniapp_url` | Mini-app manifest URL. |
| `platforms.farcaster.signer_uuid` | Signer UUID for posting. |

## Coexistence with `fc:miniapp manifest.json`

universal-spawn does NOT replace fc:miniapp manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `fc:miniapp manifest.json` (provider-native)

```json
{
  "version": "1",
  "name": "Your Mini App",
  "iconUrl": "https://app.example/icon.png",
  "homeUrl": "https://app.example",
  "tags": ["miniapp"]
}
```

### `universal-spawn.yaml` (platforms.farcaster block)

```yaml
platforms:
  farcaster:
    kind: mini-app
    miniapp_url: "https://app.example/.well-known/farcaster.json"
```

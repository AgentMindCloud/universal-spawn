# X (Twitter) compatibility — field-by-field

| universal-spawn v1.0 field | X (Twitter) behavior |
|---|---|
| `version` | Required. |
| `platforms.x-twitter.account` | Bot @-handle. |
| `platforms.x-twitter.scopes` | OAuth 2.0 scopes. |
| `platforms.x-twitter.tier` | API tier (`free`, `basic`, `pro`, `enterprise`). |
| `platforms.x-twitter.streams` | Filtered-stream rule files. |
| `platforms.x-twitter.uses_grok` | True if the bot routes inference through Grok. |

## Coexistence with `X Developer Portal app + OAuth 2.0 settings`

universal-spawn does NOT replace X Developer Portal app + OAuth 2.0 settings. Both files coexist; consumers read both and warn on conflicts.

### `X Developer Portal app + OAuth 2.0 settings` (provider-native)

```text
# Configured in the X Developer Portal; no repo-level config file by convention.
```

### `universal-spawn.yaml` (platforms.x-twitter block)

```yaml
platforms:
  x-twitter:
    account: yourbot
    scopes: [tweet.read, tweet.write]
    tier: basic
```

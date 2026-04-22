# Matrix compatibility — field-by-field

| universal-spawn v1.0 field | Matrix behavior |
|---|---|
| `version` | Required. |
| `platforms.matrix.kind` | `bot` or `appservice`. |
| `platforms.matrix.homeserver` | Homeserver URL. |
| `platforms.matrix.identifier` | MXID for bots, appservice id for bridges. |
| `platforms.matrix.registration_file` | Appservice registration.yaml path. |
| `platforms.matrix.namespaces` | Appservice user/alias/room namespaces. |

## Coexistence with `appservice registration.yaml`

universal-spawn does NOT replace appservice registration.yaml. Both files coexist; consumers read both and warn on conflicts.

### `appservice registration.yaml` (provider-native)

```yaml
id: yourbridge
url: http://localhost:9000
as_token: REPLACE
hs_token: REPLACE
sender_localpart: bridgebot
namespaces:
  users:
    - { regex: "@_yourbridge_.*:matrix.org", exclusive: true }
```

### `universal-spawn.yaml` (platforms.matrix block)

```yaml
platforms:
  matrix:
    kind: appservice
    homeserver: "https://matrix.org"
    identifier: yourbridge
    registration_file: registration.yaml
    namespaces:
      users: ["@_yourbridge_.*:matrix.org"]
```

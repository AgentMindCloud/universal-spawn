# itch.io compatibility — field-by-field

| universal-spawn v1.0 field | itch.io behavior |
|---|---|
| `version` | Required. |
| `platforms.itch-io.kind` | `html5`, `downloadable`, `physical`. |
| `platforms.itch-io.butler_channel` | butler channel. |
| `platforms.itch-io.html5_frame` | html5 frame size + fullscreen. |
| `platforms.itch-io.payment` | Payment kind. |

## Coexistence with `.itch.toml + butler push`

universal-spawn does NOT replace .itch.toml + butler push. Both files coexist; consumers read both and warn on conflicts.

### `.itch.toml + butler push` (provider-native)

```toml
[[actions]]
name = "play"
path = "index.html"

[[prereqs]]
name = "webview"
```

### `universal-spawn.yaml` (platforms.itch-io block)

```yaml
platforms:
  itch-io:
    kind: html5
    butler_channel: web
    html5_frame: { width: 1280, height: 720, fullscreen_button: true }
```

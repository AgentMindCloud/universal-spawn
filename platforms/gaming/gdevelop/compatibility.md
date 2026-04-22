# GDevelop compatibility — field-by-field

| universal-spawn v1.0 field | GDevelop behavior |
|---|---|
| `version` | Required. |
| `platforms.gdevelop.project_file` | game.json path. |
| `platforms.gdevelop.exports` | Export targets. |
| `platforms.gdevelop.engine_version` | GDevelop engine version. |

## Coexistence with `game.json`

universal-spawn does NOT replace game.json. Both files coexist; consumers read both and warn on conflicts.

### `game.json` (provider-native)

```json
{
  "properties": { "name": "Your Game", "version": "0.1.0" },
  "layouts": []
}
```

### `universal-spawn.yaml` (platforms.gdevelop block)

```yaml
platforms:
  gdevelop:
    project_file: game.json
    exports: [html5, android]
```

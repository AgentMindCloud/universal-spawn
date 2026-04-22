# Defold compatibility — field-by-field

| universal-spawn v1.0 field | Defold behavior |
|---|---|
| `version` | Required. |
| `platforms.defold.kind` | `project` or `extension`. |
| `platforms.defold.engine_version` | Defold engine version. |
| `platforms.defold.target_platforms` | Target platforms. |
| `platforms.defold.entry_collection` | Entry collection (project). |

## Coexistence with `game.project`

universal-spawn does NOT replace game.project. Both files coexist; consumers read both and warn on conflicts.

### `game.project` (provider-native)

```ini
[project]
title = Your Game
version = 1.0

[bootstrap]
main_collection = /main/main.collectionc
```

### `universal-spawn.yaml` (platforms.defold block)

```yaml
platforms:
  defold:
    kind: project
    engine_version: "1.9"
    entry_collection: main/main.collection
```

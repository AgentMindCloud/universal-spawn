# RPG Maker compatibility — field-by-field

| universal-spawn v1.0 field | RPG Maker behavior |
|---|---|
| `version` | Required. |
| `platforms.rpg-maker.engine` | `mv`, `mz`, `unite`. |
| `platforms.rpg-maker.kind` | `project` or `plugin`. |
| `platforms.rpg-maker.entry_data_dir` | data/ directory path. |
| `platforms.rpg-maker.plugin_file` | Plugin JS file (`kind: plugin`). |

## Coexistence with `data/ tree (MV/MZ) or rpgmaker_unite project`

universal-spawn does NOT replace data/ tree (MV/MZ) or rpgmaker_unite project. Both files coexist; consumers read both and warn on conflicts.

### `data/ tree (MV/MZ) or rpgmaker_unite project` (provider-native)

```text
# RPG Maker MV/MZ projects expose state as JSON files inside data/.
```

### `universal-spawn.yaml` (platforms.rpg-maker block)

```yaml
platforms:
  rpg-maker:
    engine: mz
    kind: project
    entry_data_dir: data
```

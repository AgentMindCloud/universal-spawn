# RPG Maker — universal-spawn platform extension

RPG Maker projects (MV / MZ) ship a `data/` tree plus optional plugins (`js/plugins/`). A universal-spawn manifest picks the engine generation and the kind.

## What this platform cares about

The engine (`mv`, `mz`, `unite`), the `kind` (`project` or `plugin`), and the JS-engine target.

## Compatibility table

| Manifest field | RPG Maker behavior |
|---|---|
| `version` | Required. |
| `type` | `game-world`, `extension`, `creative-tool`. |
| `platforms.rpg-maker` | Strict. |

### `platforms.rpg-maker` fields

| Field | Purpose |
|---|---|
| `platforms.rpg-maker.engine` | `mv`, `mz`, `unite`. |
| `platforms.rpg-maker.kind` | `project` or `plugin`. |
| `platforms.rpg-maker.entry_data_dir` | data/ directory. |
| `platforms.rpg-maker.plugin_file` | Plugin JS file. |

See [`compatibility.md`](./compatibility.md) for more.

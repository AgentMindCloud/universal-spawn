# LEGO SPIKE compatibility — field-by-field

| universal-spawn v1.0 field | LEGO SPIKE behavior |
|---|---|
| `version` | Required. |
| `platforms.lego-spike.generation` | `spike-prime`, `spike-essential`. |
| `platforms.lego-spike.language` | `icon-blocks` or `python`. |
| `platforms.lego-spike.entry_file` | Exported project file. |
| `platforms.lego-spike.app_version` | Minimum SPIKE App version. |

## Coexistence with `SPIKE App project export (.llsp3 / .py)`

universal-spawn does NOT replace SPIKE App project export (.llsp3 / .py). Both files coexist; consumers read both and warn on conflicts.

### `SPIKE App project export (.llsp3 / .py)` (provider-native)

```text
# SPIKE App exports include the project metadata + code.
```

### `universal-spawn.yaml` (platforms.lego-spike block)

```yaml
platforms:
  lego-spike:
    generation: spike-prime
    language: python
    entry_file: project/main.py
```

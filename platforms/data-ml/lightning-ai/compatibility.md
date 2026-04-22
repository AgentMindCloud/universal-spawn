# Lightning AI compatibility — field-by-field

| universal-spawn v1.0 field | Lightning AI behavior |
|---|---|
| `version` | Required. |
| `platforms.lightning-ai.template` | Studio template. |
| `platforms.lightning-ai.machine` | Machine class. |
| `platforms.lightning-ai.entry_file` | Entry .py / .ipynb file. |
| `platforms.lightning-ai.team_id` | Lightning team id. |

## Coexistence with `Lightning Studio template + machine settings`

universal-spawn does NOT replace Lightning Studio template + machine settings. Both files coexist; consumers read both and warn on conflicts.

### `Lightning Studio template + machine settings` (provider-native)

```text
# Lightning Studio config lives in the Studio's web UI; this manifest mirrors it.
```

### `universal-spawn.yaml` (platforms.lightning-ai block)

```yaml
platforms:
  lightning-ai:
    template: pytorch
    machine: T4
```

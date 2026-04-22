# Observable compatibility — field-by-field

| universal-spawn v1.0 field | Observable behavior |
|---|---|
| `version` | Required. |
| `platforms.observable.kind` | `notebook` or `framework`. |
| `platforms.observable.notebook_url` | Public Observable notebook URL. |
| `platforms.observable.framework_root` | Framework project root directory. |
| `platforms.observable.fork_protection` | If true, the consumer prompts before forking. |

## Coexistence with `observable notebook URL / Framework root`

universal-spawn does NOT replace observable notebook URL / Framework root. Both files coexist; consumers read both and warn on conflicts.

### `observable notebook URL / Framework root` (provider-native)

```text
# Observable notebook config lives in the notebook's metadata or in observablehq.config.js for Framework.
```

### `universal-spawn.yaml` (platforms.observable block)

```yaml
platforms:
  observable:
    kind: notebook
    notebook_url: "https://observablehq.com/@yourhandle/your-notebook"
```

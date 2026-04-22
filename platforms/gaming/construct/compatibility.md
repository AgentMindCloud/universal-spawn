# Construct compatibility — field-by-field

| universal-spawn v1.0 field | Construct behavior |
|---|---|
| `version` | Required. |
| `platforms.construct.project_file` | .c3p file path. |
| `platforms.construct.exports` | Export targets. |

## Coexistence with `*.c3p (Construct project archive)`

universal-spawn does NOT replace *.c3p (Construct project archive). Both files coexist; consumers read both and warn on conflicts.

### `*.c3p (Construct project archive)` (provider-native)

```text
# Construct projects are .c3p archives; no separate config file.
```

### `universal-spawn.yaml` (platforms.construct block)

```yaml
platforms:
  construct:
    project_file: project.c3p
    exports: [html5, android]
```

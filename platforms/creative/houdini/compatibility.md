# Houdini compatibility — field-by-field

| universal-spawn v1.0 field | Houdini behavior |
|---|---|
| `version` | Required. |
| `platforms.houdini.kind` | `hda`, `hip`, `shelf`. |
| `platforms.houdini.min_build` | Minimum Houdini build. |
| `platforms.houdini.context` | Houdini network context. |
| `platforms.houdini.entry_file` | Entry `.hda` / `.hip` / `.shelf` path. |

## Coexistence with `.hda + otls/ + shelves/*.shelf`

universal-spawn does NOT replace .hda + otls/ + shelves/*.shelf. Both files coexist; consumers read both and warn on conflicts.

### `.hda + otls/ + shelves/*.shelf` (provider-native)

```text
# HDAs contain their own metadata; no separate config file.
```

### `universal-spawn.yaml` (platforms.houdini block)

```yaml
platforms:
  houdini:
    kind: hda
    min_build: "20.5"
    context: sop
    entry_file: otls/plate_lattice.hda
```

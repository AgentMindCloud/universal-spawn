# Fortnite UEFN compatibility — field-by-field

| universal-spawn v1.0 field | Fortnite UEFN behavior |
|---|---|
| `version` | Required. |
| `platforms.fortnite-uefn.island_code` | Island code (XXXX-XXXX-XXXX). |
| `platforms.fortnite-uefn.uefnproject` | UEFN project file path. |
| `platforms.fortnite-uefn.verse_main` | Verse main module. |
| `platforms.fortnite-uefn.discover_category` | Discover category. |

## Coexistence with `.uefnproject + Verse module tree`

universal-spawn does NOT replace .uefnproject + Verse module tree. Both files coexist; consumers read both and warn on conflicts.

### `.uefnproject + Verse module tree` (provider-native)

```text
# UEFN project files + Verse modules.
```

### `universal-spawn.yaml` (platforms.fortnite-uefn block)

```yaml
platforms:
  fortnite-uefn:
    uefnproject: YourIsland.uefnproject
    verse_main: src/main.verse
```

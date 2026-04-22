# Unity (gaming) compatibility — field-by-field

| universal-spawn v1.0 field | Unity (gaming) behavior |
|---|---|
| `version` | Required. |
| `platforms.unity.kind` | `asset-store-package` or `project-template`. |
| `platforms.unity.min_editor` | Minimum Unity editor (e.g. `2023.2`). |
| `platforms.unity.render_pipeline` | `built-in`, `urp`, `hdrp`. |
| `platforms.unity.entry_scene` | Entry scene (project-template). |
| `platforms.unity.asset_store_category` | Asset Store category (asset-store). |
| `platforms.unity.upm_packages` | Required UPM packages. |

## Coexistence with `ProjectSettings/*.asset + Packages/manifest.json (UPM)`

universal-spawn does NOT replace ProjectSettings/*.asset + Packages/manifest.json (UPM). Both files coexist; consumers read both and warn on conflicts.

### `ProjectSettings/*.asset + Packages/manifest.json (UPM)` (provider-native)

```json
{
  "dependencies": {
    "com.unity.render-pipelines.universal": "17.0.3",
    "com.unity.inputsystem": "1.13.0"
  }
}
```

### `universal-spawn.yaml` (platforms.unity block)

```yaml
platforms:
  unity:
    kind: project-template
    min_editor: "2023.2"
    render_pipeline: urp
    entry_scene: Assets/Scenes/Main.unity
    upm_packages:
      - com.unity.render-pipelines.universal
      - com.unity.inputsystem
```

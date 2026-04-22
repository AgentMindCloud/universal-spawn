# Adobe compatibility — field-by-field

| universal-spawn v1.0 field | Adobe behavior |
|---|---|
| `version` | Required. |
| `platforms.adobe.platform` | `cep` or `uxp`. |
| `platforms.adobe.manifest_file` | Extension manifest file path. |
| `platforms.adobe.hosts` | Adobe host apps. |
| `platforms.adobe.min_host_version` | Minimum host version. |
| `platforms.adobe.adobe_exchange` | Exchange publication settings. |

## Coexistence with `manifest.json (UXP) or manifest.xml (CEP)`

universal-spawn does NOT replace manifest.json (UXP) or manifest.xml (CEP). Both files coexist; consumers read both and warn on conflicts.

### `manifest.json (UXP) or manifest.xml (CEP)` (provider-native)

```json
{
  "manifestVersion": 5,
  "id": "com.yourhandle.parchment",
  "name": "Parchment",
  "version": "0.1.0",
  "host": { "app": "PS", "minVersion": "25.0" },
  "entrypoints": [{ "type": "panel", "id": "main", "label": { "default": "Parchment" } }]
}
```

### `universal-spawn.yaml` (platforms.adobe block)

```yaml
platforms:
  adobe:
    platform: uxp
    manifest_file: manifest.json
    hosts: [photoshop]
    min_host_version: "25.0"
```

## CEP vs UXP — both supported

Older Adobe hosts still require **CEP** HTML extensions (`CSXS/manifest.xml`). Newer hosts (Photoshop 23+, Illustrator 26+, InDesign 18+) support **UXP** (`manifest.json`). Set `platform` to the one the extension actually targets — a single manifest cannot straddle both.

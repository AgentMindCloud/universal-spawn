# Home Assistant compatibility — field-by-field

| universal-spawn v1.0 field | Home Assistant behavior |
|---|---|
| `version` | Required. |
| `platforms.home-assistant.kind` | `integration` or `blueprint`. |
| `platforms.home-assistant.domain` | Integration domain. |
| `platforms.home-assistant.iot_class` | Integration IoT class. |
| `platforms.home-assistant.requirements` | Python requirements. |
| `platforms.home-assistant.dependencies` | HA component dependencies. |
| `platforms.home-assistant.blueprint_kind` | Blueprint kind (blueprint). |

## Coexistence with `custom_components/<domain>/manifest.json`

universal-spawn does NOT replace custom_components/<domain>/manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `custom_components/<domain>/manifest.json` (provider-native)

```json
{
  "domain": "your_integration",
  "name": "Your Integration",
  "version": "0.1.0",
  "iot_class": "local_push",
  "requirements": ["aiohttp>=3.9"],
  "dependencies": [],
  "codeowners": ["@yourhandle"]
}
```

### `universal-spawn.yaml` (platforms.home-assistant block)

```yaml
platforms:
  home-assistant:
    kind: integration
    domain: your_integration
    iot_class: local_push
    requirements: ["aiohttp>=3.9"]
    dependencies: []
```

## Mapping to Home Assistant manifest.json

| `platforms.home-assistant.*` | `custom_components/<domain>/manifest.json` |
|---|---|
| `domain`        | `domain`        |
| `iot_class`     | `iot_class`     |
| `requirements`  | `requirements`  |
| `dependencies`  | `dependencies`  |

A consumer SHOULD generate `manifest.json` from these fields if it is missing.

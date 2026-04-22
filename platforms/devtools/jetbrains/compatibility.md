# JetBrains compatibility — field-by-field

| universal-spawn v1.0 field | JetBrains behavior |
|---|---|
| `version` | Required. |
| `platforms.jetbrains.plugin_id` | Plugin id. |
| `platforms.jetbrains.ides` | Compatible IDEs. |
| `platforms.jetbrains.since_build` | IntelliJ since-build. |
| `platforms.jetbrains.until_build` | Optional until-build. |
| `platforms.jetbrains.marketplace_id` | Numeric Marketplace id (if listed). |

## Coexistence with `plugin.xml`

universal-spawn does NOT replace plugin.xml. Both files coexist; consumers read both and warn on conflicts.

### `plugin.xml` (provider-native)

```xml
<idea-plugin>
  <id>com.yourhandle.yourplugin</id>
  <name>Your Plugin</name>
  <vendor>Your Name</vendor>
  <idea-version since-build="243.0"/>
  <depends>com.intellij.modules.platform</depends>
</idea-plugin>
```

### `universal-spawn.yaml` (platforms.jetbrains block)

```yaml
platforms:
  jetbrains:
    plugin_id: com.yourhandle.yourplugin
    ides: [idea, pycharm, webstorm]
    since_build: "243.0"
```

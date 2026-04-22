# Maven compatibility — field-by-field

| universal-spawn v1.0 field | Maven behavior |
|---|---|
| `version` | Required. |
| `platforms.maven.group_id` | Maven groupId. |
| `platforms.maven.artifact_id` | Maven artifactId. |
| `platforms.maven.packaging` | `jar`, `war`, `pom`, `aar`. |
| `platforms.maven.java_range` | Java range (e.g. `>=17`). |
| `platforms.maven.repository` | Repository. |

## Coexistence with `pom.xml`

universal-spawn does NOT replace pom.xml. Both files coexist; consumers read both and warn on conflicts.

### `pom.xml` (provider-native)

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.yourhandle</groupId>
  <artifactId>your-lib</artifactId>
  <version>0.1.0</version>
  <packaging>jar</packaging>
  <properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
  </properties>
</project>
```

### `universal-spawn.yaml` (platforms.maven block)

```yaml
platforms:
  maven:
    group_id: com.yourhandle
    artifact_id: your-lib
    packaging: jar
    java_range: ">=17"
    repository: maven-central
```

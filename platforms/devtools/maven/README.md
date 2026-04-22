# Maven — universal-spawn platform extension

Maven artifacts are identified by groupId + artifactId + version. A universal-spawn manifest records those plus the distribution repository (Maven Central, GitHub Packages, private Nexus / Artifactory).

## What this platform cares about

The GAV coordinates, the packaging type, the Java version target, and the repository.

## Compatibility table

| Manifest field | Maven behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`, `plugin`. |
| `platforms.maven` | Strict. |

### `platforms.maven` fields

| Field | Purpose |
|---|---|
| `platforms.maven.group_id` | Maven groupId. |
| `platforms.maven.artifact_id` | Maven artifactId. |
| `platforms.maven.packaging` | `jar`, `war`, `pom`, `aar`. |
| `platforms.maven.java_range` | Java range. |
| `platforms.maven.repository` | Repository. |

See [`compatibility.md`](./compatibility.md) for more.

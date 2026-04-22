"""Maven — pom.xml coexistence + Maven Central / GitHub Packages."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "maven",
    "title": "Maven",
    "lede": (
        "Maven artifacts are identified by groupId + artifactId + "
        "version. A universal-spawn manifest records those plus the "
        "distribution repository (Maven Central, GitHub Packages, "
        "private Nexus / Artifactory)."
    ),
    "cares": (
        "The GAV coordinates, the packaging type, the Java version "
        "target, and the repository."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`, `plugin`."),
        ("platforms.maven", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.maven.group_id", "Maven groupId."),
        ("platforms.maven.artifact_id", "Maven artifactId."),
        ("platforms.maven.packaging", "`jar`, `war`, `pom`, `aar`."),
        ("platforms.maven.java_range", "Java range (e.g. `>=17`)."),
        ("platforms.maven.repository", "Repository."),
    ],
    "platform_fields": {
        "group_id": "Maven groupId.",
        "artifact_id": "Maven artifactId.",
        "packaging": "`jar`, `war`, `pom`, `aar`.",
        "java_range": "Java range.",
        "repository": "Repository.",
    },
    "schema_body": schema_object(
        required=["group_id", "artifact_id"],
        properties={
            "group_id": str_prop(pattern=r"^[a-z][a-zA-Z0-9_]*(\.[a-z][a-zA-Z0-9_]*)*$"),
            "artifact_id": str_prop(pattern=r"^[a-zA-Z][a-zA-Z0-9_.-]{0,63}$"),
            "packaging": enum(["jar", "war", "pom", "aar"]),
            "java_range": str_prop(pattern=r"^[><=~ |.0-9, ]+$"),
            "repository": enum(["maven-central", "github-packages", "azure-artifacts", "nexus", "artifactory", "private"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Maven Template
type: library
description: Template for a Maven-targeted universal-spawn manifest.

platforms:
  maven:
    group_id: com.yourhandle
    artifact_id: your-lib
    packaging: jar
    java_range: ">=17"
    repository: maven-central

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [maven]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/maven-template }
""",
    "native_config_name": "pom.xml",
    "native_config_lang": "xml",
    "native_config": """
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
""",
    "universal_excerpt": """
platforms:
  maven:
    group_id: com.yourhandle
    artifact_id: your-lib
    packaging: jar
    java_range: ">=17"
    repository: maven-central
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Palette Java
type: library
summary: Minimal Maven library with Residual Frequencies palette constants.
description: Java 17+ library on Maven Central.

platforms:
  maven:
    group_id: studio.plate
    artifact_id: parchment-palette
    packaging: jar
    java_range: ">=17"
    repository: maven-central

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [maven]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/maven-parchment-palette }
  id: com.plate-studio.maven-parchment-palette
""",
        "example-2": """
version: "1.0"
name: Plate Android Aar
type: library
summary: Full Maven Android AAR with Java 21 target, published to GitHub Packages.
description: Android library (AAR packaging). Java 21. Private GitHub Packages feed.

platforms:
  maven:
    group_id: studio.plate
    artifact_id: plate-android
    packaging: aar
    java_range: ">=21"
    repository: github-packages

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required:
  - name: GITHUB_TOKEN
    description: GitHub token with `read:packages` / `write:packages`.
    secret: true

deployment:
  targets: [maven]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/maven-plate-android }
  id: com.plate-studio.maven-plate-android
""",
    },
}

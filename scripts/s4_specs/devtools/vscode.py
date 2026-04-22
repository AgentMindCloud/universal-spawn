"""VS Code — Marketplace extensions + Dev Containers."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "vscode",
    "title": "VS Code",
    "lede": (
        "VS Code has two independent spawn surfaces: Marketplace "
        "extensions (via `package.json` + VS Code-specific contrib "
        "points) and Dev Containers (via `.devcontainer/devcontainer.json`). "
        "A universal-spawn manifest picks exactly one via `kind` and "
        "maps into the native config."
    ),
    "cares": (
        "The `kind` (`extension`, `devcontainer`), publisher id + "
        "extension id (for extensions), the DevContainer image and "
        "features (for devcontainers), and the target VS Code forks."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `container`."),
        ("platforms.vscode", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.vscode.kind", "`extension` or `devcontainer`."),
        ("platforms.vscode.publisher_id", "Marketplace publisher id."),
        ("platforms.vscode.extension_id", "Extension id (publisher.name)."),
        ("platforms.vscode.min_vscode", "Minimum VS Code engine version."),
        ("platforms.vscode.image", "DevContainer image."),
        ("platforms.vscode.features", "DevContainer features map."),
        ("platforms.vscode.forks", "Compatible forks (`vscode`, `cursor`, `windsurf`, `code-oss`)."),
    ],
    "platform_fields": {
        "kind": "`extension` or `devcontainer`.",
        "publisher_id": "Marketplace publisher id.",
        "extension_id": "Extension id (publisher.name).",
        "min_vscode": "Minimum VS Code engine.",
        "image": "DevContainer image.",
        "features": "DevContainer features.",
        "forks": "Compatible VS Code forks.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["extension", "devcontainer"]),
            "publisher_id": str_prop(pattern=r"^[a-zA-Z][a-zA-Z0-9-]{0,31}$"),
            "extension_id": str_prop(pattern=r"^[a-zA-Z][a-zA-Z0-9-]*\.[a-zA-Z][a-zA-Z0-9-]*$"),
            "min_vscode": str_prop(pattern=r"^\^?[0-9]+\.[0-9]+(\.[0-9]+)?$"),
            "image": str_prop(),
            "features": {
                "type": "object",
                "additionalProperties": {"type": "object"},
            },
            "forks": {
                "type": "array",
                "items": enum(["vscode", "cursor", "windsurf", "code-oss", "vscodium"]),
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: VS Code Template
type: extension
description: Template for a VS-Code-targeted universal-spawn manifest.

platforms:
  vscode:
    kind: extension
    publisher_id: yourhandle
    extension_id: yourhandle.your-extension
    min_vscode: "^1.90.0"
    forks: [vscode, cursor, windsurf]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [vscode]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/vscode-template }
""",
    "native_config_name": "package.json + devcontainer.json",
    "native_config_lang": "json",
    "native_config": """
{
  "name": "your-extension",
  "publisher": "yourhandle",
  "engines": { "vscode": "^1.90.0" },
  "contributes": { "commands": [] }
}
""",
    "universal_excerpt": """
platforms:
  vscode:
    kind: extension
    publisher_id: yourhandle
    extension_id: yourhandle.your-extension
    min_vscode: "^1.90.0"
""",
    "compatibility_extras": (
        "## Extension vs DevContainer\n\n"
        "They are independent. An `extension` manifest packages a VS "
        "Code Marketplace extension. A `devcontainer` manifest "
        "describes a fully reproducible dev environment that any "
        "VS Code fork (or Codespaces, or Gitpod) can open directly. "
        "Same creation may ship both — but in two sibling manifests, "
        "not one."
    ),
    "perks": STANDARD_PERKS,
    "examples": {
        "extension": """
version: "1.0"
name: Parchment Theme
type: extension
summary: Minimal VS Code color theme in the Residual Frequencies palette.
description: Theme extension for VS Code and its forks.

platforms:
  vscode:
    kind: extension
    publisher_id: plate-studio
    extension_id: plate-studio.parchment-theme
    min_vscode: "^1.90.0"
    forks: [vscode, cursor, windsurf, vscodium]

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [vscode]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/vscode-parchment-theme }
  id: com.plate-studio.vscode-parchment-theme
""",
        "devcontainer": """
version: "1.0"
name: Parchment Dev Container
type: container
summary: Reproducible Dev Container for the Residual Frequencies repo.
description: >
  Reads a standard .devcontainer/devcontainer.json. Includes Node 20,
  pnpm, and the SVG-lint feature so plate SVGs validate on save.

platforms:
  vscode:
    kind: devcontainer
    image: mcr.microsoft.com/devcontainers/typescript-node:20
    features:
      "ghcr.io/devcontainers/features/github-cli:1": {}
      "ghcr.io/devcontainers-contrib/features/svg-lint:1": {}
    forks: [vscode, cursor, windsurf]

safety:
  min_permissions: [fs:read, fs:write, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [vscode, codespaces, gitpod]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/vscode-devcontainer }
  id: com.plate-studio.vscode-devcontainer
""",
    },
}

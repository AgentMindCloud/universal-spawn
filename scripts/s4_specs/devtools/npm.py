"""npm — additive coexistence with package.json."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "npm",
    "title": "npm",
    "lede": (
        "A universal-spawn manifest does NOT replace `package.json`. "
        "It is additive: the same repo ships both. npm still reads "
        "`package.json` for install, build, and publish; universal-"
        "spawn adds the cross-platform discoverability + metadata + "
        "safety envelope around it."
    ),
    "cares": (
        "The package name, whether the package is public / private / "
        "scoped, the declared peer-dependency surface, and the "
        "entrypoint shape (CLI / library / workspace)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`, `plugin`."),
        ("platforms.npm", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.npm.package_name", "Package name (may be scoped)."),
        ("platforms.npm.shape", "`library`, `cli`, `workspace`."),
        ("platforms.npm.access", "`public`, `restricted`."),
        ("platforms.npm.node_range", "Engine range for Node."),
        ("platforms.npm.bin_map", "Bin entries for CLI shape."),
        ("platforms.npm.peer_deps", "Peer-dependency surface."),
    ],
    "platform_fields": {
        "package_name": "npm package name.",
        "shape": "`library`, `cli`, or `workspace`.",
        "access": "`public` or `restricted`.",
        "node_range": "Node engine range.",
        "bin_map": "Bin entries.",
        "peer_deps": "Peer deps.",
    },
    "schema_body": schema_object(
        required=["package_name", "shape"],
        properties={
            "package_name": str_prop(pattern=r"^(@[a-z0-9-][a-z0-9_.-]*/)?[a-z0-9-][a-z0-9_.-]*$"),
            "shape": enum(["library", "cli", "workspace"]),
            "access": enum(["public", "restricted"]),
            "node_range": str_prop(pattern=r"^[><=~^ |.0-9*x-]+$"),
            "bin_map": {"type": "object", "additionalProperties": str_prop()},
            "peer_deps": {"type": "object", "additionalProperties": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: npm Template
type: library
description: Template for an npm-targeted universal-spawn manifest.

platforms:
  npm:
    package_name: "@yourhandle/your-lib"
    shape: library
    access: public
    node_range: ">=20"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [npm]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/npm-template }
""",
    "native_config_name": "package.json",
    "native_config_lang": "json",
    "native_config": """
{
  "name": "@yourhandle/your-lib",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "engines": { "node": ">=20" },
  "publishConfig": { "access": "public" }
}
""",
    "universal_excerpt": """
platforms:
  npm:
    package_name: "@yourhandle/your-lib"
    shape: library
    access: public
    node_range: ">=20"
""",
    "compatibility_extras": (
        "## Additive — not a replacement\n\n"
        "`package.json` still owns `dependencies`, `devDependencies`, "
        "`scripts`, `exports`, TypeScript `types`, and every npm- "
        "specific knob. `platforms.npm` only declares what a cross-"
        "platform consumer needs in order to tell the world about the "
        "package without re-reading npm's registry."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Utils
type: library
summary: Minimal npm library with the Residual Frequencies palette constants.
description: Pure ESM library, node 20+, public access.

platforms:
  npm:
    package_name: "@plate-studio/parchment-utils"
    shape: library
    access: public
    node_range: ">=20"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [npm]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/npm-parchment-utils }
  id: com.plate-studio.npm-parchment-utils
""",
        "example-2": """
version: "1.0"
name: Plate CLI
type: cli-tool
summary: Full npm CLI with a bin entry and a peer dep on React 18+.
description: CLI shape. One bin entry exposed as `plate`.

platforms:
  npm:
    package_name: "@plate-studio/plate-cli"
    shape: cli
    access: public
    node_range: ">=20"
    bin_map:
      plate: "./bin/plate.js"
    peer_deps:
      react: ">=18"

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [npm]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/npm-plate-cli }
  id: com.plate-studio.npm-plate-cli
""",
    },
}

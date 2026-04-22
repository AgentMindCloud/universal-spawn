"""PyPI — additive coexistence with pyproject.toml."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "pypi",
    "title": "PyPI",
    "lede": (
        "A universal-spawn manifest does NOT replace `pyproject.toml`. "
        "`pyproject.toml` still owns `[build-system]`, `[project]`, "
        "dependencies, optional extras, and build backend choice. "
        "`platforms.pypi` is additive cross-platform metadata."
    ),
    "cares": (
        "The distribution name, Python version range, whether the "
        "project ships entry-point scripts, and PyPI / TestPyPI "
        "repository."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`."),
        ("platforms.pypi", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.pypi.distribution", "PyPI distribution name."),
        ("platforms.pypi.python_range", "Python range (PEP 440)."),
        ("platforms.pypi.shape", "`library`, `cli`, `plugin`."),
        ("platforms.pypi.entry_points", "`console_scripts` entries."),
        ("platforms.pypi.repository", "`pypi` or `testpypi`."),
        ("platforms.pypi.build_backend", "PEP 517 build backend."),
    ],
    "platform_fields": {
        "distribution": "PyPI distribution name.",
        "python_range": "Python range.",
        "shape": "`library`, `cli`, `plugin`.",
        "entry_points": "`console_scripts` entries.",
        "repository": "`pypi` or `testpypi`.",
        "build_backend": "Build backend.",
    },
    "schema_body": schema_object(
        required=["distribution", "python_range"],
        properties={
            "distribution": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9_.-]*$"),
            "python_range": str_prop(pattern=r"^[><=!~*.0-9, ]+$"),
            "shape": enum(["library", "cli", "plugin"]),
            "entry_points": {"type": "object", "additionalProperties": str_prop()},
            "repository": enum(["pypi", "testpypi"]),
            "build_backend": enum(["hatchling", "setuptools", "poetry-core", "flit-core", "pdm-backend", "maturin"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: PyPI Template
type: library
description: Template for a PyPI-targeted universal-spawn manifest.

platforms:
  pypi:
    distribution: your-lib
    python_range: ">=3.11"
    shape: library
    repository: pypi
    build_backend: hatchling

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [pypi]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/pypi-template }
""",
    "native_config_name": "pyproject.toml",
    "native_config_lang": "toml",
    "native_config": """
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "your-lib"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
""",
    "universal_excerpt": """
platforms:
  pypi:
    distribution: your-lib
    python_range: ">=3.11"
    shape: library
    repository: pypi
    build_backend: hatchling
""",
    "compatibility_extras": (
        "## Additive — not a replacement\n\n"
        "`pyproject.toml` remains the source of truth for build and "
        "runtime dependencies. universal-spawn only asserts the "
        "cross-platform view (discovery, safety envelope, "
        "spawnability across other platforms if applicable)."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Utils Py
type: library
summary: Minimal PyPI library exposing Residual Frequencies palette helpers.
description: Pure Python library, Python 3.11+, hatchling backend.

platforms:
  pypi:
    distribution: parchment-utils
    python_range: ">=3.11"
    shape: library
    repository: pypi
    build_backend: hatchling

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [pypi]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/pypi-parchment-utils }
  id: com.plate-studio.pypi-parchment-utils
""",
        "example-2": """
version: "1.0"
name: Plate CLI Py
type: cli-tool
summary: Full PyPI CLI tool with a console_scripts entrypoint.
description: CLI tool exposed as `plate`. Poetry-core build backend.

platforms:
  pypi:
    distribution: plate-cli
    python_range: ">=3.11"
    shape: cli
    entry_points:
      plate: "plate_cli.main:main"
    repository: pypi
    build_backend: poetry-core

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [pypi]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/pypi-plate-cli }
  id: com.plate-studio.pypi-plate-cli
""",
    },
}

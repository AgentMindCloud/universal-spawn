# PyPI compatibility — field-by-field

| universal-spawn v1.0 field | PyPI behavior |
|---|---|
| `version` | Required. |
| `platforms.pypi.distribution` | PyPI distribution name. |
| `platforms.pypi.python_range` | Python range (PEP 440). |
| `platforms.pypi.shape` | `library`, `cli`, `plugin`. |
| `platforms.pypi.entry_points` | `console_scripts` entries. |
| `platforms.pypi.repository` | `pypi` or `testpypi`. |
| `platforms.pypi.build_backend` | PEP 517 build backend. |

## Coexistence with `pyproject.toml`

universal-spawn does NOT replace pyproject.toml. Both files coexist; consumers read both and warn on conflicts.

### `pyproject.toml` (provider-native)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "your-lib"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
```

### `universal-spawn.yaml` (platforms.pypi block)

```yaml
platforms:
  pypi:
    distribution: your-lib
    python_range: ">=3.11"
    shape: library
    repository: pypi
    build_backend: hatchling
```

## Additive — not a replacement

`pyproject.toml` remains the source of truth for build and runtime dependencies. universal-spawn only asserts the cross-platform view (discovery, safety envelope, spawnability across other platforms if applicable).

# PyPI — universal-spawn platform extension

A universal-spawn manifest does NOT replace `pyproject.toml`. `pyproject.toml` still owns `[build-system]`, `[project]`, dependencies, optional extras, and build backend choice. `platforms.pypi` is additive cross-platform metadata.

## What this platform cares about

The distribution name, Python version range, whether the project ships entry-point scripts, and PyPI / TestPyPI repository.

## Compatibility table

| Manifest field | PyPI behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`. |
| `platforms.pypi` | Strict. |

### `platforms.pypi` fields

| Field | Purpose |
|---|---|
| `platforms.pypi.distribution` | PyPI distribution name. |
| `platforms.pypi.python_range` | Python range. |
| `platforms.pypi.shape` | `library`, `cli`, `plugin`. |
| `platforms.pypi.entry_points` | `console_scripts` entries. |
| `platforms.pypi.repository` | `pypi` or `testpypi`. |
| `platforms.pypi.build_backend` | Build backend. |

See [`compatibility.md`](./compatibility.md) for more.

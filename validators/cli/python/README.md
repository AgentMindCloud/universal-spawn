# `universal-spawn` — Python CLI

Reference Python implementation of the universal-spawn validator + a
small CLI surface (`validate`, `init`, `migrate`).

## Install

```bash
# uv (recommended)
uv pip install universal-spawn

# pip
pip install universal-spawn
```

## Use

```bash
# Validate the manifest at the repo root.
universal-spawn validate

# Validate a specific path.
universal-spawn validate apps/api/universal-spawn.yaml

# Validate including platform extensions.
universal-spawn validate --platform-schemas-dir platforms/

# Treat warnings as failures.
universal-spawn validate --strict

# Write a starter manifest.
universal-spawn init --type minimal           # → universal-spawn.yaml
universal-spawn init --type ai-agent --force

# Lift a legacy v1.0.0 spawn.yaml to v1.0.
universal-spawn migrate spawn.yaml --out universal-spawn.yaml
```

## API

```python
from universal_spawn import validate, validate_file

result = validate({"version": "1.0", ...})
if result.ok:
    print("ok")
else:
    for err in result.errors:
        print(err)
```

## Tests

```bash
cd validators/cli/python
uv run pytest      # or: pytest
```

15 cases cover the master schema, platform-extension validation,
the CLI surface, and migration from the v1.0.0 legacy track.

## What it bundles

The package ships the v1.0 master schema as package data. Platform
extension schemas are not bundled — pass `--platform-schemas-dir` to
the CLI or pass a `platform_schemas` dict to `validate()` to wire them.

#!/usr/bin/env python3
"""Validate every manifest in the repository against the universal-spawn
master schema and, where applicable, the platform extension schema.

Exits non-zero if any manifest fails validation.

Usage:
    python scripts/validate.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parent.parent
CORE_SCHEMA = REPO / "spec" / "v1.0.0" / "manifest.schema.json"


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    with path.open() as f:
        return json.load(f)


def iter_manifests():
    """Yield every `*.spawn.yaml`, `*-spawn.yaml`, and platform template."""
    for path in REPO.rglob("*"):
        if ".git" in path.parts:
            continue
        name = path.name
        if name.endswith(".spawn.yaml") or name.endswith(".spawn.yml"):
            yield path
        elif name.endswith("-spawn.yaml") or name.endswith("-spawn.yml"):
            yield path


def extension_schema(platform_id: str) -> Path | None:
    p = REPO / "platforms" / platform_id / "schema.extension.json"
    return p if p.is_file() else None


def main() -> int:
    core_schema = load_json(CORE_SCHEMA)
    core_v = Draft202012Validator(core_schema)

    total = 0
    failed = 0
    for path in sorted(iter_manifests()):
        total += 1
        doc = load_yaml(path)

        core_errs = sorted(core_v.iter_errors(doc), key=lambda e: list(e.path))

        ext_errs: list = []
        platforms = (doc or {}).get("platforms") or {}
        for platform_id, ext_value in platforms.items():
            ext_schema_path = extension_schema(platform_id)
            if ext_schema_path is None:
                continue
            ext_v = Draft202012Validator(load_json(ext_schema_path))
            for e in ext_v.iter_errors(ext_value):
                ext_errs.append((platform_id, e))

        rel = path.relative_to(REPO)
        if core_errs or ext_errs:
            failed += 1
            print(f"FAIL {rel}")
            for e in core_errs:
                print(f"  core      {list(e.path)}: {e.message}")
            for platform_id, e in ext_errs:
                print(f"  {platform_id:<10} {list(e.path)}: {e.message}")
        else:
            print(f"ok   {rel}")

    print(f"\n{total} file(s) checked, {failed} failed.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

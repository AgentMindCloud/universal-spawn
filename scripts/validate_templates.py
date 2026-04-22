#!/usr/bin/env python3
"""Validate every template's universal-spawn.yaml against the v1.0 master schema.

Run from the repo root:
    python3 scripts/validate_templates.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

REPO = Path(__file__).resolve().parent.parent
MASTER_ID = "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"


def main(argv: list[str]) -> int:
    schema = json.loads((REPO / "spec/v1.0/universal-spawn.schema.json").read_text())
    resource = Resource.from_contents(schema, default_specification=DRAFT7)
    registry = Registry().with_resource(MASTER_ID, resource)
    v = Draft7Validator(schema, registry=registry)

    selected = set(argv[1:])
    total = 0
    failed = 0
    for d in sorted((REPO / "templates").iterdir()):
        if not d.is_dir():
            continue
        if selected and d.name not in selected:
            continue
        manifest = d / "universal-spawn.yaml"
        if not manifest.is_file():
            print(f"miss {d.name}: no universal-spawn.yaml")
            failed += 1
            continue
        total += 1
        doc = yaml.safe_load(manifest.read_text())
        errs = list(v.iter_errors(doc))
        if errs:
            failed += 1
            print(f"FAIL {d.name}")
            for e in errs:
                print(f"    {list(e.path)}: {e.message}")
        else:
            print(f"ok   {d.name}")

    print(f"\n{total} template(s), {failed} failure(s)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

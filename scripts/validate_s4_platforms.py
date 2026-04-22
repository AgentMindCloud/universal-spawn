#!/usr/bin/env python3
"""Validate Session 4 platform folders (creative, devtools, social,
data-ml, gaming, hardware-iot).

For each `*-spawn.schema.json`:
  1. Meta-validate as draft-07.
  2. Validate every example under examples/*.yaml against the
     platform schema (master v1.0 registered via `referencing`).
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
SUBTREES = ["creative", "devtools", "social", "data-ml", "gaming", "hardware-iot"]


def main(argv: list[str]) -> int:
    master = json.loads((REPO / "spec/v1.0/universal-spawn.schema.json").read_text())
    master_resource = Resource.from_contents(master, default_specification=DRAFT7)

    selected = set(argv[1:])
    total_platforms = 0
    total_examples = 0
    failed = 0

    for subtree in SUBTREES:
        root_dir = REPO / "platforms" / subtree
        if not root_dir.is_dir():
            continue
        for schema_path in sorted(root_dir.rglob("*-spawn.schema.json")):
            folder = schema_path.parent
            platform_id = folder.name
            if selected and platform_id not in selected:
                continue
            total_platforms += 1
            schema = json.loads(schema_path.read_text())
            try:
                Draft7Validator.check_schema(schema)
            except Exception as e:  # noqa: BLE001
                failed += 1
                print(f"FAIL schema {schema_path.relative_to(REPO)}: {e}")
                continue

            registry = Registry().with_resource(MASTER_ID, master_resource)
            v = Draft7Validator(schema, registry=registry)

            example_dir = folder / "examples"
            if not example_dir.is_dir():
                continue
            for ex_path in sorted(example_dir.glob("*.yaml")):
                total_examples += 1
                doc = yaml.safe_load(ex_path.read_text())
                errs = sorted(v.iter_errors(doc), key=lambda e: list(e.path))
                if errs:
                    failed += 1
                    print(f"FAIL {ex_path.relative_to(REPO)}")
                    for e in errs:
                        print(f"    {list(e.path)}: {e.message}")
                else:
                    print(f"ok   {ex_path.relative_to(REPO)}")

    print(
        f"\n{total_platforms} S4 platform(s), {total_examples} example(s), "
        f"{failed} failure(s)"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

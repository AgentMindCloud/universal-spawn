#!/usr/bin/env python3
"""Generator for platforms/ai/<id>/ folders.

Takes a compact platform specification (Python dict) and writes the
seven canonical files to the right location:

  <root>/<id>/
    README.md
    <id>-spawn.yaml
    <id>-spawn.schema.json
    compatibility.md
    perks.md
    examples/example-1.yaml
    examples/example-2.yaml
    examples/example-3.yaml

The generator is the quickest way to keep 29+ platform folders
consistent in shape while allowing each one to carry platform-
specific schema additions and distinctive examples.

Not a runtime tool — invoked only from scripts/build_ai_platforms.py.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
MASTER_SCHEMA_URI = (
    "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"
)


def _yaml_inline_list(items: list[str]) -> str:
    return "[" + ", ".join(items) + "]"


def _emit_schema(spec: dict[str, Any]) -> str:
    pid = spec["id"]
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": f"https://universal-spawn.dev/platforms/ai/{spec['location']}/{pid}/{pid}-spawn.schema.json",
        "title": f"universal-spawn with {spec['title']} platform extension",
        "allOf": [
            {"$ref": MASTER_SCHEMA_URI},
            {
                "type": "object",
                "required": ["platforms"],
                "properties": {
                    "platforms": {
                        "type": "object",
                        "required": [pid],
                        "properties": {pid: {"$ref": "#/definitions/" + pid}},
                    }
                },
            },
        ],
        "definitions": {pid: spec["schema_body"]},
    }
    return json.dumps(schema, indent=2) + "\n"


def _emit_readme(spec: dict[str, Any]) -> str:
    compat_rows = "\n".join(
        f"| `{field}` | {note} |"
        for field, note in spec["compat_table"]
    )
    platform_rows = "\n".join(
        f"| `platforms.{spec['id']}.{k}` | {v} |"
        for k, v in spec.get("platform_fields", {}).items()
    )
    return f"""# {spec['title']} — universal-spawn platform extension

{spec['lede']}

## What this platform cares about

{spec['cares']}

## What platform-specific extras unlock

{spec['extras']}

## Compatibility table

{spec.get('compat_preamble', 'How core manifest fields map onto this platform:')}

| Manifest field | {spec['title']} behavior |
|---|---|
{compat_rows}

### `platforms.{spec['id']}` fields

| Field | Purpose |
|---|---|
{platform_rows}

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
"""


def _emit_template(spec: dict[str, Any]) -> str:
    return spec["template_yaml"].strip() + "\n"


def _emit_compatibility(spec: dict[str, Any]) -> str:
    rows = "\n".join(
        f"| `{field}` | {note} |"
        for field, note in spec["compat_table_full"]
    )
    extras = spec.get("compatibility_extras", "")
    return f"""# {spec['title']} compatibility — field-by-field

| universal-spawn v1.0 field | {spec['title']} behavior |
|---|---|
{rows}

{extras}
"""


def _emit_perks(spec: dict[str, Any]) -> str:
    perks_lines = "\n".join(f"- {p}" for p in spec["perks"])
    return f"""# {spec['title']} perks — what this platform could offer

Wishlist for what a conformant {spec['title']} consumer SHOULD offer
to manifests that declare `platforms.{spec['id']}`. Items land as the
vendor ships them.

{perks_lines}

Out of scope: this file does not speak for the vendor; it is a
wishlist. What actually ships is the vendor's call.
"""


def _emit_examples(spec: dict[str, Any]) -> list[tuple[str, str]]:
    """Return [(path, body), ...] for example-1/2/3.yaml."""
    out = []
    for i, ex in enumerate(spec["examples"], start=1):
        body = ex["yaml"].strip() + "\n"
        out.append((f"examples/example-{i}.yaml", body))
    return out


def generate(spec: dict[str, Any], root: Path | None = None) -> None:
    root = root or (REPO / "platforms" / "ai" / spec["location"] / spec["id"])
    (root / "examples").mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": _emit_readme(spec),
        f"{spec['id']}-spawn.schema.json": _emit_schema(spec),
        f"{spec['id']}-spawn.yaml": _emit_template(spec),
        "compatibility.md": _emit_compatibility(spec),
        "perks.md": _emit_perks(spec),
    }
    for rel, content in files.items():
        (root / rel).write_text(content)
    for rel, content in _emit_examples(spec):
        (root / rel).write_text(content)

    print(f"ok   {spec['id']}")


if __name__ == "__main__":
    raise SystemExit("invoke from scripts/build_ai_platforms.py")

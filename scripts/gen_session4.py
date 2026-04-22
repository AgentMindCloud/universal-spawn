#!/usr/bin/env python3
"""Generator for Session 4 platform folders.

Writes to platforms/<subtree>/<id>/:
    README.md
    <id>-spawn.yaml
    <id>-spawn.schema.json
    compatibility.md
    perks.md               (OPTIONAL — only when spec["perks"] present)
    examples/<name>.yaml   (one per key in spec["examples"])

Differences from gen_ai_platform / gen_hosting_platform:
  - Variable example count (dict keyed by filename stem).
  - No deploy-button.md (hosting-only concept).
  - perks.md is optional.
  - Subtree location taken from spec["location"] (e.g. "creative",
    "data-ml", "hardware-iot").
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
MASTER_SCHEMA_URI = (
    "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"
)


def _emit_schema(spec: dict[str, Any]) -> str:
    pid = spec["id"]
    subtree = spec["location"]
    body: dict[str, Any] = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": f"https://universal-spawn.dev/platforms/{subtree}/{pid}/{pid}-spawn.schema.json",
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
    return json.dumps(body, indent=2) + "\n"


def _emit_readme(spec: dict[str, Any]) -> str:
    compat_rows = "\n".join(
        f"| `{field}` | {note} |" for field, note in spec["compat_table"]
    )
    platform_rows = "\n".join(
        f"| `platforms.{spec['id']}.{k}` | {v} |"
        for k, v in spec.get("platform_fields", {}).items()
    )
    cross = spec.get("cross_links", "")
    cross_section = f"\n## See also\n\n{cross}\n" if cross else ""
    perks_hint = " and [`perks.md`](./perks.md)" if "perks" in spec else ""
    return f"""# {spec['title']} — universal-spawn platform extension

{spec['lede']}

## What this platform cares about

{spec['cares']}

## Compatibility table

| Manifest field | {spec['title']} behavior |
|---|---|
{compat_rows}

### `platforms.{spec['id']}` fields

| Field | Purpose |
|---|---|
{platform_rows}

See [`compatibility.md`](./compatibility.md){perks_hint} for more.
{cross_section}"""


def _emit_compatibility(spec: dict[str, Any]) -> str:
    rows = "\n".join(
        f"| `{field}` | {note} |" for field, note in spec["compat_table_full"]
    )
    native = spec.get("native_config_name")
    native_body = spec.get("native_config", "").strip()
    lang = spec.get("native_config_lang", "yaml")
    univ = spec.get("universal_excerpt", "").strip()
    extras = spec.get("compatibility_extras", "")

    native_section = ""
    if native and native_body:
        native_section = (
            f"\n## Coexistence with `{native}`\n\n"
            f"universal-spawn does NOT replace {native}. Both files "
            f"coexist; consumers read both and warn on conflicts.\n\n"
            f"### `{native}` (provider-native)\n\n"
            f"```{lang}\n{native_body}\n```\n\n"
            f"### `universal-spawn.yaml` (platforms.{spec['id']} block)\n\n"
            f"```yaml\n{univ}\n```\n"
        )
    elif native:
        native_section = (
            f"\n## Coexistence with `{native}`\n\n"
            f"universal-spawn is additive to {native}. Keep both.\n"
        )

    return f"""# {spec['title']} compatibility — field-by-field

| universal-spawn v1.0 field | {spec['title']} behavior |
|---|---|
{rows}
{native_section}
{extras}
""".strip() + "\n"


def _emit_perks(spec: dict[str, Any]) -> str:
    perks_lines = "\n".join(f"- {p}" for p in spec["perks"])
    return f"""# {spec['title']} perks — what this platform could offer

Wishlist for what a conformant {spec['title']} consumer SHOULD offer
to manifests that declare `platforms.{spec['id']}`.

{perks_lines}

This file is a wishlist, not a vendor commitment.
"""


def generate(spec: dict[str, Any]) -> None:
    root = REPO / "platforms" / spec["location"] / spec["id"]
    (root / "examples").mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(_emit_readme(spec))
    (root / f"{spec['id']}-spawn.schema.json").write_text(_emit_schema(spec))
    (root / f"{spec['id']}-spawn.yaml").write_text(spec["template_yaml"].strip() + "\n")
    (root / "compatibility.md").write_text(_emit_compatibility(spec))
    if "perks" in spec:
        (root / "perks.md").write_text(_emit_perks(spec))
    for name, body in spec["examples"].items():
        (root / "examples" / f"{name}.yaml").write_text(body.strip() + "\n")

    print(f"ok   {spec['location']}/{spec['id']}")


if __name__ == "__main__":
    raise SystemExit("invoke from scripts/build_s4_platforms.py")

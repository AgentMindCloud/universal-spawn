#!/usr/bin/env python3
"""Generator for platforms/hosting/<id>/ folders.

Writes the canonical seven-file layout for a hosting-platform spec:

    <id>/
      README.md
      <id>-spawn.yaml                (or .json if `template_kind: json`)
      <id>-spawn.schema.json
      compatibility.md               (side-by-side diff vs native config)
      deploy-button.md               (real deploy-button markdown)
      perks.md
      examples/
        static-site.yaml
        serverless-api.yaml
        full-stack-app.yaml

Differences from gen_ai_platform.py:

  - Fixed example filenames (no example-1.yaml).
  - Extra `deploy-button.md` file.
  - Compatibility doc supports a `native_config` block whose content
    is rendered side-by-side against the universal-spawn manifest.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
MASTER_SCHEMA_URI = (
    "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"
)

EXAMPLE_NAMES = ["static-site", "serverless-api", "full-stack-app"]


def _emit_schema(spec: dict[str, Any]) -> str:
    pid = spec["id"]
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": f"https://universal-spawn.dev/platforms/hosting/{pid}/{pid}-spawn.schema.json",
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
    platform_rows = "\n".join(
        f"| `platforms.{spec['id']}.{k}` | {v} |"
        for k, v in spec.get("platform_fields", {}).items()
    )
    compat_rows = "\n".join(
        f"| `{field}` | {note} |"
        for field, note in spec["compat_table"]
    )
    runtimes = spec.get("runtimes", "")
    runtimes_section = (
        f"\n## Supported runtime targets\n\n{runtimes}\n" if runtimes else ""
    )
    return f"""# {spec['title']} — universal-spawn platform extension

{spec['lede']}

## What this platform cares about

{spec['cares']}

## What platform-specific extras unlock

{spec['extras']}
{runtimes_section}
## Compatibility table

| Manifest field | {spec['title']} behavior |
|---|---|
{compat_rows}

### `platforms.{spec['id']}` fields

| Field | Purpose |
|---|---|
{platform_rows}

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `{spec['native_config_name']}`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant {spec['title']} consumer SHOULD offer manifests that
declare `platforms.{spec['id']}`.
"""


def _emit_template(spec: dict[str, Any]) -> str:
    return spec["template_yaml"].strip() + "\n"


def _emit_compatibility(spec: dict[str, Any]) -> str:
    rows = "\n".join(
        f"| `{field}` | {note} |"
        for field, note in spec["compat_table_full"]
    )
    native_name = spec["native_config_name"]
    native_body = spec["native_config"].strip()
    universal_body = spec["universal_excerpt"].strip()
    extras = spec.get("compatibility_extras", "")
    return f"""# {spec['title']} compatibility — field-by-field

{spec['title']} already has a native config format
(`{native_name}`). universal-spawn does not replace it; the two
coexist. A {spec['title']} consumer reads both:

- `{native_name}` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.{spec['id']}`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `{native_name}` (provider-native)

```{spec.get('native_config_lang', 'yaml')}
{native_body}
```

### `universal-spawn.yaml` (platforms.{spec['id']} block)

```yaml
{universal_body}
```

## Field-by-field

| universal-spawn v1.0 field | {spec['title']} behavior |
|---|---|
{rows}

{extras}
"""


def _emit_deploy_button(spec: dict[str, Any]) -> str:
    button = spec["deploy_button"]
    return f"""# {spec['title']} — Deploy-button recipe

A manifest that declares `platforms.{spec['id']}` with a
complete `{spec['native_config_name']}`-equivalent block is eligible
for the canonical {spec['title']} Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
{button['markdown']}
```

## HTML

```html
{button['html']}
```

## Parameters

{button.get('params_doc', 'The button link accepts the parameters listed in the platform docs; most let the reader pre-fill the repository URL, the branch, and the root directory.')}

## Badge style

The universal-spawn project ships a complementary "Spawns on
{spec['title']}" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `{spec['id']}-spawn.schema.json` loses the badge.

```markdown
[![Spawns on {spec['title']}](https://universal-spawn.dev/badge/{spec['id']}.svg)](https://universal-spawn.dev/registry/{spec['id']})
```
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
    """Return [(path, body), ...] for the three canonical examples."""
    out = []
    for name in EXAMPLE_NAMES:
        ex = spec["examples"][name]
        out.append((f"examples/{name}.yaml", ex.strip() + "\n"))
    return out


def generate(spec: dict[str, Any], root: Path | None = None) -> None:
    root = root or (REPO / "platforms" / "hosting" / spec["id"])
    (root / "examples").mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": _emit_readme(spec),
        f"{spec['id']}-spawn.schema.json": _emit_schema(spec),
        f"{spec['id']}-spawn.yaml": _emit_template(spec),
        "compatibility.md": _emit_compatibility(spec),
        "deploy-button.md": _emit_deploy_button(spec),
        "perks.md": _emit_perks(spec),
    }
    for rel, content in files.items():
        (root / rel).write_text(content)
    for rel, content in _emit_examples(spec):
        (root / rel).write_text(content)

    print(f"ok   {spec['id']}")


if __name__ == "__main__":
    raise SystemExit("invoke from scripts/build_hosting_platforms.py")

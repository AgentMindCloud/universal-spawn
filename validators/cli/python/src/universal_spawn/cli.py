"""universal-spawn CLI.

Subcommands:
    validate [PATH]   Validate the manifest at PATH (default: ./universal-spawn.yaml).
    init [--type T]   Write a starter manifest for type T to ./universal-spawn.yaml.
    migrate [PATH]    Lift a legacy v1.0.0 spawn.yaml to v1.0 universal-spawn.yaml.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

from . import __version__
from .validator import validate, validate_file

DEFAULT_FILES = [
    "universal-spawn.yaml",
    "universal-spawn.yml",
    "universal-spawn.json",
    "spawn.yaml",
    "spawn.yml",
    "spawn.json",
]

STARTERS: dict[str, dict[str, Any]] = {
    "minimal": {
        "version": "1.0",
        "name": "Your Project",
        "description": "Replace this with a one-paragraph description "
                       "of what your project does.",
        "type": "web-app",
        "platforms": {"vercel": {}},
        "metadata": {
            "license": "MIT",
            "author": {"name": "Your Name", "handle": "yourhandle"},
            "source": {
                "type": "git",
                "url": "https://github.com/yourhandle/your-project",
            },
        },
    },
    "ai-agent": {
        "version": "1.0",
        "name": "Your AI Agent",
        "description": "Replace with a one-paragraph description of "
                       "what this AI agent does.",
        "type": "ai-agent",
        "platforms": {
            "claude": {
                "skill_type": "subagent",
                "model": "claude-sonnet-4-6",
                "surface": ["claude-api"],
            }
        },
        "safety": {
            "min_permissions": ["network:outbound:api.anthropic.com"],
            "safe_for_auto_spawn": False,
        },
        "env_vars_required": [
            {
                "name": "ANTHROPIC_API_KEY",
                "description": "Anthropic API key.",
                "secret": True,
            }
        ],
        "metadata": {
            "license": "Apache-2.0",
            "author": {"name": "Your Name", "handle": "yourhandle"},
            "source": {
                "type": "git",
                "url": "https://github.com/yourhandle/your-agent",
            },
        },
    },
}


def _detect_default_path() -> Path | None:
    for cand in DEFAULT_FILES:
        if Path(cand).is_file():
            return Path(cand)
    return None


def _cmd_validate(args: argparse.Namespace) -> int:
    path = Path(args.path) if args.path else _detect_default_path()
    if path is None:
        print(
            "no manifest path given and no default manifest found "
            f"(looked for: {', '.join(DEFAULT_FILES)})",
            file=sys.stderr,
        )
        return 2
    result = validate_file(
        path,
        platform_schemas_dir=args.platform_schemas_dir,
        strict=args.strict,
    )
    for e in result.errors:
        print(f"error  {e}")
    for w in result.warnings:
        print(f"warn   {w}")
    if result.platforms_checked:
        print(f"info   checked platform extensions: {', '.join(sorted(result.platforms_checked))}")
    if result.ok:
        print(f"ok     {path}")
        return 0
    print(f"fail   {path}: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
    return 1


def _cmd_init(args: argparse.Namespace) -> int:
    starter = STARTERS.get(args.type)
    if starter is None:
        print(f"unknown starter '{args.type}'. Choose from: {', '.join(sorted(STARTERS))}", file=sys.stderr)
        return 2
    out_path = Path(args.out)
    if out_path.exists() and not args.force:
        print(f"refusing to overwrite {out_path} (pass --force).", file=sys.stderr)
        return 2
    out_path.write_text(yaml.safe_dump(starter, sort_keys=False))
    print(f"wrote   {out_path} (type={args.type})")
    return 0


_LIFT_FIELD_MAP = {
    # legacy v1.0.0 → v1.0 lift, conservative.
    "name": ("name", lambda v: v),
    "description": ("description", lambda v: v),
    "summary": ("summary", lambda v: v),
}


def _cmd_migrate(args: argparse.Namespace) -> int:
    src = Path(args.path) if args.path else _detect_default_path()
    if src is None:
        print("no source manifest given and no default found.", file=sys.stderr)
        return 2
    legacy = yaml.safe_load(src.read_text())
    if not isinstance(legacy, dict):
        print(f"{src}: not a YAML/JSON object.", file=sys.stderr)
        return 2

    new: dict[str, Any] = {"version": "1.0"}
    for legacy_field, (new_field, fn) in _LIFT_FIELD_MAP.items():
        if legacy_field in legacy:
            new[new_field] = fn(legacy[legacy_field])

    # `kind` (legacy) → `type` (v1.0).
    if "kind" in legacy:
        new["type"] = legacy["kind"]
    else:
        new["type"] = "web-app"

    # Merge metadata-shaped fields into `metadata`.
    metadata: dict[str, Any] = {}
    if "id" in legacy:
        metadata["id"] = legacy["id"]
    if "license" in legacy:
        metadata["license"] = legacy["license"]
    if "author" in legacy:
        metadata["author"] = legacy["author"]
    if "source" in legacy:
        metadata["source"] = legacy["source"]
    if metadata:
        new["metadata"] = metadata

    # Pass through compatible top-level blocks if present.
    for k in ("platforms", "env_vars_required", "deployment", "visuals", "safety"):
        if k in legacy:
            new[k] = legacy[k]

    # Lift legacy safety knobs.
    safety = new.setdefault("safety", {}) if isinstance(new.get("safety"), dict) else {}
    for legacy_key, new_key in [
        ("min_permissions", "min_permissions"),
        ("rate_limit_qps", "rate_limit_qps"),
        ("cost_limit_usd_daily", "cost_limit_usd_daily"),
        ("safe_for_auto_spawn", "safe_for_auto_spawn"),
        ("data_residency", "data_residency"),
    ]:
        if legacy_key in legacy and new_key not in safety:
            safety[new_key] = legacy[legacy_key]
    if safety:
        new["safety"] = safety

    # Master schema requires at least one of `platforms` or `deployment`.
    if "platforms" not in new and "deployment" not in new:
        new["platforms"] = {}

    out = Path(args.out) if args.out else Path("universal-spawn.yaml")
    if out.exists() and not args.force:
        print(f"refusing to overwrite {out} (pass --force).", file=sys.stderr)
        return 2
    out.write_text(yaml.safe_dump(new, sort_keys=False))
    print(f"wrote   {out} (lifted from {src})")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="universal-spawn",
        description="Validate, init, and migrate universal-spawn manifests.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="cmd", required=True)

    vp = sub.add_parser("validate", help="Validate a manifest.")
    vp.add_argument("path", nargs="?", help="Path to manifest. Default: auto-detect.")
    vp.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    vp.add_argument(
        "--platform-schemas-dir",
        help="Directory with <id>-spawn.schema.json files for platform-extension validation.",
    )
    vp.set_defaults(fn=_cmd_validate)

    ip = sub.add_parser("init", help="Write a starter manifest.")
    ip.add_argument("--type", default="minimal", help=f"Starter id. One of: {', '.join(sorted(STARTERS))}.")
    ip.add_argument("--out", default="universal-spawn.yaml", help="Output path.")
    ip.add_argument("--force", action="store_true", help="Overwrite an existing file.")
    ip.set_defaults(fn=_cmd_init)

    mp = sub.add_parser("migrate", help="Lift a legacy v1.0.0 spawn manifest to v1.0.")
    mp.add_argument("path", nargs="?", help="Source manifest. Default: auto-detect.")
    mp.add_argument("--out", default=None, help="Output path. Default: universal-spawn.yaml.")
    mp.add_argument("--force", action="store_true", help="Overwrite an existing file.")
    mp.set_defaults(fn=_cmd_migrate)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())

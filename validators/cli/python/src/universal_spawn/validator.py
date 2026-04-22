"""Validation core.

Loads the v1.0 master schema (bundled) and validates a manifest dict
or file. Optionally validates platform extensions when a `platforms.<id>`
block is present and a corresponding extension schema is supplied.
"""
from __future__ import annotations

import dataclasses
import json
import os
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

MASTER_ID = "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"
_BUNDLED = Path(__file__).resolve().parent / "_bundled" / "v1.0.schema.json"


class ValidationError(Exception):
    """Raised when a manifest fails validation in non-result-returning APIs."""


@dataclasses.dataclass
class ValidationResult:
    ok: bool
    errors: list[str] = dataclasses.field(default_factory=list)
    warnings: list[str] = dataclasses.field(default_factory=list)
    platforms_checked: list[str] = dataclasses.field(default_factory=list)

    def __bool__(self) -> bool:
        return self.ok


def load_master_schema(path: str | os.PathLike[str] | None = None) -> dict[str, Any]:
    """Load the v1.0 master schema. Defaults to the bundled copy."""
    p = Path(path) if path else _BUNDLED
    return json.loads(p.read_text())


def load_platform_schema(path: str | os.PathLike[str]) -> dict[str, Any]:
    """Load a platform extension schema from disk."""
    return json.loads(Path(path).read_text())


def _load_doc(source: dict[str, Any] | str | os.PathLike[str]) -> dict[str, Any]:
    if isinstance(source, dict):
        return source
    p = Path(source)
    text = p.read_text()
    if p.suffix.lower() in (".yaml", ".yml"):
        return yaml.safe_load(text)
    if p.suffix.lower() == ".json":
        return json.loads(text)
    # Best effort: try YAML (which is a JSON superset).
    return yaml.safe_load(text)


def _format_error(err: Any) -> str:
    path = "/".join(str(p) for p in err.absolute_path) or "<root>"
    return f"{path}: {err.message}"


def validate(
    source: dict[str, Any] | str | os.PathLike[str],
    *,
    master_schema: dict[str, Any] | None = None,
    platform_schemas: dict[str, dict[str, Any]] | None = None,
    strict: bool = False,
) -> ValidationResult:
    """Validate a manifest.

    Parameters
    ----------
    source
        Either a parsed dict, or a path to a YAML/JSON manifest file.
    master_schema
        Optional override for the v1.0 master schema (default: bundled).
    platform_schemas
        Optional map of platform id → extension schema dict. When set, any
        `platforms.<id>` block in the manifest is also validated against
        the matching extension schema.
    strict
        When True, treat warnings as failures (sets `ok=False`).
    """
    doc = _load_doc(source)
    if not isinstance(doc, dict):
        return ValidationResult(ok=False, errors=["root: manifest must be an object"])

    schema = master_schema or load_master_schema()
    master_resource = Resource.from_contents(schema, default_specification=DRAFT7)
    registry = Registry().with_resource(MASTER_ID, master_resource)

    v = Draft7Validator(schema, registry=registry)
    errors = [_format_error(e) for e in sorted(v.iter_errors(doc), key=lambda e: list(e.path))]

    warnings: list[str] = []
    platforms_checked: list[str] = []
    declared_platforms = (doc.get("platforms") or {}) if isinstance(doc.get("platforms"), dict) else {}

    if platform_schemas:
        for pid, ext_schema in platform_schemas.items():
            if pid not in declared_platforms:
                continue
            ext_v = Draft7Validator(ext_schema, registry=registry)
            for e in sorted(ext_v.iter_errors(doc), key=lambda e: list(e.path)):
                errors.append(f"platforms.{pid}/{_format_error(e)}")
            platforms_checked.append(pid)

    # Lightweight semantic checks → warnings (not failures unless strict).
    if doc.get("safety", {}).get("safe_for_auto_spawn") is True and not doc.get("env_vars_required"):
        warnings.append(
            "safety.safe_for_auto_spawn=true with no env_vars_required: "
            "double-check this manifest does not need any secrets."
        )

    ok = not errors
    if strict and warnings:
        ok = False
    return ValidationResult(
        ok=ok,
        errors=errors,
        warnings=warnings,
        platforms_checked=platforms_checked,
    )


def validate_file(
    path: str | os.PathLike[str],
    *,
    platform_schemas_dir: str | os.PathLike[str] | None = None,
    strict: bool = False,
) -> ValidationResult:
    """Convenience wrapper that auto-loads platform extension schemas.

    If `platform_schemas_dir` is given, every `<id>-spawn.schema.json`
    inside it is loaded and used to validate the matching
    `platforms.<id>` block in the manifest.
    """
    platform_schemas: dict[str, dict[str, Any]] | None = None
    if platform_schemas_dir is not None:
        platform_schemas = {}
        for p in Path(platform_schemas_dir).rglob("*-spawn.schema.json"):
            pid = p.stem.removesuffix("-spawn.schema")
            platform_schemas[pid] = load_platform_schema(p)
    return validate(path, platform_schemas=platform_schemas, strict=strict)

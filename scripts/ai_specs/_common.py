"""Shared helpers for batch spec modules.

Provides the standard perks list every AI platform folder starts from,
plus small convenience functions for building compat tables and schema
bodies with less repetition.
"""
from __future__ import annotations

from typing import Any


STANDARD_PERKS = [
    "**Priority discovery** — manifest-declaring entries rank above "
    "scraped or unlabelled ones in the platform's own directory.",
    "**One-click install/deploy** — a Deploy button on any "
    "universal-spawn registry card, pre-filled from the manifest.",
    "**Cost cap prefill** — `safety.cost_limit_usd_daily` "
    "pre-populates the daily spend cap UI.",
    "**Permission envelope prefill** — `safety.min_permissions` "
    "pre-populates the platform's permission dialog.",
    "**Audit trail** — canonical manifest SHA-256 logged on every "
    "spawn so authors can audit which manifest version ran.",
    "**Badges** — a manifest passing this platform's schema carries "
    "a conformance badge in its README.",
]


def schema_object(
    required: list[str] | None = None,
    properties: dict[str, Any] | None = None,
    additional: bool = False,
) -> dict[str, Any]:
    """Shortcut for a strict `additionalProperties: false` object."""
    body: dict[str, Any] = {"type": "object", "additionalProperties": additional}
    if required:
        body["required"] = required
    if properties:
        body["properties"] = properties
    return body


def enum(values: list[str]) -> dict[str, Any]:
    return {"type": "string", "enum": values}


def str_prop(pattern: str | None = None, desc: str | None = None) -> dict[str, Any]:
    p: dict[str, Any] = {"type": "string"}
    if pattern:
        p["pattern"] = pattern
    if desc:
        p["description"] = desc
    return p


def bool_prop(default: bool = False) -> dict[str, Any]:
    return {"type": "boolean", "default": default}


def int_prop(minimum: int | None = None, maximum: int | None = None) -> dict[str, Any]:
    p: dict[str, Any] = {"type": "integer"}
    if minimum is not None:
        p["minimum"] = minimum
    if maximum is not None:
        p["maximum"] = maximum
    return p


def num_prop(minimum: float | None = None, maximum: float | None = None) -> dict[str, Any]:
    p: dict[str, Any] = {"type": "number"}
    if minimum is not None:
        p["minimum"] = minimum
    if maximum is not None:
        p["maximum"] = maximum
    return p


def array_prop(items: dict[str, Any], unique: bool = False, minitems: int | None = None) -> dict[str, Any]:
    p: dict[str, Any] = {"type": "array", "items": items}
    if unique:
        p["uniqueItems"] = True
    if minitems is not None:
        p["minItems"] = minitems
    return p


def tools_array(name_pattern: str = r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$") -> dict[str, Any]:
    """A `tools: [...]` array with {name, function_ref, strict?}."""
    return array_prop(
        schema_object(
            required=["name", "function_ref"],
            properties={
                "name": str_prop(pattern=name_pattern),
                "function_ref": str_prop(desc="Relative path to the tool definition JSON."),
                "strict": bool_prop(False),
            },
        )
    )

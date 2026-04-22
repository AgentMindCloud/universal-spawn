#!/usr/bin/env python3
"""Build the AI platform folders from per-platform SPEC modules.

Imports every module under scripts.ai_specs.{providers,multi_agent,
coding,local} and runs the generator on each SPEC. Missing modules
are silently skipped so batches can land independently.

Usage:
    python3 scripts/build_ai_platforms.py [platform-id ...]

With no arguments, builds every spec. With explicit ids, builds only
those (useful while iterating).
"""
from __future__ import annotations

import importlib
import pkgutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.gen_ai_platform import generate  # noqa: E402
from scripts import ai_specs  # noqa: E402


def _discover() -> list[dict]:
    """Walk scripts/ai_specs/*/ and return every SPEC dict."""
    specs = []
    for category in ("providers", "multi_agent", "coding", "local"):
        pkg_name = f"scripts.ai_specs.{category}"
        try:
            pkg = importlib.import_module(pkg_name)
        except ModuleNotFoundError:
            continue
        for info in pkgutil.iter_modules(pkg.__path__):
            mod = importlib.import_module(f"{pkg_name}.{info.name}")
            if hasattr(mod, "SPEC"):
                spec = mod.SPEC
                # Fill location based on category if not set.
                if category == "providers":
                    spec.setdefault("location", ".")
                else:
                    spec.setdefault("location", category.replace("_", "-"))
                specs.append(spec)
    return specs


def _resolve_root(spec: dict) -> Path:
    repo = Path(__file__).resolve().parent.parent
    if spec["location"] in (".", ""):
        return repo / "platforms" / "ai" / spec["id"]
    return repo / "platforms" / "ai" / spec["location"] / spec["id"]


def main(argv: list[str]) -> int:
    wanted = set(argv[1:])
    count = 0
    for spec in _discover():
        if wanted and spec["id"] not in wanted:
            continue
        generate(spec, root=_resolve_root(spec))
        count += 1
    print(f"\ngenerated {count} platform folder(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

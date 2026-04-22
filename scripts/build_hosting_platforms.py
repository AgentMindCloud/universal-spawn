#!/usr/bin/env python3
"""Build the hosting platform folders from per-provider SPEC modules.

Walks scripts/hosting_specs/ and calls generate() on each SPEC found.
With explicit ids, builds only those (useful while iterating).
"""
from __future__ import annotations

import importlib
import pkgutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.gen_hosting_platform import generate  # noqa: E402
from scripts import hosting_specs  # noqa: E402


def _discover() -> list[dict]:
    specs = []
    for info in pkgutil.iter_modules(hosting_specs.__path__):
        mod = importlib.import_module(f"scripts.hosting_specs.{info.name}")
        if hasattr(mod, "SPEC"):
            specs.append(mod.SPEC)
    return specs


def main(argv: list[str]) -> int:
    wanted = set(argv[1:])
    count = 0
    for spec in _discover():
        if wanted and spec["id"] not in wanted:
            continue
        generate(spec)
        count += 1
    print(f"\ngenerated {count} hosting platform folder(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

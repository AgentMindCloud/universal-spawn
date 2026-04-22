#!/usr/bin/env python3
"""Build Session 4 platform folders from per-platform SPEC modules."""
from __future__ import annotations

import importlib
import pkgutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.gen_session4 import generate  # noqa: E402
from scripts import s4_specs  # noqa: E402

SUBTREES = {
    "creative": "creative",
    "devtools": "devtools",
    "social": "social",
    "data_ml": "data-ml",
    "gaming": "gaming",
    "hardware_iot": "hardware-iot",
}


def _discover() -> list[dict]:
    out = []
    for pkg_name, location in SUBTREES.items():
        try:
            pkg = importlib.import_module(f"scripts.s4_specs.{pkg_name}")
        except ModuleNotFoundError:
            continue
        for info in pkgutil.iter_modules(pkg.__path__):
            mod = importlib.import_module(f"scripts.s4_specs.{pkg_name}.{info.name}")
            if hasattr(mod, "SPEC"):
                spec = mod.SPEC
                spec.setdefault("location", location)
                out.append(spec)
    return out


def main(argv: list[str]) -> int:
    wanted = set(argv[1:])
    count = 0
    for spec in _discover():
        if wanted and spec["id"] not in wanted:
            continue
        generate(spec)
        count += 1
    print(f"\ngenerated {count} Session 4 platform folder(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

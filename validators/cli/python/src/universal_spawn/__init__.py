"""universal-spawn — validator + CLI for the universal-spawn manifest standard.

Public API:

    from universal_spawn import validate, ValidationError

    result = validate(path_or_dict)
    if result.ok:
        ...
    else:
        for err in result.errors:
            print(err)
"""
from .validator import (
    ValidationResult,
    ValidationError,
    validate,
    validate_file,
    load_master_schema,
    load_platform_schema,
)

__all__ = [
    "ValidationResult",
    "ValidationError",
    "validate",
    "validate_file",
    "load_master_schema",
    "load_platform_schema",
]

__version__ = "1.0.0"

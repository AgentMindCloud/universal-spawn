"""crates.io — additive coexistence with Cargo.toml."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "crates-io",
    "title": "crates.io",
    "lede": (
        "A universal-spawn manifest does NOT replace `Cargo.toml`. "
        "Cargo owns dependencies, features, binary targets, and "
        "`[[bin]]` / `[lib]` definitions. `platforms.crates-io` is "
        "additive cross-platform metadata."
    ),
    "cares": (
        "The crate name, edition, MSRV, and whether the crate ships "
        "a library, a binary, or both."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`."),
        ("platforms.crates-io", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.crates-io.crate_name", "Crate name."),
        ("platforms.crates-io.edition", "Rust edition."),
        ("platforms.crates-io.msrv", "Minimum supported Rust version."),
        ("platforms.crates-io.shape", "`library`, `bin`, `both`."),
        ("platforms.crates-io.features", "Named features."),
    ],
    "platform_fields": {
        "crate_name": "Crate name.",
        "edition": "Rust edition.",
        "msrv": "MSRV.",
        "shape": "`library`, `bin`, `both`.",
        "features": "Named features.",
    },
    "schema_body": schema_object(
        required=["crate_name", "edition"],
        properties={
            "crate_name": str_prop(pattern=r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$"),
            "edition": enum(["2015", "2018", "2021", "2024"]),
            "msrv": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "shape": enum(["library", "bin", "both"]),
            "features": {"type": "array", "items": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: crates.io Template
type: library
description: Template for a crates.io-targeted universal-spawn manifest.

platforms:
  crates-io:
    crate_name: your_crate
    edition: "2021"
    msrv: "1.78"
    shape: library
    features: [default, serde]

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [crates-io]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/crates-io-template }
""",
    "native_config_name": "Cargo.toml",
    "native_config_lang": "toml",
    "native_config": """
[package]
name = "your_crate"
version = "0.1.0"
edition = "2021"
rust-version = "1.78"
description = "Your crate"
license = "Apache-2.0"

[features]
default = []
serde = ["dep:serde"]

[dependencies]
""",
    "universal_excerpt": """
platforms:
  crates-io:
    crate_name: your_crate
    edition: "2021"
    msrv: "1.78"
    shape: library
    features: [default, serde]
""",
    "compatibility_extras": (
        "## Additive — not a replacement\n\n"
        "`Cargo.toml` keeps ownership of `dependencies`, `features` "
        "implementations, `[[bin]]` / `[lib]`, workspace config, and "
        "Cargo-specific metadata. universal-spawn just mirrors the "
        "cross-platform-relevant subset."
    ),
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Palette Rust
type: library
summary: Minimal crates.io library with Residual Frequencies palette constants.
description: Small Rust 2021 library, MSRV 1.78.

platforms:
  crates-io:
    crate_name: parchment_palette
    edition: "2021"
    msrv: "1.78"
    shape: library

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [crates-io]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rust-parchment-palette }
  id: com.plate-studio.rust-parchment-palette
""",
        "example-2": """
version: "1.0"
name: Plate CLI Rust
type: cli-tool
summary: Full crates.io binary crate with named features.
description: Rust 2024 binary `plate`. Two features (json, yaml) controlling optional deps.

platforms:
  crates-io:
    crate_name: plate
    edition: "2024"
    msrv: "1.80"
    shape: bin
    features: [default, json, yaml]

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [crates-io]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/rust-plate-cli }
  id: com.plate-studio.rust-plate-cli
""",
    },
}

"""Observable — notebooks + Framework pages."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "observable",
    "title": "Observable",
    "lede": (
        "Observable hosts reactive notebooks and the Observable "
        "Framework (a static-site flavor of the same DAG runtime). "
        "A universal-spawn manifest covers both."
    ),
    "cares": (
        "The `kind` (`notebook`, `framework`), the notebook URL or "
        "Framework page path, and licensing."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `web-app`, `site`."),
        ("platforms.observable", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.observable.kind", "`notebook` or `framework`."),
        ("platforms.observable.notebook_url", "Public Observable notebook URL."),
        ("platforms.observable.framework_root", "Framework project root directory."),
        ("platforms.observable.fork_protection", "If true, the consumer prompts before forking."),
    ],
    "platform_fields": {
        "kind": "`notebook` or `framework`.",
        "notebook_url": "Notebook URL.",
        "framework_root": "Framework project root.",
        "fork_protection": "Prompt before forking.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["notebook", "framework"]),
            "notebook_url": {"type": "string", "format": "uri"},
            "framework_root": str_prop(),
            "fork_protection": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Observable Template
type: notebook
description: Template for an Observable-targeted universal-spawn manifest.

platforms:
  observable:
    kind: notebook
    notebook_url: "https://observablehq.com/@yourhandle/your-notebook"

safety:
  min_permissions: [network:outbound]

env_vars_required: []

deployment:
  targets: [observable]

metadata:
  license: ISC
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/observable-template }
""",
    "native_config_name": "observable notebook URL / Framework root",
    "native_config_lang": "text",
    "native_config": "# Observable notebook config lives in the notebook's metadata or in observablehq.config.js for Framework.\n",
    "universal_excerpt": """
platforms:
  observable:
    kind: notebook
    notebook_url: "https://observablehq.com/@yourhandle/your-notebook"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Notebook
type: notebook
summary: Minimal Observable notebook visualising the parchment plate archetypes.
description: Single notebook URL.

platforms:
  observable:
    kind: notebook
    notebook_url: "https://observablehq.com/@plate-studio/plate-archetypes"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [observable]

visuals: { palette: parchment }

metadata:
  license: ISC
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/observable-plate-archetypes }
  id: com.plate-studio.observable-plate-archetypes
""",
        "example-2": """
version: "1.0"
name: Plate Framework Site
type: site
summary: Full Observable Framework data app with multiple pages.
description: Reactive Observable Framework site under `src/`.

platforms:
  observable:
    kind: framework
    framework_root: src
    fork_protection: true

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [observable]

visuals: { palette: parchment }

metadata:
  license: ISC
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/observable-plate-framework }
  id: com.plate-studio.observable-plate-framework
""",
    },
}

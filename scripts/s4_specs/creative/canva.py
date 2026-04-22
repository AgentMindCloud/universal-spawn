"""Canva — Apps SDK + Templates + duplicate-to-workspace."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "canva",
    "title": "Canva",
    "lede": (
        "Canva's extension surface is the Apps SDK (in-editor apps) "
        "and the Canva Templates gallery (duplicatable designs). The "
        "extension handles both, plus the canonical duplicate-to-"
        "workspace pattern that makes templates one-click shareable."
    ),
    "cares": (
        "The `kind` (`app`, `template`, `design`), the Canva "
        "`app.json` path for apps, and the public design URL for "
        "templates that drives the duplicate button."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `design-template`, `plugin`."),
        ("platforms.canva", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.canva.kind", "`app`, `template`, `design`."),
        ("platforms.canva.app_json", "`app.json` path for Canva Apps."),
        ("platforms.canva.design_url", "Public Canva design URL."),
        ("platforms.canva.design_id", "Canva design id."),
        ("platforms.canva.categories", "Canva category slugs."),
        ("platforms.canva.surface", "In-editor surfaces the app runs on."),
    ],
    "platform_fields": {
        "kind": "`app`, `template`, `design`.",
        "app_json": "Canva Apps SDK `app.json` path.",
        "design_url": "Public Canva design URL.",
        "design_id": "Canva design id.",
        "categories": "Canva category slugs.",
        "surface": "In-editor surfaces the app runs on.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["app", "template", "design"]),
            "app_json": str_prop(),
            "design_url": {"type": "string", "format": "uri"},
            "design_id": str_prop(pattern=r"^[A-Za-z0-9_-]{8,64}$"),
            "categories": {"type": "array", "items": str_prop()},
            "surface": {
                "type": "array",
                "items": enum(["object-panel", "content-panel", "publish", "editor"]),
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: Canva Template
type: design-template
description: Template for a Canva-targeted universal-spawn manifest.

platforms:
  canva:
    kind: template
    design_url: "https://www.canva.com/design/DAF0000000000/view"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [canva]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/canva-template }
""",
    "native_config_name": "app.json (Canva Apps SDK)",
    "native_config_lang": "json",
    "native_config": """
{
  "id": "AAF0000000000",
  "appOrigin": "https://app.example.com",
  "surfaces": ["object-panel"],
  "capabilities": ["upload-image"]
}
""",
    "universal_excerpt": """
platforms:
  canva:
    kind: app
    app_json: app.json
    surface: [object-panel]
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Duplicate-to-your-Canva button** — a manifest with "
        "`kind: template` and a valid `design_url` renders a one-"
        "click duplicate button on any universal-spawn registry card.",
    ],
    "examples": {
        "example-1": """
version: "1.0"
name: Canva App
type: creative-tool
summary: Minimal Canva Apps SDK app that adds Residual Frequencies swatches.
description: Object-panel app adding parchment palette swatches.

platforms:
  canva:
    kind: app
    app_json: app.json
    surface: [object-panel]
    categories: [color, swatches]

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [canva]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/canva-parchment-swatches }
  id: com.plate-studio.canva-parchment-swatches
""",
        "example-2": """
version: "1.0"
name: Plate Presentation
type: design-template
summary: Full Canva presentation template laid out on the parchment palette.
description: >
  Ten-slide Canva presentation that lives in the Templates gallery.
  Uses the Residual Frequencies parchment colors and Instrument Serif
  titles.

platforms:
  canva:
    kind: template
    design_id: DAF1234567890
    design_url: "https://www.canva.com/design/DAF1234567890/view"
    categories: [presentation, template]

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [canva]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/canva-plate-presentation }
  id: com.plate-studio.canva-plate-presentation
""",
        "duplicate-to-workspace": """
version: "1.0"
name: Residual Frequencies Social Pack
type: design-template
summary: Canva design pack — one-click duplicate into the viewer Canva workspace.
description: >
  Social-post pack (12 designs) hosted as a public Canva design. The
  consumer renders a "Use this template" button; clicking it opens
  Canva with the duplicate-to-your-account flow prefilled.

platforms:
  canva:
    kind: template
    design_id: DAF9988776655
    design_url: "https://www.canva.com/design/DAF9988776655/view"
    categories: [social, instagram, template]

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [canva]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/canva-social-pack }
  id: com.plate-studio.canva-social-pack
""",
    },
}

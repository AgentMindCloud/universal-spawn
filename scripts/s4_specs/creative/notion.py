"""Notion — duplicatable templates + databases."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "notion",
    "title": "Notion",
    "lede": (
        "Notion doesn't have a plugin API, but it does have a strong "
        "'duplicate this page' pattern. A universal-spawn manifest "
        "pointing at a Notion page lets consumers render a one-click "
        "duplicate button that brings the template into the user's "
        "own workspace."
    ),
    "cares": (
        "The public Notion page URL, the page id, optional CSV seed "
        "files for database duplication, and icons / covers."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`design-template`, `creative-tool`."),
        ("deployment.targets", "Must include `notion`."),
        ("platforms.notion", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Suggested key."),
        ("platforms.notion.page_url", "Public page URL (required for duplicate)."),
        ("platforms.notion.page_id", "Notion page UUID."),
        ("platforms.notion.kind", "`template`, `database`, `workspace-pack`."),
        ("platforms.notion.seed_csv", "Optional CSV to seed a duplicated database."),
    ],
    "platform_fields": {
        "page_url": "Public page URL used for the duplicate button.",
        "page_id": "Notion page UUID (32 hex chars).",
        "kind": "`template`, `database`, `workspace-pack`.",
        "seed_csv": "Optional CSV to seed a duplicated database.",
    },
    "schema_body": schema_object(
        required=["page_url", "kind"],
        properties={
            "page_url": {"type": "string", "format": "uri"},
            "page_id": str_prop(pattern=r"^[0-9a-f]{32}$"),
            "kind": enum(["template", "database", "workspace-pack"]),
            "seed_csv": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Notion Template
type: design-template
description: Template for a Notion-targeted universal-spawn manifest.

platforms:
  notion:
    page_url: "https://notion.so/yourhandle/0000000000000000000000000000"
    kind: template

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [notion]

metadata:
  license: CC-BY-4.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/notion-template }
""",
    "native_config_name": "Notion page",
    "native_config_lang": "text",
    "native_config": """
Notion has no repo-level config format.
The source of truth is the public page itself, referenced by URL.
A consumer takes ?duplicate=true on that URL to trigger the dupe flow.
""",
    "universal_excerpt": """
platforms:
  notion:
    page_url: "https://notion.so/yourhandle/0000000000000000000000000000"
    kind: template
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Lab Notebook Template
type: design-template
summary: Minimal Notion template for a parchment-style lab notebook.
description: Public Notion template page with the Residual Frequencies plate review rubric preloaded.

platforms:
  notion:
    page_url: "https://notion.so/plate-studio/lab-notebook-0123456789abcdef0123456789abcdef"
    page_id: "0123456789abcdef0123456789abcdef"
    kind: template

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [notion]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/notion-lab-notebook }
  id: com.plate-studio.notion-lab-notebook
""",
        "example-2": """
version: "1.0"
name: CRM Database Pack
type: design-template
summary: Full Notion workspace pack — CRM database plus seeded CSV.
description: >
  Duplicatable workspace pack: one CRM database, two related views,
  and a seed CSV with 200 sample rows so the receiver can see how the
  views behave before entering real data.

platforms:
  notion:
    page_url: "https://notion.so/stack-co/crm-pack-abcdef0123456789abcdef0123456789"
    page_id: "abcdef0123456789abcdef0123456789"
    kind: workspace-pack
    seed_csv: data/crm-seed.csv

safety:
  min_permissions: []
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [notion]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/notion-crm-pack }
  id: com.stack-co.notion-crm-pack
""",
    },
}

"""Figma — plugins, widgets, and community-file templates."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "figma",
    "title": "Figma",
    "lede": (
        "Figma is three surfaces in one: Plugins (code running "
        "inside the editor), Widgets (code rendering inside a file), "
        "and Community files (duplicatable design assets). The "
        "extension covers all three."
    ),
    "cares": (
        "The `kind` (`plugin`, `widget`, `template`), the Figma plugin "
        "manifest path when applicable, editor types (`figma`, "
        "`figjam`, `dev`, `slides`), network-access policy, and the "
        "community-file URL for duplicate-to-workspace."
    ),
    "compat_table": [
        ("version", "Required `\"1.0\"`."),
        ("type", "`creative-tool`, `design-template`, `plugin`, `extension`."),
        ("deployment.targets", "Must include `figma`."),
        ("platforms.figma", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key across the community registry."),
        ("name, description", "Community / plugin directory card."),
        ("type", "See above."),
        ("platforms.figma.kind", "`plugin`, `widget`, or `template`."),
        ("platforms.figma.manifest_file", "Relative path to the Figma plugin/widget `manifest.json`."),
        ("platforms.figma.editor_type", "Editor types the creation runs in."),
        ("platforms.figma.network_access", "`none`, `declared`, `allowed-hosts`."),
        ("platforms.figma.allowed_hosts", "Hosts when `network_access: allowed-hosts`."),
        ("platforms.figma.capabilities", "Figma plugin capabilities."),
        ("platforms.figma.community_file", "Community-file URL or id (for `kind: template`)."),
    ],
    "platform_fields": {
        "kind": "`plugin`, `widget`, or `template`.",
        "manifest_file": "Figma plugin / widget manifest.json path.",
        "editor_type": "Editors the plugin runs in.",
        "network_access": "Network policy.",
        "allowed_hosts": "Allowed hosts when policy is allowed-hosts.",
        "capabilities": "Figma plugin capabilities.",
        "community_file": "Community-file URL or id.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["plugin", "widget", "template"]),
            "manifest_file": str_prop(),
            "editor_type": {
                "type": "array",
                "minItems": 1,
                "items": enum(["figma", "figjam", "dev", "slides"]),
            },
            "network_access": enum(["none", "declared", "allowed-hosts"]),
            "allowed_hosts": {
                "type": "array",
                "items": {"type": "string", "format": "hostname"},
            },
            "capabilities": {
                "type": "array",
                "items": enum(["textreview", "inspect", "vscode", "codegen"]),
            },
            "community_file": str_prop(desc="Community-file URL or numeric id for kind=template."),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Figma Template
type: creative-tool
description: Template for a Figma-targeted universal-spawn manifest.

platforms:
  figma:
    kind: plugin
    manifest_file: figma.manifest.json
    editor_type: [figma, figjam]
    network_access: none

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [figma]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/figma-template }
""",
    "native_config_name": "manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "name": "Parchment Grid",
  "id": "123456789012345678",
  "api": "1.0.0",
  "main": "dist/code.js",
  "ui": "dist/ui.html",
  "editorType": ["figma", "figjam"],
  "networkAccess": { "allowedDomains": ["none"] }
}
""",
    "universal_excerpt": """
platforms:
  figma:
    kind: plugin
    manifest_file: manifest.json
    editor_type: [figma, figjam]
    network_access: none
""",
    "compatibility_extras": (
        "## Three kinds, one extension\n\n"
        "The `kind` field picks which Figma surface the creation "
        "targets. `plugin` and `widget` both point at a "
        "`manifest.json` (the key schema difference is which Figma "
        "fields are read). `template` carries a `community_file` URL "
        "and a `hero_plate` / `icon` for the community card; no code "
        "runs — the consumer opens Figma with the duplicate-to-"
        "workspace link."
    ),
    "perks": STANDARD_PERKS + [
        "**Community-file duplicate-button** — a manifest with "
        "`kind: template` and a valid `community_file` URL renders a "
        "\"Duplicate to your Figma\" button on any universal-spawn "
        "registry card.",
    ],
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Grid
type: creative-tool
summary: Minimal Figma plugin that lays a parchment grid on a frame.
description: One plugin manifest, no network access, Figma + FigJam only.

platforms:
  figma:
    kind: plugin
    manifest_file: figma.manifest.json
    editor_type: [figma, figjam]
    network_access: none

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [figma]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/figma-parchment-grid }
  id: com.plate-studio.figma-parchment-grid
""",
        "example-2": """
version: "1.0"
name: SwiftUI Codegen
type: creative-tool
summary: Full-featured Figma Dev Mode codegen plugin with license server.
description: Dev-Mode codegen plugin that converts frames to SwiftUI. Requires outbound to a license server.

platforms:
  figma:
    kind: plugin
    manifest_file: figma.manifest.json
    editor_type: [figma, dev]
    network_access: allowed-hosts
    allowed_hosts: ["license.codegen.example"]
    capabilities: [codegen, inspect]

safety:
  min_permissions: [network:outbound:license.codegen.example]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [figma]

metadata:
  license: proprietary
  author: { name: Codegen Co., handle: codegen-co, org: Codegen }
  source: { type: git, url: https://github.com/codegen-co/figma-swiftui-codegen }
  id: com.codegen-co.figma-swiftui-codegen
""",
        "duplicate-to-workspace": """
version: "1.0"
name: Residual Frequencies Design System
type: design-template
summary: Community-file template that duplicates the Residual Frequencies design system into the viewer Figma workspace.
description: >
  No code. One community-file URL. The consumer renders a
  "Duplicate to your Figma" button; clicking it opens Figma's
  duplicate flow so the template lands in the user's own workspace.

platforms:
  figma:
    kind: template
    editor_type: [figma]
    network_access: none
    community_file: "https://www.figma.com/community/file/0000000000000000000"

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [figma]

visuals: { palette: parchment, icon: assets/icon.svg, hero_plate: assets/hero.svg }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/figma-residual-frequencies }
  categories: [graphics]
  id: com.plate-studio.figma-residual-frequencies
""",
    },
}

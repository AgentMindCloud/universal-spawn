"""Obsidian — community plugins + vault snapshots + themes."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "obsidian",
    "title": "Obsidian",
    "lede": (
        "Obsidian is a local-first Markdown notes app with a plugin + "
        "theme ecosystem. A universal-spawn manifest targets a "
        "community plugin, a downloadable vault snapshot, or a theme."
    ),
    "cares": (
        "The `kind` (`plugin`, `theme`, `vault-snapshot`), the "
        "Obsidian `manifest.json` path (for plugins/themes), the "
        "minimum Obsidian version, and the vault snapshot archive "
        "when applicable."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `design-template`, `creative-tool`."),
        ("deployment.targets", "Must include `obsidian`."),
        ("platforms.obsidian", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.obsidian.kind", "`plugin`, `theme`, `vault-snapshot`."),
        ("platforms.obsidian.manifest_file", "Obsidian `manifest.json` path."),
        ("platforms.obsidian.min_app_version", "Minimum Obsidian version."),
        ("platforms.obsidian.vault_archive", "Path to the vault archive when `kind: vault-snapshot`."),
        ("platforms.obsidian.desktop_only", "`true` if desktop-only."),
    ],
    "platform_fields": {
        "kind": "`plugin`, `theme`, or `vault-snapshot`.",
        "manifest_file": "Obsidian plugin/theme manifest.json.",
        "min_app_version": "Minimum Obsidian version.",
        "vault_archive": "Vault archive path (for vault-snapshot).",
        "desktop_only": "Desktop-only flag.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["plugin", "theme", "vault-snapshot"]),
            "manifest_file": str_prop(),
            "min_app_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
            "vault_archive": str_prop(),
            "desktop_only": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Obsidian Template
type: extension
description: Template for an Obsidian-targeted universal-spawn manifest.

platforms:
  obsidian:
    kind: plugin
    manifest_file: manifest.json
    min_app_version: "1.5.0"

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [obsidian]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/obsidian-template }
""",
    "native_config_name": "manifest.json",
    "native_config_lang": "json",
    "native_config": """
{
  "id": "your-plugin",
  "name": "Your Plugin",
  "version": "0.1.0",
  "minAppVersion": "1.5.0",
  "description": "",
  "author": "yourhandle",
  "isDesktopOnly": false
}
""",
    "universal_excerpt": """
platforms:
  obsidian:
    kind: plugin
    manifest_file: manifest.json
    min_app_version: "1.5.0"
    desktop_only: false
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Lab Notebook Theme
type: extension
summary: Minimal Obsidian theme in the Residual Frequencies palette.
description: Pure CSS theme. No plugin code. Desktop + mobile.

platforms:
  obsidian:
    kind: theme
    manifest_file: manifest.json
    min_app_version: "1.5.0"
    desktop_only: false

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [obsidian]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/obsidian-lab-notebook-theme }
  id: com.plate-studio.obsidian-lab-notebook-theme
""",
        "example-2": """
version: "1.0"
name: Research Vault Snapshot
type: design-template
summary: Full vault snapshot for a research workflow.
description: >
  Distributable vault archive. Unzipped, it becomes a ready-to-use
  Obsidian vault with three starter notes and a review-rubric
  template. Desktop only because it depends on Dataview.

platforms:
  obsidian:
    kind: vault-snapshot
    vault_archive: dist/vault.zip
    min_app_version: "1.5.0"
    desktop_only: true

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [obsidian]

metadata:
  license: CC-BY-4.0
  author: { name: Research Lab, handle: research-lab }
  source: { type: git, url: https://github.com/research-lab/obsidian-research-vault }
  id: com.research-lab.obsidian-research-vault
""",
    },
}

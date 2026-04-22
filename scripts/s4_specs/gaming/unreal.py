"""Unreal Engine — Marketplace plugin + project templates."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "unreal",
    "title": "Unreal Engine",
    "lede": (
        "Unreal Engine has Marketplace plugins (`.uplugin`) and full "
        "project templates (`.uproject`). A universal-spawn manifest "
        "picks one with `kind` and pins the engine version + target "
        "platforms."
    ),
    "cares": (
        "The `kind` (`marketplace-plugin`, `project-template`), the "
        "engine version, target platforms, and Marketplace category."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-mod`, `game-world`, `creative-tool`, `extension`."),
        ("platforms.unreal", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.unreal.kind", "`marketplace-plugin` or `project-template`."),
        ("platforms.unreal.engine_version", "Engine version."),
        ("platforms.unreal.target_platforms", "Target build platforms."),
        ("platforms.unreal.marketplace_category", "Marketplace category."),
        ("platforms.unreal.entry_uproject", "Entry .uproject file (project-template)."),
    ],
    "platform_fields": {
        "kind": "`marketplace-plugin` or `project-template`.",
        "engine_version": "Engine version.",
        "target_platforms": "Target build platforms.",
        "marketplace_category": "Marketplace category.",
        "entry_uproject": "Entry .uproject file.",
    },
    "schema_body": schema_object(
        required=["kind", "engine_version"],
        properties={
            "kind": enum(["marketplace-plugin", "project-template"]),
            "engine_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "target_platforms": {
                "type": "array",
                "items": enum(["windows", "macos", "linux", "ios", "android", "ps5", "xbox-series", "switch", "vr"]),
            },
            "marketplace_category": enum(["assets", "blueprints", "code-plugins", "complete-projects", "fab"]),
            "entry_uproject": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Unreal Template
type: game-mod
description: Template for an Unreal-targeted universal-spawn manifest.

platforms:
  unreal:
    kind: marketplace-plugin
    engine_version: "5.4"
    target_platforms: [windows, macos]
    marketplace_category: code-plugins

safety:
  min_permissions: [fs:read, gpu:compute]

env_vars_required: []

deployment:
  targets: [unreal]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/unreal-template }
""",
    "native_config_name": ".uplugin / .uproject",
    "native_config_lang": "json",
    "native_config": """
{
  "FileVersion": 3,
  "Version": 1,
  "VersionName": "1.0",
  "FriendlyName": "Your Plugin",
  "Description": "Your plugin description",
  "Category": "Other",
  "EngineVersion": "5.4.0"
}
""",
    "universal_excerpt": """
platforms:
  unreal:
    kind: marketplace-plugin
    engine_version: "5.4"
    target_platforms: [windows, macos]
""",
    "compatibility_extras": "",
    "examples": {
        "asset-store": """
version: "1.0"
name: Parchment Marketplace Plugin
type: game-mod
summary: Unreal Marketplace code plugin adding the Residual Frequencies look.
description: One Marketplace plugin under code-plugins.

platforms:
  unreal:
    kind: marketplace-plugin
    engine_version: "5.4"
    target_platforms: [windows, macos]
    marketplace_category: code-plugins

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [unreal]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/unreal-parchment-plugin }
  id: com.plate-studio.unreal-parchment-plugin
""",
        "project-template": """
version: "1.0"
name: Parchment Lab Project
type: game-world
summary: Full Unreal project template starting a parchment-themed lab scene.
description: Project template covering Windows + PS5 + Xbox Series.

platforms:
  unreal:
    kind: project-template
    engine_version: "5.4"
    target_platforms: [windows, ps5, xbox-series]
    entry_uproject: ParchmentLab.uproject

safety:
  min_permissions: [fs:read, fs:write, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [unreal]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/unreal-parchment-lab-project }
  id: com.plate-studio.unreal-parchment-lab-project
""",
    },
}

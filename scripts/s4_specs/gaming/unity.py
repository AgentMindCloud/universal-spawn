"""Unity (gaming) — Asset Store + project templates (v1.0 track).

Distinct from the v1.0.0 legacy `platforms/unity/` extension. This
v1.0 entry covers both Asset Store packages and full project
templates with the same schema.
"""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "unity",
    "title": "Unity (gaming)",
    "lede": (
        "Unity creations split between Asset Store packages (drop into "
        "an existing project) and full project templates (start a new "
        "project from). A universal-spawn manifest picks one with "
        "`kind` and pins the editor + render-pipeline range."
    ),
    "cares": (
        "The `kind` (`asset-store-package`, `project-template`), the "
        "minimum Unity editor, the render pipeline, and Asset Store "
        "category for asset-store entries."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`game-mod`, `game-world`, `creative-tool`, `extension`."),
        ("platforms.unity", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.unity.kind", "`asset-store-package` or `project-template`."),
        ("platforms.unity.min_editor", "Minimum Unity editor (e.g. `2023.2`)."),
        ("platforms.unity.render_pipeline", "`built-in`, `urp`, `hdrp`."),
        ("platforms.unity.entry_scene", "Entry scene (project-template)."),
        ("platforms.unity.asset_store_category", "Asset Store category (asset-store)."),
        ("platforms.unity.upm_packages", "Required UPM packages."),
    ],
    "platform_fields": {
        "kind": "`asset-store-package` or `project-template`.",
        "min_editor": "Minimum Unity editor.",
        "render_pipeline": "`built-in`, `urp`, `hdrp`.",
        "entry_scene": "Entry scene file.",
        "asset_store_category": "Asset Store category.",
        "upm_packages": "Required UPM packages.",
    },
    "schema_body": schema_object(
        required=["kind", "min_editor"],
        properties={
            "kind": enum(["asset-store-package", "project-template"]),
            "min_editor": str_prop(pattern=r"^[0-9]{4}\.[0-9]+(\.[0-9]+)?(f[0-9]+)?$"),
            "render_pipeline": enum(["built-in", "urp", "hdrp"]),
            "entry_scene": str_prop(),
            "asset_store_category": enum(["3d-models", "animations", "audio", "essentials", "templates", "tools", "vfx", "2d", "add-ons", "ai", "scripting"]),
            "upm_packages": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z0-9.-]+(@.+)?$"),
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: Unity Template (Gaming)
type: game-mod
description: Template for a Unity-targeted universal-spawn manifest.

platforms:
  unity:
    kind: project-template
    min_editor: "2023.2"
    render_pipeline: urp
    entry_scene: Assets/Scenes/Main.unity

safety:
  min_permissions: [fs:read, gpu:compute]

env_vars_required: []

deployment:
  targets: [unity]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/unity-template }
""",
    "native_config_name": "ProjectSettings/*.asset + Packages/manifest.json (UPM)",
    "native_config_lang": "json",
    "native_config": """
{
  "dependencies": {
    "com.unity.render-pipelines.universal": "17.0.3",
    "com.unity.inputsystem": "1.13.0"
  }
}
""",
    "universal_excerpt": """
platforms:
  unity:
    kind: project-template
    min_editor: "2023.2"
    render_pipeline: urp
    entry_scene: Assets/Scenes/Main.unity
    upm_packages:
      - com.unity.render-pipelines.universal
      - com.unity.inputsystem
""",
    "compatibility_extras": "",
    "examples": {
        "asset-store": """
version: "1.0"
name: Parchment Plate Asset Pack
type: game-mod
summary: Unity Asset Store package — 40 parchment-themed props ready to drop into URP scenes.
description: One asset-store package; URP-ready. Tools / 3D Models cross-listing.

platforms:
  unity:
    kind: asset-store-package
    min_editor: "2023.2"
    render_pipeline: urp
    asset_store_category: 3d-models

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [unity]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/unity-plate-asset-pack }
  id: com.plate-studio.unity-plate-asset-pack
""",
        "project-template": """
version: "1.0"
name: Parchment Lab Project Template
type: game-world
summary: Full Unity project template — start a new lab-notebook scene with the Residual Frequencies palette pre-applied.
description: Project template. URP. Includes one demo scene + a starter prefabs library.

platforms:
  unity:
    kind: project-template
    min_editor: "2023.2"
    render_pipeline: urp
    entry_scene: Assets/Scenes/LabNotebook.unity
    upm_packages:
      - com.unity.render-pipelines.universal
      - com.unity.inputsystem
      - com.unity.cinemachine

safety:
  min_permissions: [fs:read, fs:write, gpu:compute]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [unity]

visuals: { palette: parchment }

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/unity-parchment-lab-template }
  id: com.plate-studio.unity-parchment-lab-template
""",
    },
}

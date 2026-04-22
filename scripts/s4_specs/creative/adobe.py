"""Adobe — CEP (legacy) + UXP (modern) extensions for XD/Photoshop/Premiere."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "adobe",
    "title": "Adobe",
    "lede": (
        "Adobe's extension surfaces are CEP (the HTML-based legacy "
        "platform) and UXP (the modern React-style platform). The "
        "same universal-spawn manifest can target Photoshop, "
        "Illustrator, Premiere, XD, InDesign, and After Effects by "
        "naming `hosts[]`. Three distinct examples — XD, Photoshop, "
        "and Premiere — live in the same folder."
    ),
    "cares": (
        "The extension platform (`cep`, `uxp`), the Adobe host apps "
        "(`photoshop`, `illustrator`, `premiere`, `xd`, `indesign`, "
        "`after-effects`), the manifest file, and whether the "
        "extension ships via Creative Cloud's Adobe Exchange."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `plugin`, `extension`."),
        ("platforms.adobe", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.adobe.platform", "`cep` or `uxp`."),
        ("platforms.adobe.manifest_file", "Extension manifest file path."),
        ("platforms.adobe.hosts", "Adobe host apps."),
        ("platforms.adobe.min_host_version", "Minimum host version."),
        ("platforms.adobe.adobe_exchange", "Exchange publication settings."),
    ],
    "platform_fields": {
        "platform": "`cep` (HTML extensions) or `uxp` (modern).",
        "manifest_file": "Extension manifest file path.",
        "hosts": "Target host apps.",
        "min_host_version": "Minimum host version.",
        "adobe_exchange": "Exchange publication settings.",
    },
    "schema_body": schema_object(
        required=["platform", "hosts"],
        properties={
            "platform": enum(["cep", "uxp"]),
            "manifest_file": str_prop(),
            "hosts": {
                "type": "array",
                "minItems": 1,
                "items": enum([
                    "photoshop", "illustrator", "premiere", "xd",
                    "indesign", "after-effects", "lightroom",
                ]),
            },
            "min_host_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)*$"),
            "adobe_exchange": schema_object(
                properties={
                    "listed": bool_prop(False),
                    "price_usd": {"type": "number", "minimum": 0},
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Adobe Template
type: creative-tool
description: Template for an Adobe-targeted universal-spawn manifest.

platforms:
  adobe:
    platform: uxp
    manifest_file: manifest.json
    hosts: [photoshop]
    min_host_version: "25.0"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [adobe]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/adobe-template }
""",
    "native_config_name": "manifest.json (UXP) or manifest.xml (CEP)",
    "native_config_lang": "json",
    "native_config": """
{
  "manifestVersion": 5,
  "id": "com.yourhandle.parchment",
  "name": "Parchment",
  "version": "0.1.0",
  "host": { "app": "PS", "minVersion": "25.0" },
  "entrypoints": [{ "type": "panel", "id": "main", "label": { "default": "Parchment" } }]
}
""",
    "universal_excerpt": """
platforms:
  adobe:
    platform: uxp
    manifest_file: manifest.json
    hosts: [photoshop]
    min_host_version: "25.0"
""",
    "compatibility_extras": (
        "## CEP vs UXP — both supported\n\n"
        "Older Adobe hosts still require **CEP** HTML extensions "
        "(`CSXS/manifest.xml`). Newer hosts (Photoshop 23+, "
        "Illustrator 26+, InDesign 18+) support **UXP** "
        "(`manifest.json`). Set `platform` to the one the extension "
        "actually targets — a single manifest cannot straddle both."
    ),
    "examples": {
        "xd": """
version: "1.0"
name: XD Plate Gallery
type: creative-tool
summary: Adobe XD plugin that imports a plate gallery into the current document.
description: CEP-based XD plugin; imports the Residual Frequencies plate set.

platforms:
  adobe:
    platform: cep
    manifest_file: CSXS/manifest.xml
    hosts: [xd]
    min_host_version: "55.0"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [adobe]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/adobe-xd-plate-gallery }
  id: com.plate-studio.adobe-xd-plate-gallery
""",
        "photoshop": """
version: "1.0"
name: Photoshop Parchment Grader
type: creative-tool
summary: UXP Photoshop panel that grades images against the Residual Frequencies palette.
description: UXP panel for Photoshop 25.0+ that adds a parchment grading control.

platforms:
  adobe:
    platform: uxp
    manifest_file: manifest.json
    hosts: [photoshop]
    min_host_version: "25.0"
    adobe_exchange:
      listed: true
      price_usd: 9

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [adobe]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/adobe-photoshop-grader }
  id: com.plate-studio.adobe-photoshop-grader
""",
        "premiere": """
version: "1.0"
name: Premiere Plate Captioner
type: creative-tool
summary: Premiere Pro CEP extension that captions timelines in lab-notebook voice.
description: >
  CEP-based Premiere Pro panel that scans the active sequence and
  auto-captions each clip in Residual Frequencies voice.

platforms:
  adobe:
    platform: cep
    manifest_file: CSXS/manifest.xml
    hosts: [premiere]
    min_host_version: "24.0"

safety:
  min_permissions: [fs:read, network:outbound:api.anthropic.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key for the captioner.
    secret: true

deployment:
  targets: [adobe]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/adobe-premiere-captioner }
  id: com.plate-studio.adobe-premiere-captioner
""",
    },
}

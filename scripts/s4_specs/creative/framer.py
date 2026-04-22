"""Framer — sites + code components + Framer Marketplace."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "framer",
    "title": "Framer",
    "lede": (
        "Framer is a design tool that ships published websites + "
        "reusable code components. A universal-spawn manifest "
        "describes which shape is being published — a full site, a "
        "component pack, or a project duplicate."
    ),
    "cares": (
        "The `kind` (`site`, `component-pack`, `project`), the "
        "Framer project id, custom-domain metadata, and whether the "
        "project is opted into the marketplace."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`creative-tool`, `site`, `web-app`."),
        ("deployment.targets", "Must include `framer`."),
        ("platforms.framer", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Project-slug suggestion."),
        ("name, description", "Marketplace / site card."),
        ("platforms.framer.kind", "`site`, `component-pack`, `project`."),
        ("platforms.framer.project_id", "Framer project id."),
        ("platforms.framer.custom_domain", "Optional custom domain."),
        ("platforms.framer.marketplace", "Marketplace-listing settings."),
    ],
    "platform_fields": {
        "kind": "`site`, `component-pack`, or `project`.",
        "project_id": "Framer project id.",
        "custom_domain": "Optional custom domain.",
        "marketplace": "Marketplace listing settings.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["site", "component-pack", "project"]),
            "project_id": str_prop(pattern=r"^[A-Za-z0-9_-]{8,64}$"),
            "custom_domain": {"type": "string", "format": "hostname"},
            "marketplace": schema_object(
                properties={
                    "listed": bool_prop(False),
                    "category": enum(["website", "template", "component", "plugin"]),
                    "price_usd": {"type": "number", "minimum": 0, "maximum": 999},
                },
            ),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Framer Template
type: site
description: Template for a Framer-targeted universal-spawn manifest.

platforms:
  framer:
    kind: site
    project_id: abc123xyz
    custom_domain: your-site.example.com

safety:
  min_permissions: [network:inbound]

env_vars_required: []

deployment:
  targets: [framer]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/framer-template }
""",
    "native_config_name": "framer.project.json",
    "native_config_lang": "json",
    "native_config": """
{
  "projectId": "abc123xyz",
  "customDomain": "your-site.example.com",
  "publishChannels": ["production"]
}
""",
    "universal_excerpt": """
platforms:
  framer:
    kind: site
    project_id: abc123xyz
    custom_domain: your-site.example.com
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Framer Landing
type: site
summary: Minimal Framer site with a custom domain.
description: Single published Framer site; no component pack.

platforms:
  framer:
    kind: site
    project_id: landing1
    custom_domain: landing.example.com

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [framer]

metadata:
  license: proprietary
  author: { name: Landing Co., handle: landing-co }
  source: { type: git, url: https://github.com/landing-co/framer-landing }
  id: com.landing-co.framer-landing
""",
        "example-2": """
version: "1.0"
name: Parchment Components
type: creative-tool
summary: Framer code-component pack listed on the marketplace at a fixed price.
description: >
  Eight reusable code components that implement the Residual
  Frequencies visual language. Listed in the marketplace under the
  "component" category.

platforms:
  framer:
    kind: component-pack
    project_id: parchment-components
    marketplace:
      listed: true
      category: component
      price_usd: 19

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [framer]

visuals: { palette: parchment }

metadata:
  license: proprietary
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/framer-parchment-components }
  categories: [graphics]
  id: com.plate-studio.framer-parchment-components
""",
    },
}

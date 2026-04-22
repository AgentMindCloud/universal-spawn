"""Webflow — sites + libraries + data collections."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "webflow",
    "title": "Webflow",
    "lede": (
        "Webflow publishes visual-editor sites with optional CMS "
        "collections. The extension covers a site, a Webflow Libraries "
        "component pack, or a full data-collection schema."
    ),
    "cares": (
        "The `kind` (`site`, `library`, `collection`), the site id, "
        "optional CMS collection definitions, and the custom domain."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`site`, `web-app`, `creative-tool`."),
        ("deployment.targets", "Must include `webflow`."),
        ("platforms.webflow", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Suggested site slug."),
        ("platforms.webflow.kind", "`site`, `library`, `collection`."),
        ("platforms.webflow.site_id", "Webflow site id."),
        ("platforms.webflow.custom_domain", "Custom domain."),
        ("platforms.webflow.collections", "CMS collection schemas."),
        ("platforms.webflow.localization", "Localization locales."),
    ],
    "platform_fields": {
        "kind": "`site`, `library`, `collection`.",
        "site_id": "Webflow site id.",
        "custom_domain": "Custom domain.",
        "collections": "CMS collection schemas.",
        "localization": "Webflow Localization locales.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["site", "library", "collection"]),
            "site_id": str_prop(pattern=r"^[a-f0-9]{24}$"),
            "custom_domain": {"type": "string", "format": "hostname"},
            "collections": {
                "type": "array",
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "singular": str_prop(),
                        "fields_file": str_prop(),
                    },
                ),
            },
            "localization": {
                "type": "array",
                "items": {"type": "string", "pattern": r"^[a-z]{2}(-[A-Z]{2})?$"},
            },
        },
    ),
    "template_yaml": """
version: "1.0"
name: Webflow Template
type: site
description: Template for a Webflow-targeted universal-spawn manifest.

platforms:
  webflow:
    kind: site
    site_id: "000000000000000000000000"
    custom_domain: your-site.example.com

safety:
  min_permissions: [network:inbound]

env_vars_required: []

deployment:
  targets: [webflow]

metadata:
  license: proprietary
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/webflow-template }
""",
    "native_config_name": "Webflow dashboard state (exported JSON)",
    "native_config_lang": "json",
    "native_config": """
{
  "siteId": "000000000000000000000000",
  "customDomain": "your-site.example.com",
  "collections": [{ "name": "posts", "singular": "post" }]
}
""",
    "universal_excerpt": """
platforms:
  webflow:
    kind: site
    site_id: "000000000000000000000000"
    custom_domain: your-site.example.com
    collections:
      - { name: posts, singular: post, fields_file: collections/posts.fields.json }
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Webflow Marketing Site
type: site
summary: Minimal Webflow site deployed to a custom domain.
description: Single site; no CMS collections.

platforms:
  webflow:
    kind: site
    site_id: "111111111111111111111111"
    custom_domain: marketing.example.com

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [webflow]

metadata:
  license: proprietary
  author: { name: Marketing Co., handle: marketing-co }
  source: { type: git, url: https://github.com/marketing-co/webflow-marketing-site }
  id: com.marketing-co.webflow-marketing-site
""",
        "example-2": """
version: "1.0"
name: Webflow Docs with CMS
type: web-app
summary: Webflow docs site with three CMS collections and two locales.
description: >
  Full Webflow deployment — docs site with `posts`, `authors`, and
  `categories` CMS collections, localized to en and fr.

platforms:
  webflow:
    kind: site
    site_id: "222222222222222222222222"
    custom_domain: docs.example.com
    collections:
      - { name: posts,      singular: post,     fields_file: collections/posts.fields.json }
      - { name: authors,    singular: author,   fields_file: collections/authors.fields.json }
      - { name: categories, singular: category, fields_file: collections/categories.fields.json }
    localization: [en, fr]

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [webflow]

metadata:
  license: proprietary
  author: { name: Docs Co., handle: docs-co }
  source: { type: git, url: https://github.com/docs-co/webflow-docs-cms }
  id: com.docs-co.webflow-docs-cms
""",
    },
}

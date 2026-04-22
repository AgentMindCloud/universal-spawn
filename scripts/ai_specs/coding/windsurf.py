"""Windsurf — AI-first IDE fork (Codeium)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "windsurf",
    "title": "Windsurf",
    "location": "coding-agents",
    "lede": (
        "Windsurf is Codeium's IDE, centered on the Cascade agent and "
        "Flows (persistent task contexts). Creations target Windsurf "
        "as rules files, MCP servers, or extensions."
    ),
    "cares": (
        "The kind (`rules`, `mcp-server`, `extension`), Flow metadata "
        "when the creation is a Flow template, and Cascade feature "
        "flags."
    ),
    "extras": (
        "`flow.template_file` points at a reusable Flow template. "
        "`cascade.auto_memory` pre-enables Cascade's auto-memory."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `ai-skill`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "User-level Windsurf settings."),
        ("platforms.windsurf", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Marketplace card."),
        ("type", "`extension`, `plugin`, `ai-skill`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Windsurf settings."),
        ("platforms.windsurf.kind", "`rules`, `mcp-server`, `extension`, `flow-template`."),
        ("platforms.windsurf.rules", "`.windsurfrules` path + scope."),
        ("platforms.windsurf.mcp_ref", "Cross-link to an MCP server."),
        ("platforms.windsurf.flow", "Flow template metadata."),
        ("platforms.windsurf.cascade", "Cascade feature flags."),
    ],
    "platform_fields": {
        "kind": "`rules`, `mcp-server`, `extension`, `flow-template`.",
        "rules": "`.windsurfrules` file + scope.",
        "mcp_ref": "Cross-link to an MCP server manifest.",
        "flow": "Flow template metadata.",
        "cascade": "Cascade feature flags.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["rules", "mcp-server", "extension", "flow-template"]),
            "rules": schema_object(
                properties={
                    "file": str_prop(),
                    "scope": enum(["repository", "workspace", "user"]),
                },
            ),
            "mcp_ref": str_prop(),
            "flow": schema_object(
                properties={
                    "template_file": str_prop(),
                    "auto_activate": bool_prop(False),
                },
            ),
            "cascade": schema_object(
                properties={
                    "auto_memory": bool_prop(False),
                    "agent_mode": enum(["write", "chat", "legacy"]),
                },
            ),
            "publisher_id": str_prop(),
            "min_windsurf_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Windsurf Template
type: extension
description: Template for a Windsurf-targeted universal-spawn manifest.

platforms:
  windsurf:
    kind: rules
    rules: { file: .windsurfrules, scope: repository }
    cascade: { auto_memory: true, agent_mode: write }
    min_windsurf_version: \"1.8\"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [windsurf]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/windsurf-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Windsurf Parchment Rules
type: extension
summary: Minimal Windsurf rules that teach Cascade the Residual Frequencies design system.
description: One .windsurfrules file at repository scope.

platforms:
  windsurf:
    kind: rules
    rules: { file: .windsurfrules, scope: repository }

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [windsurf]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/windsurf-parchment }
  id: com.plate-studio.windsurf-parchment
"""},
        {"yaml": """
version: \"1.0\"
name: Windsurf Flow Deploy
type: ai-skill
summary: Full Windsurf Flow template for shipping a Next.js app to Vercel end-to-end.
description: >
  Reusable Flow template for the deploy-to-Vercel task. Cascade auto-
  activates the flow in write mode. Auto-memory on so context persists
  across turns.

platforms:
  windsurf:
    kind: flow-template
    flow:
      template_file: .windsurf/flows/deploy-to-vercel.md
      auto_activate: true
    cascade:
      auto_memory: true
      agent_mode: write
    min_windsurf_version: \"1.8\"

safety:
  min_permissions:
    - fs:read
    - fs:write
    - network:outbound:api.vercel.com
  safe_for_auto_spawn: false

env_vars_required:
  - name: VERCEL_TOKEN
    description: Vercel deployment token.
    secret: true

deployment:
  targets: [windsurf]

metadata:
  license: MIT
  author: { name: Ship Co., handle: ship-co }
  source: { type: git, url: https://github.com/ship-co/windsurf-deploy-flow }
  id: com.ship-co.windsurf-deploy-flow
"""},
        {"yaml": """
version: \"1.0\"
name: Windsurf Plate Sidecar
type: extension
summary: Creative Windsurf extension that side-panels the plate archive.
description: >
  Adds a side panel to Windsurf showing the Residual Frequencies plate
  archive next to the editor. Pairs with the Plate Archive MCP.

platforms:
  windsurf:
    kind: extension
    mcp_ref: \"../../anthropic-mcp/examples/example-3.yaml\"
    publisher_id: plate-studio.windsurf-plate-sidecar
    min_windsurf_version: \"1.8\"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [windsurf, mcp]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/windsurf-plate-sidecar }
  categories: [graphics, devtools]
  id: com.plate-studio.windsurf-plate-sidecar
"""},
    ],
}

"""Cursor — AI-first IDE fork of VS Code."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "cursor",
    "title": "Cursor",
    "location": "coding-agents",
    "lede": (
        "Cursor is a VS Code fork with built-in AI agents (Tab, Chat, "
        "Agent, Composer). Creations that target Cursor are either "
        "MCP servers it can connect to, rule files (`.cursor/rules/*.mdc`) "
        "that shape its behavior in a repo, or extensions delivered "
        "via the VS Code Marketplace. This extension covers all three."
    ),
    "cares": (
        "The kind (`rules`, `mcp-server`, `extension`), the rule scope, "
        "the MCP binding if applicable, and which Cursor features the "
        "creation expects (agent, composer, tab)."
    ),
    "extras": (
        "`rules.files[]` lists `.mdc` rule files to install under "
        "`.cursor/rules/`. `mcp_ref` references an entry in "
        "`platforms/ai/anthropic-mcp/`."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `ai-skill`."),
        ("safety.*", "Inherited from the underlying provider (Claude, OpenAI, etc.)."),
        ("env_vars_required", "User-level Cursor settings."),
        ("platforms.cursor", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key for extension publication."),
        ("name, description", "Marketplace card."),
        ("type", "`extension`, `plugin`, `ai-skill`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Cursor settings."),
        ("platforms.cursor.kind", "`rules`, `mcp-server`, `extension`."),
        ("platforms.cursor.rules", "Rule files + scope."),
        ("platforms.cursor.mcp_ref", "Relative path into platforms/ai/anthropic-mcp."),
        ("platforms.cursor.features", "Cursor features the creation uses."),
        ("platforms.cursor.min_cursor_version", "Minimum Cursor editor version."),
    ],
    "platform_fields": {
        "kind": "`rules`, `mcp-server`, or `extension`.",
        "rules": "Rule files + scope.",
        "mcp_ref": "Cross-link to an MCP server manifest.",
        "features": "Cursor features the creation uses (`agent`, `composer`, `tab`, `chat`).",
        "min_cursor_version": "Minimum Cursor editor version.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["rules", "mcp-server", "extension"]),
            "rules": schema_object(
                properties={
                    "files": {"type": "array", "items": str_prop()},
                    "scope": enum(["repository", "workspace", "user"]),
                },
            ),
            "mcp_ref": str_prop(desc="Relative path to an MCP server manifest (typically under platforms/ai/anthropic-mcp/)."),
            "features": {
                "type": "array",
                "items": enum(["agent", "composer", "tab", "chat"]),
            },
            "min_cursor_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
            "publisher_id": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Cursor Template
type: extension
description: Template for a Cursor-targeted universal-spawn manifest.

platforms:
  cursor:
    kind: rules
    rules:
      files: [.cursor/rules/main.mdc]
      scope: repository
    features: [agent, composer]
    min_cursor_version: \"0.45\"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [cursor]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/cursor-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Cursor Parchment Rules
type: extension
summary: Minimal Cursor rule file that teaches Cursor the Residual Frequencies design system.
description: One .mdc rule file at repository scope.

platforms:
  cursor:
    kind: rules
    rules:
      files: [.cursor/rules/parchment.mdc]
      scope: repository
    features: [agent, chat]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [cursor]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/cursor-parchment-rules }
  id: com.plate-studio.cursor-parchment-rules
"""},
        {"yaml": """
version: \"1.0\"
name: Cursor GitHub MCP
type: extension
summary: Full Cursor manifest that binds to the GitHub MCP server.
description: >
  Binds Cursor to the GitHub MCP server (defined in platforms/ai/
  anthropic-mcp/examples/example-2.yaml). Exposes PRs, issues, and
  merge tools to Cursor's Agent mode.

platforms:
  cursor:
    kind: mcp-server
    mcp_ref: \"../../anthropic-mcp/examples/example-2.yaml\"
    features: [agent, composer]
    min_cursor_version: \"0.45\"

safety:
  min_permissions: [network:outbound:api.github.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: GITHUB_TOKEN
    description: GitHub token with repo scope.
    secret: true

deployment:
  targets: [cursor, mcp]

metadata:
  license: Apache-2.0
  author: { name: MCP Tooling, handle: mcp-tooling }
  source: { type: git, url: https://github.com/mcp-tooling/cursor-github-mcp }
  id: com.mcp-tooling.cursor-github-mcp
"""},
        {"yaml": """
version: \"1.0\"
name: Cursor Plate Critic
type: extension
summary: Creative Cursor extension that critiques SVG plates in-editor.
description: >
  A VS Code-compatible Cursor extension that adds a `Critique plate`
  command. When the active file is an SVG plate, runs a Claude-based
  critique against the Residual Frequencies rubric.

platforms:
  cursor:
    kind: extension
    publisher_id: plate-studio.cursor-plate-critic
    features: [agent, chat]
    min_cursor_version: \"0.45\"

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key supplied by the user at install.
    secret: true

deployment:
  targets: [cursor]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/cursor-plate-critic }
  categories: [ai, graphics, devtools]
  id: com.plate-studio.cursor-plate-critic
"""},
    ],
}

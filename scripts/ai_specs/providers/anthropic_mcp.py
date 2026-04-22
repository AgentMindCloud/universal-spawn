"""Anthropic MCP — Model Context Protocol servers (separate from claude/)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "anthropic-mcp",
    "title": "Anthropic MCP",
    "location": ".",
    "lede": (
        "MCP (Model Context Protocol) is an open wire protocol for "
        "model-to-tool communication. Servers expose resources, "
        "prompts, and tools; hosts (Claude Desktop, Claude Code, "
        "Cursor, Windsurf, Zed, any future host) connect to them. "
        "This extension describes a manifest whose creation IS an MCP "
        "server — independent of whether Claude is the host."
    ),
    "cares": (
        "The MCP transport (`stdio`, `http`, `websocket`), the command "
        "or URL that starts the server, the declared set of resources, "
        "prompts, and tools the server exposes."
    ),
    "extras": (
        "`resources[]`, `prompts[]`, `tools[]` list what the server "
        "advertises to its host. Purely declarative — the host does "
        "discovery at runtime; the manifest lets a registry index the "
        "server."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "MCP registry card."),
        ("type", "`extension`, `plugin`, `cli-tool`, `library`."),
        ("safety.min_permissions", "Enforced at the host sandbox boundary."),
        ("env_vars_required", "Host credential store."),
        ("platforms.anthropic-mcp", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key across MCP registries."),
        ("name, description", "Card text."),
        ("type", "`extension`, `plugin`, `cli-tool`, `library`."),
        ("safety.min_permissions", "Enforced by the host."),
        ("env_vars_required", "Host credential store."),
        ("platforms.anthropic-mcp.transport", "`stdio`, `http`, `websocket`."),
        ("platforms.anthropic-mcp.command", "stdio command to launch the server."),
        ("platforms.anthropic-mcp.args", "stdio command arguments."),
        ("platforms.anthropic-mcp.url", "http/websocket endpoint URL."),
        ("platforms.anthropic-mcp.resources", "Declared resources."),
        ("platforms.anthropic-mcp.prompts", "Declared prompts."),
        ("platforms.anthropic-mcp.tools", "Declared tools."),
        ("platforms.anthropic-mcp.hosts", "Compatible host list."),
    ],
    "platform_fields": {
        "transport": "MCP transport kind.",
        "command": "stdio launch command.",
        "args": "stdio arguments.",
        "url": "http/websocket endpoint URL.",
        "resources": "Declared resources.",
        "prompts": "Declared prompts.",
        "tools": "Declared tools.",
        "hosts": "Compatible MCP host list.",
    },
    "schema_body": schema_object(
        required=["transport"],
        properties={
            "transport": enum(["stdio", "http", "websocket"]),
            "command": str_prop(desc="Command to launch the server (stdio transport)."),
            "args": {"type": "array", "items": str_prop()},
            "url": str_prop(desc="Endpoint URL (http / websocket transport)."),
            "resources": {
                "type": "array",
                "items": schema_object(
                    required=["uri_template"],
                    properties={
                        "uri_template": str_prop(),
                        "description": str_prop(),
                    },
                ),
            },
            "prompts": {
                "type": "array",
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "description": str_prop(),
                    },
                ),
            },
            "tools": {
                "type": "array",
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "description": str_prop(),
                        "input_schema_ref": str_prop(),
                    },
                ),
            },
            "hosts": {
                "type": "array",
                "items": enum([
                    "claude-desktop", "claude-code", "cursor",
                    "windsurf", "zed", "continue", "cline", "any",
                ]),
            },
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: MCP Template
type: extension
description: Template for an MCP server universal-spawn manifest.

platforms:
  anthropic-mcp:
    transport: stdio
    command: \"node\"
    args: [\"dist/index.js\"]
    tools:
      - name: example_tool
        description: Example tool.
        input_schema_ref: schemas/example_tool.json
    hosts: [claude-desktop, claude-code, cursor, windsurf]

safety:
  min_permissions: [fs:read, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [mcp]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/mcp-template }
""",
    "compatibility_extras": (
        "## Relation to `platforms/ai/claude/`\n\n"
        "`platforms.claude.mcp_server` and `platforms.anthropic-mcp` "
        "overlap in spirit. The `claude` extension wires an MCP server "
        "specifically into Claude. The `anthropic-mcp` extension "
        "describes a server that happens to speak MCP, regardless of "
        "host. A manifest that ships both describes the same server "
        "from two vantage points.\n"
    ),
    "perks": STANDARD_PERKS + [
        "**Host-compat badge** — consumers verify `hosts[]` at "
        "registration time and mark the server as compatible with "
        "each listed host in the registry card.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: MCP Filesystem
type: extension
summary: Minimal MCP server exposing the local filesystem read-only.
description: >
  Small stdio-based MCP server that advertises one resource template
  (`file://*`) and no tools. Read-only by design.

platforms:
  anthropic-mcp:
    transport: stdio
    command: \"npx\"
    args: [\"-y\", \"@modelcontextprotocol/server-filesystem\"]
    resources:
      - uri_template: \"file://{path}\"
        description: Local filesystem path read-only.
    hosts: [claude-desktop, claude-code, cursor, windsurf]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [mcp]

metadata:
  license: MIT
  author: { name: MCP Tooling, handle: mcp-tooling }
  source: { type: git, url: https://github.com/mcp-tooling/mcp-filesystem }
  id: com.mcp-tooling.filesystem
"""},
        {"yaml": """
version: \"1.0\"
name: MCP GitHub
type: extension
summary: Full GitHub MCP server with repos, PRs, issues, and review tools.
description: >
  Docker-hosted HTTP MCP server that advertises GitHub repository,
  PR, issue, and review as resources, plus eight tools for mutating
  operations (open PR, add comment, merge, close issue).

platforms:
  anthropic-mcp:
    transport: http
    url: \"http://localhost:7811/mcp\"
    resources:
      - uri_template: \"github://{owner}/{repo}\"
        description: GitHub repository.
      - uri_template: \"github://{owner}/{repo}/pull/{n}\"
        description: GitHub pull request.
      - uri_template: \"github://{owner}/{repo}/issue/{n}\"
        description: GitHub issue.
    tools:
      - name: open_pr
        description: Open a pull request.
        input_schema_ref: schemas/open_pr.json
      - name: merge_pr
        description: Merge a pull request.
        input_schema_ref: schemas/merge_pr.json
      - name: add_comment
        description: Add a comment to a PR or issue.
        input_schema_ref: schemas/add_comment.json
      - name: close_issue
        description: Close an issue.
        input_schema_ref: schemas/close_issue.json
    hosts: [claude-desktop, claude-code, cursor, windsurf, zed]

safety:
  min_permissions:
    - network:outbound:api.github.com
    - network:inbound
  cost_limit_usd_daily: 0
  safe_for_auto_spawn: false

env_vars_required:
  - name: GITHUB_TOKEN
    description: GitHub token with repo scope.
    secret: true

deployment:
  targets: [mcp]

metadata:
  license: Apache-2.0
  author: { name: MCP Tooling, handle: mcp-tooling }
  source: { type: git, url: https://github.com/mcp-tooling/mcp-github }
  id: com.mcp-tooling.github
"""},
        {"yaml": """
version: \"1.0\"
name: MCP Plate Archive
type: extension
summary: Creative MCP server exposing the Residual Frequencies plate archive.
description: >
  Serves the parchment plate archive over MCP. Each plate is a
  resource with URI `plate://A..F/{id}`; two prompts help drafting
  captions in lab-notebook voice. Any host.

platforms:
  anthropic-mcp:
    transport: stdio
    command: \"python\"
    args: [\"-m\", \"plate_archive_mcp\"]
    resources:
      - uri_template: \"plate://{archetype}/{id}\"
        description: A single Residual Frequencies plate.
    prompts:
      - name: caption_plate
        description: Caption a plate in lab-notebook voice.
      - name: critique_plate
        description: Critique a plate against the visual-system rules.
    hosts: [any]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [mcp]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/plate-archive-mcp }
  categories: [graphics, writing]
  id: com.plate-studio.plate-archive-mcp
"""},
    ],
}

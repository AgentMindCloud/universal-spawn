"""Claude Code — the CLI from Anthropic (distinct from claude/ API extension)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "claude-code",
    "title": "Claude Code",
    "location": "coding-agents",
    "lede": (
        "Claude Code is Anthropic's official CLI — it runs under a "
        "conversational loop with slash commands, hooks, subagents, "
        "and MCP connections. A manifest targeted at Claude Code "
        "declares which surfaces the creation uses. This is distinct "
        "from `platforms/ai/claude/` (the API surface) — Claude Code "
        "is the CLI."
    ),
    "cares": (
        "The surface kind (`slash-command`, `subagent`, `hook`, "
        "`mcp-server`, `skill`), the file location inside `.claude/`, "
        "and the model choice."
    ),
    "extras": (
        "`hook.event` registers a hook on one of the Claude Code hook "
        "events (`PreToolUse`, `PostToolUse`, `Stop`, etc.). "
        "`subagent.file` points at a subagent definition."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`cli-tool`, `extension`, `ai-skill`, `ai-agent`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Shell env."),
        ("platforms.claude-code", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Surfaced in Claude Code's listing commands."),
        ("type", "`cli-tool`, `extension`, `ai-skill`, `ai-agent`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Shell env."),
        ("platforms.claude-code.kind", "`slash-command`, `subagent`, `hook`, `mcp-server`, `skill`."),
        ("platforms.claude-code.file", "Relative path inside `.claude/` where the creation installs."),
        ("platforms.claude-code.model", "Claude model (when the creation pins one)."),
        ("platforms.claude-code.hook", "Hook registration (kind+event+matcher)."),
        ("platforms.claude-code.subagent", "Subagent definition."),
        ("platforms.claude-code.mcp_ref", "Cross-link to an MCP server manifest."),
    ],
    "platform_fields": {
        "kind": "`slash-command`, `subagent`, `hook`, `mcp-server`, `skill`.",
        "file": "Relative path inside `.claude/`.",
        "model": "Claude model (optional pin).",
        "hook": "Hook registration block.",
        "subagent": "Subagent definition block.",
        "mcp_ref": "Cross-link to an MCP server manifest.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["slash-command", "subagent", "hook", "mcp-server", "skill"]),
            "file": str_prop(desc="Relative path inside `.claude/`."),
            "model": enum(["claude-opus-4-7", "claude-sonnet-4-6", "claude-haiku-4-5-20251001"]),
            "hook": schema_object(
                properties={
                    "event": enum([
                        "SessionStart", "SessionEnd", "UserPromptSubmit",
                        "PreToolUse", "PostToolUse", "Stop", "SubagentStop",
                        "Notification", "PreCompact",
                    ]),
                    "matcher": str_prop(),
                    "command": str_prop(),
                },
            ),
            "subagent": schema_object(
                properties={
                    "file": str_prop(),
                    "tools": {"type": "array", "items": str_prop()},
                },
            ),
            "mcp_ref": str_prop(),
            "min_claude_code_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Claude Code Template
type: cli-tool
description: Template for a Claude-Code-targeted universal-spawn manifest.

platforms:
  claude-code:
    kind: slash-command
    file: .claude/commands/hello.md
    model: claude-sonnet-4-6
    min_claude_code_version: \"2.0\"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [claude-code]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/claude-code-template }
""",
    "compatibility_extras": (
        "## Relation to `platforms/ai/claude/`\n\n"
        "`platforms/ai/claude/` describes how a creation appears to the "
        "Claude **API** (Messages API, Skills, Agents SDK). "
        "`platforms/ai/coding-agents/claude-code/` describes how a "
        "creation appears to the **Claude Code CLI** (slash commands, "
        "hooks, subagents, MCP bindings). A creation MAY target both; "
        "most target only one."
    ),
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Slash Hello
type: cli-tool
summary: Minimal Claude Code slash command.
description: One `/hello` slash command that greets the user.

platforms:
  claude-code:
    kind: slash-command
    file: .claude/commands/hello.md
    model: claude-haiku-4-5-20251001

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [claude-code]

metadata:
  license: Apache-2.0
  author: { name: Hello Co., handle: hello-co }
  source: { type: git, url: https://github.com/hello-co/claude-code-hello }
  id: com.hello-co.claude-code-hello
"""},
        {"yaml": """
version: \"1.0\"
name: PreToolUse Auditor
type: extension
summary: Full Claude Code PreToolUse hook that audits Bash commands against an allowlist.
description: >
  Hook runs before every Bash tool call. Matches on the Bash tool.
  Command shells out to a Python auditor that checks the command
  against an allowlist. Block on miss.

platforms:
  claude-code:
    kind: hook
    file: .claude/hooks/bash-auditor.py
    hook:
      event: PreToolUse
      matcher: Bash
      command: \"python3 .claude/hooks/bash-auditor.py\"
    min_claude_code_version: \"2.0\"

safety:
  min_permissions: [fs:read, fs:exec:/usr/bin/python3]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [claude-code]

metadata:
  license: Apache-2.0
  author: { name: Security Team, handle: security-team, org: Acme }
  source: { type: git, url: https://github.com/acme-security/claude-code-bash-auditor }
  id: com.acme-security.claude-code-bash-auditor
"""},
        {"yaml": """
version: \"1.0\"
name: Plate Subagent
type: ai-agent
summary: Creative Claude Code subagent that generates Residual Frequencies plate SVG.
description: >
  Subagent specialised for plate SVG generation. Tools limited to Read,
  Write, and WebSearch. Opus 4.7 for best composition quality.

platforms:
  claude-code:
    kind: subagent
    file: .claude/subagents/plate-generator.md
    model: claude-opus-4-7
    subagent:
      file: .claude/subagents/plate-generator.md
      tools: [Read, Write, WebSearch]

safety:
  min_permissions:
    - fs:read
    - fs:write
    - network:outbound:api.anthropic.com
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [claude-code]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/claude-code-plate-subagent }
  categories: [ai, graphics, devtools]
  id: com.plate-studio.claude-code-plate-subagent
"""},
    ],
}

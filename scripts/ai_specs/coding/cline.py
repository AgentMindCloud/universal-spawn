"""Cline — IDE extension (autonomous coding agent)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "cline",
    "title": "Cline",
    "location": "coding-agents",
    "lede": (
        "Cline is an open-source autonomous coding agent shipped as a "
        "VS Code extension. Each turn picks from a short, well-typed "
        "toolset (read_file, write_to_file, execute_command, "
        "browser_action, ask_followup_question). A manifest declares "
        "which of those tools are allowed and the default provider."
    ),
    "cares": (
        "The provider/model, the tool allowlist (auto-approve list), "
        "and the mode (`plan`, `act`)."
    ),
    "extras": (
        "`auto_approve_tools[]` pre-authorizes a subset of tools so "
        "Cline doesn't prompt the user each turn. Use sparingly."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `ai-agent`."),
        ("safety.min_permissions", "Reflected onto Cline's tool allowlist."),
        ("env_vars_required", "VS Code secret store."),
        ("platforms.cline", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Shown in Cline's workspace profile picker."),
        ("type", "`extension`, `ai-agent`."),
        ("safety.min_permissions", "Mapped to auto_approve_tools."),
        ("env_vars_required", "VS Code secret store."),
        ("platforms.cline.provider", "Model provider."),
        ("platforms.cline.model", "Model id."),
        ("platforms.cline.mode", "`plan` or `act`."),
        ("platforms.cline.auto_approve_tools", "Tools pre-authorised per turn."),
        ("platforms.cline.max_requests_per_task", "Upper bound on per-task requests."),
    ],
    "platform_fields": {
        "provider": "Model provider.",
        "model": "Model id.",
        "mode": "`plan` or `act`.",
        "auto_approve_tools": "Tools pre-authorised per turn.",
        "max_requests_per_task": "Cap on per-task requests.",
    },
    "schema_body": schema_object(
        required=["provider", "model"],
        properties={
            "provider": enum(["openai", "anthropic", "google", "mistral", "together", "fireworks", "groq", "ollama", "lmstudio"]),
            "model": str_prop(),
            "mode": enum(["plan", "act"]),
            "auto_approve_tools": {
                "type": "array",
                "items": enum([
                    "read_file",
                    "list_files",
                    "search_files",
                    "write_to_file",
                    "replace_in_file",
                    "execute_command",
                    "browser_action",
                    "ask_followup_question",
                ]),
            },
            "max_requests_per_task": {"type": "integer", "minimum": 1, "maximum": 500},
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Cline Template
type: extension
description: Template for a Cline-targeted universal-spawn manifest.

platforms:
  cline:
    provider: anthropic
    model: claude-sonnet-4-6
    mode: act
    auto_approve_tools: [read_file, list_files, search_files]
    max_requests_per_task: 50

safety:
  min_permissions: [fs:read, network:outbound:api.anthropic.com]
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [cline]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/cline-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Cline Read-only Reviewer
type: extension
summary: Minimal Cline profile — read-only review, plan mode only.
description: Sonnet in plan mode. Only read/list/search tools pre-approved.

platforms:
  cline:
    provider: anthropic
    model: claude-sonnet-4-6
    mode: plan
    auto_approve_tools: [read_file, list_files, search_files]
    max_requests_per_task: 20

safety:
  min_permissions: [fs:read, network:outbound:api.anthropic.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [cline]

metadata:
  license: Apache-2.0
  author: { name: Review Co., handle: review-co }
  source: { type: git, url: https://github.com/review-co/cline-reviewer }
  id: com.review-co.cline-reviewer
"""},
        {"yaml": """
version: \"1.0\"
name: Cline Coder Act
type: extension
summary: Full Cline profile for autonomous coding with act mode and browser access.
description: >
  Opus 4.7 in act mode. Read + write + execute tools approved. Browser
  action approved for web research. Capped at 100 requests per task.

platforms:
  cline:
    provider: anthropic
    model: claude-opus-4-7
    mode: act
    auto_approve_tools:
      - read_file
      - list_files
      - search_files
      - write_to_file
      - replace_in_file
      - execute_command
      - browser_action
    max_requests_per_task: 100

safety:
  min_permissions:
    - fs:read
    - fs:write
    - network:outbound
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [cline]

metadata:
  license: Apache-2.0
  author: { name: Code Lab, handle: code-lab, org: Lab }
  source: { type: git, url: https://github.com/code-lab/cline-coder-act }
  id: com.code-lab.cline-coder-act
"""},
        {"yaml": """
version: \"1.0\"
name: Cline Plate Composer
type: extension
summary: Creative Cline profile that composes SVG plates in act mode.
description: >
  Mistral-large in act mode. Read + write pre-approved but `execute_command`
  is NOT — plates are pure file edits. Keeps the agent honest.

platforms:
  cline:
    provider: mistral
    model: mistral-large-latest
    mode: act
    auto_approve_tools: [read_file, list_files, write_to_file, replace_in_file]
    max_requests_per_task: 30

safety:
  min_permissions: [fs:read, fs:write, network:outbound:api.mistral.ai]
  safe_for_auto_spawn: false

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true

deployment:
  targets: [cline]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/cline-plate-composer }
  categories: [ai, graphics, devtools]
  id: com.plate-studio.cline-plate-composer
"""},
    ],
}

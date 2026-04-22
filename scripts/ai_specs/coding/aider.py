"""Aider — CLI pair-programmer."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "aider",
    "title": "Aider",
    "location": "coding-agents",
    "lede": (
        "Aider is a CLI pair-programmer that edits a git repository "
        "directly, committing as it goes. Creations targeting Aider "
        "are typically rule files in `.aider.conf.yml` or task-specific "
        "wrappers around the CLI."
    ),
    "cares": (
        "The model selection, edit format (`diff`, `whole`, `udiff`, "
        "`editor-diff`), the auto-commit toggle, and the read/write "
        "file allowlist."
    ),
    "extras": (
        "`auto_commits` toggles git commits per edit. `map_tokens` "
        "sizes the repo-map context window."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`cli-tool`, `extension`, `ai-skill`."),
        ("safety.min_permissions", "Enforced when Aider runs under a sandboxed wrapper; Aider itself does not sandbox."),
        ("env_vars_required", "User shell env."),
        ("platforms.aider", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Shown in `aider --install <name>` listings."),
        ("type", "`cli-tool`, `extension`, `ai-skill`."),
        ("safety.*", "Enforced via wrapper."),
        ("env_vars_required", "Shell env."),
        ("platforms.aider.provider", "Model provider."),
        ("platforms.aider.model", "Model id."),
        ("platforms.aider.edit_format", "Edit format."),
        ("platforms.aider.auto_commits", "Commit-per-edit toggle."),
        ("platforms.aider.map_tokens", "Repo-map context window size."),
        ("platforms.aider.read", "Read allowlist."),
        ("platforms.aider.config_file", "Path to the .aider.conf.yml."),
    ],
    "platform_fields": {
        "provider": "Model provider.",
        "model": "Model id.",
        "edit_format": "`diff`, `whole`, `udiff`, `editor-diff`.",
        "auto_commits": "Commit per edit toggle.",
        "map_tokens": "Repo-map context window size.",
        "read": "Read allowlist (relative paths).",
        "config_file": "Path to the .aider.conf.yml.",
    },
    "schema_body": schema_object(
        required=["provider", "model"],
        properties={
            "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "together", "fireworks", "local"]),
            "model": str_prop(),
            "edit_format": enum(["diff", "whole", "udiff", "editor-diff"]),
            "auto_commits": bool_prop(True),
            "map_tokens": {"type": "integer", "minimum": 0, "maximum": 32768},
            "read": {"type": "array", "items": str_prop()},
            "config_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Aider Template
type: cli-tool
description: Template for an Aider-targeted universal-spawn manifest.

platforms:
  aider:
    provider: anthropic
    model: claude-sonnet-4-6
    edit_format: diff
    auto_commits: true
    map_tokens: 2048
    config_file: .aider.conf.yml

safety:
  min_permissions: [fs:read, fs:write, network:outbound:api.anthropic.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [aider]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/aider-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Aider Minimal Config
type: cli-tool
summary: Minimal Aider config with Sonnet, diff edits, auto-commits.
description: Single Aider config for a repo.

platforms:
  aider:
    provider: anthropic
    model: claude-sonnet-4-6
    edit_format: diff
    auto_commits: true
    config_file: .aider.conf.yml

safety:
  min_permissions: [fs:read, fs:write, network:outbound:api.anthropic.com]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [aider]

metadata:
  license: Apache-2.0
  author: { name: Aider Co., handle: aider-co }
  source: { type: git, url: https://github.com/aider-co/aider-minimal }
  id: com.aider-co.aider-minimal
"""},
        {"yaml": """
version: \"1.0\"
name: Aider Reviewer Config
type: cli-tool
summary: Full Aider config for a read-only reviewer with large map window.
description: >
  Aider configured for a code-review workflow. Read-only (no edits,
  no commits). Large repo-map window. Uses Claude Opus.

platforms:
  aider:
    provider: anthropic
    model: claude-opus-4-7
    edit_format: editor-diff
    auto_commits: false
    map_tokens: 16384
    read:
      - \"**/*.py\"
      - \"**/*.ts\"
      - \"**/*.md\"
    config_file: .aider.reviewer.yml

safety:
  min_permissions: [fs:read, network:outbound:api.anthropic.com]
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [aider]

metadata:
  license: Apache-2.0
  author: { name: Review Lab, handle: review-lab }
  source: { type: git, url: https://github.com/review-lab/aider-reviewer }
  id: com.review-lab.aider-reviewer
"""},
        {"yaml": """
version: \"1.0\"
name: Aider Plate Generator
type: cli-tool
summary: Creative Aider config that generates SVG plates via whole-file edits.
description: >
  Aider configured for plate generation: Mistral-large, whole-file
  edit format (because SVG diffs are noisy), auto-commits into a
  dedicated branch.

platforms:
  aider:
    provider: mistral
    model: mistral-large-latest
    edit_format: whole
    auto_commits: true
    map_tokens: 1024
    read: [\"assets/plates/*.svg\", \"design/residual-frequencies.md\"]
    config_file: .aider.plates.yml

safety:
  min_permissions: [fs:read, fs:write, network:outbound:api.mistral.ai]
  safe_for_auto_spawn: false

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true

deployment:
  targets: [aider]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/aider-plate-generator }
  categories: [ai, graphics, devtools]
  id: com.plate-studio.aider-plate-generator
"""},
    ],
}

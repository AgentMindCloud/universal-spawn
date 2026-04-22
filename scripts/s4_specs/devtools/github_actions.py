"""GitHub Actions — workflows + reusable actions."""
from scripts.ai_specs._common import STANDARD_PERKS, enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "github-actions",
    "title": "GitHub Actions",
    "lede": (
        "GitHub Actions are either workflow files (`.github/workflows/*.yaml`) "
        "or reusable actions (`action.yml` at repo root). A universal-"
        "spawn manifest picks one and records the events it listens "
        "for, the runner, and the publication channel (Actions Marketplace)."
    ),
    "cares": (
        "The `kind` (`workflow`, `reusable-action`), triggers, runner "
        "images, and the Marketplace category."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `library`, `cli-tool`."),
        ("platforms.github-actions", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.github-actions.kind", "`workflow`, `reusable-action`."),
        ("platforms.github-actions.workflow_file", "Workflow file path."),
        ("platforms.github-actions.action_type", "`docker`, `composite`, `javascript`."),
        ("platforms.github-actions.runs_on", "Runner list."),
        ("platforms.github-actions.triggers", "Events."),
        ("platforms.github-actions.marketplace_category", "Marketplace category."),
    ],
    "platform_fields": {
        "kind": "`workflow` or `reusable-action`.",
        "workflow_file": "Workflow file path.",
        "action_type": "`docker`, `composite`, `javascript`.",
        "runs_on": "Runner labels.",
        "triggers": "Workflow triggers.",
        "marketplace_category": "Marketplace category.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["workflow", "reusable-action"]),
            "workflow_file": str_prop(),
            "action_type": enum(["docker", "composite", "javascript"]),
            "runs_on": {
                "type": "array",
                "items": str_prop(),
            },
            "triggers": {
                "type": "array",
                "items": enum(["push", "pull_request", "schedule", "workflow_dispatch", "release", "issues", "deployment", "repository_dispatch"]),
            },
            "marketplace_category": enum(["CI", "Deployment", "Code quality", "Utilities", "Monitoring", "Security", "Publishing", "API management", "Code review", "Project management", "Learning"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: GitHub Actions Template
type: workflow
description: Template for a GitHub-Actions-targeted universal-spawn manifest.

platforms:
  github-actions:
    kind: workflow
    workflow_file: .github/workflows/ci.yaml
    runs_on: [ubuntu-latest]
    triggers: [push, pull_request]

safety:
  min_permissions: [network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [github-actions]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/github-actions-template }
""",
    "native_config_name": ".github/workflows/*.yaml / action.yml",
    "native_config_lang": "yaml",
    "native_config": """
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo ok
""",
    "universal_excerpt": """
platforms:
  github-actions:
    kind: workflow
    workflow_file: .github/workflows/ci.yaml
    runs_on: [ubuntu-latest]
    triggers: [push, pull_request]
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Marketplace listing** — a manifest with `kind: reusable-action` "
        "and a valid `marketplace_category` is eligible for the "
        "Actions Marketplace listing workflow.",
    ],
    "examples": {
        "example-1": """
version: "1.0"
name: CI Workflow
type: workflow
summary: Minimal universal-spawn CI workflow (lint + validate).
description: Runs markdownlint and the session validators on every push.

platforms:
  github-actions:
    kind: workflow
    workflow_file: .github/workflows/validate.yaml
    runs_on: [ubuntu-latest]
    triggers: [push, pull_request]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [github-actions]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/github-actions-ci }
  id: com.plate-studio.github-actions-ci
""",
        "example-2": """
version: "1.0"
name: Parchment Lint Action
type: workflow
summary: Reusable composite action that lints SVG plates against the Residual Frequencies rubric.
description: Published on the Actions Marketplace under Code quality.

platforms:
  github-actions:
    kind: reusable-action
    action_type: composite
    marketplace_category: Code quality
    runs_on: [ubuntu-latest]

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [github-actions]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/parchment-lint-action }
  id: com.plate-studio.parchment-lint-action
""",
    },
}

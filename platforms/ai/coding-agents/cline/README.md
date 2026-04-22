# Cline — universal-spawn platform extension

Cline is an open-source autonomous coding agent shipped as a VS Code extension. Each turn picks from a short, well-typed toolset (read_file, write_to_file, execute_command, browser_action, ask_followup_question). A manifest declares which of those tools are allowed and the default provider.

## What this platform cares about

The provider/model, the tool allowlist (auto-approve list), and the mode (`plan`, `act`).

## What platform-specific extras unlock

`auto_approve_tools[]` pre-authorizes a subset of tools so Cline doesn't prompt the user each turn. Use sparingly.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Cline behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `ai-agent`. |
| `safety.min_permissions` | Reflected onto Cline's tool allowlist. |
| `env_vars_required` | VS Code secret store. |
| `platforms.cline` | Strict. |

### `platforms.cline` fields

| Field | Purpose |
|---|---|
| `platforms.cline.provider` | Model provider. |
| `platforms.cline.model` | Model id. |
| `platforms.cline.mode` | `plan` or `act`. |
| `platforms.cline.auto_approve_tools` | Tools pre-authorised per turn. |
| `platforms.cline.max_requests_per_task` | Cap on per-task requests. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.

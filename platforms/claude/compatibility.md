# Claude — compatibility notes

This file records how the Claude platform extension interacts with the
core universal-spawn manifest fields. It refines the per-platform
column in
[`spec/v1.0.0/compatibility-matrix.md`](../../spec/v1.0.0/compatibility-matrix.md).

## Core fields

| Field                  | Behavior on Claude                                                                 |
|------------------------|-------------------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0` in v1-era. Unknown majors are rejected.                            |
| `id`                   | Used as the stable key in Claude's registries; must not collide with an existing id.|
| `name`                 | Displayed in skill pickers and the tool menu.                                      |
| `kind`                 | Must be one of `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `library`, `workflow`.|
| `description`          | Used verbatim in the skill card.                                                   |
| `summary`              | Used in compact cards and CLI listings.                                            |
| `license`              | `proprietary` is allowed but suppresses publication to Claude's public directory.  |
| `author` / `maintainers`| Shown on the skill card.                                                          |
| `source`               | Required; Claude refuses to spawn manifests without a canonical source.            |
| `homepage`             | Used for the "Learn more" link on the skill card.                                  |
| `icon`                 | Displayed at 64×64; SVG preferred.                                                 |
| `hero_plate`           | Shown in the detail view.                                                          |
| `keywords` / `categories`| Used for search.                                                                 |
| `runtime`              | Informational; Claude does not install runtimes itself.                            |
| `dependencies`         | Resolved transitively by the installer when the creation is spawned locally.       |
| `entrypoints`          | Required. At least one entrypoint of kind `tool-call`, `slash-command`, `stdio`, `http`, or `websocket`. |
| `env_vars_required`    | Surfaced to the user at first spawn; secrets are stored in Claude's credential store. |
| `min_permissions`      | Enforced on the tool-calling and code-execution sandboxes.                         |
| `rate_limit_qps`       | Advisory — enforced best-effort against outbound tool calls.                       |
| `cost_limit_usd_daily` | Enforced as a hard ceiling at the API key / org scope.                             |
| `safe_for_auto_spawn`  | If false or absent, a human must confirm the first spawn.                          |
| `data_residency`       | Used to pick the processing region when multi-region inference is available.       |
| `compat.grok_install`  | Allowed; Claude will not lower the manifest itself, but will annotate the skill card. |
| `signatures`           | Verified when present; unverified-signature manifests are gated behind a warning.  |

## Entrypoint kinds

- `tool-call` → a tool in the Messages API `tools` array.
- `slash-command` → a Claude Code `/`-prefixed command.
- `stdio` → an MCP server launched over stdio.
- `http`, `websocket` → an MCP server over HTTP or WebSocket.
- `cli` → usable only via `claude-code`.

Other kinds (`scene`, `ui-panel`, `container`, …) are ignored.

## Round-trip with `grok-install` v2.14

When `compat.grok_install.version >= "2.14"` is set, a Claude consumer
MAY display a "Also spawnable on Grok" badge on the skill card. No
automatic transformation is performed.

## Known limitations

- Claude does not expose `webhook` entrypoints today. Declare them if
  the same manifest is also targeting a webhook-capable platform like
  Discord or Vercel.
- `cost_limit_usd_daily` is enforced per API key; manifests spawned
  under different API keys each get their own daily envelope.
- `signatures` enforcement is advisory in v1.0.0. A consumer MAY
  require signatures for internal deployments via external policy.

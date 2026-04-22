# Claude compatibility — universal-spawn ↔ Anthropic surfaces

| universal-spawn v1.0 field             | Claude use                                               |
|----------------------------------------|-----------------------------------------------------------|
| `version`                              | Required literal `"1.0"`.                                |
| `metadata.id`                          | Stable key in Anthropic's registry; clashes rejected.    |
| `name`, `description`, `summary`       | Card text in Claude.ai, Claude Code, and the API console.|
| `type`                                 | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`. |
| `safety.min_permissions`               | Enforced on tool-call + code-execution sandbox.          |
| `safety.rate_limit_qps`                | Best-effort on outbound tool calls.                      |
| `safety.cost_limit_usd_daily`          | Hard ceiling at key/org.                                 |
| `safety.safe_for_auto_spawn`           | First-run confirmation gate.                             |
| `safety.data_residency`                | Routing hint for multi-region inference.                 |
| `env_vars_required[*]`                 | Credential store staging; missing required blocks spawn. |
| `metadata.author`, `metadata.maintainers` | Shown on the skill card.                              |
| `metadata.source.commit`               | Pinned in the install record for audit.                  |
| `visuals.icon`                         | 64×64 render on skill card.                              |
| `visuals.hero_plate`                   | Detail view.                                             |
| `platforms.claude.skill_type`          | Determines surface registration strategy.                |
| `platforms.claude.surface[*]`          | Restricts which Anthropic surfaces may spawn.            |
| `platforms.claude.tools[*]`            | Messages API `tools` array.                              |
| `platforms.claude.mcp_server`          | Registered with the MCP host (see `../anthropic-mcp/`).  |
| `platforms.claude.computer_use`        | Sandbox envelope for the Computer-Use API.               |
| `platforms.claude.thinking`            | Extended-thinking budget recommendation.                 |
| `platforms.claude.prompt_cache`        | Enables prompt caching for recurring context.            |
| Other `platforms.*`                    | Ignored; that sibling platform handles them.             |

## Surface matrix

| `surface[*]`         | Meaning                                                 |
|----------------------|----------------------------------------------------------|
| `claude-api`         | The Messages API and the Claude Agent SDK.              |
| `claude-code`        | Claude Code (CLI), incl. slash commands and Agent tool. |
| `claude-app`         | Claude.ai (web/mobile), incl. Skills and Projects.      |
| `claude-mcp`         | Any MCP host connected to Claude.                       |
| `claude-chrome`      | The Claude-in-Chrome extension.                         |

Omit `surface` → spec violation (schema requires `minItems: 1`).
Include only surfaces the creation actually works on; Claude refuses
to spawn on a surface the manifest did not name.

## Limitations in v1.0

- `webhook` entrypoints are not consumed by Claude today. Declare
  them if the same manifest also targets a webhook-capable platform
  (Discord, Vercel).
- `signatures` verification is advisory in v1.0. Enforce via external
  policy for internal deployments.
- The Claude-in-Chrome integration reads `computer_use.allowed_urls`
  verbatim; universal-spawn does not yet model origin-vs-URL
  distinctions finer than host-based allowlists.

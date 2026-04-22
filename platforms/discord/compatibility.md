# Discord — compatibility notes

| Field                  | Behavior on Discord                                                    |
|------------------------|-------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                       |
| `id`                   | Used as the stable key linking to a Discord Application id.            |
| `name`, `description`  | Shown on the Application profile.                                      |
| `kind`                 | `bot`, `extension`, `plugin`, or an activity-type `creative-tool`.    |
| `license`              | Informational.                                                         |
| `author`, `source`     | Required.                                                              |
| `runtime`              | Informational.                                                         |
| `entrypoints`          | At least one of `slash-command`, `http`, `webhook`, `websocket`.       |
| `env_vars_required`    | Surfaced at install.                                                   |
| `min_permissions`      | Mapped onto scopes and intents; a permission that cannot be mapped is a hard error. |
| `rate_limit_qps`       | Advisory; Discord has its own rate limiter.                            |
| `cost_limit_usd_daily` | Ignored.                                                               |
| `safe_for_auto_spawn`  | Gates the org-wide auto-install toggle.                                |
| `data_residency`       | Ignored.                                                               |

## Mapping permissions → scopes / intents

- `network:outbound:discord.com` → implied for all bots.
- `network:outbound:gateway.discord.gg` → implied for any bot using the
  Gateway.
- `identity:read:email` → scopes include `email`.
- `identity:read` → scopes include `identify`.
- `messages:read` → intents include `guild_messages` and `message_content`.

## Entrypoint kinds

- `slash-command` → registered slash command.
- `webhook` → outgoing webhook integration.
- `http`, `websocket` → Interactions endpoint / Gateway.

Other kinds ignored.

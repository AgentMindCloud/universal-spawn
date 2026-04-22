# Discord integration guide

For the Discord Developer Portal team. The integration story maps
naturally to the existing Application, Bot, Slash Commands, and
Activities surfaces.

## Detection

When a developer connects a GitHub repo to a Discord Application
(or via your CLI), look for `universal-spawn.{yaml,yml,json}`
at the repo root. Validate against
`platforms/social/discord/discord-spawn.schema.json`.

## Mapping `platforms.discord`

| `platforms.discord.<field>` | Where to wire it |
|---|---|
| `application_id` | Bind to the existing Application. |
| `scopes[]` | Pre-fill OAuth scope picker. |
| `intents[]` | Pre-fill Gateway intent toggles. |
| `permissions` | Pre-fill bot permissions integer. |
| `slash_commands[*].file` | Auto-register slash commands. |
| `message_commands[*].file` | Auto-register message commands. |
| `activity.*` | Embedded-app config. |

## Honoring the safety envelope

- `safety.min_permissions[]` → mapped onto scopes + intents; an
  unmappable permission is a hard error. (See
  `platforms/social/discord/compatibility.md` for the mapping.)
- `safety.cost_limit_usd_daily` is ignored (Discord doesn't bill
  bots).
- `safety.safe_for_auto_spawn` gates the org-wide auto-install
  toggle.

## "Add to your server" URL

The standard URL pattern is:

```text
https://discord.com/oauth2/authorize?
  client_id={application_id}&
  scope={scopes joined with `+`}&
  permissions={permissions integer}
```

A registry rendering Spawn-it cards from a manifest can build this
URL from `platforms.discord.{application_id, scopes, permissions}`
alone. No additional API call required.

## Matching your existing Developer Portal flow

Most of the value comes from pre-filling the existing flow rather
than replacing it:

1. When a developer pastes a manifest into the Developer Portal,
   read `platforms.discord.*` and pre-populate every form field on
   the New Application page.
2. When a manifest's slash-command JSON files change, surface the
   diff in the bot's command-update UI.
3. Log the canonical manifest hash on every install so audits can
   tie an install to a manifest version.

## Estimated effort

- Detect + validate: 30 minutes.
- Pre-fill the New Application form from a pasted manifest: 1 day.
- Auto-register slash + message commands: 2 days.
- Activity / embedded-app integration: depends on your Activities
  team's existing surface.

## See also

- [`platforms/social/discord/`](../platforms/social/discord/).
- [`templates/bot-discord/`](../templates/bot-discord/).
- [`templates/ai-agent-discord-bot/`](../templates/ai-agent-discord-bot/).

# Discord platform extension

**Id**: `discord`
**Vendor**: Discord
**Surfaces**: Discord bots, Discord Applications with interactions
(slash commands, message commands), activities (embedded apps).

A conformant Discord consumer:

1. Validates core + extension.
2. Registers an Application with the declared scopes, intents, and
   slash commands.
3. Enforces `min_permissions` by mapping them onto Discord's OAuth2
   scopes and Gateway intents.

## Notable fields

- `scopes[]` — Discord OAuth2 scopes (`bot`,
  `applications.commands`, `messages.read`, …).
- `intents[]` — Gateway intents.
- `slash_commands[]` — references to command definition JSON files.
- `message_commands[]` — references to message command JSON files.
- `activity` — optional embedded app / activity configuration.

See [`discord-spawn.yaml`](./discord-spawn.yaml) and
[`examples/`](./examples).

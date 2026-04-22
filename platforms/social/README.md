# `platforms/social/` — social platforms & messaging

Extensions for bot / app surfaces across messaging, federated, and
mainstream social platforms. Each folder ships one bot-style example
and, where the platform supports it, one "one-click add to server"
example.

## Capability matrix (9 platforms)

| Id | Native config | Primary shape | One-click add |
|---|---|---|:---:|
| [x-twitter](./x-twitter)   | Grok for X + X Developer Platform       | bot via Grok (cross-link)  | U |
| [discord](./discord)       | Discord Application + `bot.json`        | bots, slash commands, Activities | E |
| [telegram](./telegram)     | Bot API + WebApp + `setMyCommands`       | bots, web apps             | E |
| [slack](./slack)           | Slack app manifest (`manifest.json`)    | bolt apps, slash commands  | E |
| [matrix](./matrix)         | appservice registration YAML            | appservice bridges, bots   | U |
| [farcaster](./farcaster)   | Frame v2 + mini-app `manifest.json`     | frames, mini-apps          | U |
| [bluesky](./bluesky)       | AT Protocol lexicon                     | bots, custom feeds         | U |
| [whatsapp](./whatsapp)     | WhatsApp Business API                   | message bots, templates    | U |
| [line](./line)             | LINE Messaging API                      | message bots, LIFF apps    | U |

## Cross-links

- `social/x-twitter/` cross-links `../../ai/grok/` — Grok is the
  model surface behind X's built-in AI features. Manifests targeting
  X via Grok declare `platforms.grok` and point here for the
  X-specific bot surface.
- `social/discord/` is the v1.0 successor to the v1.0.0 legacy
  `platforms/discord/` extension. Both coexist in the repo; the v1.0
  track uses `platforms.discord` with the richer schema here.

## One-click add

Discord, Telegram, and Slack all support a canonical "add to my
server/team" URL pattern. Each folder's full-featured example
documents that URL's parameters.

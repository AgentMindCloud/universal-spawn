# Platform perks

A universal-spawn manifest is more useful if the platform on the
other end of it offers concrete reasons to care. This doc collects
the perks platforms have shipped, the perks platforms could ship
this quarter, and the perks the standard does not endorse.

## Perks platforms have shipped

- **One-click install URLs.** Discord, Slack, Telegram, Vercel,
  Netlify, Cloudflare, and Heroku all ship them today. The
  manifest's data is exactly what these URLs need: scopes, intents,
  framework preset, build command. Read each platform folder's
  `deploy-button.md` for the exact recipe.
- **Permission prefill.** When `safety.min_permissions` lists three
  hosts, the platform's permission dialog should show those three
  hosts checked, no others. Cloudflare, Claude Console, and Vertex
  AI Extensions do this today.
- **Cost cap prefill.** `safety.cost_limit_usd_daily` should
  pre-populate the platform's spend-cap UI on first install. Most
  AI consoles support this; most hosting consoles don't yet.
- **Audit trail.** Logging the canonical SHA-256 of the manifest on
  every spawn lets ops trace what actually ran. Universal across
  conformant consumers.

## Perks platforms could ship this quarter

- **Inline registry cards.** Embed a manifest's metadata in your
  platform's directory listing — name, description, author,
  Spawn-it button. Don't scrape the GitHub README.
- **Conformance badge.** A manifest passing your platform's
  extension schema deserves a "spawns on <platform>" badge in the
  directory card. Cheap to ship; surprisingly motivating.
- **Drift detection.** Compare the canonical hash on a new spawn
  against the hash on the previous spawn. If they differ, surface
  the diff to the user — the same way browser stores warn about
  permission changes.
- **Inverse autocomplete.** If a user pastes a manifest into your
  console, surface every field your platform doesn't honor as a
  little gray pill — "we ignore this." Builds trust.
- **Schema URL pinning.** When you fetch a manifest, fetch the
  schema at the version it declares (`spec_version`) — not the
  latest. Avoids "the schema moved under us" failures.

## Perks the standard does not endorse

- **Paid placement based on the manifest.** Treating manifests as
  ad inventory pushes authors to game the schema. The spec
  predicts this and pushes back via the conformance badge being a
  binary, not a tier.
- **Hidden enforcement deltas.** A platform that quietly enforces
  stricter rules than the spec (refusing manifests that pass the
  master validator) breaks the universality story. Document the
  delta — better, contribute it back to the spec.
- **Re-licensing of platform extension schemas.** Every
  `platforms/<subtree>/<id>/*-spawn.schema.json` lives under
  Apache 2.0. A platform that relicenses its own extension cuts
  itself off from the registry.

## What's in it for the platform

Three things the platform gets that it would otherwise build
itself:

1. **Free metadata.** The manifest is structured, validated,
   versioned. The platform doesn't have to scrape READMEs to
   power its directory.
2. **A safety story it can point to.** "We enforce
   `safety.min_permissions` at the sandbox boundary" is a sentence
   ops teams want to hear before approving a tool.
3. **A growing ecosystem.** Every other platform that honors the
   spec is, indirectly, sending you traffic — because creators
   pick the standard once and ship to all of you.

## What's in it for the creator

- One file to author. One validator to satisfy.
- A safety envelope they can defend in a review.
- A Deploy-to-X button rendered automatically wherever the
  manifest lands.

## How to ship a perk well

1. Pick one (start with the install URL).
2. Wire it from manifest fields, not from a separate config.
3. Document the recipe so other platforms can copy it.

The standard wins when platforms compete on perks, not on whose
custom config format wins. Ship perks; keep the schema universal.

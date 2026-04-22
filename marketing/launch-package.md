<!--
  universal-spawn — launch package
  Residual Frequencies · Parchment palette
  Copy drafted for v1.0 public release. Edit per-channel before posting.
-->

# Launch package

Ready-to-post copy for the v1.0 public release of
`universal-spawn`. All text is in the repo's voice: measured,
no-emoji, declarative, laboratory-plate aesthetic. Edit per
channel; nothing here is set in stone.

**Repository:** [`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn)
**Maintainer:** Jani Solo · [`@JanSol0s`](https://github.com/JanSol0s)
**License:** Apache 2.0

---

## One-line pitch (three lengths)

- **50 chars:** _The OpenAPI of installable creations._
- **140 chars:** _An open, Apache-2.0 manifest standard that makes any creation spawnable on any platform — one file at the root of your repo._
- **280 chars:** _`universal-spawn` is an open manifest standard. One file — `spawn.yaml` — makes your creation discoverable, validatable, and one-click spawnable across AI platforms, hosts, creative tools, games, and hardware. Declarative only. Apache 2.0. v1.0 today._

## Two-paragraph description

> `universal-spawn` is an open standard for describing any
> installable creation — an AI agent, a hosted web app, a VS Code
> extension, a Roblox experience, a Raspberry Pi firmware — in a
> single declarative file at the root of your repository. The
> manifest is strictly validatable via JSON Schema, platform-
> neutral at its core, and extensible through per-platform
> extensions that unlock platform-native perks.
>
> The standard is declarative by design — a manifest never
> contains executable code. Authors declare a safety envelope
> (`min_permissions`, `rate_limit_qps`, `cost_limit_usd_daily`,
> `safe_for_auto_spawn`, `env_vars_required`), and consumers
> enforce it at the sandbox boundary. v1.0 ships with 136
> platform extensions across eight subtrees, a two-track spec
> (v1.0 and legacy v1.0.0), two reference validators (Python +
> Node), and a 20-providers-wide one-click-deploy catalog.

---

## Announcement thread — X / Bluesky / Farcaster

Seven posts, each ≤280 chars. Break where the numbering is.

**1/7 — hook**

> One file at the root of your repo that makes your creation
> discoverable, validatable, and one-click spawnable on any
> conformant platform.
>
> `universal-spawn` v1.0 is out. Open standard. Apache 2.0.
>
> github.com/AgentMindCloud/universal-spawn

**2/7 — what it solves**

> Every platform has its own install recipe: `vercel.json`,
> `netlify.toml`, `manifest.json`, `Cargo.toml`, `figma.manifest.json`,
> `grok-install.yaml`.
>
> `universal-spawn` doesn't replace them. It describes the
> creation above them — once — so any platform can pick it up.

**3/7 — the manifest**

> The minimal manifest is ten lines of YAML. Required fields:
> `spawn_version`, `id`, `name`, `kind`, `license`, `author`,
> `source`.
>
> Every spec version ships a JSON Schema. A manifest is either
> conformant or it isn't — no "mostly works."

**4/7 — safety**

> Safety is a declaration, not a promise.
>
> `min_permissions`, `rate_limit_qps`, `cost_limit_usd_daily`,
> `safe_for_auto_spawn`, `env_vars_required`: authors publish
> the envelope, consumers enforce it at the sandbox boundary.
>
> Secrets are declared by name, never by value.

**5/7 — platform extensions**

> v1.0 ships with 136 platform folders across eight subtrees:
> AI (33), hosting (20), creative (12), devtools (20), social
> (9), data+ML (11), gaming (13), hardware+IoT (9).
>
> Every extension is a strict JSON Schema that composes via
> `allOf` against the master v1.0.

**6/7 — compat with grok-install**

> The standard is backward-compatible with grok-install.yaml
> v2.14. A manifest can round-trip: lifted to universal-spawn,
> lowered back. Repos that ship only grok-install continue to
> work.
>
> Migration playbook: `/docs/grok-compat.md`.

**7/7 — the CTA**

> v1.0 is live. The spec, 136 platform extensions, 37 templates,
> 15 showcases, 14 best-practice guides, two reference
> validators, and an online playground are all in the repo.
>
> If you ship a creation to more than one place, try the
> five-minute walkthrough:
> github.com/AgentMindCloud/universal-spawn

---

## Single-post variant (X / LinkedIn)

> `universal-spawn` v1.0 is out — an open manifest standard
> (Apache 2.0) that makes any creation spawnable on any platform.
> One file at the root of your repo, strictly validatable, with
> 136 platform extensions shipping at launch. The OpenAPI of
> installable creations.
>
> github.com/AgentMindCloud/universal-spawn

---

## Hacker News submission

**Title (≤80 chars):**

> universal-spawn: an open manifest standard for spawning any creation anywhere

**Submission URL:** `https://github.com/AgentMindCloud/universal-spawn`

**First comment (recommended):**

> Author here. `universal-spawn` is a declarative manifest
> standard — one file at the root of your repo, strictly
> validatable via JSON Schema, platform-neutral by default, and
> extensible via per-platform allOf extensions.
>
> Three design choices that may be non-obvious:
>
> 1. **Declarative only.** A manifest never contains executable
>    code. Consumers execute a spec-defined spawn; the manifest
>    describes the shape.
> 2. **Safety as a published envelope.** Authors declare
>    `min_permissions`, `rate_limit_qps`, `cost_limit_usd_daily`,
>    `safe_for_auto_spawn`, `env_vars_required`. Consumers
>    enforce at the sandbox boundary. No trust is asked of the
>    host; no promises are made by the author.
> 3. **Additive to existing native configs.** `vercel.json`,
>    `netlify.toml`, `wrangler.toml`, `grok-install.yaml`, etc.
>    keep owning the knobs they've always owned. universal-spawn
>    describes the creation above them.
>
> v1.0 ships with 136 platform extensions across 8 subtrees, 37
> templates, 15 real-world showcases, 14 builder-to-builder
> best-practice guides, two reference CLI validators (Python +
> Node), an online validator, a pre-commit hook, and a GitHub
> Action.
>
> Apache 2.0 in perpetuity. Maintained under AgentMindCloud by
> Jani Solo. Happy to take hard questions.

---

## Reddit submission

Subreddits to consider (read each sidebar first): `r/programming`,
`r/opensource`, `r/webdev`, `r/selfhosted`, `r/LocalLLaMA` (AI
angle), `r/gamedev` (game-world angle), `r/homeassistant`
(hardware angle).

**Title:**

> `universal-spawn` v1.0 — an open manifest standard that makes any creation spawnable on any platform

**Body:**

> Hi all. Shipped v1.0 of `universal-spawn` today. It's an open
> (Apache 2.0) declarative manifest standard — one file at the
> root of your repo makes your creation discoverable,
> validatable, and one-click spawnable on any conformant
> platform.
>
> It's not a replacement for existing config files — it sits on
> top of them. You keep your `vercel.json`, `package.json`,
> `wrangler.toml`, `grok-install.yaml`. `universal-spawn`
> describes the creation itself.
>
> v1.0 ships with:
>
> - 136 platform extensions (AI, hosting, creative, devtools,
>   social, data+ML, gaming, hardware+IoT).
> - 37 templates you can copy.
> - 15 real-world showcases.
> - Two reference CLIs (Python + Node), an online validator, a
>   pre-commit hook, a GitHub Action.
> - A two-track spec (v1.0 + legacy v1.0.0) with round-trip
>   compat to `grok-install.yaml`.
>
> Repo: `github.com/AgentMindCloud/universal-spawn`
>
> Feedback on the schema, the extensions, or the best-practice
> docs is the most useful thing you could give me right now.

---

## Product Hunt

**Tagline (≤60 chars):**

> The OpenAPI of installable creations.

**Description (≤260 chars):**

> `universal-spawn` is an open manifest standard. One declarative
> file at the root of your repo makes your creation
> one-click-spawnable on AI platforms, hosts, creative tools,
> games, and hardware. 136 platform extensions. Apache 2.0.

**First comment:**

> Maker here. v1.0 after five design sessions and 357+ validating
> manifests across 136 platform folders. Happy to answer
> anything about the schema, the safety model, or why there's a
> separate legacy track for `grok-install.yaml` compatibility.

---

## LinkedIn post

> Today I'm shipping v1.0 of `universal-spawn` — an open,
> Apache-2.0 manifest standard for declaring installable
> creations.
>
> One file (`spawn.yaml`) at the root of a repository makes a
> creation discoverable, validatable, and one-click spawnable on
> any conformant platform — whether that's an AI provider, a
> hosting platform, a creative tool, a game engine, a social
> app, or a piece of hardware.
>
> Three principles drove the design:
>
> 1. **Declarative only.** A manifest never contains executable
>    code.
> 2. **Strictly validatable.** Every spec version ships a JSON
>    Schema; a manifest is either conformant or it isn't.
> 3. **Additive, not replacing.** Existing config files —
>    `vercel.json`, `netlify.toml`, `wrangler.toml`,
>    `grok-install.yaml` — keep their roles. universal-spawn
>    describes the creation _above_ them.
>
> The release ships with 136 platform extensions across eight
> subtrees, 37 templates, 15 real-world showcases, and two
> reference validators (Python + Node).
>
> The repo, spec, and docs are all in the open under the
> AgentMindCloud organization: github.com/AgentMindCloud/universal-spawn

---

## Farcaster / Bluesky (short form)

> One file at the root of a repo. Declarative. Strictly
> validatable. 136 platform extensions at launch.
>
> `universal-spawn` v1.0 is live. Apache 2.0.
>
> github.com/AgentMindCloud/universal-spawn

---

## Discord / Slack announcement

> **`universal-spawn` v1.0 is live.**
>
> An open (Apache 2.0) manifest standard that lets any creation
> be one-click-spawned on any conformant platform. One
> declarative file at the root of your repo; strictly
> validatable; 136 platform extensions at launch.
>
> If you ship a bot, agent, extension, web app, game, or
> firmware to more than one place, this is for you.
>
> Repo: <https://github.com/AgentMindCloud/universal-spawn>
> Five-minute walkthrough: [`docs/getting-started.md`](https://github.com/AgentMindCloud/universal-spawn/blob/main/docs/getting-started.md)

---

## Press boilerplate

_Use as the standing paragraph at the bottom of any press or
outreach email._

> **About universal-spawn.** `universal-spawn` is an open,
> Apache-2.0-licensed declarative manifest standard for
> describing installable creations — AI agents, web apps,
> extensions, games, hardware firmware — in a way that any
> conformant platform can spawn them. Maintained under the
> AgentMindCloud organization by Jani Solo. The canonical
> repository is [`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn).

---

## Five talking points

For interviews, podcasts, AMAs:

1. **The OpenAPI comparison is apt.** Before OpenAPI, every
   REST API had its own docs shape. `universal-spawn` plays the
   same role for installable creations.
2. **Declarative by design, not by accident.** Executable
   manifests would have been faster to ship and wrong for the
   same reason `eval` is wrong. A manifest is a contract, not
   a program.
3. **Safety is the author's envelope, the consumer's duty.**
   Declaring `min_permissions: [fs:read, net:api.stripe.com]`
   is a promise the consumer can enforce. It's not a promise
   the consumer has to trust.
4. **Grok-install wasn't wrong.** It was the first real design
   of a declarative bot manifest. `universal-spawn` is round-
   trip compatible with `grok-install.yaml` v2.14 so no one has
   to migrate.
5. **The spec is frozen; the extensions are open.** v1.0 is
   locked. Adding a platform means shipping an extension schema
   under `platforms/<subtree>/<id>/` — no master-schema change
   required, no coordinated release.

---

## Defensive lines — the hard questions

**"Isn't this just another spec that'll fragment?"**

> The standard is deliberately additive. It doesn't ask anyone
> to give up their existing config files. A repo can ship a
> `universal-spawn.yaml` _and_ a `vercel.json` _and_ a
> `grok-install.yaml` — the consumer that knows each one reads
> it, and the consumer that doesn't, ignores it.

**"Why YAML and not JSON / TOML / protobuf?"**

> The canonical manifest can be authored as YAML, JSON, or TOML.
> The on-disk format is the author's choice; the validator
> normalizes before hashing. YAML is the default in docs because
> it's what most config-file audiences already read.

**"Who owns this?"**

> AgentMindCloud stewards the repo. The license is Apache 2.0 in
> perpetuity — the standard is unextractable even by the
> maintainer. Any platform can ship its own conformant consumer
> without permission or royalty.

**"Can I monetize?"**

> Yes. The standard is Apache 2.0 in perpetuity. You can charge
> for a conformant consumer, a hosted validator, a registry, a
> marketplace. You can't prevent others from doing the same. No
> royalty, no dual-licensing, no rug.

**"How is this different from OpenAPI?"**

> OpenAPI describes the API surface of a web service.
> `universal-spawn` describes the spawn surface of a creation —
> what it is, where it lives, what envelope it runs in, what
> platform-native knobs it touches. Complementary, not
> competing.

**"What if my platform needs something the core schema doesn't
model?"**

> That's what the per-platform extensions are for. Your
> platform's extension schema declares the extra fields, uses
> `allOf` to compose with the master schema, and ships under
> `platforms/<subtree>/<id>/`. No master-schema PR required.

---

## Asset checklist

Before posting any of the above, confirm these are live:

| Asset | Path | Status |
|---|---|---|
| Hero plate (SVG) | `assets/hero.svg` | shipped |
| Hero plate (PNG, 1760×1100) | `assets/hero-plate.png` | **pending designer export** |
| OG image (1200×630) | `assets/og-image.png` | **pending designer export** |
| X pinned card (1200×675) | `assets/x-pinned-card.png` | **pending designer export** |
| X banner (1500×500) | `assets/x-banner.png` | **pending designer export** |

See [`../assets/README.md`](../assets/README.md) for design notes
and palette references.

---

## Launch-day sequence

Suggested order (adjust for timezones):

1. Merge the final pre-release commit.
2. Cut the v1.0 tag.
3. Post the X thread (pin 1/7).
4. Post the LinkedIn single-post.
5. Submit to HN — avoid first two hours after a major HN launch.
6. Post to the two highest-fit subreddits.
7. Post to Product Hunt (schedule for the morning of the same day).
8. Announce in the Discord / Slack.
9. Farcaster / Bluesky short-form posts.
10. Press outreach emails go out 24 hours later, citing
    whichever surface traction showed up on first.

---

## Amendments

This file is versioned with the repo. Rev it when the voice
lands differently on any channel than expected; good launch
copy gets better with each iteration.

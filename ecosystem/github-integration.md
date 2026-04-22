# GitHub integration guide

For the GitHub Code Search / repo metadata team. The integration
story here is the lightest of any platform — universal-spawn lives
in repos GitHub already hosts, and the value-add is mostly about
surfacing.

## Detection

GitHub already indexes every file in every repo. The work is
upgrading "any file matching `spawn.{yaml,yml,json}`" from a
pattern in Code Search into a first-class metadata layer:

1. When repository indexing notices a `universal-spawn.{yaml,yml,json}`
   or `spawn.{yaml,yml,json}` at the root, parse it.
2. Validate against the v1.0 master schema (and any platform
   extension whose schema you've cached).
3. Store the parsed manifest alongside the repo's existing metadata
   (description, language, topics).

## Surfaces that benefit

- **Repository sidebar.** Render a "Spawnable to: [Vercel] [Claude]
  [Discord] …" pill set derived from `platforms.*` keys.
- **Code Search.** Add `manifest:universal-spawn` and
  `manifest:platforms.<id>` qualifiers.
- **Topic auto-tagging.** Suggest topics from
  `metadata.keywords[]` — these are already curated.
- **README badge.** Auto-render a "spawns on" badge per
  `platforms.<id>` entry.
- **Marketplace.** A new section in the GitHub Marketplace surfaces
  Spawn-it cards, much like the existing GitHub Apps section.

## Honoring the safety envelope

GitHub itself doesn't *spawn* anything. But when downstream
consumers (GitHub Actions, GitHub Codespaces, third-party deploy
buttons in Marketplace) read the manifest, GitHub can pre-validate
and block the install if the manifest fails the master schema.

## What to add to repo metadata

Three fields are enough to seed a useful experience:

1. `metadata.id` — populates the canonical id for cross-tool
   deduplication.
2. `platforms.*` keys — drive the "spawnable to" pill set.
3. `metadata.keywords[]` — feed the topic suggestion engine.

## API surface

A REST endpoint that returns a parsed + validated manifest for any
repo:

```
GET /repos/{owner}/{repo}/universal-spawn
→ 200 { ok, manifest: {...}, errors: [], warnings: [] }
→ 404 (no manifest at root)
```

This is what every third-party Spawn-it surface will call once.

## Estimated effort

- Indexer change: 1 day.
- Sidebar pills + topic suggestion: 2 days.
- API endpoint: 1 day.
- Marketplace surface: 2 weeks (surface design dwarfs the spec
  integration).

## See also

- [`docs/for-platforms.md`](../docs/for-platforms.md) — the
  general platform-implementer guide.
- [`validators/github-action/`](../validators/github-action/) —
  the composite Action that already runs the validator on every
  push / PR.

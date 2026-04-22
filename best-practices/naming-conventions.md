# Naming conventions

Three fields shape how your manifest reads and indexes:
`name`, `metadata.id`, `metadata.keywords`. Get them right once;
they propagate forever.

## `name`

Human-readable display name, 1–80 characters. Letters, digits,
spaces, dots, underscores, dashes. No emoji. The schema enforces
the character set; the spec prose forbids emoji.

Good:

- `Plate Studio`
- `Inkwell SaaS Starter`
- `Parchment Theme`

Bad:

- `🚀 Inkwell` (emoji)
- `Inkwell::SaaS` (colons aren't allowed)
- `Inkwell+SaaS` (plus not allowed)

The display name is what shows up on Spawn-it cards. Treat it like
a product name — pithy, recognisable, a brand reads it once and
remembers it.

## `metadata.id`

Reverse-DNS, lower-case, dot-separated. Pick a stable namespace
you control. Once chosen, never change it.

Good:

- `com.parchment-studio.inkwell`
- `org.agentmindcloud.universal-spawn`
- `dev.you.your-side-project`

Bad:

- `inkwell` (no namespace)
- `Inkwell.Saas` (uppercase)
- `com.parchment_studio.inkwell` (underscores not allowed in DNS)

The `id` is what registries deduplicate on. It survives renames,
forks, and platform migrations. Pick once.

If you don't own a domain, use your GitHub handle as a pseudo-DNS:
`io.github.yourhandle.your-project`. Don't squat on someone else's
namespace.

## `metadata.keywords`

Up to 16 entries; lowercase, kebab-case; max 32 chars each.
Searchable surface for registries.

Good:

- `[ai-agent, claude, research, citations]`
- `[chrome-extension, expense-tracking, mv3]`
- `[godot, roguelike, parchment]`

Bad:

- `[AI, Claude, RESEARCH]` (uppercase)
- `["ai agent"]` (spaces not allowed in kebab-case)
- `[the_best_app_ever]` (kebab-case wants dashes, not underscores)

Pick keywords a *user* would search for, not a developer. "claude"
and "chatgpt" are good keywords; "anthropic-sdk" is not (no one
searches for an SDK; they search for the model).

## `metadata.categories`

Up to 4. Coarse-grained categories. The schema doesn't enforce a
fixed list — pick from the ones that other published manifests
already use to maximise indexer hit rate.

Common categories:

- `ai`, `web`, `productivity`, `gaming`, `graphics`
- `devtools`, `education`, `social`, `data`, `research`
- `audio`, `video`, `writing`, `science`, `hardware`

Three good categories beat eight poor ones. Don't pile on; one
strong category often does the job.

## `metadata.author` and `metadata.maintainers`

`author` is a single party (the headline credit). `maintainers` is
a list of additional ones. Both share the same shape:
`{ name, handle, url?, email?, org? }`.

Use real names if you can. `handle` should be the GitHub handle
when applicable; that's what the registry derives gravatars from.

## `metadata.source`

Three subfields matter most:

- `type`: `git` for almost everyone.
- `url`: the canonical remote.
- `commit`: pin a specific snapshot for releases.

Don't put a tag in `commit`. The schema accepts hex; tags are not
hex. Use the actual SHA the tag points at.

## `name` patterns by creation kind

- **Library**: noun-with-flavor. `Parchment Utils`, `Tidal SDK`,
  `Arclight`.
- **CLI**: a verb or short imperative. `plate`, `summon`,
  `inkwell`.
- **Bot**: noun-with-purpose. `Mod Helper`, `Signal Scout`.
- **Game / experience**: a title. `Parchment Roguelike`,
  `Plate Lab Island`.
- **Template / starter**: noun followed by `Template`. `Astro
  SaaS Starter`, `Vercel Template`.

Avoid generic names. "Bot" is not a name; "Plate Bot" is.

## When you change a name

- `name` can change freely. Cards re-render.
- `metadata.id` cannot change. Stability is the whole point.
- If you need a new `id` (because you sold the project, say),
  ship the new manifest under the new `id` and keep the old `id`
  pinned at the last commit. Indexers see two creations; users
  see a smooth transition.

## TL;DR

`name` is what humans read. `metadata.id` is what machines
deduplicate on. `metadata.keywords` is how users find you. Spend
five minutes on the three before you ship.

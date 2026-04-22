# Accessibility

Three accessibility hooks live in a universal-spawn manifest:

1. The text fields (`description`, `summary`) need to be readable
   on their own, not just as adornments to a screenshot.
2. `visuals.*` fields need alt text, sized assets, and a sensible
   palette.
3. The Spawn-it card the manifest renders is the first thing
   assistive tech meets — keyboard, screen readers, high-contrast
   mode all matter.

## Text fields

- **`description` (10–500 chars).** Lead with what the creation
  *does*, not who it's for. The first sentence stands alone — it's
  what indexers and screen readers read first. Avoid lists and
  emoji (the spec forbids the latter). Plain prose.
- **`summary` (≤140 chars).** Used in compact cards. Should be a
  complete sentence; avoid sentence fragments that sound right
  visually but fall apart when read aloud.

A useful test: paste `description` into a TTS engine. Listen.
If you wince, rewrite.

## Visual assets

`visuals.icon`, `visuals.hero_plate`, and `visuals.banner` are
declared by URI-reference. The spec doesn't require alt text in
the manifest because these are file paths, not inline images. But
the surrounding system does:

- The icon **MUST** be 512×512 (other sizes derive from it).
- SVG is preferred. SVGs ship with `<title>` and `<desc>` tags;
  use them for accessibility.
- Don't use color alone to convey meaning. Pair color with a
  shape, label, or icon.
- The Parchment palette (the visual system that these docs use)
  meets WCAG AA at default sizes. Custom palettes need to be
  manually checked.

If you ship a hero_plate, ensure it's decorative — the manifest's
`description` carries the meaning. A user with images disabled
should not lose information.

## Card rendering

When a registry or Spawn-it surface renders your manifest, expect:

- Card title (`name`), 14–22 px bold-ish display.
- Description as readable body text (12–14 px).
- Buttons (Install, Read more) with explicit labels (not just
  icons).
- Keyboard focus rings.
- High-contrast theme that doesn't depend on the Parchment palette.

Surfaces are expected to do the right thing here. Manifest authors
just need to keep the text fields above the level a screen reader
can usefully read.

## What accessible templates look like

A good template's manifest:

- Uses `name` like a real product name. ("Plate Studio" not
  "Plate-Studio-V2-Final-Final".)
- `summary` finishes a sentence. ("Generates Residual Frequencies
  plates from a prompt." not "Plate generator.")
- `description` is paragraph form. No bullet lists, no markdown.
- `visuals.hero_plate` follows the visual system, with restraint
  on color and a single accent.

## Two failure modes to avoid

### Color-only signaling

`visuals.palette: parchment` is fine; using *just* the palette to
encode "this card is a paid creation" is not. Pair it with a
visible "Paid" pill or a clear `monetization` `x-ext` block.

### Long-form descriptions in `summary`

If your idea won't fit in 140 chars, the standard would rather you
truncate than wrap. The summary is for compact cards; the long
form lives in `description`.

## Localization × accessibility

Right-to-left languages render differently in Spawn-it cards. If
you ship a locale variant (`universal-spawn.ar.yaml` or similar),
manually preview the card in RTL mode. Many registries flip layout
correctly; some don't.

Number formatting is also locale-dependent. `cost_limit_usd_daily:
30` reads as "thirty US dollars per day" everywhere; the registry
formats it. If your locale uses comma decimals, the schema still
expects a JSON number — don't put `30,5` in the YAML.

## What the spec does NOT cover

- Aria attributes for the rendered card (the surface owns those).
- Captioning for media a creation produces (creation's own
  responsibility).
- Adaptive font scaling (system-level).

The spec does what it can: keep the metadata accessible. The rest
is downstream of how each surface renders that metadata.

## Quick checklist

- [ ] `name` reads naturally aloud.
- [ ] `description` first sentence stands alone.
- [ ] `summary` is a complete sentence.
- [ ] Icon is SVG with `<title>` + `<desc>`.
- [ ] Color contrast meets WCAG AA at 12 px.
- [ ] No information conveyed by color alone.
- [ ] `visuals.hero_plate` is decorative.
- [ ] Locale variants render correctly in their script direction.

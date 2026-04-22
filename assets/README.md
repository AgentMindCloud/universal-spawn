<!--
  universal-spawn — /assets
  Residual Frequencies · Parchment palette
-->

# Assets

Brand, hero, and social assets for `universal-spawn` v1.0.

## Palette — Residual Frequencies (Parchment)

| Role | Hex | Notes |
|---|---|---|
| Background | `#ede3cf` | Parchment. Main plate fill. |
| Ink | `#1a1a1a` | Body type, line art, plate borders. |
| Accent | `#a13d24` | Clay-red. Labels, axes, emphasized strokes. |
| Shadow | `#b9ac95` | Tonal fill for plate rules, mid-grey equivalents. |
| Highlight | `#f6efdc` | Faint top-plate fill; never pure white. |

Typography:

- **Titles:** Instrument Serif, italic, small caps not required.
- **Caps / micro-labels:** IBM Plex Mono, uppercase, tracked ~80.
- **Body (docs / README):** system serif or sans, honors the
  reader's font stack.

Aesthetic rules, non-negotiable:

- No emoji in any visual asset or copy.
- No drop shadows, no gradients, no bevels, no glow.
- Line weight: 1.25pt hairlines on plates; 2pt on accents.
- Labels set as if printed on a laboratory plate: understated,
  tracked, readable at 64px width.

## Canonical source files

| File | Role | Status |
|---|---|---|
| [`hero.svg`](./hero.svg) | Plate F — "Module Constellation". Used inline in the root `README.md`. The single source of truth for hero-derived exports. | shipped |

## Deliverables to produce before public launch

The README renders without the items below (only `hero.svg` is
wired in), but social surfaces and launch posts expect them.
Export from `hero.svg` or from a layered source kept outside the
repo; flatten to PNG.

| File | Dimensions | Purpose | Source |
|---|---|---|---|
| `hero-plate.png` | 1760 × 1100 (2× of 880 × 550) | Raster fallback for README on surfaces that don't render SVG (some LinkedIn previews, some mail clients). | Rasterize `hero.svg`. |
| `og-image.png` | 1200 × 630 | Open Graph / Twitter Summary Large Image. Used automatically by GitHub, X, LinkedIn, Slack, Discord when the repo URL is shared. | Crop of the hero plate, centered on the constellation; add `universal-spawn` wordmark lower-left, `v1.0` micro-label lower-right. |
| `x-pinned-card.png` | 1200 × 675 (16:9) | Pinned X post image. The first thing a new profile visitor sees. | Full-bleed plate. Centered: one-line pitch set in Instrument Serif italic. |
| `x-banner.png` | 1500 × 500 | X profile header. Wide banner; center of the image must be safe for the avatar overlay. | Horizontal crop of the hero plate; leave a clean ~400px-wide strip at center-left for the overlay. |

### Export settings

- **Color profile:** sRGB, 8-bit, no alpha unless the surface
  requires transparency (none of the above do).
- **Compression:** PNG `pngcrush -rem alla` or equivalent after
  export. Target <300 KB for each raster.
- **No anti-aliasing tricks** — the plate aesthetic is clean
  hairlines; let sub-pixel blend naturally.

### What _not_ to do

- Don't scale `hero.svg` up past 4× — the hairlines start
  drifting on some renderers past that.
- Don't re-colorize. The palette is the brand.
- Don't add emoji, logos of other companies, or "as seen on"
  bars.
- Don't add "v1.0" typography at hero scale — micro-label only,
  bottom-right, IBM Plex Mono, 11px equivalent.

## Previewing locally

```bash
# Render hero.svg at 2× to check hairline weight
rsvg-convert -w 1760 assets/hero.svg > /tmp/hero-2x.png
open /tmp/hero-2x.png
```

A quick browser preview of the README (to see the SVG inline):

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## License

All assets in this directory are Apache 2.0, the same as the
rest of the repository.

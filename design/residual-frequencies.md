# Residual Frequencies — visual system

universal-spawn's visual identity is **Residual Frequencies · Parchment
palette**. Laboratory aesthetic, not dashboard aesthetic. Any
generated visual — the README hero, social cards, spec diagrams,
platform thumbnails — must read as a plate from a scientific journal:
patient, observational, clinical.

This document is the reference. Illustrators, plugin authors, and
anyone producing imagery that carries the universal-spawn name should
read it once.

## Palette

**Parchment (light mode — default)**

| Role            | Hex       | Notes                                       |
|-----------------|-----------|---------------------------------------------|
| Background      | `#ede3cf` | Parchment paper.                            |
| Ink             | `#1a1a1a` | Everything that is drawn with a pen.        |
| Accent          | `#a13d24` | A single restrained warm red, sparingly.    |
| Muted ink       | `#3b372e` | Secondary lines, axis rules.                |
| Deep shadow     | `#2a2620` | Only on gradients; no harsh blacks.         |

The accent `#a13d24` is the only saturated color. It is used for:

- the word `manifest` in the core node of the Module Constellation
  plate,
- the small observation dots at module endpoints,
- one call-to-action line in legends.

No other color enters the palette.

## Typography

**Titles** — Instrument Serif, *italic*.
Fallback chain: `'Instrument Serif', 'Cormorant Garamond', 'EB
Garamond', Georgia, serif`. Always italic. Never bold, never caps.

**Metadata, axes, captions** — IBM Plex Mono, UPPERCASE, wide
letter-spacing (roughly 2–4 units at 10–12 px).
Fallback: `'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo,
monospace`.

**Body text** — the surrounding document's default. Avoid setting body
type inside plates; if a plate has long text, split it into a separate
caption underneath.

## Layout grammar

Every Residual Frequencies plate uses the same skeleton:

- A single thin double frame around the plate (outer 1px, inner 0.5px).
- A metadata bar across the top with a plate number, the project name,
  and the date or volume.
- A horizontal rule under the metadata and above the footer.
- A ticked baseline axis near the bottom.
- Tight bottom-left legend and bottom-right scale bar (even if the
  scale is symbolic).

Whitespace is cheap; crowd nothing. Proportions come from the 1:1.414
aspect (A-series paper) or 10:4.5 for wide plates.

## Archetypes

The visual system has six archetypes. Every asset is one of them.

| Id | Name                  | Used for                                            |
|----|-----------------------|------------------------------------------------------|
| A  | Specimen strip        | Single-subject detail sheets.                        |
| B  | Cross-section         | Showing layering or stack order.                     |
| C  | Field of points       | Showing distributions, surveys.                      |
| D  | Ladder                | Process flows and versions.                          |
| E  | Two-column comparison | Before/after, declaration/enforcement.               |
| F  | **Module Constellation** | The canonical hero. Central node, peripheral modules connected by fine lines. |

The README hero of this repository is archetype F — Module
Constellation — rendered on the Parchment palette. The source lives at
[`../assets/hero.svg`](../assets/hero.svg). Future social cards should
reuse the same skeleton with different module labels.

## Rules

1. **Never emoji.** Not in plates, not in README, not in docs.
2. **Never round corners.** Laboratory plates have square corners.
3. **Never drop shadows.** Ink on parchment, nothing else.
4. **Never full-saturation fills.** The accent `#a13d24` is a line
   color and a small dot color; never a background.
5. **Never use the accent for long text.** It is for one word, a dot,
   or a two-word call.
6. **Always include a plate number** in the top-left and a
   project/version in the top-right.
7. **Always include a date or volume** somewhere in the footer.
8. **Always ruled.** Every plate has a tick rule somewhere on a baseline
   or axis, even if the axis is metaphorical.

If a plate violates any of these, it is not a Residual Frequencies
plate. Fix it or use a different visual system.

## File conventions

- SVG preferred. Hand-authored preferred over exported from a tool.
- Embed fonts as `font-family` fallback chains — never embed the font
  files.
- Accessibility: every plate SVG has `<title>` and `<desc>` with
  meaningful alt content. The README hero does this; follow its
  pattern.
- Keep every plate under 50 KB. A scientific plate is a few lines and
  a few words. If you need more than 50 KB, you are making a diagram,
  not a plate.

## Example

The Module Constellation hero at
[`../assets/hero.svg`](../assets/hero.svg) is the canonical reference
implementation. Reading its source is the fastest way to learn the
grammar.

# Internationalization and localization

The spec's user-facing text fields (`name`, `description`,
`summary`) accept Unicode but are single-string. Multi-language
support lives one level up.

## Three patterns

### Pattern A: ship one manifest per locale

For creations whose primary product is content (templates, docs
sites, courses), ship one manifest per locale. They share
`metadata.id` (because the underlying creation is the same).

```text
your-repo/
├── universal-spawn.yaml          ← English (canonical)
├── universal-spawn.fr.yaml       ← French
└── universal-spawn.ja.yaml       ← Japanese
```

A registry surfaces the locale that matches the user's preference.
Filenames are not part of the spec's discovery list, but a
consumer can look for `universal-spawn.<bcp47>.yaml` if it knows
the convention.

### Pattern B: lift translations into `x-ext`

For creations where the manifest itself is mostly machine-readable,
keep `name` / `description` / `summary` in the canonical language
and expose translations under `x-ext`:

```yaml
name: Plate Studio
description: A small parchment-themed plate generator.
summary: Generate Residual Frequencies plates.

x-ext:
  org.agentmindcloud.i18n:
    locales:
      fr:
        name: Plate Studio
        description: Un petit générateur de planches sur fond parchemin.
        summary: Générez des planches Residual Frequencies.
      ja:
        name: Plate Studio
        description: 小さなパーチメント風プレートジェネレーター。
        summary: Residual Frequencies プレートを生成。
```

Consumers that don't speak the locale ignore the block.

### Pattern C: hand off to the platform

For creations whose target platform already has a localization
story (HF Spaces, Vercel sites with i18n routing, Discord bots
with localization JSON), put the translations *there* — not in the
manifest. Reference the file in `compat.openapi`-style or a
sibling config; the manifest stays single-language.

## What about `data_residency`?

`safety.data_residency[]` is a separate concern. It declares where
data may legally reside, not what language the UI is in. A
multilingual product can still have a single residency.

```yaml
safety:
  data_residency: [eu]   # data stays in EU; UI in any language
```

## Discovery: which locale does a registry surface?

A conformant registry's preference order:

1. The canonical manifest (`universal-spawn.yaml`).
2. The locale variant whose tag matches the user's `Accept-Language`
   header best.
3. Any sibling localized manifest if the user explicitly requests
   one.

The standard does not require registries to support locale
variants. It allows them.

## BCP-47 tags only

When you do split per locale, use BCP-47 tags. `en`, `fr`, `ja`,
`pt-BR`, `zh-Hans`. No `british`, no `american`, no `chinese`. The
filename pattern is `universal-spawn.<tag>.yaml`.

## Common mistakes

- Translating `metadata.id` (don't — it's a stable opaque key).
- Translating `metadata.author.handle` (don't — it's a username).
- Translating `metadata.keywords` (don't — registries match on
  exact strings; you'd halve your hit rate).
- Mixing scripts in a single string field. If your description
  needs to switch scripts, that's a sign you should split per
  locale.

## What translates, what doesn't

| Field | Translate? |
|---|---|
| `name` | Yes |
| `description` | Yes |
| `summary` | Yes |
| `metadata.id` | No |
| `metadata.author.handle` | No |
| `metadata.keywords` | No (use locale-specific keywords sets if needed) |
| `metadata.categories` | No |
| `env_vars_required[*].description` | Yes |
| `platforms.*.tools[*].description` | Yes (LLMs read these) |

## TL;DR

Default to a single canonical manifest in your primary language.
Add `universal-spawn.<bcp47>.yaml` siblings only when content
volume justifies it. Use `x-ext.org.you.i18n` for tiny one-page
translations. Don't touch `metadata.id` or any field that's a
machine key.

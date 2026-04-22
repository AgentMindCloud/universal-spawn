# Showcase · `parchment-ds` — a Figma design system

**Use case.** A complete Figma design system distributed as a
community-file template. Anyone can click "Duplicate to your Figma"
and get the entire kit — components, color tokens, type ramp —
in their own workspace.

## The manifest

```yaml
version: "1.0"
name: Parchment Design System
description: >
  A complete Figma design system in the Residual Frequencies
  parchment palette. Components, color tokens, type ramp, plate
  templates. Duplicates into the viewer's Figma workspace in one
  click.
type: design-template
platforms:
  figma:
    kind: template
    editor_type: [figma]
    network_access: none
    community_file: "https://www.figma.com/community/file/1212121212121212"
safety: { safe_for_auto_spawn: true }
env_vars_required: []
deployment: { targets: [figma] }
visuals: { palette: parchment }
metadata:
  license: CC-BY-4.0
  id: com.parchment-ds.kit
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/parchment-ds }
  categories: [graphics]
```

## Platforms targeted, and why

- **`figma`** with `kind: template` — the standard Figma
  duplicate-to-workspace pattern. No code, just metadata pointing
  at the community file.

## How discovery happens

The repo's `universal-spawn.yaml` is found by a designer browsing
GitHub. The registry card renders a "Duplicate to your Figma"
button; on click, Figma opens with the duplicate flow prefilled.

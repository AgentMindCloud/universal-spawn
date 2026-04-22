# Showcase · `parchment-props` — a Unity asset pack

**Use case.** 40 parchment-themed props (pen, lab notebook, microscope,
clipboard, etc.) authored for URP. Sold on the Unity Asset Store.

## The manifest

```yaml
version: "1.0"
name: Parchment Props
description: >
  40 parchment-themed Unity props authored for URP. Sold on the
  Unity Asset Store under 3D Models / Props.
type: game-mod
platforms:
  unity:
    kind: asset-store-package
    min_editor: "2023.2"
    render_pipeline: urp
    asset_store_category: 3d-models
safety: { min_permissions: [fs:read], safe_for_auto_spawn: true }
env_vars_required: []
deployment: { targets: [unity] }
visuals: { palette: parchment }
metadata:
  license: proprietary
  id: com.parchment-studio.unity-props
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/unity-props }
  categories: [gaming, graphics]
```

## Platforms targeted, and why

- **`unity`** — Asset Store-package kind. URP-only is a deliberate
  choice; supporting HDRP would double the asset budget.

## How discovery happens

The buyer finds the pack via Unity Asset Store search. The
universal-spawn manifest lets a third-party Unity package indexer
verify the URP-only claim before listing the pack in its own
catalog.

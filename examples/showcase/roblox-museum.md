# Showcase · `parchment-museum` — a Roblox experience

**Use case.** A Roblox experience that recreates a small natural-
history museum in the Residual Frequencies aesthetic. Built with
Rojo. Pairs with a Roblox Studio plugin that streamers use to
arrange exhibits.

## The manifest

```yaml
version: "1.0"
name: Parchment Museum
description: >
  A small Roblox natural-history museum experience built with Rojo.
  Pairs with a Studio plugin that streamers use to arrange exhibits.
type: game-world
platforms:
  roblox:
    kind: experience
    universe_id: "1234567890"
    place_id: "9876543210"
    rojo_project: default.project.json
safety: { min_permissions: [fs:read], safe_for_auto_spawn: false }
env_vars_required:
  - { name: ROBLOX_API_KEY, secret: true, description: Roblox Open Cloud key }
deployment: { targets: [roblox] }
visuals: { palette: parchment }
metadata:
  license: proprietary
  id: com.parchment-studio.roblox-museum
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/roblox-museum }
  categories: [gaming]
```

## Platforms targeted, and why

- **`roblox`** — the only place the experience lives.

## How discovery happens

A discovery card on the Creator Hub links to the source repo. The
manifest lets a third-party Roblox showcase site embed the
experience's metadata without depending on Roblox-specific HTML.

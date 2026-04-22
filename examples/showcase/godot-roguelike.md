# Showcase · `parchment-roguelike` — a Godot game

**Use case.** A small turn-based roguelike built in Godot 4. Single
scene entry. Distributed for free on itch.io as a web build.

## The manifest

```yaml
version: "1.0"
name: Parchment Roguelike
description: >
  A small turn-based roguelike in Godot 4. The whole game runs in
  the browser via the HTML5 export. Free on itch.io.
type: game-world
platforms:
  godot:
    kind: project
    engine_series: "4"
    renderer: forward+
    entry_scene: scenes/dungeon.tscn
  itch-io:
    kind: html5
    butler_channel: web
    html5_frame: { width: 960, height: 720, fullscreen_button: true, mobile_friendly: false }
    payment: name-your-price
safety:
  min_permissions: [network:inbound, fs:read, gpu:compute]
  safe_for_auto_spawn: true
env_vars_required:
  - { name: BUTLER_API_KEY, description: butler upload key, secret: true }
deployment: { targets: [godot, itch-io] }
visuals: { palette: parchment }
metadata:
  license: MIT
  id: com.parchment-studio.roguelike
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/godot-roguelike }
  categories: [gaming]
```

## Platforms targeted, and why

- **`godot`** — the engine.
- **`itch-io`** — the only distribution channel; free + name-your-
  price is enough.

## How discovery happens

The itch.io page is the consumer-facing entry point. The
`universal-spawn.yaml` lets a Godot game-jam directory crawl the
repo and index the entry scene + render pipeline without opening
the editor.

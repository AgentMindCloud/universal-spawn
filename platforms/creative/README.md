# `platforms/creative/` — creative tools

Registry of creative-tool platform extensions: design editors, note
apps, 3D tools, and NLE/production software. Every folder follows the
session-4 layout (README, `<id>-spawn.yaml`, `<id>-spawn.schema.json`,
`compatibility.md`, optional `perks.md`, examples/).

The emphasis for this subtree: a manifest declares **what gets
duplicated or imported into the viewer's workspace** — a Figma
template, a Canva design, a Blender project, a Notion database, an
Obsidian vault snapshot.

## Capability matrix (12 platforms)

| Id | Native config | Shape | Duplicate-to-workspace |
|---|---|---|:---:|
| [figma](./figma)       | `manifest.json` (Figma plugin) | plugins, widgets, templates | E |
| [framer](./framer)     | `framer.project.json`          | sites, components           | U |
| [webflow](./webflow)   | Webflow API + Libraries        | components, sites           | U |
| [notion](./notion)     | Notion duplicate-page API      | templates, databases        | E |
| [obsidian](./obsidian) | community-plugin `manifest.json` | plugins, vaults, themes   | U |
| [blender](./blender)   | `.blend` + add-on `__init__.py`  | add-ons, projects, asset libs | U |
| [canva](./canva)       | Canva Apps SDK + Templates     | apps, templates, designs    | E |
| [adobe](./adobe)       | CEP/UXP manifest               | XD / Photoshop / Premiere extensions | U |
| [cinema4d](./cinema4d) | Python generators + `.lib4d`   | scenes, assets, plugins     | — |
| [houdini](./houdini)   | HDA / Python shelves           | HDAs, hip files             | — |
| [rhinoceros](./rhinoceros) | Grasshopper `.gh` + Rhino plugin | plugins, grasshopper defs | — |
| [sketchup](./sketchup) | Ruby extension                  | extensions, components      | — |

## Coexistence

- `figma/compatibility.md` shows how the universal manifest cohabits
  with `manifest.json` (plugins) and `widget.json` (widgets).
- `adobe/compatibility.md` shows CEP (old) vs UXP (new) in the same
  file.
- Every other folder has its own coexistence section.

## Duplicate-to-workspace

`figma` and `canva` ship an extra
`examples/duplicate-to-workspace.yaml` that demonstrates the canonical
"one-click duplicate into my account" pattern — the thing that makes
creative tools spawnable without installing anything.

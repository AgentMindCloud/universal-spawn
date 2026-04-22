# `platforms/gaming/` — game engines, platforms, and mod ecosystems

Extensions for the gamedev and games-as-platforms world. Every folder
has README, schema, compat note, and 1–3 examples. Perks shipped
where the platform has a store ecosystem (Steam, Roblox, itch).

## Capability matrix (13 platforms)

### Engines

| Id | Native config | Shape |
|---|---|---|
| [unity](./unity)             | `ProjectSettings/*.asset` + UPM | asset-store pack + project template |
| [unreal](./unreal)           | `.uproject`                     | marketplace plugin + project template |
| [godot](./godot)             | `project.godot`                 | addon + project |
| [playcanvas](./playcanvas)   | project JSON (cloud)            | project / asset |
| [defold](./defold)           | `game.project`                  | project / extension |

### Makers + 2D engines

| Id | Native config | Shape |
|---|---|---|
| [gdevelop](./gdevelop)       | `game.json`                     | project |
| [construct](./construct)     | `.c3p` project                  | project |
| [rpg-maker](./rpg-maker)     | `data/` tree (MV/MZ)            | project / plugin |

### Stores / mods / platforms

| Id | Native config | Shape |
|---|---|---|
| [roblox](./roblox)           | `default.project.json` (Rojo)   | experience + creator-hub listing |
| [itch-io](./itch-io)         | `.itch.toml`                    | html5 / downloadable game |
| [steam](./steam)             | `steampipe` VDF + Workshop API  | Workshop item + Direct listing |
| [minecraft](./minecraft)     | `pack.mcmeta` + `fabric.mod.json` | datapack + mod (distinguished) |
| [fortnite-uefn](./fortnite-uefn) | UEFN project files          | published island |

## Special examples

- `unity/` and `unreal/`: two examples — `asset-store.yaml` +
  `project-template.yaml`.
- `minecraft/`: two examples — `datapack.yaml` + `mod.yaml`, with a
  `kind` enum in the schema that forces exactly one.
- `itch-io/`: full-featured example is a web-playable HTML5 build.
- `steam/`: separate Workshop item vs Steamworks Direct example.

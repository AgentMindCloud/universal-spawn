# npm — universal-spawn platform extension

A universal-spawn manifest does NOT replace `package.json`. It is additive: the same repo ships both. npm still reads `package.json` for install, build, and publish; universal-spawn adds the cross-platform discoverability + metadata + safety envelope around it.

## What this platform cares about

The package name, whether the package is public / private / scoped, the declared peer-dependency surface, and the entrypoint shape (CLI / library / workspace).

## Compatibility table

| Manifest field | npm behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`, `plugin`. |
| `platforms.npm` | Strict. |

### `platforms.npm` fields

| Field | Purpose |
|---|---|
| `platforms.npm.package_name` | npm package name. |
| `platforms.npm.shape` | `library`, `cli`, or `workspace`. |
| `platforms.npm.access` | `public` or `restricted`. |
| `platforms.npm.node_range` | Node engine range. |
| `platforms.npm.bin_map` | Bin entries. |
| `platforms.npm.peer_deps` | Peer deps. |

See [`compatibility.md`](./compatibility.md) for more.

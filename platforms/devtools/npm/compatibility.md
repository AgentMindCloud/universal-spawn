# npm compatibility — field-by-field

| universal-spawn v1.0 field | npm behavior |
|---|---|
| `version` | Required. |
| `platforms.npm.package_name` | Package name (may be scoped). |
| `platforms.npm.shape` | `library`, `cli`, `workspace`. |
| `platforms.npm.access` | `public`, `restricted`. |
| `platforms.npm.node_range` | Engine range for Node. |
| `platforms.npm.bin_map` | Bin entries for CLI shape. |
| `platforms.npm.peer_deps` | Peer-dependency surface. |

## Coexistence with `package.json`

universal-spawn does NOT replace package.json. Both files coexist; consumers read both and warn on conflicts.

### `package.json` (provider-native)

```json
{
  "name": "@yourhandle/your-lib",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "engines": { "node": ">=20" },
  "publishConfig": { "access": "public" }
}
```

### `universal-spawn.yaml` (platforms.npm block)

```yaml
platforms:
  npm:
    package_name: "@yourhandle/your-lib"
    shape: library
    access: public
    node_range: ">=20"
```

## Additive — not a replacement

`package.json` still owns `dependencies`, `devDependencies`, `scripts`, `exports`, TypeScript `types`, and every npm- specific knob. `platforms.npm` only declares what a cross-platform consumer needs in order to tell the world about the package without re-reading npm's registry.

# Manifest file aliases

A conformant consumer scanning a repository looks for the manifest in
this order. The **first** file found wins. This list is authoritative;
any other name is ignored for discovery.

## Accepted filenames

Order is significant — top entries are checked first.

1. `universal-spawn.yaml` ← **preferred**
2. `universal-spawn.yml`
3. `universal-spawn.json`
4. `universal-spawn.toml`
5. `spawn.yaml`
6. `spawn.yml`
7. `spawn.json`
8. `spawn.toml`
9. `.spawn/config.yaml`
10. `.spawn/config.yml`
11. `.spawn/config.json`
12. `.spawn/config.toml`
13. A top-level `universalSpawn` key inside `package.json`.
14. A `[tool.universal-spawn]` section inside `pyproject.toml`.

### Why this order?

- `universal-spawn.*` is the unambiguous name.
- `spawn.*` is shorter for authors who already know what the file is.
- `.spawn/config.*` exists for teams who prefer hidden config
  directories.
- `package.json#universalSpawn` and `pyproject.toml[tool.universal-spawn]`
  let JavaScript and Python projects avoid a separate file.

## NOT accepted

These names are explicitly rejected. A file at any of these paths
**MUST** be ignored for discovery. This list is not exhaustive; if a
name is not on the **accepted** list, it is not accepted.

- `spawn-manifest.yaml`
- `us.yaml`
- `us-spawn.yaml`
- `universal.yaml`
- `manifest.yaml` (too generic — conflicts with other formats)
- `spec.yaml` (conflicts with this repository's own structure)
- `.universal-spawn` (dotfile without extension — ambiguous)
- Anything inside a build output directory (`dist/`, `build/`,
  `out/`, `.next/`, `.nuxt/`, `target/`, `node_modules/`).
- Anything inside a `.git/` directory.
- Anything with an unknown extension such as `.yaml5`, `.hjson`,
  `.pkl`.

## Monorepo case

A monorepo **SHOULD** ship one manifest at the repository root. Each
subproject MAY ship its own manifest at its own root; in that case
the consumer scans each subproject independently.

A future v1.1 RFC proposes a `universal-spawn.lock` at the repo root
that enumerates member manifests. Until that lands, one-per-directory
is the recommended pattern.

## `.yaml` vs `.yml`

Both are accepted. `.yaml` is preferred (matches upstream YAML spec's
own recommendation). Some editors default to `.yml`; that is fine.

## Extension case-sensitivity

Filename matching is **case-sensitive**. `Universal-Spawn.yaml` and
`UNIVERSAL-SPAWN.YAML` are not accepted. This matches POSIX filesystem
semantics on Linux and macOS (when not mounted case-insensitively) and
avoids ambiguity on Windows.

## Multiple accepted files in the same repo

If more than one accepted file exists, the **first** match by the
order above wins. Tooling **MAY** warn when it encounters unused
accepted-name files; this is a lint, not a validity error.

Example: a repository containing both `universal-spawn.yaml` and
`spawn.yaml` uses `universal-spawn.yaml`; `spawn.yaml` is ignored.
Tooling should warn so the author can delete one or the other.

## Embedded manifests

When embedded inside `package.json` or `pyproject.toml`, the manifest
data is the value of the named key. The enclosing file's other keys
are ignored by universal-spawn. A consumer **MUST NOT** attempt to
extract universal-spawn data from any other key.

```json
{
  "name": "my-package",
  "universalSpawn": {
    "version": "1.0",
    "name": "My Package",
    "type": "library",
    "description": "A small library.",
    "deployment": { "targets": ["npm"] }
  }
}
```

```toml
[tool.universal-spawn]
version = "1.0"
name = "My Package"
type = "library"
description = "A small library."

[tool.universal-spawn.deployment]
targets = ["pypi"]
```

Embedded manifests **SHOULD** be used only when the project already
owns a `package.json` or `pyproject.toml`. For everything else, a
standalone `universal-spawn.yaml` at the root is simpler.

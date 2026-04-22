# Figma platform extension

**Id**: `figma`
**Vendor**: Figma
**Surfaces**: Figma Plugins, Widgets, Dev Mode extensions.

A conformant Figma consumer:

1. Validates core + extension.
2. Registers the creation as a plugin or widget from the declared
   `manifest_file` (Figma's own plugin manifest — the two coexist;
   universal-spawn does not replace it).
3. Enforces `min_permissions` by mapping them onto Figma's declared
   permissions model (`currentuser`, `activeusers`,
   `network-access`).

## Notable fields

- `manifest_file` — path to the existing Figma `manifest.json`. The
  Figma manifest and the universal-spawn manifest are not competing;
  one describes the plugin to Figma, the other describes the creation
  to the universe.
- `editor_type[]` — which editors the plugin runs in
  (`figma`, `figjam`, `dev`, `slides`).
- `network_access` — `none`, `declared`, or `allowed-hosts`.
- `allowed_hosts[]` — required when `network_access` is
  `allowed-hosts`.
- `capabilities[]` — Figma plugin capabilities
  (`textreview`, `inspect`, `vscode`, `codegen`, …).

See [`figma-spawn.yaml`](./figma-spawn.yaml) and
[`examples/`](./examples).

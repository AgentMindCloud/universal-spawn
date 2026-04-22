# IDE autocomplete via JSON Schema

universal-spawn schemas validate as draft-07 JSON Schema. Every modern
editor will load them, autocomplete fields, and surface inline errors
once you wire the URL.

## VS Code (or any fork — Cursor, Windsurf, VSCodium)

Install the [Red Hat YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml).
Then add to user or workspace `settings.json`:

```json
{
  "yaml.schemas": {
    "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json": [
      "universal-spawn.yaml",
      "universal-spawn.yml",
      "spawn.yaml",
      "spawn.yml"
    ]
  }
}
```

Restart the editor. Autocomplete + inline error squiggles work on
every matched filename in any open repo.

## JetBrains (IntelliJ IDEA, PyCharm, WebStorm, …)

Settings → Languages & Frameworks → Schemas and DTDs → JSON Schema
Mappings:

| Field | Value |
|---|---|
| Name | `universal-spawn v1.0` |
| Schema URL | `https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json` |
| Schema version | `JSON Schema version 7` |
| File path pattern | `*/universal-spawn.{yaml,yml}` (and `spawn.{yaml,yml}`) |

## neovim (coc-yaml)

```jsonc
// :CocConfig
{
  "yaml.schemas": {
    "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json":
      ["universal-spawn.yaml", "universal-spawn.yml", "spawn.yaml", "spawn.yml"]
  }
}
```

Or with `nvim-lspconfig` + `yaml-language-server`:

```lua
require("lspconfig").yamlls.setup({
  settings = {
    yaml = {
      schemas = {
        ["https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json"] = {
          "universal-spawn.yaml",
          "universal-spawn.yml",
          "spawn.yaml",
          "spawn.yml",
        },
      },
    },
  },
})
```

## Helix

```toml
# ~/.config/helix/languages.toml
[[language]]
name = "yaml"
language-servers = ["yaml-language-server"]

[language-server.yaml-language-server.config.yaml.schemas]
"https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json" = [
  "universal-spawn.yaml", "universal-spawn.yml", "spawn.yaml", "spawn.yml"
]
```

## Sublime Text (LSP-yaml)

```json
{
  "settings": {
    "yaml.schemas": {
      "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json": [
        "universal-spawn.yaml", "universal-spawn.yml", "spawn.yaml", "spawn.yml"
      ]
    }
  }
}
```

## Platform extensions

The same pattern applies for any `<platform>-spawn.yaml`. Point the
schema URL at that platform's extension schema, e.g.:

```json
{
  "yaml.schemas": {
    "https://universal-spawn.dev/platforms/ai/grok/grok-spawn.schema.json": [
      "grok-spawn.yaml"
    ]
  }
}
```

The full list of canonical schema URLs lives in
[`sources.md`](./sources.md).

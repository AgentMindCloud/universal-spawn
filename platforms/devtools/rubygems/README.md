# RubyGems — universal-spawn platform extension

Ruby gems ship via `*.gemspec`. A universal-spawn manifest records the gem name, supported Ruby version range, and the canonical host (`rubygems.org` or a private host).

## What this platform cares about

The gem name, Ruby range, the host, and whether the gem ships an executable bin.

## Compatibility table

| Manifest field | RubyGems behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`. |
| `platforms.rubygems` | Strict. |

### `platforms.rubygems` fields

| Field | Purpose |
|---|---|
| `platforms.rubygems.gem_name` | Gem name. |
| `platforms.rubygems.ruby_range` | Ruby range. |
| `platforms.rubygems.host` | RubyGems host. |
| `platforms.rubygems.bin_name` | Executable bin name. |

See [`compatibility.md`](./compatibility.md) for more.

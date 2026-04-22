# RubyGems compatibility — field-by-field

| universal-spawn v1.0 field | RubyGems behavior |
|---|---|
| `version` | Required. |
| `platforms.rubygems.gem_name` | Gem name. |
| `platforms.rubygems.ruby_range` | Ruby range. |
| `platforms.rubygems.host` | RubyGems host. |
| `platforms.rubygems.bin_name` | Executable bin name (optional). |

## Coexistence with `*.gemspec + Gemfile`

universal-spawn does NOT replace *.gemspec + Gemfile. Both files coexist; consumers read both and warn on conflicts.

### `*.gemspec + Gemfile` (provider-native)

```ruby
Gem::Specification.new do |s|
  s.name = "your-gem"
  s.version = "0.1.0"
  s.required_ruby_version = ">= 3.2"
  s.license = "MIT"
end
```

### `universal-spawn.yaml` (platforms.rubygems block)

```yaml
platforms:
  rubygems:
    gem_name: your-gem
    ruby_range: ">= 3.2"
    host: rubygems.org
```

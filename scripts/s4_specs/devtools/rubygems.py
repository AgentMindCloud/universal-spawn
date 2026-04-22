"""RubyGems — .gemspec coexistence."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "rubygems",
    "title": "RubyGems",
    "lede": (
        "Ruby gems ship via `*.gemspec`. A universal-spawn manifest "
        "records the gem name, supported Ruby version range, and the "
        "canonical host (`rubygems.org` or a private host)."
    ),
    "cares": (
        "The gem name, Ruby range, the host, and whether the gem "
        "ships an executable bin."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`."),
        ("platforms.rubygems", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.rubygems.gem_name", "Gem name."),
        ("platforms.rubygems.ruby_range", "Ruby range."),
        ("platforms.rubygems.host", "RubyGems host."),
        ("platforms.rubygems.bin_name", "Executable bin name (optional)."),
    ],
    "platform_fields": {
        "gem_name": "Gem name.",
        "ruby_range": "Ruby range.",
        "host": "RubyGems host.",
        "bin_name": "Executable bin name.",
    },
    "schema_body": schema_object(
        required=["gem_name", "ruby_range"],
        properties={
            "gem_name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "ruby_range": str_prop(pattern=r"^[><=~ |.0-9, ]+$"),
            "host": enum(["rubygems.org", "private"]),
            "bin_name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: RubyGems Template
type: library
description: Template for a RubyGems-targeted universal-spawn manifest.

platforms:
  rubygems:
    gem_name: your-gem
    ruby_range: ">= 3.2"
    host: rubygems.org

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [rubygems]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/rubygems-template }
""",
    "native_config_name": "*.gemspec + Gemfile",
    "native_config_lang": "ruby",
    "native_config": """
Gem::Specification.new do |s|
  s.name = "your-gem"
  s.version = "0.1.0"
  s.required_ruby_version = ">= 3.2"
  s.license = "MIT"
end
""",
    "universal_excerpt": """
platforms:
  rubygems:
    gem_name: your-gem
    ruby_range: ">= 3.2"
    host: rubygems.org
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Palette Ruby
type: library
summary: Minimal RubyGem with Residual Frequencies palette helpers.
description: Pure Ruby gem, Ruby 3.2+, rubygems.org host.

platforms:
  rubygems:
    gem_name: parchment-palette
    ruby_range: ">= 3.2"
    host: rubygems.org

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [rubygems]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/ruby-parchment-palette }
  id: com.plate-studio.ruby-parchment-palette
""",
        "example-2": """
version: "1.0"
name: Plate Gem CLI
type: cli-tool
summary: Full RubyGem with a `plate` executable.
description: Gem with a bin/plate executable. Private host.

platforms:
  rubygems:
    gem_name: plate-cli
    ruby_range: ">= 3.1"
    host: private
    bin_name: plate

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [rubygems]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/ruby-plate-cli }
  id: com.plate-studio.ruby-plate-cli
""",
    },
}

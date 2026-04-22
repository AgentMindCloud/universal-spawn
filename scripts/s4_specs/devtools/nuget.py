"""NuGet — .nuspec + .csproj coexistence."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "nuget",
    "title": "NuGet",
    "lede": (
        "NuGet packages ship via `.nuspec` or a `.csproj` with "
        "`PackageId`. A universal-spawn manifest records the package "
        "id, target frameworks, and the feed."
    ),
    "cares": (
        "The package id, target frameworks (`net8.0`, `net9.0`, "
        "`netstandard2.0`, ...), and the feed host."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`library`, `cli-tool`, `plugin`."),
        ("platforms.nuget", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.nuget.package_id", "NuGet package id."),
        ("platforms.nuget.target_frameworks", "Target-framework monikers."),
        ("platforms.nuget.feed", "Feed URL / name."),
        ("platforms.nuget.is_tool", "True if DotnetCliToolReference or dotnet tool."),
    ],
    "platform_fields": {
        "package_id": "NuGet package id.",
        "target_frameworks": "TFMs.",
        "feed": "Feed URL / name.",
        "is_tool": "True for `dotnet tool` packages.",
    },
    "schema_body": schema_object(
        required=["package_id", "target_frameworks"],
        properties={
            "package_id": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9._-]{0,63}$"),
            "target_frameworks": {
                "type": "array",
                "minItems": 1,
                "items": str_prop(pattern=r"^[a-z][a-z0-9.-]+$"),
            },
            "feed": enum(["nuget.org", "github-packages", "azure-artifacts", "private"]),
            "is_tool": bool_prop(False),
        },
    ),
    "template_yaml": """
version: "1.0"
name: NuGet Template
type: library
description: Template for a NuGet-targeted universal-spawn manifest.

platforms:
  nuget:
    package_id: YourCompany.YourLib
    target_frameworks: [net8.0, netstandard2.0]
    feed: nuget.org

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [nuget]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/nuget-template }
""",
    "native_config_name": "*.csproj / *.nuspec",
    "native_config_lang": "xml",
    "native_config": """
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <PackageId>YourCompany.YourLib</PackageId>
    <Version>0.1.0</Version>
    <TargetFrameworks>net8.0;netstandard2.0</TargetFrameworks>
    <PackageLicenseExpression>Apache-2.0</PackageLicenseExpression>
  </PropertyGroup>
</Project>
""",
    "universal_excerpt": """
platforms:
  nuget:
    package_id: YourCompany.YourLib
    target_frameworks: [net8.0, netstandard2.0]
    feed: nuget.org
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Parchment Palette NET
type: library
summary: Minimal NuGet library with Residual Frequencies palette constants.
description: Multi-target .NET library on nuget.org.

platforms:
  nuget:
    package_id: PlateStudio.Parchment
    target_frameworks: [net8.0, net9.0, netstandard2.0]
    feed: nuget.org

safety:
  min_permissions: []
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [nuget]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/nuget-parchment }
  id: com.plate-studio.nuget-parchment
""",
        "example-2": """
version: "1.0"
name: Plate Dotnet Tool
type: cli-tool
summary: Full `dotnet tool` CLI distributed via GitHub Packages.
description: Global tool installable via `dotnet tool install -g plate-cli`.

platforms:
  nuget:
    package_id: PlateStudio.PlateCli
    target_frameworks: [net8.0]
    feed: github-packages
    is_tool: true

safety:
  min_permissions: [fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [nuget]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/nuget-plate-cli }
  id: com.plate-studio.nuget-plate-cli
""",
    },
}

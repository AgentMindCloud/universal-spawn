# NuGet compatibility — field-by-field

| universal-spawn v1.0 field | NuGet behavior |
|---|---|
| `version` | Required. |
| `platforms.nuget.package_id` | NuGet package id. |
| `platforms.nuget.target_frameworks` | Target-framework monikers. |
| `platforms.nuget.feed` | Feed URL / name. |
| `platforms.nuget.is_tool` | True if DotnetCliToolReference or dotnet tool. |

## Coexistence with `*.csproj / *.nuspec`

universal-spawn does NOT replace `*.csproj` / `*.nuspec`. Both files coexist; consumers read both and warn on conflicts.

### `*.csproj / *.nuspec` (provider-native)

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <PackageId>YourCompany.YourLib</PackageId>
    <Version>0.1.0</Version>
    <TargetFrameworks>net8.0;netstandard2.0</TargetFrameworks>
    <PackageLicenseExpression>Apache-2.0</PackageLicenseExpression>
  </PropertyGroup>
</Project>
```

### `universal-spawn.yaml` (platforms.nuget block)

```yaml
platforms:
  nuget:
    package_id: YourCompany.YourLib
    target_frameworks: [net8.0, netstandard2.0]
    feed: nuget.org
```

# NuGet — universal-spawn platform extension

NuGet packages ship via `.nuspec` or a `.csproj` with `PackageId`. A universal-spawn manifest records the package id, target frameworks, and the feed.

## What this platform cares about

The package id, target frameworks (`net8.0`, `net9.0`, `netstandard2.0`, ...), and the feed host.

## Compatibility table

| Manifest field | NuGet behavior |
|---|---|
| `version` | Required. |
| `type` | `library`, `cli-tool`, `plugin`. |
| `platforms.nuget` | Strict. |

### `platforms.nuget` fields

| Field | Purpose |
|---|---|
| `platforms.nuget.package_id` | NuGet package id. |
| `platforms.nuget.target_frameworks` | TFMs. |
| `platforms.nuget.feed` | Feed URL / name. |
| `platforms.nuget.is_tool` | True for `dotnet tool` packages. |

See [`compatibility.md`](./compatibility.md) for more.

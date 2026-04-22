# `platforms/devtools/` — developer tools

Extensions for IDEs, browsers, container / infra tooling, language
package managers, and cloud developer environments. Each folder has
the session-4 layout. `perks.md` is present where the ecosystem has
badges or a marketplace story (VS Code, JetBrains, GitHub Actions,
Docker Hub, the three browser stores).

## Capability matrix (20 platforms)

### IDEs + browser extensions

| Id | Native config | Shape |
|---|---|---|
| [vscode](./vscode)                     | `package.json` + `devcontainer.json` | extensions + dev containers |
| [jetbrains](./jetbrains)               | `plugin.xml`                | plugins for IntelliJ family |
| [chrome-extension](./chrome-extension) | `manifest.json` (MV3)       | browser extension |
| [firefox-extension](./firefox-extension) | `manifest.json` (MV3)     | browser extension |
| [safari-extension](./safari-extension) | Xcode project + Info.plist  | browser extension |

### Infra / container / IaC

| Id | Native config |
|---|---|
| [docker](./docker)         | `Dockerfile` + `compose.yaml` |
| [kubernetes](./kubernetes) | Helm chart + kustomize         |
| [terraform](./terraform)   | `*.tf` + `terraform.tfstate`   |
| [pulumi](./pulumi)         | `Pulumi.yaml`                  |

### Language package registries

| Id | Native config |
|---|---|
| [npm](./npm)             | `package.json`      |
| [pypi](./pypi)           | `pyproject.toml`    |
| [crates-io](./crates-io) | `Cargo.toml`        |
| [rubygems](./rubygems)   | `*.gemspec`         |
| [nuget](./nuget)         | `*.csproj` + `*.nuspec` |
| [maven](./maven)         | `pom.xml`           |

### Cloud dev environments

| Id | Native config |
|---|---|
| [github-actions](./github-actions) | `.github/workflows/*.yaml` |
| [codespaces](./codespaces)         | `.devcontainer/*`          |
| [gitpod](./gitpod)                 | `.gitpod.yml`              |
| [codesandbox](./codesandbox)       | `.codesandbox/`            |
| [stackblitz](./stackblitz)         | `.stackblitzrc`            |

## Coexistence emphasis

`npm`, `pypi`, and `crates-io` ship an explicit side-by-side
coexistence block: the universal manifest is **additive** to the
native package metadata — it does not replace `package.json`,
`pyproject.toml`, or `Cargo.toml`. See their
`compatibility.md` files.

## Special examples

- `vscode/` ships two examples — `extension.yaml` (VS Code
  Marketplace extension) and `devcontainer.yaml` (Dev Containers
  spec).
- `docker/` ships two examples — `compose.yaml` (multi-container
  Compose) and `single-container.yaml` (Dockerfile-backed image).

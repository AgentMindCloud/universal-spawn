# Azure — Deploy-button recipe

A manifest that declares `platforms.azure` with a
complete `azure.yaml (azd) / function.json`-equivalent block is eligible
for the canonical Azure Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fyourhandle%2Fyour-project%2Fmain%2Fazuredeploy.json)
```

## HTML

```html
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fyourhandle%2Fyour-project%2Fmain%2Fazuredeploy.json">
  <img src="https://aka.ms/deploytoazurebutton" alt="Deploy to Azure" />
</a>
```

## Parameters

The Azure portal deploy URL accepts:

- `uri` — URL-encoded URL to an ARM template JSON.

Static Web Apps and Functions have their own deployment shortcuts; container-based deployments typically use an ARM / Bicep template.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Azure" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `azure-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Azure](https://universal-spawn.dev/badge/azure.svg)](https://universal-spawn.dev/registry/azure)
```

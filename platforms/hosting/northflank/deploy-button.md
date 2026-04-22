# Northflank — Deploy-button recipe

A manifest that declares `platforms.northflank` with a
complete `northflank.yaml (Spec CLI)`-equivalent block is eligible
for the canonical Northflank Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy on Northflank](https://assets.northflank.com/deploy-on-northflank.svg)](https://app.northflank.com/s/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://app.northflank.com/s/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://assets.northflank.com/deploy-on-northflank.svg" alt="Deploy on Northflank" />
</a>
```

## Parameters

Northflank's deploy URL accepts `template` (URL-encoded git repo URL) and looks for a `northflank.yaml` at the repo root.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Northflank" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `northflank-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Northflank](https://universal-spawn.dev/badge/northflank.svg)](https://universal-spawn.dev/registry/northflank)
```

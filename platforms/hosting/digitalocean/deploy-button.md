# DigitalOcean — Deploy-button recipe

A manifest that declares `platforms.digitalocean` with a
complete `app.yaml (App Platform) / project.yml (Functions)`-equivalent block is eligible
for the canonical DigitalOcean Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://cloud.digitalocean.com/apps/new?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://www.deploytodo.com/do-btn-blue.svg" alt="Deploy to DO" />
</a>
```

## Parameters

The DO App Platform new-app URL accepts `repo` (URL-encoded git repo URL) and `refresh` (to redeploy).

## Badge style

The universal-spawn project ships a complementary "Spawns on
DigitalOcean" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `digitalocean-spawn.schema.json` loses the badge.

```markdown
[![Spawns on DigitalOcean](https://universal-spawn.dev/badge/digitalocean.svg)](https://universal-spawn.dev/registry/digitalocean)
```

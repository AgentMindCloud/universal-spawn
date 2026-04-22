# Hetzner Cloud — Deploy-button recipe

A manifest that declares `platforms.hetzner` with a
complete `cloud-init.yaml (+ hcloud CLI)`-equivalent block is eligible
for the canonical Hetzner Cloud Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Create Hetzner server](https://img.shields.io/badge/Create%20on-Hetzner-red)](https://console.hetzner.cloud/projects)
```

## HTML

```html
<a href="https://console.hetzner.cloud/projects">
  <img src="https://img.shields.io/badge/Create%20on-Hetzner-red" alt="Create on Hetzner" />
</a>
```

## Parameters

Hetzner has no native Deploy button. Use Terraform or `hcloud` CLI driven by this manifest; the linked console shortcut is for convenience.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Hetzner Cloud" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `hetzner-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Hetzner Cloud](https://universal-spawn.dev/badge/hetzner.svg)](https://universal-spawn.dev/registry/hetzner)
```

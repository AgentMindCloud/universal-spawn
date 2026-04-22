# Vultr — Deploy-button recipe

A manifest that declares `platforms.vultr` with a
complete `cloud-init.yaml + Vultr API`-equivalent block is eligible
for the canonical Vultr Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy on Vultr](https://img.shields.io/badge/Deploy%20on-Vultr-blue)](https://my.vultr.com/deploy/)
```

## HTML

```html
<a href="https://my.vultr.com/deploy/">
  <img src="https://img.shields.io/badge/Deploy%20on-Vultr-blue" alt="Deploy on Vultr" />
</a>
```

## Parameters

Vultr has no native Deploy button. Drive provisioning with the Vultr API or Terraform using the fields above.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Vultr" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `vultr-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Vultr](https://universal-spawn.dev/badge/vultr.svg)](https://universal-spawn.dev/registry/vultr)
```

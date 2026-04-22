# Koyeb — Deploy-button recipe

A manifest that declares `platforms.koyeb` with a
complete `koyeb.yaml`-equivalent block is eligible
for the canonical Koyeb Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com%2Fyourhandle%2Fyour-project">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" />
</a>
```

## Parameters

The Koyeb deploy URL accepts `type`, `repository`, `branch`, and `env[KEY]=value` pairs.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Koyeb" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `koyeb-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Koyeb](https://universal-spawn.dev/badge/koyeb.svg)](https://universal-spawn.dev/registry/koyeb)
```

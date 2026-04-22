# Linode (Akamai Cloud) — Deploy-button recipe

A manifest that declares `platforms.linode` with a
complete `StackScript + linode-cli`-equivalent block is eligible
for the canonical Linode (Akamai Cloud) Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy on Linode](https://img.shields.io/badge/Deploy%20on-Linode-green)](https://cloud.linode.com/stackscripts/123456)
```

## HTML

```html
<a href="https://cloud.linode.com/stackscripts/123456">
  <img src="https://img.shields.io/badge/Deploy%20on-Linode-green" alt="Deploy on Linode" />
</a>
```

## Parameters

Linode's canonical deploy flow links to a public StackScript id in the Cloud Manager. The UDF answers come from `stackscript.udf[]` in this manifest.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Linode (Akamai Cloud)" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `linode-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Linode (Akamai Cloud)](https://universal-spawn.dev/badge/linode.svg)](https://universal-spawn.dev/registry/linode)
```

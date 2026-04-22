# Firebase — Deploy-button recipe

A manifest that declares `platforms.firebase` with a
complete `firebase.json`-equivalent block is eligible
for the canonical Firebase Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Try it on Firebase](https://img.shields.io/badge/Try%20it%20on-Firebase-orange)](https://console.firebase.google.com/?githubImport=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://console.firebase.google.com/?githubImport=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://img.shields.io/badge/Try%20it%20on-Firebase-orange" alt="Try it on Firebase" />
</a>
```

## Parameters

Firebase does not ship an official Deploy-to-Firebase button. The common pattern links to the Firebase console with a `githubImport` query param. Generators SHOULD document that the user needs to run `firebase init` and `firebase deploy` locally after cloning.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Firebase" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `firebase-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Firebase](https://universal-spawn.dev/badge/firebase.svg)](https://universal-spawn.dev/registry/firebase)
```

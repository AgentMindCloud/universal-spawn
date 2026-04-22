# PythonAnywhere — Deploy-button recipe

A manifest that declares `platforms.pythonanywhere` with a
complete `wsgi.py (plus dashboard-managed web apps)`-equivalent block is eligible
for the canonical PythonAnywhere Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Try on PythonAnywhere](https://img.shields.io/badge/Try%20on-PythonAnywhere-blue)](https://www.pythonanywhere.com/signup/?plan=free)
```

## HTML

```html
<a href="https://www.pythonanywhere.com/signup/?plan=free">
  <img src="https://img.shields.io/badge/Try%20on-PythonAnywhere-blue" alt="Try on PythonAnywhere" />
</a>
```

## Parameters

PythonAnywhere has no native Deploy button. The badge above links to signup; the install itself runs via the community bash helper, which reads this manifest.

## Badge style

The universal-spawn project ships a complementary "Spawns on
PythonAnywhere" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `pythonanywhere-spawn.schema.json` loses the badge.

```markdown
[![Spawns on PythonAnywhere](https://universal-spawn.dev/badge/pythonanywhere.svg)](https://universal-spawn.dev/registry/pythonanywhere)
```

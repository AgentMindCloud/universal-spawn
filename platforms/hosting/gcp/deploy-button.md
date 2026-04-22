# Google Cloud (GCP) — Deploy-button recipe

A manifest that declares `platforms.gcp` with a
complete `app.yaml / cloudbuild.yaml`-equivalent block is eligible
for the canonical Google Cloud (GCP) Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run/?git_repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://deploy.cloud.run/?git_repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" />
</a>
```

## Parameters

The `deploy.cloud.run` endpoint accepts:

- `git_repo` — URL-encoded git repo URL.
- `dir` — subdirectory with the Dockerfile.
- `revision` — branch, tag, or commit.

The button targets Cloud Run only; Cloud Functions and App Engine deploys require `gcloud` today.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Google Cloud (GCP)" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `gcp-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Google Cloud (GCP)](https://universal-spawn.dev/badge/gcp.svg)](https://universal-spawn.dev/registry/gcp)
```

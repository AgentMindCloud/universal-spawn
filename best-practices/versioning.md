# Versioning

Two version numbers matter to a universal-spawn manifest: the
**spec version** (`version: "1.0"` in your manifest) and the
**creation version** (whatever you keep in the project's own
release notes, package.json, Cargo.toml, etc.). They are not the
same thing.

## Spec version

The `version` field declares which version of the universal-spawn
spec the manifest targets. Today the only accepted value is `"1.0"`.

When the spec ships v1.1, your manifest stays valid as a v1.0
manifest until you change it. v1.1 will be backward-compatible at
the validator level: any v1.0 manifest is also a valid v1.1
manifest. New optional fields land; nothing existing breaks.

When the spec ships v2.0 — should that ever happen — the upgrade
will be deliberate. There will be a written migration note, the
v1.0 schema will continue to validate v1.0 manifests indefinitely,
and a `migrate` subcommand will lift v1.0 → v2.0 in one shot.

## Creation version

Your manifest does not include a `creation_version` field. Use
`metadata.source.commit` to pin the exact snapshot a consumer
should treat as canonical:

```yaml
metadata:
  source:
    type: git
    url: https://github.com/yourhandle/your-project
    commit: a1b2c3d4e5f6
```

A consumer that wants reproducibility pins on this commit; a
consumer that wants the latest reads `HEAD` of the named branch.
Neither pattern requires a `creation_version` field, and adding
one would just be a second source of truth that drifts from the
git tags.

If your audience is package-manager users (npm, PyPI, crates.io),
the `package.json`/`pyproject.toml`/`Cargo.toml` `version` field is
where the version lives — and `universal-spawn.yaml` is purely
additive metadata. Don't duplicate the version in the manifest.

## Semver applied to the manifest itself

When you change a manifest:

- **Patch-level (no consumer impact)**: tweaking `description`,
  re-ordering an `env_vars_required` list, fixing a typo in
  `summary`. No need to bump anything.
- **Minor (additive)**: adding a new platform under `platforms.*`,
  adding a new `env_vars_required` entry that you've made
  `required: false`, adding a new `safety.data_residency` entry.
  Note in the changelog; don't bump the spec version.
- **Major (consumer-visible breaking change)**: removing a
  `platforms.*` block, renaming `metadata.id`, tightening
  `safety.min_permissions` to drop a host you previously needed,
  adding a `required: true` env var. These need a release note,
  ideally a migration line, and a corresponding bump in your
  package's own version (tag).

## Migration strategy when the spec moves

Three rules:

1. **Pin a commit, not a branch, when you need stability.**
   `metadata.source.commit` exists for this. Pinning protects you
   against silent upstream changes.
2. **Run the validator in CI.** If the spec's schema tightens in a
   minor release, you find out immediately, not when a customer
   reports a Deploy button is broken.
3. **Run the validator in `--strict` mode for production deploys.**
   Warnings become failures. You learn about the gaps before
   they become user-facing.

## Breaking changes in your own platform extension

If you maintain a `platforms.<id>` extension under
`platforms/<subtree>/<id>/`, version it the same way. Bump
`<id>-spawn.schema.json`'s `$id` URL to include the new version
when you make a breaking change:

```
https://universal-spawn.dev/platforms/ai/<id>/v2/<id>-spawn.schema.json
```

Old manifests stay valid against the v1 schema, new manifests
validate against v2, and your platform consumer routes by URL.

## Don't do this

- Add a `creation_version` field at the root of the manifest.
  There's no place for it; the schema rejects it.
- Inline a changelog into `description`. Use a CHANGELOG.md.
- Stamp every commit with a new `metadata.source.commit`.
  `commit` is for *snapshots a third party should reproduce*, not
  for "what's HEAD right now."

## What the registry does with versions

A universal-spawn registry typically hashes the manifest and uses
the hash as a stable id. When you bump anything, the hash changes,
and the registry shows a new card. Consumers can pin to a hash for
reproducibility; otherwise they get the latest. Your `metadata.id`
stays constant across bumps — that's what's stable across renames,
forks, and platform migrations.

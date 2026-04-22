# Versioning policy

The universal-spawn specification uses strict semantic versioning.

## Version meaning

- **Major (`X.0.0`)** — breaking change. Valid v1 manifests MAY be
  invalid under v2. Consumers MUST refuse any major version they do not
  support. Majors are reserved for structural rework — removing a
  required field, renaming identifiers, changing the permission
  vocabulary.
- **Minor (`X.Y.0`)** — additive. New optional fields, new enum values,
  new platforms, new entrypoint kinds. Manifests valid under `X.Y` are
  valid under `X.(Y+1)`. Consumers MAY support any minor revision of a
  major they implement.
- **Patch (`X.Y.Z`)** — editorial. Clarifications, schema fixes,
  documentation. No semantic change.

## How a new version ships

1. A proposal opens as a spec-change issue (see
   `.github/ISSUE_TEMPLATE/spec_proposal.md`).
2. The editor drafts a new version directory `spec/vX.Y.Z/` with the
   updated `spec.md` and `manifest.schema.json`. Old versions are never
   edited after release except for typo corrections.
3. The change is discussed in public on the issue. Two maintainer
   approvals are required.
4. Release is tagged `spec-vX.Y.Z` in this repository. The `$id` inside
   the new schema points to
   `https://universal-spawn.org/spec/vX.Y.Z/manifest.schema.json`.
5. `CHANGELOG.md` is updated in the same commit.

## Deprecation

A field MAY be marked deprecated in a minor release. It MUST continue to
validate and be honored until the next major. Deprecations appear in
`fields.md` with the version in which the field was deprecated and the
planned removal version.

## Stability guarantees

- Field names and types are stable within a major.
- `id` namespace rules never change within a major.
- Enum values may only be added (never removed or re-purposed) within a
  major.
- The canonical serialization procedure (Appendix C) is stable within a
  major.

## Security fixes

Changes that only close a security hole may be shipped as a patch even
if they narrow the acceptance set, provided affected manifests are
already known to be unsafe. Such patches will be accompanied by a
SECURITY advisory.

# universal-spawn — specification

Versioned specification documents live here.

| Version                          | Status | Released | Notes                        |
|----------------------------------|--------|----------|------------------------------|
| [v1.0.0](./v1.0.0/spec.md)       | Stable | 2026-04  | Initial public spec.         |

Each version directory contains:

- `spec.md` — normative prose specification.
- `manifest.schema.json` — normative JSON Schema (draft 2020-12).
- `fields.md` — field-by-field reference with examples.
- `compatibility-matrix.md` — which core fields each platform honors.

See [`versioning.md`](./versioning.md) for the version policy.

The repository is the canonical source. If you mirror or cache the
specification, please preserve the version directory structure so that
`$id` URIs resolve.

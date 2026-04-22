---
name: Spec proposal
about: Propose a change to the specification — additive or breaking
title: "[spec] "
labels: spec-proposal
---

## Summary

One paragraph describing what you want to change in the specification.

## Kind of change

- [ ] Editorial (typo, clarification) — patch
- [ ] Additive (new optional field, new enum value, new platform) —
      minor
- [ ] Breaking (removes or renames a field, changes acceptance) —
      major

## Motivation

What are you trying to express that the current spec can't? Describe
a concrete manifest you can't write today.

## Proposed prose change

Link to or quote the paragraph in
[`spec/v1.0.0/spec.md`](../../spec/v1.0.0/spec.md) you would add or
modify.

## Proposed schema change

Show the diff against
[`spec/v1.0.0/manifest.schema.json`](../../spec/v1.0.0/manifest.schema.json).
Be precise — a spec proposal without a schema diff is a discussion,
not a proposal.

```diff
# unified-diff style
```

## Impact

- Which existing manifests become invalid?
- Which platform extensions need updates?
- Which `compatibility-matrix.md` cells change?
- Is a new spec version required? Minor or major?

## Backwards compatibility plan

For breaking changes, describe:

- Transition window (at least one minor release with the old shape
  deprecated).
- Lowering rules to the previous major, if applicable.
- Tooling that will help authors migrate.

## Open questions

List any decisions still needed.

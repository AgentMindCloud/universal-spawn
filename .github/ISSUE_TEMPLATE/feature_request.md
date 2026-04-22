---
name: Feature request
about: Suggest an improvement that is additive and does not break v1 manifests
title: "[feature] "
labels: enhancement
---

## Problem

What cannot currently be expressed in a universal-spawn manifest?
Describe the concrete authoring or consumption scenario.

## Proposed shape

Sketch the field(s) you would add. Keep it additive — new optional
fields, new enum values, new platforms. Breaking changes belong in a
[spec proposal](./spec_proposal.md).

```yaml
# rough shape
```

## Why universal and not platform-specific

universal-spawn's core fields should work on every platform. If the
proposed field is platform-specific, open a PR against that platform's
extension schema instead.

## Alternatives considered

Including "do nothing" and why it is or isn't acceptable.

## Impact on existing manifests

Must be zero. Existing valid manifests MUST remain valid. If your
proposal breaks that, you want a spec proposal, not a feature
request.

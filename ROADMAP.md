# Roadmap

Directions for the universal-spawn specification and this repository.
Dates are **targets**, not commitments. The only hard promise is that
**v1.x** remains backwards compatible: a manifest valid under v1.0
stays valid under v1.5.

## v1.0 — Now (2026-04)

**Status**: shipped.

- Declarative manifest across nine platforms (Claude, Gemini, OpenAI,
  Vercel, Netlify, Unity, Figma, Discord, Hugging Face).
- JSON Schema draft-07 in `spec/v1.0/` and draft 2020-12 reference
  track in `spec/v1.0.0/`.
- Twelve worked examples.
- Migration guide from `grok-install` v2.14 and from `vercel.json`.
- Core governance and contributor scaffolding.

## v1.1 — +30 days

**Status**: planned.

- **Richer platform perks.** Tighter extension schemas for each of
  the nine platforms; promote the `compatibility.md` table to a
  machine-readable `compatibility.json`.
- **Per-platform validators.** A reference validator SDK that takes a
  manifest + a platform id and runs the core schema, the extension
  schema, and a platform lint pass in one invocation.
- **RFC process.** Formal RFC template in Discussions; first cohort of
  RFCs open for comment.
- **Reference registry.** A read-only index that crawls public repos
  containing `universal-spawn.yaml` at the root.

## v1.2 — +60 days

**Status**: planned.

- **Signed manifests** as an optional but first-class feature.
  Canonical serialization (JCS + SHA-256, already defined in spec
  Appendix C) paired with reference tooling for ed25519 signing and
  verification.
- **Key discovery.** A `.well-known/universal-spawn-keys.txt`
  convention so verifiers can pin keys without a central PKI.
- **Revocation** — the mechanism, not a hosted service.

## v1.5 — +120 days

**Status**: directional.

- **Badges & certification.** "Universal-spawn conformant" badge a
  repo can embed in its README once a validator CI check passes.
- **Certification levels.** Declaration-only (`c1`), validator-passing
  (`c2`), signed + validator-passing (`c3`).
- **Conformance tests** shipped alongside the schema; platforms can
  link to their conformance report.
- **Multi-language SDKs.** Validators in Python, Go, Rust, Swift, with
  shared conformance tests.

## v2.0 — Vision

**Status**: vision, not a plan. Ships only when the below make sense.

- **Monetization hooks.** Declarative price / licensing surfaces so a
  paid creation can be spawned with a checkout flow attached.
- **Cross-platform identity linking.** A stable `author.did` that ties
  a human or org to a manifest across platforms.
- **Registry federation.** A protocol so multiple registries can
  mirror each other without a central authority.
- **Capability advertisements.** Platforms publish what they enforce
  and what they do not; consumers pick accordingly.

See [`spec/future-versions/v2.0-vision.md`](spec/future-versions/v2.0-vision.md)
for the full sketch.

## How items land here

Proposals open in
[Discussions](https://github.com/AgentMindCloud/universal-spawn/discussions)
under the **RFC** category. When two maintainers approve and the editor
tags `accepted`, the item moves onto this roadmap. Items that land
ship under the appropriate spec version; items that don't ship are
moved to `spec/future-versions/` with a rationale.

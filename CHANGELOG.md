# Changelog

All notable changes to the universal-spawn specification are recorded
here. The repository uses two tag namespaces:

- `spec-vX.Y.Z` — specification releases.
- `repo-vX.Y.Z` — repository tooling / docs releases (if separate).

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
The specification follows strict [Semantic Versioning](https://semver.org/).

## [spec-v1.0.0] — 2026-04-22

First public specification release.

### Added

- Core manifest schema: `spec/v1.0.0/manifest.schema.json`
  (draft 2020-12, strict `additionalProperties: false` throughout).
- Normative prose: `spec/v1.0.0/spec.md`.
- Field reference: `spec/v1.0.0/fields.md`.
- Platform compatibility matrix:
  `spec/v1.0.0/compatibility-matrix.md`.
- Canonical permission vocabulary (spec Appendix B).
- Canonical serialization procedure for signing (spec Appendix C, JCS
  / RFC 8785 + SHA-256).
- Compatibility layer with `AgentMindCloud/grok-install` v2.14 via
  `compat.grok_install`.
- Platform extension folders for Claude, Gemini, OpenAI, Vercel,
  Netlify, Unity, Figma, Discord, and Hugging Face, each with its own
  strict extension schema and at least two worked examples.
- Example manifests: minimal, full-coverage, ai-agent, web-app,
  creative-tool, game-mod, hardware-device, cross-platform.
- Safety model (`min_permissions`, `rate_limit_qps`,
  `cost_limit_usd_daily`, `safe_for_auto_spawn`,
  `env_vars_required`).
- Residual Frequencies · Parchment design plate (archetype F) used as
  the README hero and social card.
- Governance and security policies.

### Notes

- No previous public version exists. This document begins the public
  changelog.
- Editor: Jani Solo (`@JanSol0s`) for AgentMindCloud.

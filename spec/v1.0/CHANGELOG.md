# Changelog — spec/v1.0

Changes to the v1.0 track of the universal-spawn specification. Format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The
specification uses strict [Semantic Versioning](https://semver.org/).

## [1.0] — 2026-04-22

Initial public release of the v1.0 specification on JSON Schema
draft-07.

### Added

- Normative prose: `spec/v1.0/spec.md`.
- Normative schema (draft-07): `spec/v1.0/universal-spawn.schema.json`.
- YAML mirror of the schema: `spec/v1.0/universal-spawn.schema.yaml`.
- Twelve worked examples, each demonstrating a distinct project
  shape: Claude skill, multi-AI agent, Next.js on Vercel, Discord
  moderation bot, Hugging Face Gradio Space, Unity OpenXR experience,
  Figma Dev Mode codegen plugin, CLI developer tool, USB firmware,
  Minecraft mod, grok-install migration, Netlify docs site.
- Migration guides: `from-grok-install.md`, `from-vercel-json.md`.
- File discovery order (§3), including `universal-spawn.*`, `spawn.*`,
  `.spawn/config.*`, `package.json#universalSpawn`, and
  `pyproject.toml[tool.universal-spawn]`.
- Declarative safety envelope: `min_permissions`, `rate_limit_qps`,
  `cost_limit_usd_daily`, `safe_for_auto_spawn`, `data_residency`.
- `env_vars_required` with SCREAMING_SNAKE_CASE name pattern.
- `visuals` object with Residual Frequencies palette ids.
- `metadata` block with SPDX license, author, maintainers, source,
  keywords, categories, optional reverse-DNS `id`.
- Canonical signing procedure (§15, JCS + SHA-256); signatures
  remain optional in v1.0.
- Proposed IANA media types (§16).

### Relationship to v1.0.0 (legacy draft 2020-12 track)

The `spec/v1.0.0/` directory ships the initial draft 2020-12 schema
with a different top-level shape. The two tracks coexist during the
v1.x line. A reconciliation may fold one into the other in a minor
release; until then, conformant validators should pick one track per
deployment.

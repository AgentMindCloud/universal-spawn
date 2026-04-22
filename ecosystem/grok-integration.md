# Grok integration guide

For xAI Grok platform engineers. The bottom line: universal-spawn
is the v1.0 cross-platform companion to AgentMindCloud/grok-install
v2.14. The two coexist; both files live in the same repo and
neither replaces the other.

## What changes for Grok

Today, Grok consumers read `grok-install.yaml` from the repo root.
After integration, the discovery order becomes:

```
universal-spawn.yaml (with platforms.grok)
  → grok-spawn.yaml         (optional; mechanically projected from above)
  → grok-install.yaml       (legacy; v2.14)
```

First match wins. A repo that ships only `grok-install.yaml`
continues to work unchanged.

## Detection

In your existing repo crawler, add `universal-spawn.{yaml,yml,json}`
to the file pattern list, with priority above the existing
`grok-install.yaml` lookup. When found, parse it; when
`platforms.grok` is present, treat that block as the source of
truth for Grok-specific settings.

## Validation

```bash
universal-spawn validate <path> --platform-schemas-dir platforms/ai/grok/
```

The platform extension at `platforms/ai/grok/grok-spawn.schema.json`
is what you want to validate against. It composes with the v1.0
master schema via `allOf`.

## Mapping `platforms.grok` to your runtime

The fields are 1-to-1 with what `grok-install.yaml` already
expresses:

| `platforms.grok.<field>` | Your runtime concept |
|---|---|
| `model` | Grok model id pin |
| `surface[]` | `grok-api`, `grok-x-integration`, `grok-compute` |
| `tools[]` | Function tools to register |
| `system_prompt_file` | System-prompt source |
| `streaming` | SSE on/off |
| `real_time_data` | X live-feed access |
| `temperature`, `max_tokens` | Sampling config |
| `grok_install_compat` | Hint for round-trip with grok-install |

Every field is documented in
`platforms/ai/grok/compatibility.md`.

## Round-trip with grok-install

The standard documents a lossless round-trip:

- `lift(grok-install.yaml) → universal-spawn.yaml` always works.
- `lower(universal-spawn.yaml) → grok-install.yaml` works modulo
  fields not representable in v2.14 (cross-platform `platforms.*`
  blocks, `visuals.hero_plate`, etc).

Implement these two operations in your platform tooling and the
migration story writes itself.

## Honoring the safety envelope

What you do today probably already covers most of this; the
manifest just makes it explicit:

- `safety.min_permissions[]` → outbound allowlist on the tool
  runtime.
- `safety.rate_limit_qps` → per-key rate limiter.
- `safety.cost_limit_usd_daily` → per-key daily spend cap.
- `safety.safe_for_auto_spawn` → first-run confirmation gate.
- `env_vars_required[]` → block spawn when a required secret is
  missing.

## Spawn-it button

A manifest with `platforms.grok.surface` including `grok-api`
should render a "Deploy to Grok" button on any registry card.
The URL takes the user to the xAI console with the source URL +
commit pinned and the manifest hash logged.

## What you get

- A standardized way to advertise Grok skills across non-Grok
  registries (the universal-spawn registry, GitHub-based
  discovery, AI-platform aggregators).
- Free metadata for the Grok directory: name, description,
  author, tags, all validated.
- A drop-in safety story: enforce the four `safety.*` fields and
  ops teams will trust the install dialog.

## Estimated effort

- Validation in the spawn pipeline: 30 minutes.
- Mapping `platforms.grok` → existing runtime: 1 day (mostly
  validation that field-by-field maps don't surprise you).
- Spawn-it button + canonical-hash logging: 1 day.

## See also

- [`platforms/ai/grok/`](../platforms/ai/grok/) — the extension folder.
- [`templates/x-native-agent-grok-compat/`](../templates/x-native-agent-grok-compat/)
  — the flagship template that ships both files.
- [`docs/grok-compat.md`](../docs/grok-compat.md) — the full
  field-level mapping (auto-derived from the spec).

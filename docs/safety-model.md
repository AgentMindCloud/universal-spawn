# Safety model

The universal-spawn safety model is **declaration + enforcement**:

- The author publishes an envelope: `min_permissions`,
  `rate_limit_qps`, `cost_limit_usd_daily`, `env_vars_required`,
  `safe_for_auto_spawn`.
- The platform enforces it. A manifest that claims a permission it
  does not need is a documentation bug; a platform that grants a
  permission the manifest did not ask for is a security bug.

This document walks through the threat model that shapes those
choices.

## Threat T1 — Capability sneak

**Scenario.** A creation declares no `network:outbound` permission but
actually makes outbound calls once a user spawns it.

**Mitigation.** The platform denies all network traffic by default and
only opens the outbound sockets listed in `min_permissions`. An
undeclared call fails at the syscall / fetch boundary. The platform
MUST enforce this; "log and allow" is not a conformant implementation.

## Threat T2 — Cost runaway

**Scenario.** A creation makes so many model calls that the operator's
bill explodes.

**Mitigation.** `cost_limit_usd_daily` is a hard ceiling. The platform
tracks spend against the caller's account and halts spawning before
the ceiling is exceeded. Implementations SHOULD include a soft
warning threshold (e.g. 80%) before the hard cap.

## Threat T3 — Secret exfiltration

**Scenario.** A creation reads `ANTHROPIC_API_KEY` from its environment
and posts it to an attacker-controlled host.

**Mitigation.** Three layers:

1. Secrets are never stored in the manifest. They are supplied by the
   platform's credential store at spawn time.
2. Outbound network is locked to `min_permissions`. A manifest that
   declared `network:outbound:api.anthropic.com` cannot send a POST to
   `evil.example`.
3. The platform MAY redact known secret shapes from the creation's
   stdout/stderr and logs.

## Threat T4 — Drive-by spawn

**Scenario.** A user clicks a link and a creation runs with arbitrary
permissions before they can react.

**Mitigation.** `safe_for_auto_spawn` defaults to false. If it is
false or missing, the platform MUST require explicit human
confirmation on first spawn. Even when true, the platform MAY still
require confirmation — this is a floor, not a ceiling.

## Threat T5 — Supply-chain swap

**Scenario.** An attacker replaces the manifest at the upstream URL
with a malicious one while keeping the `id`.

**Mitigation.**

1. `source.commit` lets the author pin a specific hash.
2. `signatures[]` lets the author sign the canonical serialization of
   the manifest (spec Appendix C). Consumers with a key pin verify
   before spawning.
3. Platforms SHOULD log the manifest hash on every spawn so later
   audits can detect swaps.

## Threat T6 — Misleading declaration

**Scenario.** A manifest claims `rate_limit_qps: 1` but actually bursts
at 100 qps.

**Mitigation.** The platform enforces the rate, not the manifest. The
manifest is the creator's public promise; the platform is the
enforcer of that promise. A mis-declaring creation is subject to the
platform's abuse policy, the same as any other rate-abusing client.

## Threat T7 — Permission elevation via deps

**Scenario.** A creation's `min_permissions` are empty, but it depends
on another spawn manifest that claims broad permissions.

**Mitigation.** A spawn host resolving dependencies MUST union all
`min_permissions` from the transitive closure and present that
**union** to the user for consent. Silent inheritance is not allowed.

## Non-threats / out of scope

- **Bugs in the creation's own logic** — not the spec's concern.
  Conformant validation will not save you from shipping broken code.
- **Supply-chain compromise of the registry itself** — the spec does
  not define a registry. That is an implementation problem.
- **Social engineering at install time** — if a user clicks "Allow
  everything," the envelope collapses. The spec narrows the blast
  radius; it does not abolish trust decisions.

## Implementer checklist

A platform that says it implements universal-spawn v1.0.0 MUST:

- [ ] Validate every manifest against the core schema before any other
      processing.
- [ ] Refuse unknown major spec versions.
- [ ] Enforce `min_permissions` at the kernel / runtime boundary, not
      at the policy layer.
- [ ] Enforce `rate_limit_qps` and `cost_limit_usd_daily` as hard
      ceilings.
- [ ] Store values for `env_vars_required` in a credential store, not
      in the manifest.
- [ ] Require user confirmation when `safe_for_auto_spawn` is false
      or absent.
- [ ] Preserve unknown `x-ext.*` fields on round-trip.
- [ ] Log the canonical manifest hash on every spawn.

A platform that skips any of the above SHOULD NOT claim conformance.

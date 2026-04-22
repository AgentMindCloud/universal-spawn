# Security policy

## Reporting

Report suspected security issues in the universal-spawn specification,
schema, or platform extensions to:

- **Email**: `security@agentmindcloud.org`
- **GitHub**: use the "Report a vulnerability" button on the Security
  tab (private vulnerability reporting enabled).

Please include:

- a description of the issue and its impact,
- a minimal reproducer manifest if applicable,
- the spec version and platform extension id, if applicable,
- whether the issue is already public.

We aim to acknowledge reports within three business days and to publish
a fix within 30 days for critical issues.

Do **not** open a public issue for a vulnerability until we have
coordinated a release.

## Scope

Issues in scope:

- Schema acceptance flaws that let a malicious manifest claim more
  capability than it actually needs.
- Canonicalization or signing flaws (spec Appendix C) that allow two
  different manifests to produce the same signed hash, or that allow
  signature bypass.
- Prose / schema mismatches that cause conformant consumers to disagree
  on validity.
- Permission-vocabulary gaps that let real-world capabilities escape
  declaration (a kind of "capability sneak").
- Issues in platform extension schemas in this repository.

Issues out of scope:

- Vulnerabilities in specific tools or platforms that implement the
  standard. Report those to the vendor.
- Issues in a third-party manifest. Report those to its maintainer.
- Denial-of-service caused by very large manifests (platforms should
  impose size limits).

## Advisories

Advisories are published via GitHub Security Advisories on this
repository. Each advisory includes:

- Affected spec versions and platform extensions.
- A CVE if applicable.
- Mitigation steps for implementers.
- Whether a schema change is required, and in which spec version it
  lands.

## Keys

The Editor signs release tags with an ed25519 key. The current public
key fingerprint is published at
`https://universal-spawn.org/.well-known/keys.txt` (populated when the
domain is provisioned).

## Hardening guidance for implementers

If you are building a tool that consumes universal-spawn manifests:

1. **Validate before parsing application logic.** Reject anything that
   fails the JSON Schema.
2. **Refuse unknown major versions.** Do not try to "do your best".
3. **Enforce declared ceilings.** Rate-limit and cost-cap in code, not
   in policy.
4. **Isolate secrets.** Never store values for `env_vars_required`
   alongside the manifest in the same namespace.
5. **Sandbox at least to `min_permissions`.** If a creation requests
   `fs:write:/tmp/x`, prevent `fs:write:/etc`. Capability containment
   is the only real safety boundary.
6. **Require confirmation if `safe_for_auto_spawn` is absent or false.**
7. **Log the manifest hash.** Store the canonical SHA-256 so later
   audits can match what was actually spawned.

These map directly to the obligations in spec §6.

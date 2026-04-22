# Governance

universal-spawn is an open standard developed in public at
[`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn).
This document describes how decisions are made.

## Roles

### Editor

The Editor owns the direction and coherence of the specification.
There is exactly one Editor at any time. The current Editor is
**Jani Solo ([@JanSol0s](https://github.com/JanSol0s))**, appointed by
the AgentMindCloud organization.

Editor responsibilities:

- Approving or rejecting spec-proposal issues.
- Tagging spec releases (`spec-vX.Y.Z`).
- Resolving deadlocks between maintainers.
- Nominating new maintainers.
- Appointing a successor before stepping down.

### Maintainers

Maintainers triage issues, review PRs, and approve additive spec
changes. Every merged PR requires two maintainer approvals, one of
which may be the Editor.

Maintainers are listed in `MAINTAINERS.md` (TBD when the first external
maintainer is appointed). Until then, the Editor is the sole
maintainer.

### Contributors

Everyone who opens an issue or PR is a contributor. There is no formal
membership. Contributions are governed by
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Decision rules

| Decision                                 | Rule                                  |
|------------------------------------------|---------------------------------------|
| Typo, clarification                      | One maintainer approval.              |
| Additive spec change (minor version)     | Two maintainer approvals.             |
| Breaking spec change (major version)     | Editor + two maintainer approvals.    |
| New platform folder                      | Two maintainer approvals.             |
| Removing a platform folder               | Editor + two maintainer approvals.    |
| Governance change (this file)            | Editor + majority of maintainers.     |
| Changing the Editor                      | AgentMindCloud organization.          |

In all cases, the Editor may request additional review time (up to 14
days) for public comment before merging a spec change.

## Scope of the standard

The standard covers:

- The manifest schema.
- The canonical serialization for signing.
- The permission vocabulary.
- The platform-extension registration process.

The standard does not cover:

- How a platform implements spawning.
- How a registry stores manifests.
- How a UI presents a manifest to a user.
- Tooling (validators, generators, etc.).

Tooling MAY live in sibling repositories under the AgentMindCloud
organization but is not part of the standard.

## Conflicts of interest

Maintainers employed by a platform that is listed under
[`platforms/`](platforms) MUST recuse from votes on changes to that
platform's extension schema or its compatibility matrix row.

## Trademark

"universal-spawn" is used as a descriptive term for any implementation
of this standard. The "universal-spawn" name and the Residual
Frequencies plate marks are stewarded by AgentMindCloud to prevent
dilution; see [`TRADEMARK.md`](TRADEMARK.md) when that file is added.
For now, fair use of the name to describe conformant tools is
permitted; forks that rebrand the standard are not.

## Sunset

If AgentMindCloud can no longer maintain the standard, the Editor will
transfer the repository to a neutral foundation. Until such transfer,
this file remains authoritative.

# Partners

Platforms that have shipped a universal-spawn integration.

This page is a structured skeleton. Real entries land via the
`new_platform` issue template and a maintainer review.

## Partner tiers

| Tier | What's required | What's offered |
|---|---|---|
| **Listed** | Platform extension folder under `platforms/<subtree>/<id>/` plus a brief integration note here. | Listed in the README, recognised in the registry. |
| **Conformant** | Implements detection + validation + safety enforcement of the four `safety.*` fields. | Conformant badge in cards. |
| **Spawn-it** | Implements a one-click install URL derived from the manifest. | Spawn-it button in cards; cross-link from `ecosystem/<platform>-integration.md`. |

## Listed partners

_(skeleton — no entries yet)_

| Platform | Tier | Folder | Integration doc |
|---|---|---|---|
| _Your platform_ | _tier_ | `platforms/<subtree>/<id>/` | `ecosystem/<id>-integration.md` |

## How to become a partner

1. Open a [new platform issue](../.github/ISSUE_TEMPLATE/new_platform.yml).
2. Submit a PR adding `platforms/<subtree>/<id>/` per the contributing guide.
3. Submit `ecosystem/<id>-integration.md` describing detection +
   validation + honoring at your end.
4. Two maintainer approvals.

Maintainers do not gate by company size, traffic, or pricing tier.
The bar is technical: a working extension schema + at least two
validating examples + a clear integration note.

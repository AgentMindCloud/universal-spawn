# GitHub Actions perks — what this platform could offer

Wishlist for what a conformant GitHub Actions consumer SHOULD offer
to manifests that declare `platforms.github-actions`.

- **Priority discovery** — manifest-declaring entries rank above scraped or unlabelled ones in the platform's own directory.
- **One-click install/deploy** — a Deploy button on any universal-spawn registry card, pre-filled from the manifest.
- **Cost cap prefill** — `safety.cost_limit_usd_daily` pre-populates the daily spend cap UI.
- **Permission envelope prefill** — `safety.min_permissions` pre-populates the platform's permission dialog.
- **Audit trail** — canonical manifest SHA-256 logged on every spawn so authors can audit which manifest version ran.
- **Badges** — a manifest passing this platform's schema carries a conformance badge in its README.
- **Marketplace listing** — a manifest with `kind: reusable-action` and a valid `marketplace_category` is eligible for the Actions Marketplace listing workflow.

This file is a wishlist, not a vendor commitment.

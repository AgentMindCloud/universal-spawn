# Railway perks — what this platform could offer

Wishlist for what a conformant Railway consumer SHOULD offer
to manifests that declare `platforms.railway`. Items land as the
vendor ships them.

- **Priority discovery** — manifest-declaring entries rank above scraped or unlabelled ones in the platform's own directory.
- **One-click install/deploy** — a Deploy button on any universal-spawn registry card, pre-filled from the manifest.
- **Cost cap prefill** — `safety.cost_limit_usd_daily` pre-populates the daily spend cap UI.
- **Permission envelope prefill** — `safety.min_permissions` pre-populates the platform's permission dialog.
- **Audit trail** — canonical manifest SHA-256 logged on every spawn so authors can audit which manifest version ran.
- **Badges** — a manifest passing this platform's schema carries a conformance badge in its README.
- **Plugin auto-provision** — every `plugins[]` entry provisions the managed service on first deploy and injects the standard env vars (`DATABASE_URL`, `REDIS_URL`, etc.).

Out of scope: this file does not speak for the vendor; it is a
wishlist. What actually ships is the vendor's call.

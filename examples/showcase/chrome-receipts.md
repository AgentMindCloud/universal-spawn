# Showcase · `receipt-catcher` — a Chrome extension

**Use case.** A Chrome extension that catches receipts on three
named vendor sites and forwards them to the user's expense backend
over HTTPS. Listed on the Web Store; private organization deploy.

## The manifest

```yaml
version: "1.0"
name: Receipt Catcher
description: >
  Catches receipts on three named vendor sites and forwards them to
  the user's expense backend. Narrow host permissions, signed
  webhook delivery, listed on the Chrome Web Store.
type: extension
platforms:
  chrome-extension:
    manifest_version: 3
    permissions: [activeTab, storage, scripting, webRequest]
    host_permissions:
      - "https://vendor-a.example.com/*"
      - "https://vendor-b.example.com/*"
      - "https://vendor-c.example.com/*"
    service_worker: dist/background.js
    web_store_id: "abcdefghijklmnopabcdefghijklmnop"
    min_chrome_version: "120"
safety:
  min_permissions:
    - network:outbound:vendor-a.example.com
    - network:outbound:vendor-b.example.com
    - network:outbound:vendor-c.example.com
    - network:outbound:api.receipts.example
  safe_for_auto_spawn: false
env_vars_required:
  - { name: RECEIPTS_API_TOKEN, description: API token for the backend, secret: true }
deployment: { targets: [chrome-extension] }
metadata:
  license: proprietary
  id: com.receipts.catcher
  author: { name: Receipts Co., handle: receipts-co }
  source: { type: git, url: https://github.com/receipts-co/chrome-receipt-catcher }
```

## Platforms targeted, and why

- **`chrome-extension`** — the browser is where the receipts live.
  MV3 service worker + narrow host permissions keeps the install
  envelope small.

## How discovery happens

Discovered through the Web Store listing. The `universal-spawn.yaml`
lets the IT team's MDM tool validate the install envelope against
its own org policy before pushing the extension to laptops.

# Adobe — universal-spawn platform extension

Adobe's extension surfaces are CEP (the HTML-based legacy platform) and UXP (the modern React-style platform). The same universal-spawn manifest can target Photoshop, Illustrator, Premiere, XD, InDesign, and After Effects by naming `hosts[]`. Three distinct examples — XD, Photoshop, and Premiere — live in the same folder.

## What this platform cares about

The extension platform (`cep`, `uxp`), the Adobe host apps (`photoshop`, `illustrator`, `premiere`, `xd`, `indesign`, `after-effects`), the manifest file, and whether the extension ships via Creative Cloud's Adobe Exchange.

## Compatibility table

| Manifest field | Adobe behavior |
|---|---|
| `version` | Required. |
| `type` | `creative-tool`, `plugin`, `extension`. |
| `platforms.adobe` | Strict. |

### `platforms.adobe` fields

| Field | Purpose |
|---|---|
| `platforms.adobe.platform` | `cep` (HTML extensions) or `uxp` (modern). |
| `platforms.adobe.manifest_file` | Extension manifest file path. |
| `platforms.adobe.hosts` | Target host apps. |
| `platforms.adobe.min_host_version` | Minimum host version. |
| `platforms.adobe.adobe_exchange` | Exchange publication settings. |

See [`compatibility.md`](./compatibility.md) for more.

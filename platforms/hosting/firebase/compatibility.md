# Firebase compatibility — field-by-field

Firebase already has a native config format
(`firebase.json`). universal-spawn does not replace it; the two
coexist. A Firebase consumer reads both:

- `firebase.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.firebase`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `firebase.json` (provider-native)

```json
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"]
  },
  "functions": {
    "source": "functions",
    "runtime": "nodejs22"
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  },
  "storage": { "rules": "storage.rules" }
}
```

### `universal-spawn.yaml` (platforms.firebase block)

```yaml
platforms:
  firebase:
    project_id: your-firebase-project
    region: us-central1
    hosting:
      public_dir: dist
      ssr: false
    functions:
      source: functions
      runtime: nodejs22
    firestore:
      rules_file: firestore.rules
      indexes_file: firestore.indexes.json
    storage:
      rules_file: storage.rules
```

## Field-by-field

| universal-spawn v1.0 field | Firebase behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Firebase project slug suggestion. |
| `name, description` | Card. |
| `type` | `web-app`, `api-service`, `workflow`, `bot`, `site`. |
| `safety.min_permissions` | Informational. |
| `safety.cost_limit_usd_daily` | Advisory; Blaze plan budget alert honors it. |
| `env_vars_required` | Functions config + secrets. |
| `platforms.firebase.project_id` | Firebase project id. |
| `platforms.firebase.region` | Primary region. |
| `platforms.firebase.hosting` | Hosting configuration. |
| `platforms.firebase.functions` | Cloud Functions for Firebase. |
| `platforms.firebase.firestore` | Firestore rules + indexes. |
| `platforms.firebase.realtime_db` | Realtime Database rules. |
| `platforms.firebase.storage` | Storage rules + buckets. |
| `platforms.firebase.auth` | Auth providers. |
| `platforms.firebase.extensions` | Firebase Extensions. |

## DB provisioning as first-class

Firestore's `rules_file` and `indexes_file` are deployment artifacts — a consumer MUST apply them before marking the deploy healthy. Same for `realtime_db.rules_file` and `storage.rules_file`. Rules changes that deny existing queries block the deploy unless the consumer is told to force through via `safety.safe_for_auto_spawn: true`.

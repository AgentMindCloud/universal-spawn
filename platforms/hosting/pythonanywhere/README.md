# PythonAnywhere — universal-spawn platform extension

PythonAnywhere hosts Python web apps via WSGI, runs scheduled tasks, and ships managed MySQL + Postgres. There is no repo-level config file by convention — app settings live in the dashboard. The extension models that dashboard state declaratively so an installer can reproduce it.

## What this platform cares about

The Python version, WSGI entrypoint, virtualenv path, static file mappings, scheduled tasks, always-on tasks, and managed databases.

## What platform-specific extras unlock

`always_on_tasks[]` declares tasks that PythonAnywhere keeps running continuously. `static_mappings[]` routes URLs to directories.

## Compatibility table

| Manifest field | PythonAnywhere behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `api-service`, `cli-tool`, `workflow`. |
| `env_vars_required` | PythonAnywhere webapp env variables. |
| `deployment.targets` | Must include `pythonanywhere`. |
| `platforms.pythonanywhere` | Strict. |

### `platforms.pythonanywhere` fields

| Field | Purpose |
|---|---|
| `platforms.pythonanywhere.python_version` | Python major.minor. |
| `platforms.pythonanywhere.wsgi_file` | WSGI entrypoint path. |
| `platforms.pythonanywhere.virtualenv` | Virtualenv path. |
| `platforms.pythonanywhere.static_mappings` | URL → directory map. |
| `platforms.pythonanywhere.scheduled_tasks` | Scheduled tasks. |
| `platforms.pythonanywhere.always_on_tasks` | Always-on tasks. |
| `platforms.pythonanywhere.databases` | Managed databases. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `wsgi.py (plus dashboard-managed web apps)`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant PythonAnywhere consumer SHOULD offer manifests that
declare `platforms.pythonanywhere`.

# PythonAnywhere compatibility — field-by-field

PythonAnywhere already has a native config format
(`wsgi.py (plus dashboard-managed web apps)`). universal-spawn does not replace it; the two
coexist. A PythonAnywhere consumer reads both:

- `wsgi.py (plus dashboard-managed web apps)` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.pythonanywhere`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `wsgi.py (plus dashboard-managed web apps)` (provider-native)

```python
# /var/www/yourname_pythonanywhere_com_wsgi.py
import os, sys
path = '/home/yourname/app'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### `universal-spawn.yaml` (platforms.pythonanywhere block)

```yaml
platforms:
  pythonanywhere:
    python_version: "3.12"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/app
    static_mappings:
      - { url: /static/, path: /home/yourname/app/static }
```

## Field-by-field

| universal-spawn v1.0 field | PythonAnywhere behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Account.subdomain suggestion. |
| `name, description` | Dashboard card. |
| `type` | `web-app`, `api-service`, `cli-tool`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Webapp env. |
| `platforms.pythonanywhere.python_version` | Python major.minor. |
| `platforms.pythonanywhere.wsgi_file` | WSGI entrypoint path. |
| `platforms.pythonanywhere.virtualenv` | Virtualenv path. |
| `platforms.pythonanywhere.static_mappings` | URL → directory map. |
| `platforms.pythonanywhere.scheduled_tasks` | Scheduled tasks. |
| `platforms.pythonanywhere.always_on_tasks` | Always-on tasks. |
| `platforms.pythonanywhere.databases` | Managed databases. |

## Dashboard state as declarative

PythonAnywhere traditionally configures via the dashboard. A conformant consumer (or a community installer script) uses the declared fields to call the PythonAnywhere API and set the dashboard state to match the manifest.

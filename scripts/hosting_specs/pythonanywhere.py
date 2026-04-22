"""PythonAnywhere — Python-only hosting (WSGI + scheduled tasks + consoles)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "pythonanywhere",
    "title": "PythonAnywhere",
    "native_config_name": "wsgi.py (plus dashboard-managed web apps)",
    "native_config_lang": "python",

    "lede": (
        "PythonAnywhere hosts Python web apps via WSGI, runs scheduled "
        "tasks, and ships managed MySQL + Postgres. There is no repo-"
        "level config file by convention — app settings live in the "
        "dashboard. The extension models that dashboard state "
        "declaratively so an installer can reproduce it."
    ),
    "cares": (
        "The Python version, WSGI entrypoint, virtualenv path, static "
        "file mappings, scheduled tasks, always-on tasks, and managed "
        "databases."
    ),
    "extras": (
        "`always_on_tasks[]` declares tasks that PythonAnywhere keeps "
        "running continuously. `static_mappings[]` routes URLs to "
        "directories."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `cli-tool`, `workflow`."),
        ("env_vars_required", "PythonAnywhere webapp env variables."),
        ("deployment.targets", "Must include `pythonanywhere`."),
        ("platforms.pythonanywhere", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Account.subdomain suggestion."),
        ("name, description", "Dashboard card."),
        ("type", "`web-app`, `api-service`, `cli-tool`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Webapp env."),
        ("platforms.pythonanywhere.python_version", "Python major.minor."),
        ("platforms.pythonanywhere.wsgi_file", "WSGI entrypoint path."),
        ("platforms.pythonanywhere.virtualenv", "Virtualenv path."),
        ("platforms.pythonanywhere.static_mappings", "URL → directory map."),
        ("platforms.pythonanywhere.scheduled_tasks", "Scheduled tasks."),
        ("platforms.pythonanywhere.always_on_tasks", "Always-on tasks."),
        ("platforms.pythonanywhere.databases", "Managed databases."),
    ],
    "platform_fields": {
        "python_version": "Python major.minor.",
        "wsgi_file": "WSGI entrypoint path.",
        "virtualenv": "Virtualenv path.",
        "static_mappings": "URL → directory map.",
        "scheduled_tasks": "Scheduled tasks.",
        "always_on_tasks": "Always-on tasks.",
        "databases": "Managed databases.",
    },

    "schema_body": schema_object(
        required=["python_version", "wsgi_file"],
        properties={
            "python_version": str_prop(pattern=r"^3\.(1[0-4])$"),
            "wsgi_file": str_prop(),
            "virtualenv": str_prop(),
            "static_mappings": {
                "type": "array",
                "items": schema_object(
                    required=["url", "path"],
                    properties={
                        "url": str_prop(),
                        "path": str_prop(),
                    },
                ),
            },
            "scheduled_tasks": {
                "type": "array",
                "items": schema_object(
                    required=["command", "hour", "minute"],
                    properties={
                        "command": str_prop(),
                        "hour": {"type": "integer", "minimum": 0, "maximum": 23},
                        "minute": {"type": "integer", "minimum": 0, "maximum": 59},
                    },
                ),
            },
            "always_on_tasks": {
                "type": "array",
                "items": schema_object(
                    required=["command"],
                    properties={"command": str_prop()},
                ),
            },
            "databases": {
                "type": "array",
                "items": schema_object(
                    required=["engine", "name"],
                    properties={
                        "engine": enum(["mysql", "postgres"]),
                        "name": str_prop(),
                    },
                ),
            },
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: PythonAnywhere Template
type: web-app
description: Template for a PythonAnywhere-targeted universal-spawn manifest.

platforms:
  pythonanywhere:
    python_version: \"3.12\"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/app
    static_mappings:
      - { url: /static/, path: /home/yourname/app/static }
    scheduled_tasks:
      - { command: \"python /home/yourname/app/jobs/nightly.py\", hour: 3, minute: 0 }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DJANGO_SECRET_KEY
    description: Django SECRET_KEY.
    secret: true

deployment:
  targets: [pythonanywhere]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/pythonanywhere-template }
""",

    "native_config": """
# /var/www/yourname_pythonanywhere_com_wsgi.py
import os, sys
path = '/home/yourname/app'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
""",

    "universal_excerpt": """
platforms:
  pythonanywhere:
    python_version: \"3.12\"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/app
    static_mappings:
      - { url: /static/, path: /home/yourname/app/static }
""",

    "compatibility_extras": (
        "## Dashboard state as declarative\n\n"
        "PythonAnywhere traditionally configures via the dashboard. "
        "A conformant consumer (or a community installer script) uses "
        "the declared fields to call the PythonAnywhere API and set "
        "the dashboard state to match the manifest."
    ),

    "deploy_button": {
        "markdown": "[![Try on PythonAnywhere](https://img.shields.io/badge/Try%20on-PythonAnywhere-blue)](https://www.pythonanywhere.com/signup/?plan=free)",
        "html": (
            '<a href="https://www.pythonanywhere.com/signup/?plan=free">\n'
            '  <img src="https://img.shields.io/badge/Try%20on-PythonAnywhere-blue" alt="Try on PythonAnywhere" />\n'
            '</a>'
        ),
        "params_doc": "PythonAnywhere has no native Deploy button. The badge above links to signup; the install itself runs via the community bash helper, which reads this manifest.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: PA Static Assets
type: site
summary: Serve a static site via PythonAnywhere's static mappings.
description: WSGI returns 404 for non-static paths; static mappings serve everything else.

platforms:
  pythonanywhere:
    python_version: \"3.12\"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/static
    static_mappings:
      - { url: /, path: /home/yourname/site/public }

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [pythonanywhere]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/pa-static }
  id: com.static-co.pa-static
""",
        "serverless-api": """
version: \"1.0\"
name: PA Flask API
type: api-service
summary: Flask API on PythonAnywhere with a nightly scheduled task.
description: Flask WSGI app, one scheduled task that rolls over logs.

platforms:
  pythonanywhere:
    python_version: \"3.12\"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/api
    static_mappings:
      - { url: /static/, path: /home/yourname/api/static }
    scheduled_tasks:
      - { command: \"python /home/yourname/api/jobs/rotate_logs.py\", hour: 3, minute: 30 }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: FLASK_SECRET_KEY
    description: Flask session secret.
    secret: true

deployment:
  targets: [pythonanywhere]

metadata:
  license: MIT
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/pa-flask-api }
  id: com.api-co.pa-flask-api
""",
        "full-stack-app": """
version: \"1.0\"
name: PA Django Full Stack
type: web-app
summary: Django app on PythonAnywhere with managed MySQL, always-on worker, and scheduled jobs.
description: >
  Django webapp, a managed MySQL database, an always-on Celery worker,
  and two scheduled tasks (nightly email + weekly cleanup). Typical
  PythonAnywhere production shape.

platforms:
  pythonanywhere:
    python_version: \"3.12\"
    wsgi_file: /var/www/yourname_pythonanywhere_com_wsgi.py
    virtualenv: /home/yourname/.virtualenvs/django
    static_mappings:
      - { url: /static/, path: /home/yourname/app/static }
      - { url: /media/,  path: /home/yourname/app/media }
    scheduled_tasks:
      - { command: \"python /home/yourname/app/manage.py send_nightly_emails\", hour: 4, minute: 0 }
      - { command: \"python /home/yourname/app/manage.py cleanup_stale_sessions\", hour: 5, minute: 0 }
    always_on_tasks:
      - { command: \"celery -A app worker -l info\" }
    databases:
      - { engine: mysql, name: yourname$app }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 2
  safe_for_auto_spawn: false

env_vars_required:
  - name: DJANGO_SECRET_KEY
    description: Django SECRET_KEY.
    secret: true
  - name: MYSQL_PASSWORD
    description: Managed MySQL password.
    secret: true

deployment:
  targets: [pythonanywhere]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/pa-django-full-stack }
  id: com.stack-co.pa-django-full-stack
""",
    },
}

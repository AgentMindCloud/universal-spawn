"""Jupyter — local notebook project + JupyterLab extensions."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "jupyter",
    "title": "Jupyter",
    "lede": (
        "Jupyter notebooks ship as `.ipynb` files plus a `requirements.txt` "
        "or `pyproject.toml`. JupyterLab also has an extension ecosystem. "
        "A universal-spawn manifest covers a notebook project or a "
        "JupyterLab extension via `kind`."
    ),
    "cares": (
        "The `kind` (`notebook-project`, `lab-extension`), the entry "
        "notebook, the requirements file, and the kernel name."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`notebook`, `library`, `extension`."),
        ("platforms.jupyter", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.jupyter.kind", "`notebook-project` or `lab-extension`."),
        ("platforms.jupyter.entry_notebook", "Entry .ipynb path."),
        ("platforms.jupyter.requirements", "Requirements file."),
        ("platforms.jupyter.kernel", "Kernel name."),
        ("platforms.jupyter.lab_extension_id", "JupyterLab extension id."),
    ],
    "platform_fields": {
        "kind": "`notebook-project` or `lab-extension`.",
        "entry_notebook": "Entry .ipynb.",
        "requirements": "Requirements file.",
        "kernel": "Kernel name.",
        "lab_extension_id": "JupyterLab extension id.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["notebook-project", "lab-extension"]),
            "entry_notebook": str_prop(),
            "requirements": str_prop(),
            "kernel": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "lab_extension_id": str_prop(pattern=r"^@[a-z0-9-][a-z0-9_.-]*/[a-z0-9-][a-z0-9_.-]*$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Jupyter Template
type: notebook
description: Template for a Jupyter-targeted universal-spawn manifest.

platforms:
  jupyter:
    kind: notebook-project
    entry_notebook: notebooks/index.ipynb
    requirements: requirements.txt
    kernel: python3

safety:
  min_permissions: [fs:read]

env_vars_required: []

deployment:
  targets: [jupyter]

metadata:
  license: BSD-3-Clause
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/jupyter-template }
""",
    "native_config_name": "*.ipynb + requirements.txt / pyproject.toml",
    "native_config_lang": "text",
    "native_config": "# A Jupyter project's source of truth is the .ipynb files plus the package config used to install the kernel.\n",
    "universal_excerpt": """
platforms:
  jupyter:
    kind: notebook-project
    entry_notebook: notebooks/index.ipynb
    requirements: requirements.txt
    kernel: python3
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate EDA Project
type: notebook
summary: Minimal Jupyter notebook project for parchment-plate EDA.
description: One entry notebook + requirements.txt; default Python 3 kernel.

platforms:
  jupyter:
    kind: notebook-project
    entry_notebook: notebooks/eda.ipynb
    requirements: requirements.txt
    kernel: python3

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [jupyter]

visuals: { palette: parchment }

metadata:
  license: BSD-3-Clause
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/jupyter-plate-eda }
  id: com.plate-studio.jupyter-plate-eda
""",
        "example-2": """
version: "1.0"
name: Parchment Lab Extension
type: extension
summary: Full JupyterLab extension recoloring the lab UI to the parchment palette.
description: Lab extension installed via pip; lights up the Residual Frequencies palette.

platforms:
  jupyter:
    kind: lab-extension
    lab_extension_id: "@plate-studio/jupyterlab-parchment-theme"

safety:
  min_permissions: [fs:read]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [jupyter]

visuals: { palette: parchment }

metadata:
  license: BSD-3-Clause
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/jupyterlab-parchment-theme }
  id: com.plate-studio.jupyterlab-parchment-theme
""",
    },
}

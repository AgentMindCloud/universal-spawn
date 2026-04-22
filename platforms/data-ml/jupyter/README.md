# Jupyter — universal-spawn platform extension

Jupyter notebooks ship as `.ipynb` files plus a `requirements.txt` or `pyproject.toml`. JupyterLab also has an extension ecosystem. A universal-spawn manifest covers a notebook project or a JupyterLab extension via `kind`.

## What this platform cares about

The `kind` (`notebook-project`, `lab-extension`), the entry notebook, the requirements file, and the kernel name.

## Compatibility table

| Manifest field | Jupyter behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `library`, `extension`. |
| `platforms.jupyter` | Strict. |

### `platforms.jupyter` fields

| Field | Purpose |
|---|---|
| `platforms.jupyter.kind` | `notebook-project` or `lab-extension`. |
| `platforms.jupyter.entry_notebook` | Entry .ipynb. |
| `platforms.jupyter.requirements` | Requirements file. |
| `platforms.jupyter.kernel` | Kernel name. |
| `platforms.jupyter.lab_extension_id` | JupyterLab extension id. |

See [`compatibility.md`](./compatibility.md) for more.

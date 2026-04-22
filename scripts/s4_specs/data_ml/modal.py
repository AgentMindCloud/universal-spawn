"""Modal — serverless Python with `modal run`."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "modal",
    "title": "Modal",
    "lede": (
        "Modal runs Python functions and apps as serverless workloads. "
        "A universal-spawn manifest pins the entry app file, the GPU "
        "type if any, the image kind, and any persistent volumes."
    ),
    "cares": (
        "The entry file, the App name, the GPU class, the image "
        "(prebuilt vs custom), and persistent volumes."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `web-app`, `api-service`, `library`."),
        ("platforms.modal", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.modal.entry_file", "Modal app entry file."),
        ("platforms.modal.app_name", "Modal App name."),
        ("platforms.modal.gpu", "GPU class (if any)."),
        ("platforms.modal.image_kind", "`debian-slim`, `from-registry`, `dockerfile`."),
        ("platforms.modal.volumes", "Persistent volume names."),
        ("platforms.modal.secrets", "Modal Secret names."),
    ],
    "platform_fields": {
        "entry_file": "Modal app entry file.",
        "app_name": "Modal App name.",
        "gpu": "GPU class.",
        "image_kind": "Image kind.",
        "volumes": "Persistent volume names.",
        "secrets": "Modal Secret names.",
    },
    "schema_body": schema_object(
        required=["entry_file", "app_name"],
        properties={
            "entry_file": str_prop(),
            "app_name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            "gpu": enum(["none", "T4", "L4", "A10G", "A100", "A100-80GB", "H100", "H200", "B200"]),
            "image_kind": enum(["debian-slim", "from-registry", "dockerfile"]),
            "volumes": {"type": "array", "items": str_prop()},
            "secrets": {"type": "array", "items": str_prop()},
        },
    ),
    "template_yaml": """
version: "1.0"
name: Modal Template
type: workflow
description: Template for a Modal-targeted universal-spawn manifest.

platforms:
  modal:
    entry_file: app.py
    app_name: your-app
    gpu: none
    image_kind: debian-slim

safety:
  min_permissions: [network:outbound:api.modal.com]

env_vars_required:
  - name: MODAL_TOKEN_ID
    description: Modal token id.
    secret: true
  - name: MODAL_TOKEN_SECRET
    description: Modal token secret.
    secret: true

deployment:
  targets: [modal]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/modal-template }
""",
    "native_config_name": "modal app.py + modal CLI",
    "native_config_lang": "python",
    "native_config": """
import modal
app = modal.App("your-app")
@app.function()
def hello():
    return "ok"
""",
    "universal_excerpt": """
platforms:
  modal:
    entry_file: app.py
    app_name: your-app
    gpu: none
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Modal Job
type: workflow
summary: Minimal Modal app running a daily plate-rollup function.
description: CPU-only debian-slim image. One scheduled function.

platforms:
  modal:
    entry_file: rollup.py
    app_name: plate-rollup
    gpu: none
    image_kind: debian-slim

safety:
  min_permissions: [network:outbound:api.modal.com, network:outbound:api.plate.example]
  safe_for_auto_spawn: false

env_vars_required:
  - name: MODAL_TOKEN_ID
    description: Modal token id.
    secret: true
  - name: MODAL_TOKEN_SECRET
    description: Modal token secret.
    secret: true

deployment:
  targets: [modal]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/modal-plate-rollup }
  id: com.plate-studio.modal-plate-rollup
""",
        "example-2": """
version: "1.0"
name: Plate Diffusion Worker
type: workflow
summary: Full Modal GPU worker generating plates with a diffusion model.
description: A100 GPU, custom Dockerfile image, attached persistent volume for the model weights.

platforms:
  modal:
    entry_file: worker.py
    app_name: plate-diffusion
    gpu: A100
    image_kind: dockerfile
    volumes: [model-weights]
    secrets: [hf-token]

safety:
  min_permissions: [network:outbound:api.modal.com, network:outbound:huggingface.co, gpu:compute]
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: MODAL_TOKEN_ID
    description: Modal token id.
    secret: true
  - name: MODAL_TOKEN_SECRET
    description: Modal token secret.
    secret: true
  - name: HF_TOKEN
    description: HF token for the model weights.
    secret: true

deployment:
  targets: [modal]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/modal-plate-diffusion }
  id: com.plate-studio.modal-plate-diffusion
""",
    },
}

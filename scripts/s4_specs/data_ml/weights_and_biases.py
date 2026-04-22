"""Weights & Biases — experiment tracker + sweeps."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "weights-and-biases",
    "title": "Weights & Biases",
    "lede": (
        "W&B tracks experiments, runs hyperparameter sweeps, and "
        "stores artifacts. A universal-spawn manifest declares the "
        "entity / project, the optional sweep config, and the "
        "artifact registry."
    ),
    "cares": (
        "The entity, project, sweep config path, artifact registry, "
        "and whether runs are public."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `library`, `notebook`."),
        ("platforms.weights-and-biases", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.weights-and-biases.entity", "W&B entity."),
        ("platforms.weights-and-biases.project", "W&B project."),
        ("platforms.weights-and-biases.sweep_file", "Sweep config YAML path."),
        ("platforms.weights-and-biases.artifact_registry", "Artifact registry name."),
        ("platforms.weights-and-biases.visibility", "`public` or `private`."),
    ],
    "platform_fields": {
        "entity": "W&B entity.",
        "project": "W&B project.",
        "sweep_file": "Sweep YAML.",
        "artifact_registry": "Artifact registry.",
        "visibility": "`public` or `private`.",
    },
    "schema_body": schema_object(
        required=["entity", "project"],
        properties={
            "entity": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "project": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
            "sweep_file": str_prop(),
            "artifact_registry": str_prop(),
            "visibility": enum(["public", "private"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: W&B Template
type: workflow
description: Template for a W&B-targeted universal-spawn manifest.

platforms:
  weights-and-biases:
    entity: your-entity
    project: your-project
    visibility: private

safety:
  min_permissions: [network:outbound:api.wandb.ai]

env_vars_required:
  - name: WANDB_API_KEY
    description: W&B API key.
    secret: true

deployment:
  targets: [weights-and-biases]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/wandb-template }
""",
    "native_config_name": "wandb/config.yaml + sweep.yaml",
    "native_config_lang": "yaml",
    "native_config": """
program: train.py
method: bayes
metric: { name: val_loss, goal: minimize }
parameters:
  learning_rate:
    min: 0.0001
    max: 0.1
""",
    "universal_excerpt": """
platforms:
  weights-and-biases:
    entity: your-entity
    project: your-project
    sweep_file: sweep.yaml
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Classifier WandB
type: workflow
summary: Minimal W&B project tracking parchment-classifier runs.
description: Private project, no sweeps.

platforms:
  weights-and-biases:
    entity: plate-studio
    project: parchment-classifier
    visibility: private

safety:
  min_permissions: [network:outbound:api.wandb.ai]
  safe_for_auto_spawn: false

env_vars_required:
  - name: WANDB_API_KEY
    description: W&B API key.
    secret: true

deployment:
  targets: [weights-and-biases]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/wandb-plate-classifier }
  id: com.plate-studio.wandb-plate-classifier
""",
        "example-2": """
version: "1.0"
name: Bayes Sweep
type: workflow
summary: Full W&B Bayesian sweep + artifact-registry deployment.
description: Public project with a Bayes sweep over learning rate + dropout, artifacts registered to a model registry.

platforms:
  weights-and-biases:
    entity: plate-studio
    project: parchment-sweep
    sweep_file: sweep.yaml
    artifact_registry: parchment-models
    visibility: public

safety:
  min_permissions: [network:outbound:api.wandb.ai]
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false

env_vars_required:
  - name: WANDB_API_KEY
    description: W&B API key.
    secret: true

deployment:
  targets: [weights-and-biases]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/wandb-bayes-sweep }
  id: com.plate-studio.wandb-bayes-sweep
""",
    },
}

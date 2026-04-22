# `platforms/data-ml/` — data science & ML environments

Registry of "spin up a runnable environment" platforms: notebook
hosts, ML experiment trackers, and model-hosting surfaces. Each
manifest tells a consumer **how to materialise a running environment
this creation expects** — a HF Space, a Kaggle notebook, a Colab
link, a Modal app.

## Capability matrix (11 platforms)

| Id | Native config | Shape |
|---|---|---|
| [huggingface-spaces](./huggingface-spaces) | `README.md` front-matter + `app.py` | Gradio / Streamlit / Docker / static Space |
| [kaggle](./kaggle)                         | `kernel-metadata.json`              | notebook + dataset |
| [google-colab](./google-colab)             | Drive-hosted `.ipynb`               | runnable notebook |
| [observable](./observable)                 | Observable notebook ref             | notebook + framework page |
| [weights-and-biases](./weights-and-biases) | `wandb/config.yaml` + `sweep.yaml`  | experiment tracker + sweeps |
| [replicate](./replicate)                   | `cog.yaml`                          | model hosting (cross-link to AI) |
| [jupyter](./jupyter)                       | `requirements.txt` + `.ipynb`       | local notebook project |
| [modal](./modal)                           | `modal run app.py`                  | serverless Python functions / apps |
| [anyscale](./anyscale)                     | `service.yaml`                      | Ray Serve / Ray Data workloads |
| [paperspace](./paperspace)                 | Gradient + Machines                 | notebooks, deployments, VMs |
| [lightning-ai](./lightning-ai)             | Lightning Studio                    | cloud studio environment |

## Cross-links

- **Replicate** is shared with `platforms/ai/replicate/`. The AI-track
  folder describes the *inference* surface; this data-ml folder
  describes the *training / notebook / research* ergonomics on top of
  the same Cog format. Fields like `cog_file` and `training.*` live
  here; `model` + `version` live on the AI side. See
  [`replicate/README.md`](./replicate) for the relative-path link.
- **HuggingFace Spaces** here complements `platforms/ai/huggingface/`
  (models + datasets). Manifests that only ship a Space target
  `data-ml/huggingface-spaces`; manifests that ship a model repo
  target `ai/huggingface`.

## Emphasis

Every example in this subtree answers the question:
"what exactly runs when a user clicks 'Open in …' ?"

# Showcase · `plate-archetype` — a Hugging Face Space

**Use case.** A Gradio Space that classifies an image as one of the
six Residual Frequencies plate archetypes (A–F). Free zero-GPU tier;
public visibility.

## The manifest

```yaml
version: "1.0"
name: Plate Archetype Classifier
description: >
  Gradio Space that classifies an uploaded image as one of the six
  Residual Frequencies plate archetypes (A–F). Free zero-GPU tier.
type: web-app
platforms:
  huggingface-spaces:
    sdk: gradio
    visibility: public
    hardware: zero-gpu
    front_matter: { title: Plate Archetype, license: apache-2.0, pinned: false }
safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true
env_vars_required:
  - { name: HF_TOKEN, description: HF token used to publish the Space, secret: true }
deployment: { targets: [huggingface-spaces] }
visuals: { palette: parchment }
metadata:
  license: Apache-2.0
  id: com.plate-studio.archetype-space
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/hf-archetype-space }
  categories: [ai, graphics]
```

## Platforms targeted, and why

- **`huggingface-spaces`** — the runtime + the publication channel.
  Zero-GPU tier is enough for a small ViT classifier.

## How discovery happens

The HF Space card itself is found via HF's search. The
`universal-spawn.yaml` in the linked repo lets non-HF surfaces (a
universal-spawn registry, a Discord bot's inline preview) embed the
Space without having to scrape HF's HTML.

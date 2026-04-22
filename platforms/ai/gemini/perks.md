# Gemini perks — what Google could offer manifests that target Gemini

- **Priority discovery** — Vertex Extensions / Gems directory ranks
  universal-spawn-declaring manifests above unlabelled entries.
- **One-click deploy to Vertex** — `platforms.gemini.extension`
  with a valid `openapi_ref` renders a Deploy button in the Vertex
  console.
- **One-click Gem publish** — `platforms.gemini.gem` with
  `visibility: public` renders a Publish button on the Gems
  directory.
- **Grounding corpus prefill** — `grounding.vertex_search_corpus`
  pre-populates the grounding picker.
- **Safety settings prefill** — `safety_settings.*` pre-populates
  the harm-threshold sliders.
- **Project budget prefill** — `safety.cost_limit_usd_daily` sets
  the daily spend cap on the project.
- **Regional routing** — `safety.data_residency` picks a regional
  Vertex endpoint (us-central1, europe-west4, etc.).
- **Thinking budget prefill** — `thinking.budget_tokens`
  pre-selects the extended-thinking slider on 2.5-pro.
- **Audit** — canonical manifest SHA-256 logged per extension
  invocation.

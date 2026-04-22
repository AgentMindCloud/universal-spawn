"""Batch specs for platforms/ai/ folders.

Each batch module exposes a module-level `SPECS: list[dict]` where each
dict is a platform specification consumed by scripts/gen_ai_platform.py.

Layout:

    batch_a_providers.py   — 5 inference providers
                             (llama, mistral, groq-cloud, cohere, ai21)
    batch_b_hosts.py       — 4 inference hosts
                             (perplexity, together-ai, fireworks, replicate)
    batch_c_hubs.py        — 2 hub-shape platforms
                             (huggingface, anthropic-mcp)
    batch_d_agents1.py     — 4 multi-agent frameworks
                             (langchain, crewai, autogen, langgraph)
    batch_e_agents2.py     — 4 multi-agent frameworks
                             (semantic-kernel, litellm, mastra, vercel-ai-sdk)
    batch_f_coding.py      — 6 coding agents
                             (cursor, windsurf, aider, continue, cline, claude-code)
    batch_g_local.py       — 4 local runtimes
                             (ollama, lm-studio, llamacpp, vllm)

Batches are independent; editing one does not force re-reading the
others. The build driver imports every module and runs the generator
over the combined list.
"""

---
concept: Odysseus PewDiePie self-hosted workspace
tags: [koo-project, odysseus, self-hosted, ollama, ai-tools]
source: ChatGPT convs
---

# Odysseus — PewDiePie's Self-Hosted AI Workspace

## Insight
Odysseus is an open-source, self-hosted AI workspace created by Felix Kjellberg (PewDiePie). Think of it as a private alternative to ChatGPT/Claude that you run on your own hardware, with support for local models, AI agents, document editing, research workflows, and more. Currently more like software you install and host yourself on a computer (Windows/Mac/Linux, Docker installed, some setup through the terminal, optionally a local AI model such as Ollama) — not a normal app from an App Store. After installation it runs through a web browser on your machine.

Architecture: `opencode · MCP · web · files · shell · skills · memory`, with **llmfit** as the VRAM-aware LLM layer (GGUF/FP8/AWQ, vLLM/llama.cpp) and **@playwright/mcp** for browser MCP. Can connect to local models (Ollama, llama.cpp, vLLM) or cloud APIs like OpenAI and OpenRouter.

Common setup pattern: install Odysseus on your laptop/desktop → open it in a browser on the laptop → optionally access the same workspace from your phone through a browser if you configure remote access. Phone access via browser over LAN, or via Tailscale / Cloudflare Tunnel for secure remote access. Phone is for accessing, not hosting.

**The tradeoff:** ownership of the stack rather than renting access to someone else's AI — but you become your own IT department. The benefit for Ilham isn't privacy; it's that building/operating local models, agent workflows, retrieval systems, self-hosting, and AI operations are marketable skills. If the only goal was "best possible resume," ChatGPT or Claude directly. If the goal is "become the kind of person who can build and operate AI workflows," the Odysseus route makes sense.

## Context
First researched 2026-06-10 (Pewd Odysseus Overview). Ilham asked "what is pewd odysseus? Can I use it on my phone and laptop?" Same convo later expanded into a deep dive on Mads Lorentzen vs Odysseus for job-application automation.

## Related
- [[mads-lorentzen-vs-odysseus-job-pipeline]]
- [[chatgpt-vs-claude-vs-local-ai-verdict]]
- [[agency-of-one-job-search-reframe]]
- [[resume-gpt-custom-instructions-workflow]]
- [[koo-project-highlights]]

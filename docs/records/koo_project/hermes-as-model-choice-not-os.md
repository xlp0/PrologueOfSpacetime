---
concept: Hermes as model choice not OS
tags: [koo-project, hermes, ai-tools, model-selection]
source: ChatGPT convs
---

# Hermes as Model Choice, Not OS

## Insight
Hermes is a **model choice**, not an operating system. For Ilham's use case (repos, notes, transcripts), **OpenCode + GLM + Obsidian** is the strategically useful center; Hermes is optional garnish. "Don't spend time figuring out Hermes agent — focus on OpenCode + GLM + Obsidian first."

Hermes is a tuned version of a base model that is often better at: following instructions, acting like an autonomous assistant, using tools in a structured way, handling multi-step workflows without getting confused every 3 minutes. But Hermes by itself is **not** the whole system. To make it useful, you need to wrap it in: a system prompt/role, tool access (read files, search notes, shell commands), memory/context source (Obsidian vault, markdown notes, SQLite/vector DB), and a loop (plan → act → inspect results → continue). Without that, Hermes is just another LLM sitting in a chair — "a smart guy locked in a white room with no access to your stuff."

For Ilham's actual bottleneck — building a system that can ingest tools/ideas, store them cleanly, retrieve them later, synthesize them into decisions, help understand repos fast — that screams **workflow architecture, not model shopping**. The system around the model matters more than the mascot. Build around OpenCode + knowledge files + workflows, and Hermes becomes one possible worker you can slot in. **Hermes as foundation = wrong hierarchy.** Hermes as possible backend model = right hierarchy.

For 3D modelling specifically (where Ilham had heard Hermes was "good"), Hermes is not a magical text-to-3D system. It's a *good foreman* — good at writing Blender Python scripts, editing parametric model code, generating procedural geometry instructions, reading a 3D repo to figure out the pipeline. Not the construction site itself. For 3D: Hermes-as-foreman writing Blender scripts beats magical text-to-3D framing. For everything else Ilham cares about: OpenCode + GLM first.

## Context
Came up 2026-06-26 (Using Hermes Agent). Ilham had heard Hermes was "good at 3D modelling" and asked how to use it. The convo also reaffirmed the 3-layer stack (Obsidian / skills / model) as the right hierarchy.

## Related
- [[second-brain-three-layer-architecture]]
- [[opencode-vs-claude-code-vs-pi-agent]]
- [[chatgpt-vs-claude-vs-local-ai-verdict]]
- [[koo-project-highlights]]
- **Hermes Agent update**
- **Hermes Agent Explained**
- **OpenClaw vs Hermes**

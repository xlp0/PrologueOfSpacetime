---
concept: Second brain three-layer architecture
tags: [koo-project, second-brain, obsidian, skills, architecture]
source: ChatGPT convs
---

# Second-Brain Three-Layer Architecture

## Insight
The canonical architecture that resolved weeks of confusion about "Obsidian vs skills files vs model": three layers, each with a different job.

**(1) Obsidian / markdown = long-term human-readable knowledge (memory palace).** Store summaries, tool notes, architecture notes, implementation ideas, comparisons, decisions. The library. The place where you think.

**(2) Skills files = reusable machine instructions / behavior / procedure.** "When user gives transcript: 1) summarize 2) extract tool name 3) create source note 4) update relevant master note 5) suggest backlinks." Not knowledge — *behavior*. Doctrine. The agent's playbook for acting on knowledge.

**(3) Any model (Hermes / GLM / Claude / GPT / Qwen / DeepSeek) = worker** that reads the repo/notes/docs and executes the workflow. The interchangeable part. The system around it matters more than the mascot.

Mental model: **"Obsidian is the library. OpenCode is the researcher inside the library. If the library is a warehouse with books thrown on the floor, your researcher is going to look stupid."** A giant vault becomes noise; LLMs don't magically become wise because you dumped 200 markdown files into the basement.

The four valuable things OpenCode can do once it has vault access: (1) answer questions from notes ("what do my notes say about MCP servers?"); (2) update master notes ("read these 3 transcripts and update `Tools/OpenCode.md`"); (3) compare across sources ("compare Claude Code vs OpenCode for my workflow"); (4) turn knowledge into execution ("make me a skill file from all notes related to transcript summarization"). Simple file access is enough on day 1; frontmatter, consistent templates, tags, master notes, optionally embeddings/vector search or SQLite index come later.

## Context
Crystallized 2026-06-26 (Obsidian vs Skills Files + Using Hermes Agent convo). Ilham had asked: "I can paste transcripts somewhere, get a comprehensive summary, store in obsidian and connect that to opencode right? Or better to make skills files?" Answer: not either/or — both, for different jobs.

## Related
- [[obsidian-vs-sqlite-memory-split]]
- [[one-master-note-per-tool-principle]]
- [[think-pipeline-not-plugin]]
- [[hermes-as-model-choice-not-os]]
- [[koo-project-highlights]]
- **AI Second Brain**
- **Obsidian + Claude Cowork**
- **Claude Skill Token Costs**
- [[sessions/vault/2026-06-27-mem0-convo-summary-skill-wired|mem0 + convo-summary skill]]

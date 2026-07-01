---
concept: One master note per tool principle
tags: [koo-project, second-brain, obsidian, principle]
source: ChatGPT convs
---

# One Master Note per Tool Principle

## Insight
**Maintain ONE canonical master note per tool.** Video summaries are evidence/source notes; the tool master note is distilled truth. Don't keep 7 scattered notes all explaining OpenCode — that's weak.

The division of labor: each video gets its own summary note (e.g. `Summaries/Video-01-OpenCode-setup.md`), then you maintain **one master note per tool** (e.g. `Tools/OpenCode.md`, `Tools/ClaudeCode.md`, `Tools/GeminiCLI.md`). When a new video or transcript comes in, the workflow is: agent uses a skill (`summarize_transcript`, `extract_tool_knowledge`, `create_obsidian_note`) → output becomes an Obsidian note in `/Summaries/` **and updates** the master `/Tools/<ToolName>.md`. The master note is the distilled truth; the source notes are evidence.

Master tool-note template: What it is / What problem it solves / How it fits my stack / Strengths / Weaknesses / Setup difficulty / Use cases for me / Overlap with existing tools / Final verdict. Repo-note template: What the repo does / Main architecture / Important files / Entry points / Dependencies / Key abstractions / Questions / Whether I should actually use it.

Recommended vault structure:
```
/AI-Knowledge/{Tools, Workflows, Summaries, Concepts}
/.opencode/skills/
```
With `/Sources` for raw transcripts/notes/copied docs, `/Summaries` for one note per video/article/doc, `/Tools` for one master note per tool, `/Concepts` for MCP / context engineering / memory / agents / RAG vs skills, `/Workflows` for transcript-summarization / resume-tailoring / market-research workflows. Practical rule: put something in **Obsidian** if it answers "What do I know about this?" / "How does this connect?" Put something in a **skill file** if it answers "How should the agent perform this task every time?" Don't dump every transcript into Obsidian with no structure. Don't create 50 skill files for tiny nonsense. Don't let the system become more work than the work itself — that's the trap of a beautiful graveyard of markdown.

## Context
Crystallized 2026-06-26 (Obsidian vs Skills Files). Ilham had been treating every transcript as a separate knowledge dump without canonical master notes — the exact anti-pattern the convo warned against.

## Related
- [[second-brain-three-layer-architecture]]
- [[obsidian-vs-sqlite-memory-split]]
- [[think-pipeline-not-plugin]]
- [[koo-project-highlights]]
- **AI Second Brain**
- **Obsidian + Claude Cowork**

---
concept: Operator anti-pattern YAML cult
tags: [koo-project, second-brain, anti-pattern, principle]
source: ChatGPT convs
---

# Operator Anti-Pattern — The YAML Cult

## Insight
The anti-pattern call-out: **"six vector DBs, ten MCP servers, autonomous multi-agent councils" = masturbation with YAML.** Pick one recurring workflow first.

The trap: building a beautiful graveyard of markdown. People get excited by the architecture and forget the architecture's only purpose is to make *one* recurring workflow actually work. The system becomes more work than the work itself. Ilham had been collecting tool notes, transcripts, summaries, comparisons, decisions — and the vault risked becoming noise. LLMs don't magically become wise because you dumped 200 markdown files into the basement.

**What NOT to do:**
- dump every transcript into Obsidian with no structure
- ask the model to search a giant vault raw every time
- treat summaries, instructions, and personal notes as the same thing
- create 50 skill files for tiny nonsense
- let the "system" become more work than the work itself
- start with 100 skills and a YAML cult
- start at "automate 500 applications" when the underlying resume is weak

**What TO do:**
- start with Obsidian + 3–5 high-value skill files (summarize_transcript, create_obsidian_note, update_master_tool_note, compare_tools, extract_actionable_workflows)
- pick one recurring workflow (job-search operator, investment war room, or coding operator — pick ONE)
- maintain ONE canonical master note per tool (distilled truth vs scattered evidence notes)
- structure the vault by purpose: `/Sources` (raw), `/Summaries` (one note per video/article/doc), `/Tools` (one master per tool), `/Concepts` (cross-cutting ideas), `/Workflows` (procedures)
- only add embeddings/vector search or SQLite index when simple file access is no longer enough

The swordsman principle: sharpen the blade before learning spinning tricks. Start with the master resume and the achievement bank — fundamentals compound. The automation comes after. Most candidates start at #6 (full automation) because it's exciting. The winners usually start at #1 (master resume) because fundamentals compound.

## Context
Came up 2026-06-26 (Obsidian vs Skills Files + Harness Explanation). Ilham had been hoarding tools and transcripts without picking one workflow to actually ship.

## Related
- [[second-brain-three-layer-architecture]]
- [[obsidian-vs-sqlite-memory-split]]
- [[one-master-note-per-tool-principle]]
- [[harness-vs-model-concept]]
- [[agency-of-one-job-search-reframe]]
- [[koo-project-highlights]]

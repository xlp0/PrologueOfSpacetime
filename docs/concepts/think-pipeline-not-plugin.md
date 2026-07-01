---
concept: Think pipeline not plugin
tags: [koo-project, opencode, claude-code, mcp, pipeline]
source: ChatGPT convs
---

# Think Pipeline, Not Plugin

## Insight
The "Understand Anything" Claude plugin pivot. Ilham asked whether the plugin (which scans a codebase, maps modules/files/dependencies/concepts, generates summaries + explanations) could be integrated into OpenCode + GLM + Obsidian. Short answer: **yes for the use case, no for the integration fantasy — unless you route it through files/artifacts.** No Claude Code = no Claude Code plugin. Simple.

The reframing: think **pipeline, not plugin**. The real goal is not "use this plugin." The real goal is: *"How do I make any repo — Prologue, Shape of Spacetime, whatever — legible fast, and reusable across OpenCode/GLM/Obsidian?"* That can be done without Claude Code.

Workflow without Claude Code: use OpenCode/GLM directly on the repo with a structured interrogation prompt — Purpose / Stack / Entry points / Architecture / Folder map / Runtime flow / Change map / Risk zones / Glossary / Suggested reading order — then save outputs to `repo-notes/` (00-overview.md → 06-questions.md). Stack: Repo on disk → OpenCode/GLM inspects → Obsidian stores generated understanding → maybe SQLite for structured notes later. "80% of the value of the plugin without paying tribute to Anthropic."

The grown-man architecture: Claude plugin = reconnaissance unit; Obsidian / markdown / knowledge files = memory; OpenCode / GLM = ongoing reasoning + implementation. Not "one plugin will save me." If Understand Anything produces portable artifacts (markdown summaries, JSON/graph files, generated docs, knowledge maps), pipe them into Obsidian → OpenCode → skills files. If the plugin only works inside Claude Code (tightly coupled, no clean export), then Claude understands the repo *inside Claude Code* and OpenCode/GLM do **not inherit that understanding** — you'd need to manually export outputs and feed them elsewhere. Tool memory vs portable knowledge — people confuse the two all the time.

## Context
Came up 2026-06-26 (Claude Plugin Integration). Ilham had asked: "There is a claude plugin, Understand anything, for understanding codebases. My use case for this would be to understand prologue and shape of spacetime repos right? Or can it not be integrated into opencode and glm? But I dont have claudecode."

## Related
- [[second-brain-three-layer-architecture]]
- [[one-master-note-per-tool-principle]]
- [[opencode-vs-claude-code-vs-pi-agent]]
- [[harness-vs-model-concept]]
- [[koo-project-highlights]]
- **Understand Anything plugin**
- **Claude Code Plugin**

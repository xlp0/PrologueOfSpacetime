---
concept: Obsidian vs SQLite memory split
tags: [koo-project, second-brain, obsidian, sqlite, memory]
source: ChatGPT convs
---

# Obsidian vs SQLite Memory Split

## Insight
**Obsidian is for human memory. SQLite is for machine memory.** That is the clean distinction. Mixing them too much gets messy.

**Obsidian = knowledge / thinking layer.** Notes, ideas, journal/thoughts, market writeups, thesis notes, life planning, reading notes. Where *you* think. Example folders: `Career`, `Masters`, `Indonesia Macro`, `Stock Theses`, `Life Planning`.

**SQLite = execution layer.** Structured state the agent needs to act on: jobs applied to, deadlines, company records, task queues, logs, watchlists/alerts. Where *the agent operates*. Example tables: `jobs`, `applications`, `deadlines`, `theses`, `alerts`, `tasks`. Better than YAML/JSON for real operational memory because it's fast to query, structured, filterable/sortable, reliable for updates, no server needed, simple local file.

**YAML/JSON = config / preferences / rules.** Settings, prompt templates, profile/preferences, system rules. Small, human-readable, slow-changing. Example files: `user_profile.yml`, `resume_rules.yml`, `job_scoring_rules.yml`, `agent_settings.yml`.

The ideal relationship: the agent **reads Obsidian** to understand your thinking and **writes SQLite** to track actions and state. Example: an Obsidian note says "Why I like ANTM / thesis / risks"; a SQLite row says "ANTM thesis last updated June 20; catalyst = nickel policy; alert status = watch." Memory is *not* the harness itself — it is one part of the harness. Anti-pattern: "six vector DBs, ten MCP servers, autonomous multi-agent councils" = masturbation with YAML. Pick one recurring workflow first.

## Context
Came up 2026-06-25 (Harness Explanation). Ilham had asked: "basically you are saying I can create ordered memory right? using YML? or SQL? someone told me using SQLite would be far more efficient." Answer: yes, both, for different jobs.

## Related
- [[second-brain-three-layer-architecture]]
- [[harness-vs-model-concept]]
- [[one-master-note-per-tool-principle]]
- [[operator-anti-pattern-yaml-cult]]
- [[koo-project-highlights]]
- **AI Second Brain**

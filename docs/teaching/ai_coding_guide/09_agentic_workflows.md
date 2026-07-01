---
title: 'Chapter 9 — Agentic Workflows'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Quadrivium-Music]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 9
liberal_art: Quadrivium-Music
audience: professional
---

# Chapter 9 — Agentic Workflows

## What "agentic workflow" means

An **agentic workflow** is any repeatable way of getting work done by letting an agent run the loop from Chapter 2 — gather, prompt, model, execute, feed back — against a defined goal, with you steering at the points that matter. The shift from "vibe coding" (Chapter 1) to "agentic engineering" (the word the field has settled on for the current era) is, at root, a shift from ad-hoc prompting to deliberate workflows.

This chapter is the practical one. It covers the patterns people actually use, the configuration files that make them repeatable, and the methodologies that try to package all of it. If you read one chapter to start working differently tomorrow, read this one.

---

## The spectrum: how much autonomy?

Before the patterns, a frame. Any agentic workflow sits somewhere on a spectrum of autonomy:

1. **Manual / human-every-step.** You approve every tool call. Slow, safe, good for unfamiliar code or high-risk tasks.
2. **Plan-then-execute.** The agent proposes a plan; you approve or edit; it executes, checking back at defined milestones. The sweet spot for most real work.
3. **Goal-driven with checkpoints.** You give a goal ("implement the CSV export feature"); the agent runs, pausing at gates (PR created, tests failing, etc.) for your input. Good for medium-sized features.
4. **Highly autonomous.** You give a goal; the agent runs to completion, including opening PRs, responding to review comments, and merging. The frontier of what people are doing — powerful, dangerous, and where most of the Chapter 11 caveats live.

The right point on the spectrum depends on the task's risk, your trust in the harness's permissions, and how much you understand the codebase. Most professionals spend most of their time in slots 2 and 3. Slot 4 is real but rare, and should never be the default for code you care about.

---

## Pattern 1 — Plan-then-execute

The single most important workflow habit. Before letting an agent edit anything, ask it to plan:

> "I want to add CSV export to the reports page. Don't edit anything yet. List the files you'd touch, the approach, and any questions. Wait for my approval."

The agent produces a plan. You read it. You catch the bad assumptions *before* any code is written, when they cost nothing to fix. You approve (or amend). Then the agent executes, and you have a shared spec to check the result against.

Most harnesses have a built-in "plan mode" for exactly this. Use it. The cost of planning is one extra round-trip; the cost of *not* planning is implementing the wrong thing.

**When to use:** anything beyond a one-line edit. Especially anything touching multiple files.

---

## Pattern 2 — One task per session

Resist the urge to pile multiple unrelated tasks into one agent session. The context window (Chapter 4) and [[static-vs-dynamic-context|context engineering]] (Chapter 6) both punish sprawl. A session focused on "add CSV export" will produce better work than a session that says "add CSV export, fix the login bug, and refactor the User model."

This sounds obvious and is consistently violated in practice. The fix is operational: when you finish a task, start a fresh session for the next one. Carry over only what's still relevant (the file you're working on, the decision you made), not the whole conversation history.

**When to use:** always. The exception is genuinely coupled tasks.

---

## Pattern 3 — Subagents for noisy sub-tasks

Some sub-tasks generate a lot of context that's useful briefly and useless afterward: "search the whole codebase for every place we call this function," "run the full test suite and tell me what failed," "read this 5,000-line log and find the error." A good harness lets you delegate these to a **subagent** — a separate context window that does the noisy thing, returns a short answer, and is then discarded.

The main context stays clean. The agent's "working memory" doesn't get polluted with the search results or the log dump. Subagent orchestration is one of the highest-leverage features of a modern harness; if you're not using it, your context windows are filling up with junk.

**When to use:** any time a sub-task will produce a lot of output but only a short answer is needed.

---

## Pattern 4 — Test-driven loops

For features and bug fixes both: have the agent write the failing test first, then implement until the test passes. This is just TDD, but the leverage is amplified because the agent can run the test itself in the loop:

1. Agent writes a failing test.
2. Agent runs the test, sees it fail.
3. Agent implements the change.
4. Agent runs the test, sees it pass.
5. Agent runs the *rest* of the suite to check for regressions.

You verify at the end. The test is the spec; the loop is the iteration; the green bar is the gate. This pattern is the single best defense against the agent "looks done but isn't" failure mode.

**When to use:** any task that admits a test, which is most of them.

---

## Pattern 5 — Review-then-merge

Never let an agent's edit go straight to `main`. The workflow is:

1. Agent makes changes on a branch.
2. Agent (or a separate review subagent, or you) produces a diff summary.
3. You review the diff.
4. Tests and CI run.
5. Merge only after both pass.

This is just normal software engineering, but it's worth restating because the speed of agentic edits makes it tempting to skip. Don't. The cost of a bad merge is always higher than the cost of a review.

---

## The configuration layer: rules files

The patterns above describe *how* you work. Rules files describe *what the agent should assume* about your project, so you don't restate it every time. This is the configuration layer of agentic workflows.

### The menagerie of rules file formats

Different tools read different files. As of 2026, the landscape is roughly:

| File | Tool(s) that read it | Notes |
|---|---|---|
| `AGENTS.md` | Codex CLI, opencode, and an emerging cross-tool standard | The closest thing to a universal format. Often the right default. |
| `CLAUDE.md` | Claude Code | Claude Code's native format. Powerful — can scope to subdirectories. |
| `GEMINI.md` | Gemini CLI | Gemini's equivalent. |
| `.cursorrules` | Cursor (legacy) | Older Cursor format. |
| `.cursor/rules/` | Cursor (current) | Newer Cursor rules directory; supports multiple files and globs. |
| `.windsurfrules` | Windsurf | Windsurf's format. |
| `.clinerules` | Cline | Cline's format. |
| `.github/copilot-instructions.md` | GitHub Copilot | Copilot's format. |

The pattern across all of them is the same: a plain-text (usually Markdown) file at the root of your project that the harness loads into context automatically. It contains the standing facts about your project: tech stack, conventions, what to avoid, how to run tests, where things live.

### What goes in a rules file

- Tech stack and versions ("TypeScript 5.x, Node 20, Vitest, Drizzle ORM").
- Commands (`npm test`, `npm run lint`, `npm run migrate`).
- Conventions that matter ("we use named exports," "no default exports," "tests live next to the file they test").
- What to avoid ("don't add new dependencies without asking," "don't touch `legacy/` — it's frozen").
- Where things go ("new endpoints go in `src/routes/`, new tests in `src/routes/__tests__/`").
- Anything else the agent keeps getting wrong by default.

### What does *not* go in a rules file

- Multi-step procedures. Those are skills (Chapter 8).
- One-off instructions for the current task. Those go in your prompt.
- Anything that's true of all projects. The file is for what's specific to *this* one.

### The cross-tool strategy

If your team uses more than one AI tool, the modern advice is:

- Put your canonical rules in `AGENTS.md` (the cross-tool standard is converging here).
- Add tool-specific stubs (`CLAUDE.md`, `.cursor/rules/AGENTS.md`, etc.) that just say "see AGENTS.md" or symlink to it.

This avoids the maintenance nightmare of keeping five copies in sync. Some tools natively read `AGENTS.md` already; for the rest, a one-line "see AGENTS.md" pointer costs nothing.

---

## The workflow layer: slash commands and custom commands

Rules files are passive — they're always in context. **Slash commands** (also called custom commands) are active: pre-built prompts you trigger on demand.

You've seen them: `/fix`, `/review`, `/refactor`, `/code-review`, `/security-scan`. Typing one injects a pre-written prompt into the agent. The prompt can be a single line or a multi-step procedure that effectively runs a skill (Chapter 8).

Different tools store them differently:

- **Cursor:** `.cursor/commands/*.md` — Markdown files where the filename becomes the command name.
- **Claude Code:** project commands in `.claude/commands/`, user commands in `~/.claude/commands/`. Supports both built-in (`/code-review`, `/init`, etc.) and custom.
- **opencode:** its own commands directory.
- **Windsurf, Cline, etc.:** their own conventions, same pattern.

The pattern across all of them: a folder of Markdown files, each defining a slash command, often parameterized. Team-shared commands go in the repo (so everyone gets them); personal commands go in your home directory.

Why this matters: a well-stocked command library turns "explain to the agent how we do code review" into a one-keystroke operation. The procedure lives in a file, versioned with the repo, applied identically every time. This is the bridge between ad-hoc prompting and a real engineering methodology.

---

## The methodology layer: BMAD and friends

Once you have rules files (configuration) and slash commands (procedures), the next step up is a full **methodology** — a packaged way of running an entire project with agents. This is where frameworks like **BMAD** live.

### BMAD Method

**BMAD** (variously expanded as "Breakthrough Method for Agile AI-Driven Development" or "Build More Architect Dreams," depending on which doc you read) is an open-source AI-native development framework that has gained significant traction in 2025–2026. The pitch, in one sentence: it gives you a set of specialized agents, guided workflows, and planning templates that take a project from ideation through implementation, adapted to the project's scale.

The interesting parts of BMAD:

- **Specialized agent roles** — instead of one generic agent, BMAD defines roles (architect, implementer, reviewer, etc.) with different system prompts and tool access. You orchestrate between them.
- **Guided workflows** — pre-defined sequences for common project activities (planning a feature, implementing it, reviewing it). These are essentially skills (Chapter 8) at methodology scale.
- **Scale-adaptive intelligence** — the framework adjusts its ceremony to the project's size: a bug fix gets a lightweight flow, an enterprise system gets the full planning workflow.
- **Skill-folder generation** — BMAD can produce ready-to-install skill folders from a conversational discovery process, so the methodology customizes itself to your project.

BMAD is not the only player in this space — there are competing methodologies, and the vocabulary is still settling — but it's the most visible example of the pattern: *packaging the entire agentic workflow into a reusable framework*, the way Scrum or Kanban packaged human workflow a generation ago.

### Other methodologies and patterns

Beyond BMAD, you'll encounter:

- **Lighter-weight "agent fleet" patterns** — teams defining a small set of role-specific agents (a reviewer agent, a test-writer agent, a planner) and orchestrating between them, without buying into a full framework.
- **Workflow-as-code** — defining multi-step agent workflows in YAML or similar, versioned with the repo, runnable on demand or in CI. This is the natural extension of slash commands to multi-step procedures.
- **CI-integrated agents** — agents that run on PRs or on schedule, doing review, security scans, dependency bumps, etc. The agentic loop, but in a pipeline rather than at your keyboard.

The common thread: **the agentic loop is composable.** Once you have a harness, [[mcp-anthropic-standard|MCP]], skills, rules files, and slash commands, you can assemble them into higher-level workflows — and those workflows can themselves be packaged and shared. This is the trajectory of the field.

---

## Choosing a workflow

You don't need a methodology on day one. A reasonable progression:

1. **Start with rules files.** One `AGENTS.md` at the repo root. Cover the basics. This alone makes every agent session better.
2. **Add plan-then-execute as a habit.** Don't let the agent edit without a plan. This costs you nothing and saves you constantly.
3. **Add a few slash commands** for the procedures you repeat (review, test, PR description).
4. **Start writing skills** when you notice procedures that are bigger than a slash command but smaller than a methodology.
5. **Consider a methodology like BMAD** when you're running a whole project with multiple people and agents and need shared conventions for how that works.

Most individuals and small teams will be perfectly served by steps 1–4. Step 5 is for organizations trying to standardize across many projects and teams — and even there, the lighter-weight patterns often beat the full framework.

---

## A note on the temptation of slot 4

It is very tempting, especially after a few good experiences, to let the agent run autonomously — give it a goal, walk away, come back to a merged PR. Sometimes this even works. More often it works *just well enough* to lull you into letting it run on something that matters, and then it doesn't.

The agentic workflows that hold up in production are the ones with **gates** — points where a human looks at what happened before it propagates. The gates can be lightweight (a quick diff review) or heavy (a full code review), but they exist. Workflows without gates are vibe coding with extra steps, and they will eventually produce something you regret.

Chapter 11 is the long version of this paragraph. But the seed of it lives here, in the workflow chapter, because the workflow *is* where you decide whether to have gates. Decide on purpose.

---
title: 'Chapter 8 — Agent Skills — Packaged Know-How'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Grammar]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 8
liberal_art: Trivium-Grammar
audience: professional
---

# Chapter 8 — Agent Skills — Packaged Know-How

## The one-line answer

An **agent skill** is a packaged bundle of know-how that teaches an agent how to do a particular kind of task well — without you having to re-explain it every time. If [[mcp-anthropic-standard|MCP]] (Chapter 7) gives an agent new *tools*, skills give an agent new *procedures*: when to use which tool, in what order, against what inputs, and what good looks like at the end.

You can think of a skill as a small, opinionated playbook that loads into the agent's context on demand.

---

## The problem skills solve

A capable agent with good tools can do almost anything *badly*. What it lacks is *judgment about your specific situation* — the kind of thing a senior engineer on your team knows and a new hire doesn't:

- "In this codebase, a refactor means X, not Y."
- "When you fix a bug in the billing service, also update the migration in `db/migrations/` and run `pnpm test:billing`."
- "Before you open a PR here, run `/security-scan` and address anything flagged."
- "Our code review process has four steps — here they are, in order."

You *could* retype all of this into every conversation. You'd go mad. You *could* stuff it all into your global rules file (Chapter 9), but then it's in context all the time, even when irrelevant, eating tokens. Skills exist to put know-how *only* where and when it's relevant.

A skill is essentially: **a folder of instructions and resources, with a description that tells the agent when to load it, loaded into context on demand.**

---

## What's actually in a skill

Concretely, a skill is usually a directory containing:

- **A manifest** — name, description, what the skill does, when it applies. This is the metadata the harness uses to decide whether the skill is relevant to the current task.
- **Instructions** — the playbook itself: a Markdown file (or set of files) that tells the agent how to approach this kind of task. This is what loads into context when the skill is activated.
- **Optional resources** — scripts, reference snippets, templates, schemas, example outputs. Anything the agent might need to actually execute the playbook.
- **Optional references to tools** — many skills assume particular MCP tools are available ("this skill requires the `github` and `filesystem` MCP servers").

The key design choice is **on-demand loading**. The skill's *description* lives in context all the time (cheap — a few hundred tokens per skill). The skill's *instructions* only load when the agent decides the skill applies to the current task. So you can have dozens of skills installed without paying for all of them on every turn — only the relevant ones expand.

This is the same pattern as functions in a program: the symbol table is always in memory; the function body executes only when called.

---

## How skills differ from rules files (Chapter 9)

This is the question everyone asks, so let's answer it up front:

| | Rules files | Skills |
|---|---|---|
| **What they hold** | Always-on project conventions ("we use Vitest," "don't add comments") | On-demand procedures ("how to do a code review in this repo") |
| **When they're in context** | Always (or scoped to a directory) | Only when the agent decides they're relevant to the current task |
| **Granularity** | One or a few per project | Many per project, each for a specific kind of task |
| **Authored by** | You, for your project | You, your team, or third parties |
| **Reusable across projects** | Rarely (they're project-specific) | Often (a "good PR description" skill is the same in any repo) |

Rules files are the constitution; skills are the runbooks. You need both.

---

## How skills differ from MCP (Chapter 7)

Already covered briefly in Chapter 7, but to make it explicit:

- **MCP gives tools.** "Here is a function called `query_database` you can call."
- **Skills give procedures.** "When the user asks you to investigate a slow query, first call `query_database` to get the slow query log, then call `run_shell_command` to look at the indexes, then write a summary in this format..."

A skill will often *use* MCP tools — the playbook says "call this tool, then this one, then format the result like this." But the skill is the procedure; the MCP server is the capability. The same MCP server can be used by many skills; the same skill can orchestrate many MCP servers.

---

## Real examples of skills

Skills are still a young pattern, and the ecosystem is in flux (different tools use slightly different formats and names — "skills," "commands," "playbooks," "workflows" — but the underlying idea is converging). A representative sample of what a skill looks like in practice:

- **Code review skill.** "When asked to review code: diff against `main`, read the changed files, check for tests covering the changes, run `/security-scan`, summarize the change in plain English, then list issues ordered by severity. Don't suggest style nits."
- **Migration skill.** "When writing a database migration in this repo: copy `db/migrations/_template.sql`, name it `YYYYMMDD_description.sql`, include both `up` and `down`, and add a corresponding test in `db/migrations/tests/`."
- **PR-description skill.** "When opening a PR: read the diff, summarize what changed and why, link the ticket, note any breaking changes, list what was tested, and call out anything a reviewer should look at closely."
- **Bug-triage skill.** "When given a bug report: reproduce it in a branch, add a failing test, fix the bug, verify the test passes, then commit with the format `fix(scope): description`."
- **Refactoring skill.** "When refactoring: don't change behavior, run the full test suite before and after, commit in small steps, and never mix a refactor with a feature change."
- **Onboarding skill.** "When a new contributor asks 'how do I get this running': walk them through the setup in `README.md`, then the architecture overview, then point them at the easy first issues."

You'll notice these read like things you'd put in a `CONTRIBUTING.md` or a team wiki. That's the point — a skill is the *operationalized* version of those documents. Instead of hoping a new contributor reads `CONTRIBUTING.md` and remembers step 4, the skill loads step 4 into the agent's context at exactly the moment it's relevant.

---

## Third-party skills and the skill ecosystem

Because skills are mostly plain text (Markdown + maybe some scripts), they're trivially shareable. There's a growing ecosystem of pre-written skills you can install into your agent:

- General-purpose skills (code review, PR description, migration writing) that work in any repo.
- Domain-specific skills (e.g. "how to work with this framework," "how to debug this service") shared by communities.
- Tool-vendor skills — Claude Code, opencode, and others ship with bundled skills and accept third-party ones.

The install pattern is usually: drop the skill folder into a known directory (e.g. `.agents/skills/` or `~/.agents/skills/`), and the harness picks it up. Some tools have a `skills-lock.json` or similar to pin versions; some have package-manager-style installs.

This is meaningfully different from MCP's ecosystem: MCP servers are *code* (a process that runs and speaks a protocol), so they need to be trusted and often sandboxed. Skills are mostly *instructions* (text that goes into context), so they're lower-risk to install but still worth reviewing — a malicious skill can absolutely steer an agent to do bad things, just via instructions rather than code.

---

## When to write a skill (and when not to)

Write a skill when:

- You're repeating the same multi-step procedure to the agent across sessions.
- A procedure has non-obvious steps that the agent keeps getting wrong on its own.
- You want to share a procedure with teammates (or the public) in a way that just works when they install it.

Do *not* write a skill when:

- A single line in your rules file would do. Skills are for *procedures*, not single conventions.
- The procedure is so project-specific it'll never be reused. A rules-file entry or a one-off prompt is cheaper.
- You haven't actually figured out the procedure yet. Skills are best written *after* you've done the thing a few times and know what works — writing them prospectively tends to produce playbooks that don't match reality.

There's an art to scope: too small and the skill isn't worth loading; too big and it eats the context window. The good skills tend to be sized like a single focused meeting agenda — a page or two of instructions, covering one specific kind of task.

---

## Skills and the bigger picture

Skills are part of a broader pattern you'll see across this guide: **moving intelligence out of the model's training data and into the runtime.** The model knows how to write code in general; it doesn't know how to write code in *your* codebase. MCP tells it what tools are available. Skills tell it how to use those tools here. Rules files (Chapter 9) tell it the standing constraints of the project. None of these replace the model; together, they wrap the model in enough context to actually be useful in your specific situation.

The model is the brain. The harness is the body. MCP is the hands. Skills are the training.

Next chapter pulls it together: how to actually *run* an agent productively — the workflows, the rules files, the slash commands, the frameworks like BMAD that try to package all of this into a coherent methodology.

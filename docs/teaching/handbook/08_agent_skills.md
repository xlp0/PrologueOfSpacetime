# Chapter 8 — Agent Skills: Packaged Know-How

> A **skill** is a packaged unit of workflow knowledge that an AI loads on demand. This chapter explains what skills are, what they are for, and examples of skills people have built.

---

## The Simple Version

A **tool** is one capability — "read a file," "run a command," "search the web."

A **skill** is a recipe that uses tools — "review a pull request by reading the diff, checking the style guide, running the tests, and writing a structured report."

The tool is a verb. The skill is a recipe.

---

## Skills vs. Tools

| Aspect | Tool | Skill |
| :--- | :--- | :--- |
| Granularity | One capability | One workflow (uses many tools) |
| Format | A callable function | A markdown file plus supporting files |
| Lives where | In a running server or harness | On the filesystem, loaded when needed |
| Example | `grep_search(pattern, path)` | "Review a PR against our style guide" |

Skills and tools work together. A skill's instructions tell the AI which tools to call. The tools do the actual work.

---

## What a Skill Looks Like

A skill is just a folder with a `SKILL.md` file in it, plus any supporting files it needs:

```
.agents/skills/
  pr-review/
    SKILL.md          ← the instructions
    checklist.md      ← a reference file
    style_guide.md    ← another reference
    scripts/
      diff_stat.sh    ← a helper script
```

The `SKILL.md` file has:

- A short description (so the AI knows when to load the skill).
- A longer set of instructions (what the AI should do when the skill is activated).

That is the whole format. The skill tells the AI what to do; the AI already knows how to read files, run shell commands, and write text.

---

## Example Skills (What People Have Built)

To give you a sense of the range, here are some examples of skills that exist in the wild. These are illustrative — they show what a skill can describe, not a tutorial on how to use them.

- **Codebase exploration skill** — Points the AI at a pre-built knowledge graph of a codebase (nodes for files, functions, classes; edges for calls, imports). The AI searches the graph to answer "how does authentication work?" instead of reading every source file.

- **YouTube video analysis skill** — Defines a multi-step forensic analysis of a video transcript: extract hooks, map retention mechanics, decode emotional beats, score virality, produce a structured blueprint. Packages a 250-line analysis framework so the AI applies the same rigor to every video.

- **Parallel execution skill** — Describes how to spawn multiple subagents at once for independent tasks, with rules like "all Task calls must be in one assistant message for true parallelism."

- **Skill discovery skill** — When a user asks "how do I do X?", this skill directs the AI to search a public skills registry before writing custom instructions from scratch. It is a meta-skill — a skill whose job is to find other skills.

- **Multi-agent orchestration skill** — Describes how to deploy and coordinate swarms of agents via an MCP server: initialize a swarm, spawn specialized agents (researcher, coder, analyst), assign tasks, monitor, scale, tear down.

- **Code review skill** — Walks the AI through reviewing a pull request: fetch the diff, read the changed files for context, check against a project style guide, run the tests, write a structured review with sections for risks, suggestions, and approval.

The common shape: each of these skills packages a procedure that would otherwise have to be re-explained every time. The skill is loaded once when the task matches, and the AI follows it.

---

## Why Skills Reduce Tokens (Conceptually)

You do not need to know the exact numbers, but it helps to understand the shape of why skills are token-efficient. Four mechanisms:

1. **Pointing instead of loading.** A skill can tell the AI "search the index, do not read every file." The index is small; the files are large. The AI spends tokens reading the relevant slice, not the whole.

2. **Isolation via subagents.** A skill can describe spawning subagents for independent pieces. Each subagent does its reading in its own context; the main context only sees the short summary.

3. **Reuse instead of retyping.** A skill loads once and applies to every future task of that kind. The framework does not need to be re-explained each session.

4. **Avoiding failed attempts.** A skill with concrete tool names and parameter examples helps the AI get it right the first time, instead of guessing, failing, and retrying.

The unifying principle: **a skill is a way to describe a procedure once, so that the AI does not have to rediscover it — and re-spend the tokens to rediscover it — on every session.** That is the whole idea.

---

## 8.5 The Skills Ecosystem

Skills are not just something you write for yourself. There is a whole ecosystem of public skills you can find, install, and use.

### What is skills.sh?

**skills.sh** is a public registry of agent skills — a website where people publish skills they have built and others can find and install them. Think of it like npm for JavaScript packages or PyPI for Python, but for AI agent skills.

### How Many Skills Are Out There?

The ecosystem is growing fast. As of late 2025, hundreds of skills are published across the major registries. The numbers change weekly because anyone can publish one.

### Who Publishes Skills?

- **Companies** — Anthropic publishes official skills for working with their models and for common tasks like document processing and frontend design. Vercel publishes skills for React, Next.js, and web design.
- **Open source projects** — projects like GitNexus, Understand, and others publish skills that wrap their tools so agents can use them.
- **Individual developers** — anyone can write a skill and share it on GitHub or via `npx skills add`.

### How Are Skills Shared?

Three common ways:

1. **GitHub repos** — the most common. A skill is just a folder with a `SKILL.md` and supporting files. Clone it, fork it, install it.
2. **npm packages** — some skills are published as npm packages, installable with `npx skills add <package-name>`.
3. **Direct copy** — for private or personal skills, just drop the folder into `.agents/skills/` on your machine.

### What is a `skills-lock.json` File For?

A **lock file** pins the exact versions of installed skills. It records which skills you have, what version, and where they came from. This makes installs reproducible across machines — if your teammate has the same `skills-lock.json`, they get the same skills you do. It is the same idea as `package-lock.json` for npm or `Cargo.lock` for Rust.

### Where to Start

If you want to see what skills look like:

1. Browse **skills.sh** for popular skills.
2. Look at **github.com/anthropics/skills** for official Anthropic skills.
3. Look at **github.com/vercel-labs/agent-skills** for web development skills.
4. Check your own machine — if you have any AI coding tools installed, you may already have skills under `~/.agents/skills/` or `.agents/skills/` in your project.

Read a few `SKILL.md` files to get a feel for the format. You do not need to install them — just reading the instructions teaches you what a good skill looks like.

---

## When People Author Skills

People write a skill when they find themselves giving the AI the same multi-step instructions repeatedly. If you have typed "review this PR by checking the diff, the style guide, and the tests" three times, you write the skill once.

People do NOT write a skill for:

- A single tool call (just use the tool).
- A one-off task (just do it).
- Something the AI already does well without instructions (the skill adds nothing).

---

## The Big Picture

- A **skill** is packaged workflow knowledge — a recipe the AI follows.
- A **tool** is one capability; a **skill** is a procedure that uses many tools.
- Skills live as `SKILL.md` files in a folder, loaded on demand.
- People have built skills for codebase exploration, video analysis, parallel execution, code review, and more.
- Skills save tokens by describing a procedure once, instead of re-explaining it every session.

## 8.6 A Concrete Example: Browsing skills.sh

Section 8.5 mentioned **skills.sh** as a public registry. Here is what you actually see if you open it in a browser today. Think of this as a tour, not a tutorial — you are just looking.

### When you visit skills.sh, you see...

A page titled **"The Open Agent Skills Ecosystem"** with the tagline: *"Skills are reusable capabilities for AI agents. Install them with a single command to enhance your agents with access to procedural knowledge."* (source: skills.sh homepage, June 2026). Below that is the install command — `npx skills add <owner/repo>` — and a row of logos showing which agents are supported: Claude Code, Cursor, Codex, GitHub Copilot, Gemini, and about fifteen others.

Then comes the main event: a **Skills Leaderboard**. It is a ranked list. At the top there are three tabs: **All Time** (746,231 installs total), **Trending (24h)**, and **Hot**. The default view is "All Time," sorted from most-installed to least.

### Each skill entry shows...

Every row on the leaderboard has four things:

1. **A rank number** — 1, 2, 3, and so on down the list.
2. **A skill name** — like `find-skills` or `frontend-design`.
3. **An owner/repo** — like `vercel-labs/skills` or `anthropics/skills`. This tells you who wrote it and where it lives on GitHub.
4. **An install count** — like `2.2M` (2.2 million) or `588.0K` (588 thousand).

That is the whole row. Click the name and you go to a detail page with the full `SKILL.md` and install instructions.

### For example, a popular skill might look like...

The number-one skill on the leaderboard right now is **`find-skills`** by **`vercel-labs/skills`**, with **2.2M installs** (source: skills.sh All Time leaderboard, June 2026). That is the same "skill discovery" idea described in section 8.4 — a meta-skill whose job is to help the AI find *other* skills. The fact that it is the most-installed skill makes sense: people install it first, and then it helps them find everything else.

Other top entries: **`frontend-design`** by `anthropics/skills` at 588K, **`vercel-react-best-practices`** by `vercel-labs/agent-skills` at 501K, and **`microsoft-foundry`** by `microsoft/azure-skills` at 415K. You can see the pattern — official skills from real companies (Anthropic, Vercel, Microsoft) sit near the top.

### The install count tells you...

How many times people have run `npx skills add` for that skill. A high number like 2.2M means a *lot* of people have tried it, which usually means three things: the skill works (it would not get reinstalled if it broke), it is maintained (the owner keeps it working as tools change), and it is battle-tested across many different projects. A low number does not mean the skill is bad — it might just be new, or only useful for a niche task. But if you are picking between two skills that do the same thing, the one with more installs is the safer bet.

### You do not need to install anything to browse

This is the most important point for a beginner. You can click any skill name on the leaderboard and read its `SKILL.md` file right there in your browser. No commands, no installs, no account. Just reading.

Why bother? Because reading real skills is the fastest way to learn what a *good* skill looks like. You see how experienced authors write descriptions, structure instructions, and decide what to include versus what to leave out. After you have read five or ten of them, the format from section 8.2 stops feeling abstract — you can recognize the patterns. Then, when you write your own first skill, you have a mental library of examples to copy from.

Browsing is free. Reading is free. Install only when you actually want to use one.

---

Continue to [Chapter 9 — Agentic Workflows: Letting AI Do More](09_agentic_workflows.md).

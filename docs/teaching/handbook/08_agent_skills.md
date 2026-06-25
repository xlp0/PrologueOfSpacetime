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

Continue to [Chapter 9 — Agentic Workflows: Letting AI Do More](09_agentic_workflows.md).

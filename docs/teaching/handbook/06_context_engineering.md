# Chapter 6 — Context Engineering

> There is a newer idea you will hear about: **context engineering**. It is the skill of choosing what the AI sees, so it gives you better answers. This chapter explains what it is and why it matters more than prompt wording.

---

## The Simple Version

**Prompt engineering** asks: "What words do I type?"

**Context engineering** asks: "What does the AI see, in total, before it answers?"

The second question matters more. A perfect prompt in a polluted context still produces bad output. A mediocre prompt in a clean, well-chosen context often produces great output.

---

## What Is "Context"?

The **context** is everything the AI sees in one conversation:

- Your prompt (what you typed)
- The AI's previous responses
- Any files you pasted in
- Any files the AI read using tools
- Any command output the AI saw
- Any web pages the AI fetched
- The system prompt (instructions from the harness)

All of this goes into the context window (see [Chapter 4](04_tokens_and_context.md)). When the window fills, the oldest stuff drops out.

---

## Why Context Engineering Matters

Imagine you are studying for a test. Which is better:

1. A desk with your textbook, your notes, and a clear study guide.
2. A desk piled with every book you own, all your old homework, three laptops, and a stack of random printouts.

Most people do better with option 1. The same is true for AI. A focused context with the right 5 files beats a sprawling context with 500 files.

When you give the AI too much:

- It **loses focus**. Important details get buried.
- It **costs more**. Every token you put in costs money.
- It **slows down**. The AI has to process everything before it responds.
- It **forgets**. The window fills, old stuff falls out, the AI loses track of what you asked.

When you give the AI too little:

- It **guesses**. And guesses are often subtly wrong.
- It **hallucinates**. It makes up plausible-sounding but incorrect details.

The professional skill is **curating** the context — giving the AI exactly what it needs, no more, no less.

---

## The Levers of Context Engineering

Context engineering has several levers. You do not need to use all of them every time, but knowing they exist helps you understand what professionals do.

### Lever 1: File Selection

Instead of pasting the whole codebase, pick the specific files that matter. If the AI needs more, let it ask for them using tools (file search, grep).

**Beginner move**: Paste 10 files "for context."
**Pro move**: Paste the 2 files that matter, and let the AI grep for more if it needs to.

### Lever 2: Tool Selection

Instead of giving the AI every tool, give it only the tools it needs for this task. Do not enable the GitHub MCP server if the task only needs the filesystem.

**Beginner move**: Turn on every MCP server and every skill, just in case.
**Pro move**: Enable only what the task requires.

### Lever 3: Subagents

When a task has independent parts, you can spawn **subagents** — secondary AIs with their own context windows. Each subagent does its reading in its own window, then returns a short summary. The main context only sees the summaries, not all the files the subagent read.

**Beginner move**: Read 10 files into the main context, hope the AI remembers them all.
**Pro move**: Spawn a subagent to read the 10 files and return a summary. The main context stays clean.

### Lever 4: System Prompt (AGENTS.md, .cursorrules)

Most harnesses let you write a project-level file (often called `AGENTS.md` or `.cursorrules`) that becomes part of the system prompt. This is where you put standing instructions: "We use tabs, not spaces. Run tests with `npm test`. Do not touch the `legacy/` folder."

**Beginner move**: Retype these rules in every conversation.
**Pro move**: Write them once in `AGENTS.md`. The AI sees them automatically every session.

### Lever 5: Session Management

When a conversation gets long and the AI starts losing track, the professional move is to **start a fresh session**. Summarize what you have done, paste the summary into a new chat, and continue. The new session has a clean context window.

**Beginner move**: Keep going in the same chat for 3 hours until the AI forgets the original task.
**Pro move**: Start a fresh session when context gets crowded. Carry over a short summary.

---

## A Real Example

Imagine you ask the AI: "Fix the bug in the login page."

**Beginner approach**:
1. Paste the whole codebase (50 files, 200,000 tokens).
2. The AI gets confused, suggests a fix that does not work.
3. You paste the error log (5,000 tokens).
4. The AI suggests another fix, also wrong.
5. Repeat for an hour. Total cost: a lot of tokens, no progress.

**Pro approach**:
1. Tell the AI: "There is a bug in the login page. Read `src/auth/login.ts` and `src/auth/login.test.ts`."
2. The AI reads 2 files (about 2,000 tokens), finds the bug, fixes it.
3. The AI runs the tests (a few hundred tokens of output).
4. Tests pass. Done.

The pro approach used fewer tokens, was faster, and got a better result. The difference was not the prompt — it was the context.

---

## The Big Picture

- **Prompt engineering** = choosing the right words.
- **Context engineering** = choosing what the AI sees.
- Context matters more than wording. A clean context with a mediocre prompt beats a polluted context with a perfect prompt.
- The levers: file selection, tool selection, subagents, system prompt, session management.
- **More is not better.** Curate what the AI sees.

This idea — curate the context, do not just polish the prompt — is the foundation of every professional workflow in this handbook.

Continue to [Chapter 7 — MCP: Plugging Things In](07_mcp.md).

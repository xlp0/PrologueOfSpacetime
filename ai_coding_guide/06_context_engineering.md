# Chapter 6 — Context Engineering

## The shift in one sentence

**Prompt engineering** asked: "how do I word my question?"
**Context engineering** asks: "what should the model be *looking at* when it answers?"

The second question is the one that matters now. The model is stateless; it can only act on what's in the context window on this call; so the skill that separates a great AI-assisted developer from a mediocre one is the deliberate curation of that window. "Context engineering" is the name the field has settled on for that skill, and it's the right name, because it reframes the work as *engineering* — gathering, filtering, prioritizing, evicting — rather than *writing*.

---

## Why it's a discipline, not a trick

Go back to the agentic loop from Chapter 2. On every turn, the harness assembles a context window containing some mix of:

- The system prompt and tool definitions (stable).
- Project rules files (stable, but only if loaded — see Chapter 9).
- The conversation so far (grows every turn).
- Files the harness has read (grows as the loop runs).
- Tool results — test output, search results, command output (grows fast).
- Snippets retrieved from elsewhere in the codebase (varies).

That window has a hard size limit (Chapter 4). Every turn, the harness has to decide: **what stays, what goes, what gets summarized, what gets fetched fresh.** Those decisions, multiplied across dozens of turns per task, are the difference between an agent that nails it in three iterations and one that loops forever getting steadily more confused.

A good harness automates a lot of this. But you, the human, influence it enormously — by what you put in your rules files, by how you scope your request, by whether you point the agent at the right files, by whether you let it flail or steer it. That influence is context engineering.

---

## The five jobs of context engineering

Think of it as five distinct jobs, all of which you're doing (or failing to do) on every task:

### 1. Gathering — what to put in

The most basic question: what does the model need to see to do this task well?

- The file being edited (obviously).
- The file's tests, if any.
- The types/interfaces it depends on.
- A relevant example of the pattern you want it to follow (few-shot, Chapter 5).
- The error message or failing test, if it's a fix.
- The spec or ticket, if there is one.

The mistake most people make is under-gathering — pointing the agent at one file and expecting it to figure out the rest. Modern harnesses will search the codebase on their own, but a search is not the same as you saying "start here, here, and here." Direct pointers are nearly always better than letting the agent discover.

The opposite mistake — over-gathering, dumping the whole repo in — is rarer but worse: it eats the context window, costs money, and triggers "lost in the middle" problems (Chapter 4). Curation is the skill.

### 2. Filtering — what to keep out

Just as important: what should the model *not* see?

- Generated files: `dist/`, `node_modules/`, build artifacts, lockfiles. They're huge and rarely informative.
- Unrelated modules of your codebase. Just because a search hit a file doesn't mean it belongs in context.
- Old conversation turns that are no longer relevant.
- Boilerplate the model already knows (e.g. you don't need to explain what a `package.json` is).

This is what `.gitignore`-style exclusion lists and per-project "don't read these paths" rules are for (Chapter 9). A surprising amount of context engineering is just keeping junk out of the window.

### 3. Prioritizing — what goes first and last

Models attend better to the beginning and end of a long context than the middle (the "lost in the middle" effect). So:

- Put the *instruction* near the end, after the context.
- Put the most important reference material at the *start* of the context block, right after the system prompt.
- Don't bury a critical constraint on line 4,000 of a 5,000-line dump.

A good harness does some of this automatically, but if you're hand-assembling a prompt or writing a rules file, the order matters.

### 4. Eviction — what to drop when the window is full

When the window fills, something leaves. What?

- Conversation turns older than the current task: usually safe to evict.
- Tool results that have been superseded (an old test run when you have a newer one): safe.
- Whole files that were read "just in case": candidates for eviction.
- The original instruction or the current plan: **never evict these.** Losing them is what causes the agent to drift.

The worst eviction failure is "the agent forgot the task." This is almost always because the task statement got pushed out of the window by accumulating tool output. A good harness pins the task at the top and never evicts it. If you're seeing drift in a long task, this is the first thing to suspect.

### 5. Retrieval — fetching the right thing on demand

For anything beyond a small project, you can't pre-load every relevant file — the window won't fit. So the harness needs to retrieve things on demand: a search of the codebase, a grep for a symbol, a lookup of a type definition. This is where things like **agentic RAG** come in (glossary, Chapter 12).

**RAG** (Retrieval-Augmented Generation) is the general idea of "fetch relevant stuff and put it in the context before answering." Classic RAG was a one-shot retrieval — run a search, dump the top-K results in, answer. **Agentic RAG** is the loop version: the agent decides what to retrieve, retrieves it, looks at it, decides if it needs more, retrieves more, iterates. The smartest 2026 systems combine an agentic loop with a graph-backed knowledge base so the agent can navigate relationships, not just keyword hits.

For most day-to-day AI coding, the harness handles retrieval internally (it greps your repo, reads files on demand). For larger or cross-repo work, dedicated tools like a code knowledge graph — indexed ahead of time and queried during the loop — make a big difference. The principle is the same either way: **don't make the model guess what it can't see. Give it a way to look it up.**

---

## The practical moves

Here's what good context engineering looks like at the keyboard:

### Move 1 — Point, don't describe

Bad: "in the auth file, the function that checks passwords."
Good: "in `src/auth/password.ts`, the `verifyPassword` function on line 42."

The first makes the agent search and guess. The second puts the exact thing in the window. Direct pointers almost always beat descriptions.

### Move 2 — Provide a reference example

If you want the agent to match a pattern that exists in your codebase, paste that pattern. "Match the style of `src/components/Button.tsx`" is context engineering. Few-shot is context engineering.

### Move 3 — Scope the task explicitly

Bad: "improve the auth."
Good: "in `src/auth/login.ts`, the `loginWithPassword` function returns a 500 when the database is slow. Add a timeout and return a 503 instead. Don't touch the session logic."

The scoping is context engineering: you've told the agent what's in scope, what's out, and what success looks like. Without it, the agent will do something adjacent to what you wanted and you'll have to course-correct.

### Move 4 — Use rules files for the stable stuff

If you find yourself repeating the same instruction ("we use Vitest, not Jest," "don't add comments," "imports are sorted alphabetically") then it belongs in a rules file (Chapter 9), not in your per-task prompt. The harness loads the rules file into context automatically, so you don't have to restate it every time and you don't risk the model forgetting.

### Move 5 — Use subagents for noisy sub-tasks

Some sub-tasks generate a lot of context that's useful briefly and useless afterward — searching the whole codebase, running a big test suite, reading a long log. A good harness lets you spin up a **subagent** for that work: a separate context window that does the noisy thing, returns a short answer, and is then discarded. The main context never fills with the noise. This is subagent orchestration, and it's one of the most powerful context-engineering moves available. (Chapter 9 has more on this.)

### Move 6 — Refresh when the context is stale

If you've been working with an agent for an hour and it's started drifting — repeating itself, forgetting decisions, contradicting things it knew earlier — the context window is the problem, not the model. Start a fresh session, paste in the *current* state of the task and the *current* files, and proceed. Don't try to repair a polluted context; replace it.

---

## Why this chapter is the most important one in the guide

You can use the best model in the world, in the best harness, with the best MCP servers and the best skills, and if the context window contains the wrong stuff, the agent will produce wrong output. Conversely, a mid-tier model with a beautifully curated context will often outperform a frontier model with a polluted one.

Almost every "the AI is being dumb" moment is, on inspection, a context problem:

- It edited the wrong file → it didn't have the right file in context, or it had the wrong one and guessed.
- It forgot the constraint → the constraint was evicted or never stated.
- It's looping on the same error → the error output is being evicted between turns.
- It used the wrong pattern → it didn't have a reference example in context.
- It contradicted something it said earlier → the earlier turn is gone.

Every one of those is fixable with context engineering, not with a fancier model or a cleverer prompt. That's why this chapter exists, and that's why the field has largely moved on from "prompt engineering" to "context engineering" as the name for the actual skill.

The next two chapters are about extending what the agent can reach — Chapter 7 on MCP (giving it new tools), Chapter 8 on skills (giving it packaged know-how). Both are, in a sense, more context engineering: ways to put the right thing in the window at the right time without you having to do it by hand every task.

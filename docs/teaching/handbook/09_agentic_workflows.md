# Chapter 9 — Agentic Workflows: Letting AI Do More

> An **agentic workflow** is when you give the AI a task and let it run on its own — planning, calling tools, checking results, and iterating until done. This chapter explains when to use it and the patterns people use.

---

## The Simple Version

Normally, you type one thing to the AI, it gives one answer, and you decide what to do next. That is a **chat**.

An **agentic workflow** is different: you give the AI a task, and it runs the **agentic loop** (see [Chapter 2](02_how_ai_tools_work.md)) on its own — observe, reason, act, check, repeat — until the task is done or it gets stuck and asks you for help.

The AI is not just answering. It is *doing*.

---

## When to Use an Agentic Workflow

Use an agentic workflow when the task has three properties:

1. **Multi-step** — the task cannot be done in one shot. It requires reading, editing, testing, iterating.
2. **Verifiable** — there is a concrete signal the AI can check: a test passing, a build succeeding, a diff looking right.
3. **Bounded** — you can describe the "done" condition clearly enough that the AI knows when to stop.

If any of these is missing, use direct chat instead:

- **Single-shot question** (what does this function do?): chat is faster.
- **Unverifiable creative task** (write a marketing email): chat gives you output to edit yourself.
- **Unbounded task** ("improve the codebase"): the AI will thrash. Narrow the scope first.

---

## The Patterns

Here are the common patterns people use. You do not need to memorize them — just know they exist.

### Pattern 1: Direct Edit

The simplest pattern. You ask the AI to make a change, it edits the file, you review the result.

```
You: rename getUserData to fetchUserProfile everywhere
AI: [runs grep, edits 7 files, runs tests, reports]
```

Use this for mechanical, well-scoped changes.

---

### Pattern 2: Plan Then Execute

For non-trivial tasks, ask the AI to plan first. You approve the plan, then it executes.

```
You: add pagination to the users list endpoint. Show me a plan first.
AI: [reads the code, writes a plan]
  1. Add page and pageSize query params to the route schema.
  2. Modify the query in userRepo.list() to accept offset/limit.
  3. Update the response shape to include total and page.
  4. Add tests in users.test.ts.
  5. Update the API doc.
You: looks good, go.
AI: [executes each step, runs tests, reports]
```

This catches scope creep early. It is cheaper to reject a plan than to undo 12 file edits.

---

### Pattern 3: Subagent Delegation

When a task has independent parts, the main AI can spawn **subagents** to work in parallel. Each subagent gets its own context window, does its piece, and returns a result. The main AI then assembles.

Example: "Refactor the auth module and update the docs."

- Subagent A: refactor `src/auth/` (reads code, edits, runs auth tests).
- Subagent B: update `docs/auth.md` (reads the new code, rewrites the docs).
- Main AI: verifies both are consistent and the build passes.

Use subagents when:

- The parts are truly independent (otherwise they will conflict on the same files).
- Each part needs a lot of context (subagents keep the main context clean).
- You want parallelism (multiple subagents can run at once).

---

### Pattern 4: Explore Then Edit

For unfamiliar codebases, the first phase is exploration (read-only), the second is editing. Splitting them prevents the AI from making changes based on a misunderstanding.

```
Phase 1 (Explore):
  AI: [reads package.json, README, directory tree, key files]
  AI: "I now understand the structure. Where would you like me to start?"

Phase 2 (Edit):
  You: start with the auth module.
  AI: [makes changes, runs tests]
```

This mirrors what a human engineer does on day one at a new job.

---

### Pattern 5: Verify and Loop

The AI makes a change, runs the verification (tests, build, lint), reads any failure, and iterates until green.

```
AI: [edits code]
AI: [runs npm test] -> 2 failures
AI: [reads failures, edits code]
AI: [runs npm test] -> 1 failure
AI: [reads failure, edits code]
AI: [runs npm test] -> all pass
AI: done.
```

This is where the agentic loop shines: the AI can catch its own mistakes without a round trip to you. Set a cap on iterations (3-5) to avoid infinite loops on problems that need human judgment.

---

## Context Management

The most common failure mode of a long agentic session is **context exhaustion**: the window fills, important early context drops, and the AI starts repeating itself or losing track.

Tactics:

- **Re-scope mid-session**: if the task drifts, stop the AI, write a fresh prompt with the current state, and continue.
- **Use subagents for big reads**: instead of reading a 10,000-line log into the main context, have a subagent read it and return a summary.
- **Checkpoint with git**: commit after each meaningful step. If the AI goes off the rails, you can reset to the last good state.
- **Watch the token counter**: most tools show context usage. When you cross 60-70%, start wrapping up or start a fresh session.

---

## When to Intervene

Intervene immediately when:

- The AI edits files you did not ask it to touch.
- The AI runs commands with side effects (deploys, emails, payments) without confirmation.
- The AI is stuck in a loop (same failed action twice).
- The AI's plan diverges from the task.

Do NOT intervene every step. The point of an agentic workflow is to let the AI run. If you micromanage every action, you lose the benefit and may as well drive each tool call yourself.

---

## The Big Picture

- An **agentic workflow** lets the AI run on its own: plan, act, check, repeat.
- Use it for **multi-step, verifiable, bounded** tasks.
- Common patterns: direct edit, plan-then-execute, subagent delegation, explore-then-edit, verify-and-loop.
- Watch the **context window** — long sessions can exhaust it.
- Intervene when the AI goes off scope or gets stuck in a loop. Let it run the rest of the time.

Continue to [Chapter 10 — The Tools People Use](10_the_tools_people_use.md).

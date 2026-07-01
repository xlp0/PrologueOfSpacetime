---
concept: Safe autopilot vs human approval guardrails
tags: [koo-project, harness, guardrails, trust, agents]
source: ChatGPT convs
---

# Safe Autopilot vs Human Approval

## Insight
A decent harness separates actions into two tiers. This matters because Ilham already spotted the obvious problem with full automation — "I don't trust it to apply on my behalf." Correct. You shouldn't.

**Safe autopilot (agent does without asking):**
- scrape job listings / market news
- summarize job descriptions
- draft tailored resume/cover letter
- rank jobs by fit
- prepare application packets
- fill forms *up to review step*
- create git branches / draft PRs
- run tests, log results

**Human approval required (agent must ask first):**
- clicking "Submit" on any application
- sending emails
- deleting files
- pushing to production
- spending money
- trading
- anything that creates external obligations

This separation is half the game of building a real agent. Without it, you either (a) have a toy that can only summarize, or (b) have a reckless system that submits 500 garbage applications overnight while you sleep. The harness's job is to make the safe-autopilot tier *stateful and resumable* (continue yesterday's job-search batch, resume half-finished code refactor, compare today's filings with last week's, keep a queue of already-processed companies) while strictly gatekeeping the human-approval tier behind explicit confirmation.

This is what upgrades "Here's a prompt and some files" to "Take a goal, inspect the environment, plan steps, call tools, store notes, retry failures, checkpoint progress, and ask me only when needed." Working memory stores what the agent tried, which files it changed, what failed and why, what assumptions it made, current subtask state — examples: "Resume tailoring run #4 failed because PDF parser dropped bullet formatting"; "User prefers not to auto-submit applications"; "For McKinsey-style cover letters, use the conservative template, not the startup one." That's not romance-novel memory; that's **operational memory**.

## Context
Came up 2026-06-25 (Harness Explanation). Ilham had built an agent before that scrapes jobs and tailors resume/cover letter, but "avoiding that cuz I dont trust it as much."

## Related
- [[harness-vs-model-concept]]
- [[three-concrete-stacks-to-build]]
- [[agency-of-one-job-search-reframe]]
- [[resume-gpt-custom-instructions-workflow]]
- [[koo-project-highlights]]

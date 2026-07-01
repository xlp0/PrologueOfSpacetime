---
title: 'Chapter 1 — What Is AI Coding?'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 1
liberal_art: Trivium-Rhetoric
audience: professional
---

# Chapter 1 — What Is AI Coding?

## The short answer

AI coding is using a large language model (LLM) to write, edit, review, or explain software — usually through a tool that wraps the model with file access, a terminal, and the ability to take actions on your behalf. The model is the brain; the tool around it is the body. Both matter.

That sentence would have been nonsense in 2019. In 2026 it is how a large and growing share of professional developers spend their day.

---

## How we got here, in three eras

If you want to understand the vocabulary people use today, it helps to know the arc. Three loosely defined eras, each with its own dominant word:

### 1. The autocomplete era (2021–2023)

GitHub Copilot shipped in 2021 as a VS Code extension that finished your line, then your function. It was magical and also limited: it saw roughly the file you had open, plus a little context, and it predicted the next tokens. You were always the one typing. The model never ran a command, never opened a file, never asked a clarifying question.

The word of this era was **autocomplete**. Useful, but fundamentally passive.

### 2. The chat / vibe coding era (2023–mid 2025)

ChatGPT landed in late 2022. Within a year, every IDE had a chat panel where you could paste an error, ask for a function, or describe a feature in plain English and get code back. The model was now writing whole functions, whole files, sometimes whole small apps. Andrej Karpathy gave this style a name that stuck: **vibe coding** — you describe the vibe of what you want, the AI produces code, you accept or reject.

The defining trait was still that **you** were the executor. The AI generated text; you copied it into your editor, ran the tests, fixed the errors, and pasted the failures back. It was a conversation, not an agent.

### 3. The agentic era (mid 2025 onward)

At some point the tools stopped just *suggesting* code and started *doing things*. Claude Code, Cursor's agent mode, Codex CLI, opencode — these don't just predict the next line. They read your codebase, edit files directly, run shell commands, run tests, read the test output, fix what broke, and iterate. The model is now wrapped in what people call a **harness**: the scaffolding that turns a pure text predictor into something that can act in a loop.

Karpathy named the successor too: **agentic engineering**. You stop writing code line by line and start orchestrating agents that write code. You own the architecture, the tests, and the review. The agents do the typing.

This is where the vocabulary you'll see in job postings and architecture docs comes from. The rest of this guide is mostly about this era.

---

## So what counts as "AI coding" now?

A useful working definition for 2026:

> **AI coding is software development where an LLM, operating inside a harness that can read files, edit files, and run commands, does a meaningful share of the actual production of code — under the direction and review of a human who owns the result.**

Three things to notice in that definition:

1. **The model is inside a harness.** A raw LLM in a chat box is not "AI coding" in the modern sense — it's just chat. The harness is what makes it agentic. (Chapter 2 and Chapter 3 cover this in depth.)
2. **It does a meaningful share of the production of code.** Not all of it. The line moves depending on the task and the developer's trust level, but the AI is genuinely writing code that ships, not just suggesting a variable name.
3. **A human owns the result.** This is the part Chapter 11 is about. "The AI wrote it" is not a defense. The human who merged the pull request owns what's in main.

---

## Why it matters

Three reasons, in increasing order of importance:

### It changes what the job is

When the model writes most of the code, the scarce skill stops being "can you type the syntax correctly" and becomes "can you describe the system well enough that the right code gets produced, and can you verify it's correct." That's a different job. Chapter 6 calls the new skill **[[static-vs-dynamic-context|context engineering]]** — the deliberate curation of what the AI sees.

### It changes who can build

A senior engineer with a good harness can ship like a small team. A junior engineer can build things that would have been out of reach a year ago. Both of those are real and both of them come with the same caveat, which is that the gap between "it works" and "I understand why it works" is now the dangerous part.

### It changes what you are responsible for

When you wrote every line, you were implicitly responsible for every line. When the model writes half of them and you accept the diff, you are *explicitly* responsible for every line — including the ones you didn't read carefully. Most of the bad outcomes from AI coding come from people not updating their sense of ownership to match the new reality. Chapter 11 is the most important chapter in this guide for exactly this reason.

---

## What it is not

A few things people call "AI coding" that the rest of this guide will *not* treat as the same thing:

- **A chat box where you paste errors.** Useful. Not agentic. Belongs to the previous era.
- **No-code / low-code platforms.** Different thing. AI coding produces real source code in real languages that you read, version, and maintain.
- **"Letting the AI do your job."** Not the model being advocated here. The agentic era still has a human in the loop; the human's role just shifts up the stack to architecture, verification, and review. Pure vibe coding — accept whatever it spits out, ship it, hope — is a real phenomenon and a real problem, and the reason "agentic engineering" exists as a distinct term is to draw a line against it.
- **A way to skip understanding your codebase.** The opposite is true. To steer an agent well you have to understand the codebase better than you did when you were just editing one file at a time.

---

## The mental shift, in one sentence

You are moving from **writing code** to **directing, reviewing, and verifying code that an AI produces inside a harness you control.** Everything in the rest of this guide — the stack, the context window, the prompting styles, the [[mcp-anthropic-standard|MCP]] servers, the skills, the workflows, the responsibility — is in service of that one shift.

Turn the page.

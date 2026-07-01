---
title: 'Chapter 2 — How AI Tools Work'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Logic]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 2
liberal_art: Trivium-Logic
audience: professional
---

# Chapter 2 — How AI Tools Work

## The one mental model

If you only remember one thing from this chapter, make it this:

> An AI coding tool is a **model** wrapped in a **harness**, running in a **loop**, against a **context window** full of stuff the harness has gathered for it.

Four pieces. Every tool — Claude Code, Cursor, opencode, Codex, Copilot — is some variation on those four. Once you can name them, every other conversation about AI coding gets easier.

Let's take them one at a time.

---

## 1. The model

The model is the LLM itself: the thing that takes text in and predicts text out. GPT-4-class models, Claude, Gemini, the open-weights models like Llama or DeepSeek — these are the models. The model is the only part that is genuinely "the AI." Everything else is plumbing.

Two things to keep in mind about the model:

- **It is stateless.** It has no memory between calls. Everything it "knows" about your project must be handed to it fresh on every single request, inside its context window. This is the single most important fact about LLMs and the source of half the engineering around them.
- **It is a text predictor.** Not a compiler, not a runtime, not a database. It produces tokens that *look like* the next thing a human would write. When it produces correct code, it is because the correct code was the most likely continuation given the context. When it produces wrong code, same reason.

The model cannot, by itself, read a file, run a command, or remember what you asked five minutes ago. For any of that it needs the harness.

---

## 2. The harness

The **harness** is the scaffolding around the model that turns it from a text predictor into something that can act. Different teams mean slightly different things by the word, but in practice a harness is the collection of:

- A way to **format the user's request and the available context** into a prompt the model can read.
- A way to **call the model** (an API request) and get a response back.
- A way to **parse the model's output** for things like "I want to edit this file" or "I want to run this shell command" — what the field calls **tool calls** or **function calls**.
- A way to **execute those tool calls** against the real world: read files, write files, run shell commands, hit HTTP endpoints, query databases.
- A way to **feed the results back** into the next prompt, so the model can react to what just happened.
- Often: **permissions and guardrails** (what the harness is allowed to do without asking), **memory** (what to remember across turns), and **orchestration** (how to coordinate multiple agents or sub-tasks).

The harness is where almost all the engineering happens in 2026. A bad harness in front of a great model produces a frustrating tool. A great harness in front of a mediocre model can produce a surprisingly usable one. People who used to write "prompt engineering" blog posts now write "harness engineering" blog posts, and they're talking about this layer.

The harness is also what people mean when they say things like "the runtime around the LLM can outshine the model itself." That's a real claim, not marketing.

---

## 3. The context window

The context window is the slab of text the model can see on any single call. Think of it as the model's working memory for that one request. It contains, in some order:

- A **system prompt** — instructions from the harness about how to behave.
- The **conversation so far** — your messages and the model's replies.
- **Tool results** — the contents of files it read, the output of commands it ran.
- Anything else the harness decided to include: rules from your project, snippets retrieved from elsewhere in the codebase, results from a web search.

The context window is **finite**. It is measured in **tokens** (roughly: words and pieces of words — Chapter 4 explains tokens properly). When the window is full, something has to leave. What leaves, and in what order, is one of the most important decisions a harness makes, and it's the entire subject of Chapter 6.

The window being finite is not a bug to be fixed by waiting for bigger models. It is a permanent constraint that shapes how the whole stack is designed. Even a model with a million-token window fills up fast when the harness is dumping file contents, command output, and tool results into it on every turn of the loop.

---

## 4. The loop

Here is what actually happens when you type "fix the failing test" into an agentic tool:

1. The harness gathers context: the failing test output, the test file, maybe the file under test, maybe a relevant rule from your project.
2. The harness packs all that into a prompt, plus your instruction, plus a description of the tools available ("you may read files, you may edit files, you may run shell commands").
3. The harness sends the prompt to the model.
4. The model responds. The response is text, but it may contain structured **tool calls** — for example: "edit `auth.ts`, lines 42–58, replace with this" or "run `npm test`."
5. The harness executes the tool calls and collects the results.
6. The harness packs the results back into the context, along with everything from step 1, and sends a *new* request to the model.
7. The model responds again. Maybe it makes another tool call. Maybe it says "done, the tests pass."
8. Repeat until the model stops calling tools, at which point the harness shows you the final answer.

That cycle — gather, prompt, model, parse, execute, feed back, prompt again — is **the agentic loop**, and it is the heartbeat of every modern AI coding tool. A single "fix the failing test" instruction might run the loop five times or fifty times before it returns control to you.

This is why the harness matters so much. The loop only works if the harness can reliably parse tool calls, execute them safely, and decide what to keep in context as the loop spins. A model that's brilliant at writing code but only gets called inside a harness that drops important context will look stupid. A model that's merely okay but runs in a harness that curates context beautifully can look like magic.

---

## Putting it together: the picture to hold in your head

```
   you
    │
    │  "fix the failing test"
    ▼
┌──────────────────────────────────────────┐
│                  HARNESS                   │
│                                            │
│   context window  ◄──── gather (files,     │
│   ┌────────────┐       rules, tool defs,   │
│   │ system     │       prior results)      │
│   │ prompt     │                          │
│   │ history    │                          │
│   │ tool defs  │                          │
│   │ file: x.ts │                          │
│   │ output: …  │                          │
│   └────────────┘                          │
│         │                                  │
│         │  prompt                         │
│         ▼                                  │
│   ┌────────────┐                          │
│   │   MODEL    │  ◄── stateless text       │
│   │  (the LLM) │      predictor            │
│   └────────────┘                          │
│         │                                  │
│         │  response + tool calls          │
│         ▼                                  │
│   parse → execute (read/write/run)         │
│         │                                  │
│         └──── results back into context ───┘
│                                            │
│   (repeat until model stops calling tools) │
└──────────────────────────────────────────┘
    │
    ▼  final answer back to you
   "fixed — auth.ts line 47, tests pass"
```

That is the whole game. Every chapter after this is about one part of that picture: Chapter 3 names the layers (model, harness, client, server), Chapter 4 is about the context window and its tokens, Chapter 5 is about how to write the prompts that go in, Chapter 6 is about what the harness chooses to put in the window, Chapter 7 is about extending what the harness can do, and so on.

---

## Why this mental model matters

Once you have it, a lot of confusing things become clear:

- **"The AI forgot what I told it."** It didn't forget. It has no memory. The harness stopped including your earlier message in the context window — probably because the window filled up. (Chapter 4 and Chapter 6.)
- **"It works in Claude Code but not in raw ChatGPT."** Of course — Claude Code has a harness that reads your files and runs your tests. Raw ChatGPT has no harness. Same model, different body. (Chapter 3 and Chapter 10.)
- **"Why did it edit the wrong file?"** Because the harness gave it a context window in which the wrong file looked like the right thing to edit. The model can only act on what's in the window. (Chapter 6.)
- **"It keeps running the same broken command."** The loop is spinning but the context isn't being curated well — the failure output is probably being evicted or truncated, so each iteration looks to the model like the first one. (Chapter 6.)
- **"Is it safe to let it run commands?"** Only if the harness has good permissions and sandboxing. This is a harness question, not a model question. (Chapter 11.)

If you catch yourself thinking "the AI did X," try rephrasing it as "the harness, running the loop against this model, with this context window, produced X." It's clumsier English, but it's more honest about what happened, and it tells you where to look when something goes wrong.

---

## One last thing: the model is not the tool

When someone says "I built this with Claude," what they almost always mean is "I built this with a tool whose harness called a Claude model." The model is one ingredient. The harness, the context it gathered, the permissions it had, the rules files it read, the [[mcp-anthropic-standard|MCP]] servers it could talk to, the skills loaded into it — all of those are part of the actual tool that produced the result.

This is why Chapter 3 exists. The stack has layers, and knowing which layer does what is the difference between understanding your tools and being mystified by them.

---
title: 'Chapter 2 — How AI Tools Work'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Logic]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 2
liberal_art: Trivium-Logic
audience: beginner
---

# Chapter 2 — How AI Tools Work

> Before we talk about tools and workflows, you need a clear picture of what an AI coding tool actually *is*. Most confusion comes from having the wrong picture in your head.

---

## The Simple Version

An AI coding tool has two main parts:

1. **The model** — the "brain." This is the AI itself. It reads text and writes text. That is all it does.
2. **The harness** — the "body." This is the software around the model. It gives the model tools, files, and a way to talk to you.

The model is smart but cannot do anything on its own. The harness is what turns the model into something useful.

---

## The Model: The Brain

A **model** (also called an LLM, or Large Language Model) is a computer program that takes text in and gives text back. You give it a question, it gives you an answer. You give it code, it explains the code. You give it a bug, it suggests a fix.

Here is the important part: **the model can only write text.** It cannot read a file. It cannot run a command. It cannot search the web. It can only read what you paste into it and write back a response.

Two more things to know about models:

1. **They have no memory between conversations.** Every time you start a new chat, the model starts fresh. It does not remember yesterday's conversation. Anything you want it to know has to be in *this* conversation.

2. **They are confident even when they are wrong.** A model can write something that sounds very sure but is actually incorrect. This is called **hallucination**, and it is why you always need to check the AI's work. (More on this in [Chapter 11: Code of Conduct](11_code_of_conduct.md).)

---

## The Harness: The Body

A **harness** is the software that wraps the model and turns it into a usable tool. Think of it this way:

- The **model** is the engine.
- The **harness** is the whole car — steering wheel, brakes, dashboard, seatbelt.

opencode, Cursor, Claude Code, and Aider are all **harnesses**. They use different models underneath (Claude, GPT, Gemini, Llama), but they all do the same fundamental job: take a smart-but-limited model and give it the parts it needs to actually work on your code.

The harness gives the model:

- **Tools** — read a file, edit a file, run a shell command, search the web.
- **A chat window** — so you can talk to it.
- **Safety checks** — so it does not do something dangerous without asking you.
- **Memory within a session** — so it remembers what you said earlier in the same conversation.

When you pick a tool like opencode or Cursor, you are picking a **harness**, not a model. Most harnesses let you swap the model underneath. The harness is what shapes your experience.

---

## The Agentic Loop

Here is the thing that makes modern AI tools feel different from a chatbot. It is called the **agentic loop**:

```
1. Observe   - read the task, look at relevant files
2. Reason    - decide what to do next
3. Act       - call a tool: edit a file, run a command
4. Observe   - read the result of the action
5. Repeat    - until the task is done or the agent gets stuck
```

Without tools, the loop cannot *act*. It can only write text, and you have to do everything it suggests yourself. With tools, the loop can run on its own for many steps before needing your help.

Here is what this looks like in real life:

1. You say: "Fix the bug in login.ts."
2. The AI reads `login.ts` to see what is there.
3. It figures out the bug.
4. It edits the file.
5. It runs the tests to see if they pass now.
6. If they fail, it reads the error, fixes the code again, and reruns the tests.
7. When the tests pass, it stops and tells you.

That whole sequence is the agentic loop in action. The AI is not just answering a question — it is *doing* something, step by step, until the job is done.

---

## Why Tools Matter More Than Prompting

A common beginner mistake is to focus on writing the perfect prompt. But the prompt is only half the story. The **tools** the AI has access to matter just as much, often more.

Here is why: a mediocre prompt with good tools (file search, run tests, edit code) will outperform a brilliant prompt with no tools. Why? Because with tools, the AI can **check its own work**. It can read the file, make a change, run the test, see if it passes, and fix it if not. Without tools, it just guesses and hopes.

The professional shift is this: **stop trying to write the perfect prompt, and start making sure the AI has the right tools.** Then almost any reasonable prompt works.

---

## The Big Picture

- A **model** is the brain — text in, text out.
- A **harness** is the body — tools, files, safety, chat.
- The **agentic loop** is what makes the tool feel alive — observe, reason, act, repeat.
- **Tools** are what let the AI actually do things, not just talk.

Now that you have the picture, the next chapter explains the four layers of an AI coding tool in more detail.

---

## 2.6 A Brief History of AI Coding Tools

To see where AI coding tools are today, it helps to look at how we got here. The change was fast — about five years turned a research demo into the tools you use right now.

### Before 2021: Brains, No Body

The big breakthrough was the **transformer**, a new way to build language models, introduced by Google researchers in 2017. By 2020, OpenAI had built **GPT-3**, a model so large it could write essays, answer questions, and even draft code from a prompt. But there was a catch: it lived behind a chat box. You had to copy your code in, copy the answer out, and do everything yourself. The model was the brain, but there was no body attached. ([Wikipedia: Large language model](https://en.wikipedia.org/wiki/Large_language_model))

### 2021: The First Real Coding Tool

In 2021, **GitHub Copilot** launched as the first AI tool made specifically for programmers. It was built on **Codex**, a version of GPT-3 trained on billions of lines of code. Copilot lived inside your editor and suggested the next line as you typed. This was a big shift — instead of asking a chatbot and pasting code back, the AI was right there where you worked. ([GitHub Copilot](https://github.blog/news-insights/product-news/github-copilot))

### Late 2022: ChatGPT Changes Everything

In November 2022, OpenAI released **ChatGPT**. Almost overnight, millions of people who had never used an AI were talking to one. For coding, this mattered in two ways: people saw the model was good enough to explain bugs and write small programs, and they got a taste of "talking to the AI" instead of just "getting autocomplete." But ChatGPT was still just a chat box — no tools, no files, no body. ([Wikipedia: Large language model](https://en.wikipedia.org/wiki/Large_language_model))

### 2023: Models Learn to Use Tools

In 2023, models gained **function calling** (sometimes called "tool use"). Instead of only writing text, the model could now say "I want to run this command" or "I want to read that file," and the harness would actually do it. This is the moment the agentic loop from earlier in this chapter became possible. The brain finally got hands.

### 2024–2025: The Agentic Loop Becomes Normal

By 2024 and into 2025, the loop was everywhere. Tools like Cursor, Aider, and opencode gave the model a file system, a terminal, and a chat window — then let it work in cycles: read, think, edit, run, repeat. In February 2025, Anthropic released **Claude Code**, an agent built to run straight from the terminal and edit whole projects on its own. The harness was no longer just fancy autocomplete. It was a body that let the model act. ([Claude Code](https://www.anthropic.com/news/claude-code))

### Today: Which Models Lead?

The strongest models for coding right now come from three labs:

- **Claude** (Anthropic) — especially the Sonnet and Opus versions, known for careful, long coding tasks.
- **GPT** (OpenAI) — GPT-4, GPT-4o, and the GPT-5 line, fast and broad.
- **Gemini** (Google) — strong on long files and large codebases.

Open-weight models like **DeepSeek** and **Llama** are catching up fast and let you run them on your own hardware. The brain keeps getting better; the harness is what decides how much of that brain you actually get to use. ([Wikipedia: Large language model](https://en.wikipedia.org/wiki/Large_language_model))

### The Pattern

Notice the shape of this history: the model came first, then a thin body (autocomplete), then a chat body (ChatGPT), then a real body with tools (the agentic loop). Each step did not replace the last — it added to it. Today's tools are all of those layers stacked together: a smart model, a real harness, and a loop that keeps going until the job is done.

---

Continue to [Chapter 3 — The Stack: Model, Harness, Client, Server](03_the_stack.md).

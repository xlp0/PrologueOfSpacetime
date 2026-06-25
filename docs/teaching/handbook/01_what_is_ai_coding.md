# Chapter 1 — What Is AI Coding?

> You have probably heard of ChatGPT. Maybe you have used it to write an essay, answer a question, or tell a joke. AI coding is the same idea, but for building software.

---

## The Simple Version

An **AI coding tool** is a computer program that helps you write, understand, and fix code. It uses a big AI model (like the one behind ChatGPT) to understand what you want, and then it helps you get there.

Think of it like a really smart friend who has read a lot of code and can help you figure things out. You describe what you want, and the AI suggests how to do it — or just does it for you, if you let it.

---

## Why People Use It

People use AI coding tools for three main reasons:

1. **To go faster.** Instead of typing every line yourself, the AI can write the boring parts. You focus on the interesting problems.

2. **To learn.** If you do not understand a piece of code, you can ask the AI to explain it. It is like having a tutor that never gets tired of your questions.

3. **To do things you could not do alone.** Maybe you have an idea for an app but do not know the language it should be written in. The AI can fill in the gaps in your knowledge.

---

## What Changed in the Last Few Years

A few years ago, AI was mostly an **autocomplete** — it would finish your sentence, but it could not really *do* anything. You typed, it suggested, you accepted or rejected. That was it.

Then three big things happened:

### 1. Tools (2023)

AI learned how to **use tools**. Instead of just writing text, the AI could call a function — read a file, run a command, search the web. This was a big deal. It meant the AI could actually *do things*, not just talk about them.

### 2. MCP (late 2024)

A standard called **MCP** (Model Context Protocol) was invented. Before MCP, every AI tool had its own way of connecting to things like GitHub or your files. MCP made it so one tool could work with many AI programs — like how a USB-C cable works with many different laptops.

### 3. Agentic Loops (2025)

AI tools started to **run on their own**. Instead of you typing one instruction and the AI doing one thing, you could give the AI a task and it would plan, act, check, and keep going until it was done (or until it got stuck and asked you for help). This is called an **agentic workflow**, and it is what makes modern AI coding tools feel different from a chatbot.

---

## The Big Idea

If your only experience with AI is typing questions into ChatGPT, you are at step zero. The tools people use today are at step three. This handbook is the path from zero to three — explained simply.

---

## What You Will Learn

By the end of this handbook, you will understand:

- What an AI coding tool actually is, and what the pieces are called.
- How AI "sees" text, and why that matters.
- Different ways to talk to AI (prompting styles).
- What MCP is and what people have plugged into it.
- What skills are and why they save time and money.
- When to let AI run on its own, and when to drive yourself.
- The tools people use (opencode, Cursor, Claude Code, and others).
- How to use AI responsibly — verification, security, honesty.

You will not learn how to build an AI model. You will not learn how to train one. You will learn what they are, what they can do, and how to think about them clearly.

---

## A Note on Tone

This handbook is written in plain language. No fancy jargon without explaining it. No assuming you already know things. If a word is new, we will define it the first time it appears, and you can always look it up in [Chapter 12: The Words You'll Hear](12_words_youll_hear.md).

---

## 1.5 The Landscape Today

The tools described in this chapter are not science experiments — they are how millions of people write software right now. Here is a snapshot of where things stand in mid-2026.

### How big is this?

Big. [OpenCode](https://opencode.ai), a free open-source agent covered later in this handbook, reports over 7.5 million developers using it every month. GitHub Copilot alone has over 1 million paying subscribers. Cursor, a popular commercial editor, [doubled its recurring revenue to $2 billion in three months](https://www.bloomberg.com/news/articles/2026-03-02/cursor-recurring-revenue-doubles-in-three-months-to-2-billion) in early 2026. AI coding is no longer a niche — it is a normal part of how software gets written.

### The four kinds of tools

Most AI coding tools fall into one of four buckets. They overlap, but the categories are useful:

1. **Chat assistants** (ChatGPT, Claude.ai). You talk to the AI in a chat window. Good for asking questions, drafting small pieces of code, and learning. The AI cannot see your files unless you paste them in.

2. **Inline completion** (Cursor Tab, GitHub Copilot autocomplete). The AI watches you type and finishes your line — or your next few lines — as you go. It is the modern version of autocomplete, but smarter.

3. **Agentic CLIs** (opencode, Claude Code, OpenAI Codex CLI). You run these in a terminal. They can read your files, run commands, and edit code across a whole project on their own. This is the "agentic loop" from earlier in the chapter, in tool form.

4. **Editor-integrated agents** (Cursor, Claude Code in your IDE). A full code editor with the AI baked in. You can ask it to plan a feature, edit multiple files, run tests, and explain what it changed — all in one place.

### What changed in the last year

A few things matter to a beginner:

- **New models.** Anthropic released [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) in May 2026, with stronger coding and agentic-task performance. OpenAI shipped the [GPT-5 family](https://openai.com/news/) (5.3, 5.4, 5.5). Both are noticeably better at long, multi-step coding tasks than a year ago.

- **Agents moved into the editor.** Cursor launched [Cursor 3](https://cursor.com/blog/cursor-3) in April 2026 as a "unified workspace for building software with agents," and introduced [Composer 2.5](https://cursor.com/blog/composer-2-5), a model tuned for long-running agentic tasks. The pattern — AI that runs many steps on its own, inside your editor — is now standard.

- **Cloud agents.** Tools like [Cursor Cloud Agents](https://cursor.com/blog/cloud-agent-lessons) and OpenAI Codex can run tasks on a server in the background, so you can kick off a long job and keep working. This was rare a year ago.

- **Open source went mainstream.** [OpenCode](https://opencode.ai) crossed 160,000 GitHub stars and is free to use, with optional paid models. You no longer have to pay to try a serious agent.

### What it costs

- **Free.** [OpenCode](https://opencode.ai) is open source and ships with free models. You can also log in with an existing GitHub Copilot or ChatGPT Plus account at no extra cost.

- **Around $20/month.** A paid subscription to ChatGPT Plus, Claude Pro, or a coding-specific tool like Cursor typically runs about $20 per month. That covers most personal use.

- **Pay-as-you-go (API).** If you write your own scripts and call the AI model directly, you pay per request — usually a few cents to a few dollars per million words of text in or out. This is how power users and teams build custom tools.

The big picture: the field has moved from "AI finishes your sentence" to "AI does the task." Prices have come down, free options are good, and the hardest part is no longer getting access — it is learning to use these tools well. That is what the rest of this handbook is for.

---

Ready? Let's go to [Chapter 2 — How AI Tools Work](02_how_ai_tools_work.md).

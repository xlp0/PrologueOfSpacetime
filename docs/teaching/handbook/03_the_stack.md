# Chapter 3 — The Stack: Model, Harness, Client, Server

> When people talk about AI coding tools, they use a lot of words that sound similar but mean different things. This chapter explains the four layers and what each one is **for**.

---

## The Simple Version

An AI coding tool is made of four layers, stacked on top of each other:

1. **Model** — the brain.
2. **Harness** — the body around the brain.
3. **MCP Client** — the part of the body that talks to outside services.
4. **MCP Server** — a separate program that exposes a specific service.

You are the user at the top. You talk to the harness, which runs the model, which calls tools provided by MCP servers. Each layer has one job.

---

## The Four Layers

| Layer | What it is | What it is for | Examples |
| :--- | :--- | :--- | :--- |
| **Model** | The trained AI. Text in, text out. | Raw intelligence — reasoning, writing, planning. | GPT-4, Claude, Gemini, Llama. |
| **Harness** | The software that wraps the model into a usable tool. | Tools, file access, safety, the chat, the agentic loop. | opencode, Claude Code, Cursor, Aider. |
| **MCP Client** | The part of the harness that talks to MCP servers. Often just the harness itself. | Connecting the AI to outside tools and data. | The MCP client built into opencode, Cursor, Claude Desktop. |
| **MCP Server** | A separate program that exposes tools via the MCP protocol. | Giving the AI access to a specific system (GitHub, your files, a database). | server-github, server-filesystem, server-postgres. |

---

## A Real Example

Let's say you are using opencode to fix a bug. Here is what each layer is doing:

1. **You** type: "Fix the bug in login.ts."
2. **The harness (opencode)** receives your message. It uses its built-in tools to read `login.ts`.
3. **The model (Claude, GPT, etc.)** reads the file and figures out the bug. It tells the harness: "Edit line 42 to change this exception handler."
4. **The harness** makes the edit.
5. If the model needs to check something on GitHub — say, look at an issue — the **MCP client** inside the harness calls the **GitHub MCP server**, which talks to GitHub and returns the issue text.
6. **The model** reads the issue, adjusts its fix, and the harness applies the change.
7. **You** see the result.

Each layer did its job:

- The **model** reasoned.
- The **harness** gave the model tools and safety.
- The **MCP client** connected to outside services.
- The **MCP server** exposed GitHub to the AI.

---

## Why Knowing the Layers Matters

When something goes wrong, knowing which layer is responsible tells you where to look:

- **Wrong answer?** That is the model. Try a different model, or a clearer prompt.
- **Cannot read a file?** That is the harness. Check its file permissions.
- **Cannot connect to GitHub?** That is the MCP client or MCP server. Check the server is running and the credentials are right.
- **Slow?** Could be any layer — the model is slow to respond, the harness is doing too much, the MCP server is slow, or the network is slow.

If you do not know the layers, you cannot diagnose problems. You just say "the AI is broken" and give up. Knowing the layers turns "broken" into "the GitHub MCP server is not running, let me start it."

---

## The Model Is Not the Harness

This is the most common confusion. People say "I am using Claude" when they mean "I am using Claude Code" (a harness that runs the Claude model). Or they say "Cursor is smart" when they mean "the model Cursor is using is smart."

Two consequences:

1. **You can swap models.** Most harnesses let you pick the model. You can use Claude in Cursor, or GPT in opencode, or a local Llama model for privacy. The harness stays the same; the brain changes.

2. **You can swap harnesses.** You can use the same model (say, Claude Sonnet) in opencode, Cursor, or Claude Code. The brain is the same; the body — the tools, the safety, the workflow — is different.

This is why picking a harness is a bigger decision than picking a model. The model is the engine; the harness is the car. You spend your time in the car, not the engine.

---

## The Big Picture

- **Model** = brain (raw intelligence)
- **Harness** = body (tools, safety, chat)
- **MCP Client** = the body's hands (reaching out to services)
- **MCP Server** = the service (the thing being reached)

You do not need to memorize this. You just need to know that when someone says "the model is wrong," they mean the brain. When they say "the harness does not support that," they mean the body. When they say "the MCP server is down," they mean an outside service is unreachable.

## 3.5 Real-World Examples of Each Layer

Now let's look at real products you can actually download or use today. Here is what each layer looks like in the wild.

### Layer 1 — Models (the brain)

The model is the trained AI itself. Text in, text out. You pick which brain to use.

- **Claude Sonnet 4.5** — Anthropic's smart, fast model. Good at coding, writing, and following tricky instructions. Used inside Claude Code and many other harnesses.
- **GPT-5** — OpenAI's flagship model. Strong reasoning and chat. Powers ChatGPT and can be plugged into other harnesses too.
- **Gemini 2.5** — Google's model. Handles text, images, and code. Built into Google's tools and available to others.
- **Llama 4** — Meta's open model you can run on your own computer. Great for privacy, since your data never leaves your machine.

### Layer 2 — Harnesses (the body)

The harness wraps the model with tools, file access, safety, and the chat loop. This is what you actually install and use.

- **opencode** — Open source agent that runs in your terminal, IDE, or desktop. Works with any model from any provider.
- **Claude Code** — Anthropic's official harness for the Claude model. Built for long coding sessions and agentic work.
- **Cursor** — A code editor with the AI built in. You write code side-by-side with the AI in the same window.
- **Aider** — A lightweight terminal tool that edits your files inside git. Great for quick fixes and small projects.

### Layer 3 — MCP Clients (the body's hands)

The MCP client lives inside the harness. It speaks the MCP protocol to reach outside services. You usually do not pick this separately — it comes with the harness.

- **opencode's built-in MCP client** — Connects to any MCP server you list in your config file.
- **Claude Code's MCP client** — Same idea, inside Claude Code. Wires up GitHub, your files, databases, and more.
- **Cursor's MCP client** — Built into Cursor so the AI can reach external tools from inside the editor.
- **Claude Desktop's MCP client** — Inside the Claude desktop app, so Claude can read your local files and call services.

### Layer 4 — MCP Servers (the services)

These are separate programs that expose one system to the AI through MCP. Each server has one job.

- **filesystem** — Lets the AI read and write files in folders you allow.
- **github** — Lets the AI read issues, open pull requests, and search code on GitHub.
- **postgres** — Lets the AI run SQL queries against your Postgres database.
- **palmier-pro** — Lets the AI edit video timelines: add clips, captions, and generate media.
- **slack** — Lets the AI read and post messages in your Slack workspace.
- **puppeteer** — Lets the AI drive a real web browser, click buttons, and scrape pages.
- **brave-search** — Lets the AI run web searches through Brave's search API.

The same MCP server works with every client. Build it once, plug it into opencode, Cursor, Claude Code, or any other harness that speaks MCP.

---

Continue to [Chapter 4 — Tokens and the Context Window](04_tokens_and_context.md).

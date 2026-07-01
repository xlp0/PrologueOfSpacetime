---
title: 'Chapter 7 — MCP: Plugging Things In'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Grammar]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 7
liberal_art: Trivium-Grammar
audience: beginner
---

# Chapter 7 — [[mcp-anthropic-standard|MCP]]: Plugging Things In

> **MCP** stands for **[[mcp-anthropic-standard|Model Context Protocol]]**. It is a standard for connecting AI tools to outside systems — like your files, GitHub, a database, or a video editor. This chapter explains what MCP is, what it is for, and what people have plugged in.

---

## The Simple Version

Without MCP, every AI tool had its own way of connecting to things. To let an AI read your files, you wrote custom code. To let it talk to GitHub, you wrote different custom code. Every AI program, every integration, all bespoke.

MCP fixed this. It is a standard shape — like how USB-C is a standard shape for cables. Write the integration once, and it works with any AI tool that speaks MCP.

The analogy people use: **MCP is "USB-C for AI tools."** A more precise analogy: MCP is to AI tools what LSP (Language Server Protocol) is to code editors. One server, many clients.

---

## What MCP Connects

MCP connects an **AI tool** (the client) to an **outside system** (the server). The server exposes things the AI can use:

- **Tools** — things the AI can *do* (read a file, create an issue, run a query).
- **Resources** — things the AI can *read* (a file tree, a database schema, a list of open PRs).

The AI never talks to the server directly. The harness (the AI tool) mediates: it lists the tools to the AI, the AI decides which to call, the harness forwards the call to the server, the server returns a result, and the harness feeds the result back to the AI.

---

## The Four Concepts

| Concept | What it is | Example |
| :--- | :--- | :--- |
| **Server** | A program that exposes capabilities via MCP. Can run locally or remotely. | `server-filesystem` exposing your project folder. |
| **Client** | The AI tool that connects to servers. | opencode, Cursor, Claude Desktop. |
| **Tools** | Callable functions the server exposes. | `read_file(path)`, `create_issue(title, body)`. |
| **Resources** | Read-only data the server exposes. | A file tree, a database schema. |

---

## Why MCP Matters

Three reasons:

1. **Tool reuse.** A community-written GitHub server works with Claude Desktop, Cursor, opencode, and any other MCP client. You do not write a separate integration for each.

2. **Local-first by default.** Most MCP servers run on your machine. Your data does not leave your machine unless you choose a remote server. This matters for security and for speed.

3. **Composability.** You can run many MCP servers at once. The harness shows all their tools to the AI. The AI picks which to call.

---

## Example MCP Servers (What People Have Built)

To give you a sense of the range, here are some MCP servers that exist in the wild. These are illustrative — they show what is possible.

- **Filesystem server** — Exposes a folder on your machine so the AI can read, write, and search files. The most common starter server.

- **GitHub server** — Exposes GitHub: create issues, read pull requests, search code, comment on PRs. Lets the AI work with your project's social layer, not just the files.

- **Postgres server** — Exposes a Postgres database as read-only resources and query tools. The AI can answer "what does the users table look like?" without you pasting screenshots.

- **PalmierPro server** — Exposes a full AI-native video editor. The AI can inspect the timeline, add and trim clips, place text overlays, generate captions from spoken audio, generate AI images and video, search the media library by what is on screen or what was said, and export the cut. This is an example of an MCP server wrapping a complex creative application.

- **Slack server** — Exposes Slack: read channels, post messages, search history. Lets an AI summarize a channel or answer "what did the team decide this week?"

- **Puppeteer / Playwright server** — Exposes a headless browser: navigate to URLs, click, fill forms, take screenshots, extract text. Lets the AI do web automation.

- **Fetch server** — A simple server that retrieves a URL's content as markdown. The AI can read a web page without a full browser.

- **Memory server** — Exposes a persistent key-value store the AI can read and write across sessions. Useful for remembering user preferences or project context.

- **SQLite server** — Like the Postgres server, but for local SQLite files. Handy for inspecting an app's local database during development.

- **Brave Search / Google server** — Exposes web search. The AI can look up current information or research a problem it has not seen before.

- **Linear / Jira server** — Exposes a project tracker: read and create tickets, update status. Lets the AI connect code changes to the relevant task.

- **Sentry server** — Exposes error monitoring: list errors, stack traces, affected users. Lets the AI investigate a production bug by reading actual error data.

---

## The Pattern

Look at all those examples. The pattern is the same:

> An MCP server takes an existing system — a database, an API, an application, a service — and exposes it to the AI in a standard shape.

The AI does not learn a new integration for each. It just sees a list of tools and calls them. The server does the translation.

If you are wondering "can an MCP server expose X?" — the answer is almost always yes, if X has an API or a CLI or a file format you can read. People have written servers for everything from AWS to Figma to Spotify. The ecosystem is growing fast.

---

## The Big Picture

- **MCP** is a standard for connecting AI tools to outside systems.
- It is "USB-C for AI tools" — write once, use with any MCP-compatible client.
- A **server** exposes **tools** (things the AI can do) and **resources** (things the AI can read).
- The **client** (the harness) mediates between the AI and the servers.
- People have built servers for **everything** — files, GitHub, databases, Slack, browsers, video editors, project trackers, and more.

---

## 7.5 The MCP Ecosystem Today

MCP launched in **November 2024**, announced by Anthropic as an open-source protocol for connecting AI assistants to outside data and tools ([modelcontextprotocol.io](https://modelcontextprotocol.io)). In about 18 months it went from an idea to a real ecosystem with tens of thousands of servers.

### How many servers are out there?

Two community directories track the count:

- **mcp.so** lists roughly **22,700+ MCP servers** ([mcp.so](https://mcp.so)).
- **Glama** lists about **48,300+ servers** and updates daily ([glama.ai/mcp/servers](https://glama.ai/mcp/servers)).

The numbers differ because each directory counts differently — Glama includes more remote and niche servers. Either way, MCP grew from zero to tens of thousands of servers in under two years.

### The most popular servers

The most-installed servers are the ones you would expect — tools that let an AI touch files, code, browsers, and databases. On Glama, the official **Filesystem** server (by `modelcontextprotocol`) leads by a wide margin: about **321,000 weekly downloads** and **87,400+ GitHub stars** as of June 2026 ([glama.ai/mcp/servers](https://glama.ai/mcp/servers)).

The official reference repo at **github.com/modelcontextprotocol/servers** has about **87,700 stars** and **11,100 forks** — meaning thousands of developers copied it to build their own variants ([GitHub](https://github.com/modelcontextprotocol/servers)).

### Surprising servers

Because MCP just means "expose any system to an AI," people have plugged in some wild stuff:

- A **3D-printer** server — the AI designs a model in Blender and sends it straight to a printer ([modelcontextprotocol.io](https://modelcontextprotocol.io)).
- A **"Howtocook"** server that recommends recipes and plans meals, based on a programmer's home-cooking guide ([mcp.so](https://mcp.so)).
- Servers for **stock-market data**, **Amazon ad scraping**, **disability-insurance quoting**, **torrent search**, and **local SEO ranking** ([glama.ai/mcp/servers](https://glama.ai/mcp/servers)).

If a thing has an API or a CLI, someone has probably wrapped it in MCP.

### Where to find MCP servers

Three main places:

1. **[mcp.so](https://mcp.so)** — a community marketplace, easy to browse, with categories and featured servers.
2. **[glama.ai/mcp/servers](https://glama.ai/mcp/servers)** — a larger registry with filters by language, hosting type, and category.
3. **[github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** — the official reference repo. It now points you to **registry.modelcontextprotocol.io** for the full published list.

### Who maintains all this?

- **Anthropic** maintains the protocol itself and a small set of **reference servers** (Filesystem, Git, Memory, Fetch, Time, Sequential Thinking, Everything). The repo states: *"Managed by Anthropic, but built together with the community"* ([GitHub](https://github.com/modelcontextprotocol/servers)).
- **Companies** maintain servers for their own products — e.g. Brave runs the official Brave Search server, and Zencoder maintains the Slack server.
- **The community** maintains the vast majority. Anyone can write one and publish it to a registry.

The takeaway: MCP is no longer just an Anthropic project. It is an open standard with a real ecosystem behind it — built by Anthropic, companies, and hobbyists together.

---

## 7.6 A Concrete Example: Browsing mcp.so

Reading about MCP is one thing. Seeing the actual list of servers makes it click. Let's walk through [mcp.so](https://mcp.so), one of the community directories, and look at what is really there as of June 2026.

### When you visit mcp.so, you see...

A big banner that reads **"Find Awesome MCP Servers and Clients"**, and right under it a live counter: **"22,777 MCP Servers collected"** ([mcp.so](https://mcp.so)). That number is the whole ecosystem in one glance — over twenty thousand things you could plug into an AI tool. Below the banner sit a row of tabs: **Today**, **Featured**, **Latest**, **Clients**, **Hosted**, and **Official**. Think of it like an app store, except every "app" is an MCP server. There is also a **Submit** button in the top nav, because anyone can add their own.

### Each server entry shows...

A small card with three things:

1. **A name** — like "Playwright Mcp" or "Filesystem".
2. **A short description** — one sentence saying what the server does.
3. **A tag or badge** — like "Official" (maintained by Anthropic or the product's own company), "Hosted" (runs on a remote server, not your machine), or "Featured" (the directory's editors picked it out).

That's the whole card. No long README on the card itself — just enough to help you decide whether to click. Click the name and you land on a detail page with setup instructions and the install command.

### For example, a popular server might look like...

On the **Official** tab there is an entry called **Filesystem**, described as *"Secure file operations with configurable access controls"* ([mcp.so](https://mcp.so)). That is the same Filesystem server mentioned earlier in this chapter — the one that lets an AI read, write, and search files in a folder you pick. The "Official" badge tells you it is maintained by Anthropic's team, not a random hobbyist. Right next to it sits **PostgreSQL** — *"Read-only database access with schema inspection"* — letting an AI look at a database without being able to change anything. Two servers, two totally different jobs, same standard shape.

### The categories tell you...

What kinds of things MCP can connect to. Scrolling the directory, you spot servers for:

- **Databases** — Postgres, Redis, SQLite.
- **Browsers** — Puppeteer, Playwright (drive a real browser from code).
- **Maps** — Amap, Baidu Map.
- **Search** — Serper, Jina AI, Zhipu Web Search.
- **Creative apps** — MiniMax (text-to-speech, image and video generation), EverArt (AI image generation).
- **Code platforms** — GitLab, Sentry, AWS.
- **Quirky stuff** — Howtocook MCP, a recipe-recommender built on a programmer's home-cooking guide.

That range is the whole point of MCP. One protocol, every kind of system.

### You do not need to install anything to browse

Here is the thing beginners often miss: **just reading the directory teaches you what MCP is for.** You do not have to install a single server. Open [mcp.so](https://mcp.so), scroll, read the one-line descriptions. Every card is a small answer to the question *"what could an AI do if it could touch this system?"* Twenty-two thousand answers, all on one page. That is the ecosystem in one glance — no setup required.

Continue to [Chapter 8 — Agent Skills: Packaged Know-How](08_agent_skills.md).

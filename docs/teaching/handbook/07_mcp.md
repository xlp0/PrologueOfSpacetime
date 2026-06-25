# Chapter 7 — MCP: Plugging Things In

> **MCP** stands for **Model Context Protocol**. It is a standard for connecting AI tools to outside systems — like your files, GitHub, a database, or a video editor. This chapter explains what MCP is, what it is for, and what people have plugged in.

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

Continue to [Chapter 8 — Agent Skills: Packaged Know-How](08_agent_skills.md).

# Chapter 14 — Concrete Examples

The best way to understand AI coding tools is to see real examples. This chapter points you to real places you can browse right now, without installing anything.

---

## 14.1 Browse Skills at [skills.sh](https://skills.sh)

[skills.sh](https://skills.sh) is a public registry of agent skills — the "Open Agent Skills Ecosystem." Anyone can publish a skill; anyone can install one with a single command (`npx skills add <owner/repo>`).

When you visit, you see a **leaderboard** of skills ranked by installs. Tabs let you switch between *All Time*, *Trending (24h)*, and *Hot*. Each row shows the skill name, the owner, and its install count.

A few real examples near the top:

- **find-skills** (by `vercel-labs/skills`) — ~2.2M installs. Helps an agent discover and install other skills.
- **frontend-design** (by `anthropics/skills`) — ~588K installs. Teaches an agent the rules of good frontend design.
- **vercel-react-best-practices** (by `vercel-labs/agent-skills`) — ~501K installs. Bakes Vercel's React conventions into the agent.
- **agent-browser** (by `vercel-labs/agent-browser`) — ~483K installs. Lets an agent drive a web browser.

**What browsing teaches you:** skills are how people package *procedural know-how* — design rules, coding standards, how to debug, how to grill a codebase. The leaderboard shows what kinds of tasks the community finds useful enough to wrap up and share.

---

## 14.2 Browse MCP Servers at [mcp.so](https://mcp.so)

[mcp.so](https://mcp.so) is a public directory of MCP servers — over 22,000 of them as of this writing. It is a community-driven marketplace, not the official spec site.

When you visit, you see servers sorted into tabs: *Featured*, *Latest*, *Hosted*, and *Official*. Each card shows the server name, its author, and a one-line description of what it lets an AI do.

A few real examples:

- **[Playwright MCP](https://mcp.so/server/playwright-mcp/microsoft)** (by Microsoft) — browser automation. Lets an AI drive a real browser.
- **[PostgreSQL](https://mcp.so/server/postgres/modelcontextprotocol)** (official) — read-only access to a Postgres database with schema inspection.
- **[Sentry](https://mcp.so/server/sentry/modelcontextprotocol)** (official) — retrieving and analyzing errors from Sentry.
- **[Filesystem](https://mcp.so/server/filesystem)** (official) — secure file operations with access controls.

**What browsing teaches you:** MCP servers are how people connect AI to *real systems* — databases, browsers, code-hosting sites, monitoring, maps, search engines. Whatever software you already use, someone has probably wrapped an MCP server around it.

---

## 14.3 Try a Harness at [opencode.ai](https://opencode.ai)

[opencode.ai](https://opencode.ai) is the home of **opencode** — an open source, terminal-native AI coding agent. It is one of the harnesses you will meet in [Chapter 10](10_the_tools_people_use.md).

When you visit the site, you see: a one-line pitch ("The open source AI coding agent"), a copy-paste install command, a feature list, and links to docs. The features tell you what a modern harness cares about — LSP integration, multi-session agents, shareable session links, login with GitHub Copilot or ChatGPT, and support for 75+ model providers. The site also notes that opencode does not store your code or context, which is its pitch for privacy-sensitive environments.

**What it shows you:** a harness presents itself by listing *what it can plug into* (models, editors, logins) and *what it will not do* (store your data). That is the language harnesses speak.

---

## 14.4 Read the MCP Spec at [modelcontextprotocol.io](https://modelcontextprotocol.io)

[modelcontextprotocol.io](https://modelcontextprotocol.io) is the official site for the Model Context Protocol — the spec you met in [Chapter 7](07_mcp.md). It is the standard that makes "USB-C for AI tools" real.

When you visit, you see: a short explainer (MCP is "an open-source standard for connecting AI applications to external systems"), a diagram of the client–server model, and three starting points — *Build servers*, *Build clients*, and *Build MCP Apps*. Dig in and you find the full spec, the SDKs (TypeScript, Python, and more), and a list of reference servers maintained by the protocol team. The site also lists who supports MCP in the wild: Claude, ChatGPT, VS Code, Cursor, and others.

**What it teaches you:** MCP is not a product — it is a *rule* two programs follow so they can talk. Reading the spec, even just the intro, shows you how a simple rule can let one AI talk to thousands of tools without anyone asking permission.

---

## 14.5 The Big Picture

These four sites — [skills.sh](https://skills.sh), [mcp.so](https://mcp.so), [opencode.ai](https://opencode.ai), [modelcontextprotocol.io](https://modelcontextprotocol.io) — give you the full picture: the skills people package, the servers they connect, the tools they use, and the standard that connects them. Browse them when you want to see what is actually out there.

---

Back to [the handbook README](README.md).

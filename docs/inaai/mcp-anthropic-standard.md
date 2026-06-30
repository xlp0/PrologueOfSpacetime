---
concept: mcp-anthropic-standard
tags: [mcp, anthropic, llm, tools, integration, standardization]
source: YouTube — MCP Explained in 2 Minutes (Model Context Protocol) (https://www.youtube.com/watch?v=taeX8tgpPRQ)
date: 2026-06-26
---

# MCP — Anthropic's Tool Integration Standard

## Insight
**MCP (Model Context Protocol)** is a standard way for LLMs (ChatGPT, Gemini, Claude) to talk to external tools. Instead of every vendor building their own AI integration, an **MCP server** sits between the AI and the tool, enabling both context-pull and action.

**Why we need it**: LLMs alone are great at conversation but can't *act*: writing an email, updating tasks, querying a CRM. Connecting them to tools unlocks two things:

1. **Pull context** — e.g. ask "what are the most common job titles of new customers?" and the LLM pulls data straight from Salesforce.
2. **Take action** — not just draft the email, but create it in Gmail or send it.

**What MCP is specifically:**

- An agreed-upon standard for how tools interact with AI models.
- Developed by **Anthropic**.
- Replaces the "every tool builds its own AI connector" pattern with one shared protocol.
- Uses an **MCP server** per tool/service.
- Industry is hoping for broad adoption.

The standardization move is the load-bearing piece. Before MCP, every AI integration was bespoke — Salesforce built a ChatGPT connector, Notion built a Claude connector, Gmail built a Gemini connector. Each one a separate engineering effort, each with its own auth model, each with its own bugs. MCP says: build one MCP server per tool, and any AI that speaks MCP can use it. The N×M problem (N tools × M AI vendors) collapses to N+M.

Setting up your own MCP server is easy and requires **no code** — see the linked follow-up video for a step-by-step demo. This is what makes MCP a real standard rather than a vendor pitch: low enough friction that individual developers actually deploy their own.

The pattern appears throughout the vault: [[second-brain-business-os-wiring]] uses MCP to connect the vault to Gmail/Calendar/Drive; [[hermes-ue5-mcp]] uses it for Unreal Engine 5.8 game-dev integration; [[agentic-os-shared-brain]] uses it as the glue between agents and the shared registry; [[deerflow-sandbox-architecture]] consumes MCP servers for tool extension. And every MCP server is a new prompt-injection blast radius (see [[prompt-injection-anatomy]]).

## Context
From "MCP Explained in 2 Minutes" — the short primer on the protocol that powers most of the agentic tooling in the vault.

## Related
- [[second-brain-business-os-wiring]]
- [[hermes-ue5-mcp]]
- [[agentic-os-shared-brain]]
- [[prompt-injection-anatomy]]
- [[minio-s3-compatible-object-storage]] — same "open protocol as portability layer" thesis, applied to object storage
- [[InaAI]]

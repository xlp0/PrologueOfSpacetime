---
concept: OpenCode vs Claude Code vs Pi Agent
tags: [koo-project, opencode, claude-code, pi-agent, ai-tools]
source: ChatGPT convs
---

# OpenCode vs Claude Code vs Pi Agent

## Insight
These are different **access layers**, not competitors. Three things must be distinguished: **(1) the model** (GLM2 / Claude / GPT), **(2) the interface** (OpenCode / Claude Code / Pi Agent), **(3) the access layer** (private server at Toba vs cloud subscription). Ilham already has GLM2 + OpenCode + private server; "download Pi Agent" was about a different access path, not a replacement.

**OpenCode** = the client / interface you use to work. Open-source terminal AI coding interface (github.com/sst/opencode). Can use Claude API (paid), OpenAI API (paid), Gemini API (sometimes free tier), or local Ollama models (free, weaker). Does not require paid Claude.

**Claude Code** = Anthropic's official terminal coding agent. Requires Anthropic access/subscription/API usage. Good at understanding large codebases, planning multi-file changes, debugging. The workflow "install Claude Code, then install OpenCode from Claude Code" = Claude Code bootstraps OpenCode; not a forced marriage.

**Pi Agent** = most likely the tunnel / access layer / connector into Toba's private infra. If OpenCode already lets you SSH into the Toba machine, browse/edit files on the remote box, run commands there, access the internal services you need — then Pi Agent is probably redundant for that workflow. But if OpenCode only works because someone preconfigured the remote connection and you still can't reach certain internal URLs, databases, dashboards, or private repos — then Pi Agent may be the missing access layer. Pi Agent is probably for: VPN/private network access to Toba infra, device authentication / zero-trust access, port forwarding / secure tunnel to internal services, or policy compliance ("everyone accessing company infra must use this agent").

Mental model: **OpenCode = steering wheel; Pi Agent = gate pass / road into the compound.** Having the steering wheel doesn't mean you've got the gate pass. The fast verification question: *"I already have access to the remote environment through OpenCode. Is Pi Agent still required? If yes, what exactly is it needed for — VPN/private network access, SSH auth, or access to specific internal services?"* That cuts through the fog immediately.

## Context
Came up 2026-06-25 (OpenCode vs Pi Agent) and 2026-06-24 (Claude Code and Repos). Ilham had been told to download Pi Agent for Toba data center access but already had OpenCode access.

## Related
- [[chatgpt-vs-claude-vs-local-ai-verdict]]
- [[hermes-as-model-choice-not-os]]
- [[toba-data-center-and-glm2]]
- [[think-pipeline-not-plugin]]
- [[koo-project-highlights]]
- **Claude Code Skills**

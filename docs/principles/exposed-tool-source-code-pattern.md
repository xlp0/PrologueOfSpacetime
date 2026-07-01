---
title: 'exposed-tool-source-code-pattern'
date: 2026-06-27
tags: [Trivium-Rhetoric, Seven-Liberal-Arts, opengeoagent, tool-orchestration, code-teaching, agent, transparency]
type: principle
sources: [YouTube — OpenGeoAgent: A Multimodal AI Agent for Automated Geospatial Analysis (https://www.youtube.com/watch?v=5zkXQlHUsu8)]
status: stable
liberal_art: Trivium-Rhetoric
---

# Exposed Tool Source Code Pattern

## Insight
OpenGeoAgent's most underrated design move: **tool source code is exposed.** Every step the agent runs prints the Python underneath, which you can copy into your own console. That detail matters — it turns the agent into a **code-teaching surface**, not a black box.

Why this is non-obvious: most agent frameworks treat the tool layer as an implementation detail. The agent calls a tool, gets a result, moves on. The user sees the result; they don't see what the tool actually did. That's fine for "send the email" or "schedule the meeting" — opaque actions where the user only cares about the outcome. It's terrible for "run the watershed delineation" — where the user might want to rerun the step with a different parameter, or learn how to do it themselves, or audit whether the right algorithm was used.

The pattern in OpenGeoAgent: a mode dropdown switches the available toolset (General QGIS / Whitebox Tools / cloud-catalog mode), and every step in the chat prints the underlying Python. The user can copy any step into their own console and rerun it standalone, parameter-tweak it, or learn from it.

This reframes what an agent is for. The default framing is "the agent does the work for you." The exposed-source-code framing is "the agent does the work *and teaches you how to do it yourself*." That's a meaningfully different value prop — it builds the user's capability over time, not just their dependency on the agent.

It also creates a trust surface. If the agent runs a step you don't understand, you can read the code. If the agent runs a step you disagree with, you can copy the code, modify it, and rerun. You're not trapped in the agent's interpretation.

The same pattern shows up in [[skills-sh-markdown-spec]] — skills are markdown, readable, modifiable. And it's the inverse of [[agentic-os-shared-brain]] where the graph is the abstraction layer; here, the source code is the abstraction layer.

## Context
From the OpenGeoAgent walkthrough; the tool-orchestration section.

## Related
- [[opengeoagent-architecture]]
- [[skills-sh-markdown-spec]]
- [[second-brain-business-os-wiring]]
- [[InaAI]]

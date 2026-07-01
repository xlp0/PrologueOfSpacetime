---
title: 'deerflow-sandbox-architecture'
date: 2026-06-27
tags: [Trivium-Grammar, Seven-Liberal-Arts, deer-flow, sandbox, docker, isolation, security, allowed-tools]
type: concept
sources: [Web research — DeerFlow 2.0 by bytedance (https://github.com/bytedance/deer-flow)]
status: stable
liberal_art: Trivium-Grammar
---

# DeerFlow Sandbox Architecture

## Insight
DeerFlow gives the agent a real computer via the **Sandbox** — an isolated execution environment with a defined filesystem layout:

- `/mnt/user-data/{uploads,workspace,outputs}` — user files
- `/mnt/skills/{public,custom}` — skill files

Two providers: `AioSandboxProvider` (Docker-isolated, recommended) vs `LocalSandboxProvider` (host bash disabled by default).

The security properties are non-trivial and worth pulling apart:

- **Rejects symlinked upload destinations** — prevents path-traversal attacks where a malicious upload points outside the sandbox.
- **Masks MCP secrets in API responses** — secrets don't leak back through the agent's output.
- **Caps skill-artifact decompression** — zip-bomb defense. A malicious skill archive can't OOM the sandbox by decompressing to 1000× its size.
- **Mounts host Docker socket only in aio (DooD) mode** — the dangerous host-Docker-socket mount is opt-in, not default.
- **Doesn't bind-mount host CLI auth dirs by default** — agent can't read your `~/.aws` or `~/.config/gcloud` unless you explicitly allow it.
- **Per-tool loop detection with frequency overrides** — catches an agent stuck in a tool-call loop and breaks it.
- **Enforces skill `allowed-tools` metadata** — skills declare which tools they're allowed to use; the runtime enforces it.
- **Hardened slash-skill activation across channels** — IM-channel skill activation is locked down so a malicious message can't trigger a privileged skill.

This is the productionized version of [[prompt-injection-defense-in-depth]]: least privilege + sandboxing + per-tool auth, baked into the runtime rather than bolted on. Pair with [[openclaw-vs-hermes-security-posture]] for the same pattern in OpenClaw and Hermes.

The sandbox is also what makes sub-agents safe to spawn (see [[deerflow-lead-agent-dynamic-subagents]]) — each sub-agent gets its own isolated context with only the tools it needs, so a compromised sub-agent can't escalate.

## Context
From web research on the DeerFlow 2.0 release; the security section of the docs.

## Related
- [[deerflow-harness-vs-framework]]
- [[deerflow-lead-agent-dynamic-subagents]]
- [[prompt-injection-defense-in-depth]]
- [[openclaw-vs-hermes-security-posture]]
- [[InaAI]]

---
title: 'skills-sh-markdown-spec'
date: 2026-06-26
tags: [Trivium-Grammar, Seven-Liberal-Arts, skills, claude-code, anthropic, markdown, yaml, agentskills, spec]
type: principle
sources: [YouTube — Claude Code Skills & skills.sh - Crash Course (https://www.youtube.com/watch?v=rcRS8-7OgBo) and YouTube — I Turned Claude Into the Ultimate Second Brain (https://m.youtube.com/watch?v=8QQ_INxAhRs)]
status: stable
liberal_art: Trivium-Grammar
---

# skills.sh — Markdown Skill Spec

## Insight
Agent skills are markdown files with specialized procedural instructions for AI agents. The spec is just **markdown with a YAML header** — anyone can author one.

The history:
- Originated Oct 2025 with Anthropic's Claude Code agent skills.
- Dec 2025: open standard adopted by OpenAI Codex, Microsoft, GitHub, Cursor, etc.

Top of the file has a YAML header with **name** + **description** — the only thing the agent sees in context before deciding to load the skill. This is the progressive-disclosure contract from [[static-vs-dynamic-context]]: the agent sees the description, decides if it's relevant, and only then loads the full skill body.

`skills.sh` is Vercel's CLI for installing/managing/sharing skills. The shape:

- `npx skills add <owner>/<repo>` → interactive installer. Choose target agents (Claude Code, etc.), scope (project vs global), and install method (symlink recommended).
- `npx skills initialize <name>` → creates `<name>/skill.md`. Optionally add scripts, references, templates — link them from `skill.md`.
- Verify with `/skills` in Claude Code.

The whole spec is "markdown with a YAML header." That's it. The simplicity is the point — portability across any agent that reads markdown, version-controllable like code, shareable via git. Same spec under different brands: agentskills.io (Hermes), ClawHub (OpenClaw), the Vercel skill package registry. All interoperable at the file level.

Best practices:
- Start by using existing skills to learn the patterns.
- Build custom skills for repetitive workflows.
- Use **global** installs for cross-project tools (skill creator, front-end design); **project** installs for project-specific skills.
- Co-locate the skill with the tool it documents (e.g. inside the CLI's repo) so it stays in sync.
- Generate log files once a skill is validated.
- Iterate — first versions rarely work; teach Claude the edge cases. The deeper move (Nate Herk): **every use of a skill is data**. Each time you run it, give feedback ("here's what I liked, here's what I didn't"), then `update the skill`. Even a 4-month-old skill is still being iterated — preferences change, models change, endpoints change. No such thing as a finished skill; the question is whether it's getting better with use.

The packaging argument (see [[packaging-is-the-product]]) is built on this spec.

## Context
From the "Claude Code Skills & skills.sh" crash course; the spec is the foundation for Caveman, Ponytail, Graphify, and most of the rest of the vault.

## Related
- [[packaging-is-the-product]]
- [[skills-install-best-practices]]
- [[static-vs-dynamic-context]]
- [[hermes-self-improving-skills]]
- [[InaAI]]

---
title: 'skills-install-best-practices'
date: 2026-06-26
tags: [Trivium-Grammar, Seven-Liberal-Arts, skills, claude-code, install, project-vs-global, symlink, co-location]
type: principle
sources: [YouTube — Claude Code Skills & skills.sh - Crash Course (https://www.youtube.com/watch?v=rcRS8-7OgBo)]
status: stable
liberal_art: Trivium-Grammar
---

# Skills Install Best Practices

## Insight
The `skills.sh` install pattern is simple but the best-practice layer is where the real value is. Decisions that matter:

**Project vs global scope:**
- **Global** installs for cross-project tools (skill creator, front-end design, anything you'd want in every repo).
- **Project** installs for project-specific skills (the schema, the conventions, the workflow rules for this codebase).

**Install method:** symlink recommended. Why — a symlinked skill stays in sync with its source repo. A copied skill drifts. A symlink means `git pull` on the source repo updates the skill in every project that uses it.

**Co-location:** co-locate the skill with the tool it documents (e.g. inside the CLI's repo) so it stays in sync. The skill and the tool evolve together; if they live in separate repos, one drifts while the other changes. Same logic as keeping tests next to code.

**Iteration discipline:** first versions rarely work. Teach Claude the edge cases. The pattern is:
1. Use existing skills to learn the patterns (don't author from scratch).
2. Build custom skills for repetitive workflows (the ones you've done 3+ times this month).
3. Generate log files once a skill is validated to avoid using unvalidated ones.
4. Share useful ones with the community.

**The skill = entry point + linked resources:** the `skill.md` is the entry point, but you can add scripts, references, templates — link them from `skill.md`. The agent figures out the rest. Don't cram everything into the markdown; structure it as a small entry point + supporting files.

This is the operational layer on top of [[skills-sh-markdown-spec]] — the spec defines what a skill is, the install best practices define how to deploy one well. And it's the answer to "why use a skill instead of a system-prompt phrase?" from [[packaging-is-the-product]] — versioned, shared, auto-injected.

## Context
From the "Claude Code Skills & skills.sh" crash course; the best-practices section near the end of the video.

## Related
- [[skills-sh-markdown-spec]]
- [[packaging-is-the-product]]
- [[catalog-vs-curator]]
- [[InaAI]]

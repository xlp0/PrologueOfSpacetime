---
title: 'catalog-vs-curator'
date: 2026-06-27
tags: [Trivium-Logic, Seven-Liberal-Arts, openclaw, hermes-agent, comparison, skills, clawhub, skill-workshop]
type: concept
sources: [YouTube — OpenClaw vs Hermes Agent (Don't choose WRONG!) (https://www.youtube.com/watch?v=jOK10k70XWE)]
status: stable
liberal_art: Trivium-Logic
---

# Catalog vs Curator — OpenClaw vs Hermes

## Insight
OpenClaw and Hermes Agent are open-source AI agents you self-host and chat with over Telegram, Slack, or Discord. Same ingredients — read files, run scripts, browse the web, send emails, schedule jobs. The difference is **where each project spent its design effort:**

- **OpenClaw** bet on a community **catalog**: 50,000+ skills and plugins on ClawHub (Google Workspace, web scraping, image generation, accounting). Browse, one-click install, done.
- **Hermes** bet on a **learning loop**: the Curator (shipped in Hermes .12 / April 2026) auto-writes skills from the agent's own work. The library starts small and grows from your own usage.

Hermes shipped its own catalog equivalent ("Skill Workshop") in June 2026, but with one key difference: Hermes does it **automatically by default**; OpenClaw **asks you to approve each new skill** first. OpenClaw bets on the community catalog; Hermes bets on the agent improving itself.

Where OpenClaw wins: the catalog (50k+ skills day one), provider variety (50+ AI providers natively), and a polished dashboard by default (Hermes is CLI-first; the dashboard is optional). Where Hermes wins: the automatic learning loop (no approval needed), token cost on repeat tasks (solves once, saves the skill, runs cheaply every time), and day-one ergonomics (paste key, send message, done).

The honest CVE story isn't close: OpenClaw had ~130 security advisories Feb–April 2026 including a high-severity RCE flaw that exposed 40,000+ instances, plus a ClawHub audit flagging 1,000+ malicious skills. Hermes had ~12 CVEs across 2026 plus an April audit flagging 4 critical + 9 high in default config — all patched. Slower rate partly because there's no third-party marketplace running through Hermes the way ClawHub runs through OpenClaw.

Pick framework: want to browse and install pre-built capabilities → OpenClaw. Want the agent to learn your work and get cheaper over time → Hermes.

## Context
From the "OpenClaw vs Hermes Agent" comparison; the catalog-vs-curator axis is the spine of the entire video.

## Related
- [[hermes-self-improving-skills]]
- [[openclaw-vs-hermes-security-posture]]
- [[skills-sh-markdown-spec]]
- [[skills-install-best-practices]]
- [[InaAI]]

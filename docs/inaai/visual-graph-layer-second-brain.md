---
concept: visual-graph-layer-second-brain
tags: [visual-graph, second-brain, claude-code, obsidian, dashboard]
source: YouTube — The Next Era of Second Brains Is Here (https://www.youtube.com/watch?v=xHAZo1SmnhM)
date: 2026-06-28
---

# Visual Graph Layer for a Markdown Second Brain

## Insight
A second brain of `.md` files is invisible by default — folders and a `claude.md` router (see [[claude-md-routing-rules]]). This tool adds a **visual graph layer** on top: drag a folder (Obsidian vault, Claude Code project, or any `.md` files) onto it and it opens a localhost page that auto-populates a force-directed graph of every note and its links.

Two render modes share the same control set: a 2D version and a full 3D version you can orbit, zoom, and tilt. The interaction model is the load-bearing part, not the prettiness:

- **Click a node → it highlights and zooms; everything else dims.** You see only what's connected and the direction data flows.
- **Depth 1 / 2 / 3 exploration** — expand outward from a node by hops. More depth lights up more of the neighborhood.
- **Pin** to isolate one node and drop the rest.
- **Search** (e.g. "SiteView") jumps to a node and surfaces a detail pane with the note's actual content — "Live GEO Audit SaaS at siteview.com, gets cited by AI."
- **Toggle layers** on the right (tools / worlds / clients) to declutter; **heat map** and **by-type** color-coding to read structure at a glance; themes, particle flow, curved-vs-straight links, icons (Claude = brain icon), Aurora-sky background — all cosmetic toggles.

The point isn't the eye candy. Once your whole business lives as linked markdown, **you can see how the AI sees it** — which client connects to which service, which skill sits under which product. The author is explicit that he's a visual person and seeing the connections is how he understands the system; a flat folder tree hides that, a graph exposes it.

This is the dashboard pattern from [[codebase-knowledge-graph-dashboard]] (and the lighter [[graphify-codebase-knowledge-graph]]) ported from *codebase* to *business knowledge*. Same shape — graph + node-detail pane + layer toggles — different substrate. It's also the visual half of the [[agentic-os-shared-brain]] idea: the shared brain is the files; this is the human-readable lens on it. Built with Claude Code on the (now-shutdown) Fable 5 model; runs on any Claude model.

A free version ships with the author's branding; a paid white-label version exists for reselling (see [[second-brain-agency-product]]).

## Context
From "The Next Era of Second Brains Is Here" (Zubair / AI Workshop) — a walkthrough of a localhost graph viewer rendered over a markdown second brain.

## Related
- [[codebase-knowledge-graph-dashboard]]
- [[graphify-codebase-knowledge-graph]]
- [[agentic-os-shared-brain]]
- [[second-brain-obsidian-foundations]]
- [[InaAI]]

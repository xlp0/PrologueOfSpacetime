---
concept: hermes-imessage-photon-routing
tags: [hermes, imessage, photon, telegram, channel-routing, agents]
source: YouTube — The new Hermes Agent update has me speechless (https://www.youtube.com/watch?v=bQ1LCFrwj08)
date: 2026-06-26
---

# Hermes iMessage + Photon Channel Routing

## Insight
Hermes Agent's biggest update shipped native iMessage support, courtesy of a free service called **Photon** that provisions a textable number. Setup is a single prompt: *"Hook Hermes up to iMessage using Photon according to the best practices from the new update."* After that, you chat with Hermes directly through iMessage on your phone — agent texts just like a human, message after message, with all rich features intact.

The interesting design move is the **channel routing logic** the update implies — different surfaces for different kinds of work:

- **On the go, quick messages** → iMessage (lowest friction, phone-native).
- **At the computer, focused work** → desktop app (full window, model selector, built-in terminal).
- **On the go, complex deep work / threading** → Telegram (richer formatting, streaming, tables).

This matters because the right surface for a task depends on its complexity and your context. A 30-second investor-report question on the train doesn't need a desktop window; a multi-agent research task doesn't fit in iMessage's narrow thread. Hermes doesn't force one channel for everything — it routes by what you're trying to do.

The investor-report demo in the video is the proof: Hermes built a stock table (description, price, market cap) right inside Telegram using the new agent-friendly formatting Telegram rolled out (smoother streaming, tables, lists, bold). The table rendered cleanly without leaving the chat.

Universal tip from the author: anything in the update you don't know how to implement, just ask Hermes. It sets itself up.

## Context
From "The new Hermes Agent update has me speechless" — one of 8 updates, focused on iMessage + Photon + channel routing.

## Related
- [[hermes-background-subagents]]
- [[mcp-anthropic-standard]]
- [[hermes-self-improving-skills]]
- [[InaAI]]

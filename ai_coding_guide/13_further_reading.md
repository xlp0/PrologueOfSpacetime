# Chapter 13 — Where to Learn More

## How to use this chapter

This is a curated starting point, not an exhaustive list. The AI coding space moves fast enough that any specific link may rot or go stale within months; the strategy is to find the *sources* that update continuously, not the articles that are perfect on a given day. Where I point to a specific resource, prefer its current version over the snapshot from when this was written.

The chapter is organized by what you're trying to learn next.

---

## 1. To understand the models themselves

Start with the model providers' own technical reports and documentation. They are unusually good primary sources:

- **Anthropic's documentation** (docs.anthropic.com) — especially the sections on tool use, prompt caching, and extended thinking. Anthropic's writing about how to use their models well is some of the clearest in the industry.
- **OpenAI's documentation and cookbook** (platform.openai.com/docs, github.com/openai/openai-cookbook) — practical patterns for working with GPT-class models, including tool calling and structured output.
- **Google's Gemini documentation** (ai.google.dev) — Gemini-specific patterns, including long-context use.
- **The original transformer paper** ("Attention Is All You Need," Vaswani et al., 2017) — not because you need to implement a transformer, but because the mental model of attention is genuinely useful for understanding why context engineering matters.

For a deeper conceptual grounding in how LLMs actually work, Karpathy's lectures and essays (find them via his YouTube and GitHub) remain the best layperson-accessible treatment by someone who actually builds these systems.

---

## 2. To understand the harness and the loop

This is where primary sources are weakest, because harness engineering is newer than the models and the field hasn't settled on shared vocabulary. Useful things to read:

- **Your tool's own docs** — whichever terminal agent or IDE tool you use, read its docs end to end. Claude Code, opencode, Codex CLI, and Cursor all have substantial docs explaining their harness's behavior. This is the single most useful thing you can do, and the most commonly skipped.
- **The MCP specification** (modelcontextprotocol.io) — the protocol itself is short and readable. Understanding what the protocol defines (and what it leaves to implementers) is the fastest way to demystify MCP.
- **The growing "harness engineering" literature** — search for "agent harness engineering" and "production AI agents." The field is actively producing write-ups; the good ones explain *why* certain design choices matter, not just *what* they are. Look for content from practitioners who've shipped agents at scale, not from people selling courses.

A note on quality: the AI coding space has a lot of content produced by people who have used the tools for a week. Prefer writers who have shipped real software with these tools over months. The signal-to-noise ratio is low; curate ruthlessly.

---

## 3. To understand context engineering specifically

- **Anthropic's writing on context engineering** — they've been the most vocal proponent of the term and have published useful breakdowns of what good context curation looks like.
- **Practitioner blogs on RAG and agentic RAG** — the retrieval-augmented generation literature is older and deeper than the "context engineering" rebrand; the underlying ideas (what to retrieve, how to rank it, when to evict) are the same.
- **Your own tool's behavior** — the best way to learn context engineering is to watch what your harness puts in the context window on each turn. Most tools will show you (often via a debug or "show messages" mode). Reading those messages is the single most educational thing you can do.

---

## 4. To understand MCP and the server ecosystem

- **The MCP spec and quickstarts** (modelcontextprotocol.io) — start here. The quickstarts walk through writing a trivial server, which is the best way to understand what a server actually is.
- **The MCP server directories** — there are several community-maintained lists of MCP servers (search "awesome MCP servers" or check the official registry). Browse to get a sense of the ecosystem's shape.
- **Source of a real server** — pick one well-maintained server (the official filesystem or git server is a fine choice) and read its source. Servers are small; you can understand one in an afternoon.

---

## 5. To understand skills, rules files, and workflows

This is the newest and least documented area, so primary sources matter most:

- **Your tool's docs on rules files and skills** — Claude Code, opencode, Cursor, and Codex CLI all have sections explaining their rules file format and how they load skills. These are the canonical sources; third-party write-ups age fast.
- **The AGENTS.md spec or examples** — search for "AGENTS.md specification" and look at well-maintained open-source repos that use it. Reading a real `AGENTS.md` from a real project is more instructive than any abstract guide.
- **Existing skills and slash command collections** — there are GitHub repos collecting community-written slash commands and skills for Claude Code, Cursor, and others. Browse them to see the range of what people package. Copy the patterns; don't copy the content blindly.
- **BMAD Method documentation** (docs.bmad-method.org) — if you want to see what a full methodology looks like, BMAD's docs are unusually thorough. Read it critically — it's one opinionated approach, not the only one — but as an example of "packaged agentic workflow at scale" it's instructive.

---

## 6. To stay current

The news cycle in AI coding is fast and noisy. A few high-signal sources:

- **Your tool's changelog** — read it every release. Most of what changes in your day-to-day experience is here, not in the news.
- **The MCP spec's changelog** — protocol changes affect what's possible across the whole ecosystem.
- **A small number of practitioner blogs** — find three to five people who ship real software with these tools and read them. Ignore the rest. The trick is curating aggressively; the volume of content is far higher than the quality.
- **One frontier model provider's blog** (Anthropic, OpenAI, or Google) — for model-level changes that ripple through the tools.
- **HN, lobste.rs, and similar aggregators** — useful for catching new things, but apply a strong filter. Most AI coding discussion on aggregators is people who've used the tools briefly.

What *not* to do: try to read everything. You can't, and trying will eat the time you should be spending actually using the tools. Read narrowly; practice broadly.

---

## 7. To learn by doing (the most important section)

Honestly, this is the only section that matters. Reading about AI coding is a poor substitute for doing it. A suggested progression:

1. **Install one terminal agent** (Claude Code, opencode, or Codex CLI — pick based on which model you want to use). Run it on a small real project of yours.
2. **Write an `AGENTS.md`** for that project. Iterate on it as the agent gets things wrong. This is the fastest way to learn context engineering.
3. **Use plan mode** for anything non-trivial. Notice the difference between planning-first and diving-in.
4. **Connect one MCP server** — the filesystem or git server if your harness doesn't already include it, or a database server for a real database you have. Feel the agent's reach expand.
5. **Write one slash command** for a procedure you repeat. Then one skill for a bigger procedure.
6. **Read the context window** — turn on the debug mode that shows you what the harness is sending to the model. This single habit will teach you more about AI coding than any ten articles.
7. **Ship one real feature** end-to-end with the agent — plan, implement, test, review, merge. Notice where the agent excels, where it struggles, and where you have to take over. That map is the actual skill.

You will learn more in a week of doing this than in a month of reading, including reading this guide. The guide exists to give you the vocabulary and the mental model so the doing goes faster; it is not a substitute for the doing.

---

## 8. A closing note

The field will keep changing. The specific tools, the specific file formats, the specific methodologies — all of it is in motion. What's stable is the underlying picture this guide has tried to give you:

- A model, wrapped in a harness, running in a loop, against a finite context window.
- A stack of layers — model, harness, client, server — each with its own concerns.
- A skill: curating what the model sees.
- An extension mechanism: MCP for tools, skills for know-how.
- A discipline: verify, sandbox, own what you ship.

Hold onto the picture; update the specifics as they evolve. The practitioners who do well in this space are not the ones who memorized the most tools, but the ones who understood the picture clearly enough to keep up as the tools changed underneath them.

Go build something.

---

*This guide was written in June 2026. If you're reading it much later, treat the specific tool names and file formats as historical examples of the patterns, not as current recommendations. The patterns will still hold.*

# Chapter 4 — Tokens and Context

## The two facts that explain everything

If you understand two things, you understand most of the weird behavior you'll see from AI coding tools:

1. **The model's working memory — the context window — is measured in tokens, and it is finite.**
2. **Everything the model sees costs money and time, roughly proportional to the number of tokens.**

That's it. Those two facts drive the design of every harness, the shape of every bill, and a surprising amount of the difference between a tool that feels smart and one that feels stupid.

Let's unpack them.

---

## What is a token?

A token is the unit the model actually reads and writes. It is *not* a word, and it is *not* a character — it's somewhere in between. Rough rules of thumb for English text and source code:

- **1 token ≈ ¾ of a word**, or about **4 characters**.
- A short common word (`if`, `for`, `return`) is usually one token.
- A long word or identifier (`authenticationMiddleware`) might be three or four tokens.
- Whitespace and punctuation are tokens too.
- Code tends to be slightly more token-dense than prose, because of all the symbols.

Different models use different tokenizers, so the exact count varies, but the order of magnitude is stable. A 500-line TypeScript file is somewhere around 4,000–8,000 tokens. A typical chapter of this guide is roughly 3,000–5,000 tokens.

You don't need to count tokens by hand. Every harness shows you a token count somewhere, and there are command-line tokenizers if you want to measure. What you need is the *feel*: a sense of how big things are in token terms, because the context window is sized in tokens and so is your bill.

---

## The context window

The context window is the maximum number of tokens the model can take in on a single call. This is a property of the model, set by its architecture, and it has grown fast:

- 2022 GPT-3.5 era: ~4K–8K tokens.
- 2023: ~16K–32K tokens became common.
- 2024: 128K–200K became standard on the frontier models.
- 2025–2026: 1 million+ tokens on some models, with the frontier settling around 200K–1M for coding work.

A 200K-token window sounds enormous. It is not. Here's why.

### The window fills up faster than you think

When you ask an agent to "fix the failing test," the harness doesn't just send the test and the fix. It sends, roughly:

- The system prompt and tool definitions: a few thousand tokens, sometimes more.
- Any project rules files it loaded (Chapter 9): a few hundred to a few thousand.
- The conversation history so far: grows with every turn.
- The file containing the failing test: maybe 1,000–3,000 tokens.
- The file under test: 1,000–5,000.
- The test's failure output: a few hundred to a few thousand.
- Possibly other files the harness retrieved as relevant: each another 1,000–5,000.
- Possibly the results of a codebase search: hundreds to thousands.

Add it up and a single "fix the test" turn can easily consume 20K–50K tokens, before the model has even replied. Run the loop five times (Chapter 2) and you can burn through 100K+ tokens on one small task. This is why even a million-token window is a real constraint in agentic work: the loop is greedy.

### When the window is full, something has to leave

The model is stateless. It can only act on what's in the window *right now*. When the window fills, the harness has to decide what to evict. Bad eviction is the #1 cause of "the AI forgot what I told it" and "the AI keeps making the same mistake in a loop." You told it; it was in the window; the harness evicted it to make room for new tool output; the model now has no idea.

This is the entire subject of Chapter 6 (context engineering), so we won't dwell here. The takeaway is that **the context window is not just a size — it's a budget that has to be managed.** A good harness manages it well; a bad one manages it badly; and you, by writing good rules files and giving good instructions, influence what's worth keeping.

---

## Tokens cost money

Every token that goes *into* the model costs money. Every token that comes *out* costs money (usually more). Pricing is per million tokens and varies wildly by model:

- Frontier closed models (Claude Opus-class, GPT-5-class): the most expensive.
- Frontier mid-tier (Claude Sonnet-class, GPT-4o-class): much cheaper, often 80%+ of the quality.
- Open-weights models hosted yourself: cheap on tokens, expensive on infra.

For a single chat, costs feel negligible. For an agentic loop that runs 20 turns gathering files and running commands, a single task can cost anywhere from a few cents to a few dollars on the frontier models. Do that all day, every day, and it adds up. This is why **prompt caching** exists — see below — and why harness engineers obsess over keeping the stable parts of a prompt from being re-billed on every turn.

A practical implication: when you're picking a model for routine work, the second-tier model is almost always the right call. Reserve the most expensive frontier model for the hardest reasoning tasks. Most coding is not the hardest reasoning task.

---

## Prompt caching: the lever that makes agentic loops affordable

Here's the thing about the agentic loop: most of what goes into the context window on turn N is the *same* as what went in on turn N-1. The system prompt is identical. The tool definitions are identical. The project rules are identical. The files you already read are identical. Only the new tool result and the model's latest reply are new.

**Prompt caching** lets the model provider cache that stable prefix and charge you much less (often 10x–20x less) for the cached tokens on subsequent calls. The harness has to opt into this by structuring prompts so the stable part comes first and the dynamic part comes last, but a well-engineered harness does this automatically.

This is the difference between an agentic loop being affordable and being ruinous. When you read that some tool "supports prompt caching," what it means is: the harness is structured to reuse the stable prompt prefix across loop iterations, so you're not paying full price for the same 50K tokens on every turn. It's a quiet feature with a huge impact on cost.

---

## Output tokens and reasoning tokens

Two wrinkles worth knowing:

1. **Output tokens cost more than input tokens.** Often 3–5x more. So a model that reads a 10K-token prompt and produces a 2K-token reply is paying mostly for the reply. This is why "be concise" is not just a stylistic preference in agent prompts — it's a cost decision.
2. **Reasoning models produce hidden "thinking" tokens.** Some frontier models (the "reasoning" or "extended thinking" variants) generate internal chain-of-thought tokens that you don't see but that you pay for. These can dramatically improve quality on hard tasks and dramatically increase cost. Use them for hard problems; turn them off for routine edits.

---

## Why "bigger context window" didn't solve everything

When models went from 8K to 200K tokens, a lot of people assumed the context problem was solved. It wasn't, for three reasons:

1. **The loop is greedy.** As shown above, an agentic loop can fill a 200K window on a single moderate task. A million-token window is a few tasks, not infinite memory.
2. **Lost in the middle.** Models have a well-documented weakness: they attend well to the beginning and end of a long context and lose fidelity in the middle. Cramming 200K tokens in doesn't mean the model uses all 200K equally well.
3. **Cost and latency scale with the window.** A 200K-token prompt is slower and more expensive than a 20K-token prompt, even if the model can handle it. Bigger isn't free just because it's possible.

The result is that context engineering — the deliberate choice of what goes in the window — is a real skill even when the window is enormous. The window being big enough to hold everything is not the same as the window being *small enough* to hold only the right things. Chapter 6 is about exactly this.

---

## A practical rule of thumb

If you remember nothing else from this chapter:

- **The context window is a budget, not a bucket.** Treat it like RAM: finite, valuable, and something you should be deliberate about filling.
- **Every token costs money and time.** Bigger prompts are slower and pricier; output is worse than input; reasoning tokens are worst of all.
- **Prompt caching is what makes the loop affordable.** A good harness uses it; you don't have to think about it, but you should know it's there.
- **"The AI forgot" almost always means "the harness evicted it."** Not a memory bug — a context-management decision.

With the model, the harness, the loop, the context window, and tokens all in hand, you now have the full lower stack. The next chapter moves up a level: how to actually talk to the thing.

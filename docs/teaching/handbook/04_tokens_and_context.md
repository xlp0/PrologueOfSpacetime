# Chapter 4 — Tokens and the Context Window

> To use AI tools well, you need to understand two things: **tokens** (how the AI measures text) and the **context window** (how much text the AI can hold in its head at once). These two ideas explain almost every weird behavior you will see.

---

## The Simple Version

- A **token** is a small chunk of text — roughly 4 characters, or about 3/4 of a word.
- The **context window** is how much text the AI can "see" at once, measured in tokens.
- When the window is full, old text falls out and the AI forgets it.

That is the whole idea. The rest is just details.

---

## What Is a Token?

Computers do not read letters the way humans do. AI models read **tokens** — small chunks of text. A token might be a whole word, part of a word, or just a few characters.

Rough rules of thumb:

- 1 token ≈ 4 characters of English
- 1 token ≈ 3/4 of a word
- A line of code is often 5 to 15 tokens
- This sentence is about 15 tokens

Different things produce different numbers of tokens:

- "Hello world" — about 2 tokens
- A 1,000-word essay — about 1,300 tokens
- A 2,000-line code file — about 15,000 to 20,000 tokens

---

## Why Tokens Matter

Tokens matter for three reasons:

### 1. Cost

AI companies charge per token. You pay for what you send (input tokens) and what the AI writes back (output tokens). A long conversation can cost more than a short one. A big file pasted into chat costs more than a small one.

### 2. Speed

More tokens in = more time before the AI starts responding. If you paste a 50,000-token file, the AI has to "read" all of it before it can answer. That takes time.

### 3. The Context Window (the limit)

Every model has a maximum number of tokens it can hold in its head at once. This is the **context window**. Common sizes are 100,000 to 200,000 tokens (some are larger, some smaller). When you fill the window, the oldest text starts falling out, and the AI forgets what was at the beginning.

---

## The Context Window: The AI's Working Memory

Think of the context window as the AI's **short-term memory** for one conversation. Everything the AI knows about your task lives in this window:

- Your prompt (what you typed)
- The AI's response
- Any files you pasted in
- Any tool output (file reads, command results, web searches)
- The system prompt (instructions from the harness)

When the window fills up, older content gets dropped or summarized. The AI does not know it has forgotten something — it just stops seeing it.

---

## The Beginner Mistake

The most common beginner mistake is **pasting too much**. Someone thinks: "I will give the AI everything — the whole codebase, all the docs, every file — so it has full context." This sounds reasonable, but it is usually wrong, for three reasons:

1. **It costs a lot.** A whole codebase might be a million tokens. That is real money.
2. **It fills the window.** The AI cannot hold a million tokens. The oldest stuff falls out before the AI even starts.
3. **It confuses the AI.** Models lose focus when given too much at once. A focused prompt with the right 5 files often beats a sprawling prompt with 500 files.

**The professional move**: give the AI only what it needs. If it needs more, let it ask for it using tools (file search, grep). This is called **context engineering**, and it is the topic of [Chapter 6](06_context_engineering.md).

---

## How Much Is a Token, Really?

Here are some real examples to give you a sense:

| What | Roughly how many tokens |
| :--- | :--- |
| The word "hello" | 1 |
| This sentence | ~15 |
| A paragraph of text | ~80 |
| A page of a book | ~300 |
| A 100-line code file | ~1,000 |
| A 2,000-line code file | ~15,000 |
| This whole chapter | ~2,000 |
| A whole novel | ~80,000 |
| A whole large codebase | millions |

When you hear "the model has a 200K context window," that means it can hold about 200,000 tokens at once — roughly a 500-page book, or a medium-sized codebase. It sounds like a lot, but it fills up fast when you start reading files and running commands.

---

## Tool Output Is Also Tokens

Here is a thing that surprises people: **everything the AI sees counts as tokens**, not just what you type.

- When the AI reads a file, that file's content goes into the context window.
- When the AI runs a command and sees the output, that output goes into the window.
- When the AI searches the web, the search results go into the window.

A 5,000-line log file dumped into context is 35,000+ tokens. That is a big chunk of your window gone. This is why professionals are careful about what tools they run and what they let the AI read — every read costs tokens.

---

## The Big Picture

- A **token** is how the AI measures text (about 4 characters).
- The **context window** is how much the AI can hold at once (often 100,000 to 200,000 tokens).
- When the window is full, old stuff falls out and the AI forgets.
- **More is not better.** Load what you need, not everything.
- **Tool output counts.** Reading files and running commands uses tokens too.

Understanding tokens and the context window is the foundation for everything else in this handbook. When you understand why the AI forgets things, why it costs money, and why it gets confused with too much input, the rest makes sense.

---

## 4.6 Current Model Context Windows (Late 2025)

Here are real context window sizes for popular models available in late 2025. These numbers come from each company's own model pages. They change fast — always check the source for the latest number.

| Model | Context Window (tokens) | Approx. pages of text | Cost tier |
| :--- | :--- | :--- | :--- |
| Claude Sonnet 4.5 (Anthropic) | 200,000 | ~300 pages | Medium |
| Claude Opus 4.1 (Anthropic) | 200,000 | ~300 pages | Expensive |
| GPT-5 (OpenAI) | 400,000 | ~600 pages | Expensive |
| GPT-5 mini (OpenAI) | 400,000 | ~600 pages | Cheap |
| Gemini 2.5 Pro (Google) | 1,000,000 | ~1,500 pages | Expensive |
| Gemini 2.5 Flash (Google) | 1,000,000 | ~1,500 pages | Cheap |
| Llama 4 Scout (Meta) | 10,000,000 | ~15,000 pages | Free (open weights) |
| Llama 4 Maverick (Meta) | 1,000,000 | ~1,500 pages | Free (open weights) |

Sources: [Anthropic — claude](https://www.anthropic.com/claude), [OpenAI](https://openai.com), [Google DeepMind — Gemini](https://deepmind.google/technologies/gemini/), [Meta — Llama blog](https://ai.meta.com/blog/llama/).

**Cost tier** is a rough guide. "Cheap" means a few cents per million tokens. "Expensive" means $10–$30+ per million output tokens. Prices fall fast — by the time you read this, everything may be cheaper. Open-weight Llama models are free to download, though you still pay for whatever computer runs them.

### What "1 Million Tokens" Actually Looks Like

When a model brags about a "1 million token context window," what does that mean in real life?

- 1 token ≈ 3/4 of a word, so 1 million tokens ≈ **750,000 words**.
- A typical novel is about 80,000–100,000 words, so 1 million tokens is roughly **7 to 8 novels**.
- A typical textbook page is about 500 words, so that's about **1,500 pages** of text.
- In code, it's roughly a **large codebase** — think 20,000 to 30,000 lines of code.

That sounds huge, and it is. But remember: the context window is shared by **everything** the AI sees — your prompt, past messages, files you paste, tool output, even hidden system instructions. A million tokens fills up faster than you think, especially once tools start dumping log files. Big windows are great, but "load only what you need" is still the right instinct.

---

Continue to [Chapter 5 — Talking to AI: Prompting Styles](05_prompting_styles.md).

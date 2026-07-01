---
title: 'Chapter 5 — Talking to AI: Prompting Styles'
date: 2026-06-25
tags: [Teaching, AI-Coding-Handbook, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Handbook
chapter: 5
liberal_art: Trivium-Rhetoric
audience: beginner
---

# Chapter 5 — Talking to AI: Prompting Styles

> A **prompt** is what you type to the AI. There are many named "styles" of prompting you will hear about. This chapter explains what each one is and what it is **for** — in plain language.

---

## The Simple Version

All prompting styles are just different ways to tell the AI what you want. There is no "best" one. Each style fits a different kind of task. The more styles you know, the more flexible you are.

The common thread: **clarity beats cleverness.** A plain, clear prompt beats a fancy-named technique applied wrong.

---

## The Styles

### Zero-Shot Prompting

**What it is**: You just ask the AI to do something, with no examples.

**Example**: "Write a function to reverse a string."

**What it is for**: Common tasks the AI already knows well. Most modern models are good enough that zero-shot just works for everyday things. This is the default — if you do not know which style to use, start here.

---

### Few-Shot Prompting

**What it is**: You give the AI 2 to 5 examples of what you want, then ask it to do the next one.

**Example**:
```
Input: "I love this!" → Sentiment: positive
Input: "This is terrible." → Sentiment: negative
Input: "It was okay, I guess." → Sentiment: ?
```

**What it is for**: When the task has a specific format, or the pattern is unusual. Showing examples teaches the AI what you want better than describing it.

---

### Caveman Prompting

**What it is**: Very short, direct prompts with no politeness or filler.

**Example**: "fix bug login.ts line 42"

Instead of: "Could you please help me figure out why the login endpoint is returning a 500 error when I submit the form?"

**What it is for**: Mechanical tasks where you know exactly what you want. The point is not to be rude — it is to strip away words the AI does not need. Long polite sentences can actually dilute the signal.

**When it fails**: When the task is subtle and the AI needs to understand the "why." If you are not sure what the problem is, switch to full sentences and explain.

---

### Chain-of-Thought (CoT)

**What it is**: You ask the AI to think step by step before giving the answer.

**Example**: "Think step by step. If a train travels 60 mph for 2 hours, how far does it go?"

**What it is for**: Math, logic, and multi-step reasoning. By thinking out loud, the AI uses the intermediate steps to "show its work" — which often leads to a more correct answer. Some models now do this automatically; for others, you still need to ask.

---

### Role Prompting

**What it is**: You tell the AI who to be.

**Example**: "You are a senior security engineer reviewing this code."

**What it is for**: Setting the AI's perspective. It is not magic — the AI cannot actually be a security engineer — but it biases the output toward the right lens. Use sparingly. Overdone role prompts waste tokens and can make the AI play-act instead of think.

---

### Step-Back Prompting

**What it is**: Before answering, you ask the AI to state the broader principle.

**Example**: "What are the general principles of input validation? Now apply them to this code."

**What it is for**: When the AI is about to dive into details and miss the bigger picture. Stepping back first helps it see the forest, not just the trees.

---

### Self-Consistency

**What it is**: You run the same prompt a few times (with randomness turned up) and take the majority answer.

**What it is for**: Reasoning questions where one run might go wrong. If 4 out of 5 runs give the same answer, that is probably the right one. Expensive in tokens — use only when correctness matters more than cost.

---

### Tree of Thoughts

**What it is**: A fancier version of chain-of-thought where the AI explores multiple branches of reasoning and picks the best.

**What it is for**: Mostly research. Most everyday tools do not use it directly, but you may see the name. Do not worry about it unless you are building advanced reasoning systems.

---

## Two Big Categories

All the styles above fall into two broad flavors:

### Instruction Style

Direct commands. "Do X, then Y, then Z."

**Good for**: Code tasks, mechanical work, anything with a clear right answer.

**Example**: "Read login.ts, find the bug on line 42, fix it, run the tests."

### Conversation Style

More open and exploratory. "Hey, I was thinking about X, what do you think?"

**Good for**: Brainstorming, exploration, ambiguous problems.

**Example**: "I am trying to add pagination to the users endpoint. What are the trade-offs between offset/limit and cursor-based pagination?"

Most beginners default to conversation style when instruction style would serve them better. For code work, prefer instruction style. For thinking out loud, use conversation style.

---

## The Four-Part Prompt

For code work specifically, a good prompt has four parts:

1. **Goal** — what you want, stated clearly.
2. **Context** — the relevant files, the error, the test that fails.
3. **Constraints** — what NOT to touch, what libraries to use.
4. **Done condition** — how you will know the task is complete.

**Bad example**:
> fix the login bug

**Good example**:
> **Goal**: The login endpoint returns 500 instead of 401 when the password is wrong.
>
> **Context**: `src/auth/login.ts:42` calls `verifyPassword`, which throws when the hash does not match.
>
> **Constraints**: Do not change the public API. Use the existing `AuthError` class.
>
> **Done**: `npm test auth` passes, and a wrong password returns 401.

The second prompt is longer to write, but it saves a round trip and prevents the AI from "fixing" things you did not ask it to touch.

---

## Anti-Patterns (What Not to Do)

**Prompt-as-task-dump**: Pasting a 800-word Jira ticket and saying "just do it." The AI gets lost. Translate business language into engineering language first.

**Trust-without-verify**: Accepting the first answer because it looks plausible. The AI is fluent even when it is wrong. Fluency is not correctness.

**"Do it again but better"**: Gives the AI no signal about what was wrong. Always say specifically what failed.

**Vague scope**: "Refactor this module." The AI will rewrite everything, including things you wanted kept. Always say what is in scope and what is out.

---

## The Big Picture

- There are many prompting styles, but they are all just ways to be clear.
- **Zero-shot** (just ask) is the default for everyday tasks.
- **Few-shot** (give examples) is for unusual formats.
- **Caveman** (short and direct) is for mechanical tasks you understand.
- **Chain-of-thought** (think step by step) is for reasoning.
- **Role**, **step-back**, **self-consistency**, **tree of thoughts** are rarer, for special cases.
- For code: use the **four-part prompt** (goal, context, constraints, done).
- **Clarity beats cleverness.** A plain clear prompt beats a fancy technique applied wrong.

---

## 5.5 Prompting Myths and What Actually Matters

There is a lot of "magic prompt" advice online that does not hold up. Here are the big myths and what actually matters.

**"You need the perfect prompt."** No. A clear prompt matters, but the model, the tools around it, and the context you give the AI usually matter more. Anthropic's own docs point out that problems like cost and latency are often fixed by choosing a different model, not by tweaking words. Get the prompt "good enough," then improve the system around it.

**"More examples = better."** Two or three well-chosen examples usually beat twenty. Past a small number, extra examples stop teaching the AI anything new and just add noise, cost, and length. Pick examples that cover the hard cases, then stop.

**"Always say 'please' and 'thank you.'"** The AI does not care. Politeness does not change the answer, and it wastes tokens and your time. Be direct — that is efficiency, not rudeness.

**"Role prompting makes the AI smarter."** Role prompting does not raise the model's intelligence. It just biases the lens the AI answers through — "senior security engineer" makes it look at code one way, "performance expert" another. It is a perspective trick, not a power-up.

**"Chain-of-thought always helps."** CoT shines on math and multi-step reasoning, where thinking out loud prevents silly mistakes. On simple tasks it adds words for no gain and can even make answers worse by overthinking. Use it when the task actually has steps, not as a default.

**"Longer prompts are better."** Length is not quality. A short, focused prompt that gives the AI exactly what it needs usually beats a long one full of filler, pleasantries, and repetition. Say what you want, give the context that matters, then stop.

### What Actually Matters

1. **Clarity** — say what you want in plain words.
2. **Context** — give the AI the files, errors, and constraints it needs.
3. **The right model** — pick the one that fits the job.
4. **Tools** — evaluations, tests, and structured inputs beat clever wording.
5. **Verification** — check the answer; fluency is not correctness.

A boring, clear prompt with good context beats a clever one every time.

---

Continue to [Chapter 6 — Context Engineering](06_context_engineering.md).

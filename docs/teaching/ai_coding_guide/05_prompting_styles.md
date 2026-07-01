---
title: 'Chapter 5 — Talking to AI: Prompting Styles'
date: 2026-06-25
tags: [Teaching, AI-Coding-Guide, Seven-Liberal-Arts, Trivium-Rhetoric]
type: note
sources: []
status: stable
course: AI Coding Guide
chapter: 5
liberal_art: Trivium-Rhetoric
audience: professional
---

# Chapter 5 — Talking to AI: Prompting Styles

## The honest framing first

There is a whole genre of "prompt engineering" content that treats prompting like a secret spellbook — say the magic words, get the magic result. Most of it is overwrought. With modern models, a clear instruction in plain English gets you 90% of the way there, and the remaining 10% is mostly about *context* (Chapter 6), not wording.

That said, there are a handful of distinct prompting styles, each useful for a different kind of task. Knowing them by name helps you pick the right one, and more importantly helps you read other people's prompts and rules files without wondering what they were trying to do.

This chapter is the short tour.

---

## Style 1 — Caveman / direct

Just say what you want, bluntly.

> "write a function that takes a list of users and returns the ones whose email ends in @example.com, sorted by last name"

This is how most people prompt most of the time, and for most routine coding tasks it's fine. Modern models are good enough that you don't need ceremony. The trade-off: the model fills in a lot of implicit choices for you (naming, error handling, style), and it fills them in according to its training data, which may not match your project's conventions.

**When to use it:** small, self-contained tasks where the result is easy to verify and you don't care about stylistic alignment.

**When not to:** anything where the model needs to match your project's existing patterns, or where the task is ambiguous enough that being explicit will save a round-trip.

---

## Style 2 — Role-based

Tell the model who it is.

> "You are a senior TypeScript engineer who cares about readable code and minimal dependencies. Review this function and tell me what you'd change."

The role doesn't magically summon expertise the model doesn't have, but it does bias the output. Asking for "a senior engineer's review" tends to produce a more critical, more thorough answer than "what do you think?" Telling a model to "act as a security reviewer" before asking it to find vulnerabilities meaningfully changes what it focuses on.

The mechanism is simple: the role changes the prior, which changes what continuations look likely, which changes the output. There's nothing mystical about it.

**When to use it:** when you want a particular *kind* of answer (review, critique, beginner-friendly explanation, security-focused analysis) and the model's default mode wouldn't naturally produce it.

**When not to:** as cargo cult. Slapping "you are an expert developer" on every prompt does nothing.

---

## Style 3 — Few-shot

Show the model examples of what you want, then ask for the next one.

> "Here are three examples of how we format our commit messages:
>
> `feat(auth): add rate limiting to login endpoint`
> `fix(billing): handle null invoice number in PDF renderer`
> `refactor(db): extract connection pooling into its own module`
>
> Now write a commit message for this change: [diff]"

Few-shot is the single most powerful prompting technique for *alignment* — getting the model to match a specific format, style, or convention that isn't in its training data. The model is extraordinarily good at pattern-matching from a small number of examples. Two or three examples is often enough; five is rarely necessary; ten is overkill.

This is also what's happening when you paste an existing function from your codebase and say "write another one like this for [new feature]." You're few-shot prompting, whether you call it that or not.

**When to use it:** any time you want the output to match a pattern that's easier to show than describe — commit messages, error formats, log lines, test structures, component patterns, DSL syntax.

**When not to:** when the examples would eat too much context for the value they add. A few good examples beat many mediocre ones.

---

## Style 4 — Chain-of-thought

Ask the model to reason before answering.

> "Before writing the code, think step by step about the edge cases in this function. List them, then write the implementation that handles each one."

Or, with reasoning-capable models, just let it think — many modern models do chain-of-thought internally by default and don't need to be told.

The classic finding (from 2022, when this was a hot research result) was that asking a model to "think step by step" measurably improved performance on multi-step reasoning. In 2026, with reasoning-trained models, the explicit instruction matters less, but it still helps for tasks where the model is tempted to jump to a confident wrong answer.

**When to use it:** genuinely hard problems where the model has to reason through multiple constraints — tricky bug diagnosis, algorithm design, anything with subtle edge cases.

**When not to:** trivial tasks. Telling a model to think step by step about "capitalize this string" wastes tokens and time.

---

## Style 5 — Decomposition / "plan then do"

Break the task into pieces, explicitly.

> "I want to add CSV export to the reports page. Let's do this in steps:
>
> 1. First, list the files you'd need to touch and why. Don't edit anything yet.
> 2. Then, propose the function signature for the CSV serializer and wait for my approval.
> 3. Then implement it.
> 4. Then add the route handler.
> 5. Then write the test.
>
> Start with step 1 only."

This is the prompting style that most resembles *managing* the agent rather than asking it for a single answer. It's especially valuable when the task is big enough that a one-shot attempt will go off the rails, but you don't want to hand the agent a blank cheque to do whatever it wants.

Most agentic harnesses have a "plan mode" that's essentially this style baked into the loop: the agent proposes a plan, you approve or edit it, then it executes. Asking for a plan first is one of the highest-leverage habits you can build.

**When to use it:** anything non-trivial. The cost of a wrong plan is much lower than the cost of a wrong implementation.

**When not to:** tiny edits where planning would be slower than just doing.

---

## Style 6 — Constraints and negative prompting

Tell the model what *not* to do, and what it must satisfy.

> "Refactor this function. Constraints:
>
> - No new dependencies.
> - Keep the public signature unchanged.
> - Don't touch the logging — there's a reason it's like that.
> - Must still pass the existing tests in `auth.test.ts`.
>
> If you can't satisfy all constraints, say so rather than violating one."

Models are surprisingly obedient about explicit constraints, and surprisingly bad at inferring constraints you didn't state. Negative prompting ("don't do X") is especially important because models have strong default tendencies — e.g. to add a dependency, to add error handling, to add tests, to "improve" things you didn't ask about — and the only reliable way to stop them is to say so.

**When to use it:** any time the model's defaults are likely to conflict with your project's actual needs. Which is most of the time.

**When not to:** never, really. Constraints are free to state and expensive to omit.

---

## Style 7 — Reflective / self-critique

Ask the model to review its own output.

> "Now critique what you just wrote. What would a senior engineer find wrong with it? Then revise it."

This sounds silly — why would a model catch its own mistakes the second time when it didn't the first? In practice it works more often than it has any right to, partly because the act of articulating the criteria surfaces them, and partly because the model's "critique mode" and "generation mode" are slightly different priors. It's not magic, but it's cheap and it sometimes catches real issues.

**When to use it:** when the task is high-stakes enough to justify the extra round-trip, and when you don't have a human reviewer handy.

**When not to:** routine work where you'll review it yourself anyway.

---

## How these combine in real prompts

You rarely pick one style. A real prompt often layers two or three:

- **Role + constraints:** "You're a security reviewer. Don't suggest style changes, only vulnerabilities."
- **Few-shot + decomposition:** "Here are three examples of our migration format. Plan the migration in steps, then execute step 1 only."
- **Chain-of-thought + constraints:** "Reason through the edge cases first, then implement. Don't add error handling beyond what the spec requires."

The styles are tools, not religions. Mix freely.

---

## The thing this chapter is not

This chapter is not "prompt engineering" in the 2023 sense — the meme where you memorize a 400-word template with "STRICTLY FOLLOW THESE RULES" in caps. Modern models don't need that, and the templates mostly stopped mattering around the time GPT-4 shipped. What matters now is:

1. **Clear intent.** Say what you actually want.
2. **Good context.** (Chapter 6. More important than wording.)
3. **Explicit constraints.** Especially negative ones.
4. **A plan first, for non-trivial tasks.**
5. **Verification afterward.** (Chapter 11. Always.)

If you have those five, the specific phrasing almost doesn't matter. If you're missing the first two, no amount of prompt alchemy will save you.

The next chapter is about the part that does matter — context — and why "[[static-vs-dynamic-context|context engineering]]" has largely replaced "prompt engineering" as the word serious practitioners use.

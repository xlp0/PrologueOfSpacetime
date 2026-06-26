# One-Week Teaching Plan: AI Coding Workflow for Schools

> A presentation plan for the Head of School, designed for a one-week session teaching students (ages 13+) how to use AI coding tools professionally. Built on top of the [AI Coding Handbook](handbook/README.md) and the project's narrative docs by Ben Koo.

---

## The Pitch (For the Head of School)

**The problem**: Students are already using ChatGPT to do homework. They are doing it badly — copying answers without understanding, without verification, without knowing when the AI is wrong. We cannot ban it; we can only teach them to use it well.

**The opportunity**: AI coding tools are not just a shortcut — they are a new literacy. Students who learn to work with AI professionally will be dramatically more capable than those who do not. This is the equivalent of teaching word processing in 1990, or the web in 2000.

**The proposal**: A one-week course (5 days, ~3 hours per day) that takes students from "I use ChatGPT to cheat on homework" to "I use AI tools professionally, verify my work, and know the difference." The course is based on a 14-chapter handbook already written, plus hands-on exercises using the project's existing narrative docs as teaching material.

**The outcome**: Students who can:
- Explain what AI coding tools are and how they work.
- Use prompting styles (caveman, few-shot, chain-of-thought) appropriately.
- Understand MCP (Model Context Protocol) and skills — the building blocks of professional AI workflows.
- Verify AI output instead of trusting it blindly.
- Apply a code of conduct: security, IP, honesty, when NOT to use AI.

---

## Why This Project, Why Now

This project — *Prologue of Spacetime* — is not a textbook. It is a **living example** of professional AI workflow. Ben Koo has been building it since November 2025 using exactly the tools and patterns this course teaches. The git log is the proof:

- **36 commits by Ben Koo**, including the most recent narrative docs (TAME, Lambda Calculus, Symmetry, Science of Approximation) written on June 24, 2026 — yesterday.
- **147 commits by Henry Koo**, including the cleanup pass and this handbook, written today (June 25).
- The project uses **Obsidian + git + AI agents** as its workflow — the same workflow we are teaching.
- The **narrative docs** (`docs/narrative/`) are real examples of AI-assisted writing — students can see how a professional writes with AI, not just what the AI produces.

This is not a hypothetical course. It is a course built from the actual work of people who do this every day.

---

## The Five-Day Plan

Each day is ~3 hours: 45 min lecture + 15 min break + 90 min hands-on + 30 min reflection.

### Day 1 (Monday): What Is AI Coding?

**Goal**: Students understand what AI coding tools are, how they work, and why they matter. No hands-on yet — just understanding.

**Chapters covered**: [Ch 1](handbook/01_what_is_ai_coding.md), [Ch 2](handbook/02_how_ai_tools_work.md), [Ch 3](handbook/03_the_stack.md)

**Morning lecture (45 min)**:
- What is an AI coding tool? (Not just ChatGPT — the whole stack.)
- The model is the brain; the harness is the body.
- The agentic loop: observe, reason, act, repeat.
- Why tools matter more than prompting.
- Show the git log of this project as proof that real work happens this way.

**Afternoon hands-on (90 min)**:
- Visit https://opencode.ai together — read what a harness looks like.
- Visit https://modelcontextprotocol.io — read what MCP is.
- Visit https://skills.sh — browse skills, read 2-3 `SKILL.md` files.
- Visit https://mcp.so — browse MCP servers, see what people have connected.
- No installation, no coding — just looking and discussing.

**Reflection (30 min)**:
- "What surprised you?" "What confused you?" "What do you want to try?"

**Reference material**: Ben Koo's [TAME narrative](../narrative/TAME.md) — shows how a professional writes about complex ideas with AI assistance. Read the first 30 lines together as an example of AI-assisted writing.

---

### Day 2 (Tuesday): How AI Thinks

**Goal**: Students understand tokens, the context window, and why "more is not better." They try their first prompts.

**Chapters covered**: [Ch 4](handbook/04_tokens_and_context.md), [Ch 5](handbook/05_prompting_styles.md), [Ch 6](handbook/06_context_engineering.md)

**Morning lecture (45 min)**:
- What is a token? (4 characters ≈ 1 token.)
- What is the context window? (The AI's working memory.)
- Why pasting the whole codebase is a mistake.
- Prompting styles: caveman, zero-shot, few-shot, chain-of-thought.
- The four-part prompt: Goal, Context, Constraints, Done.
- Prompting myths: "always say please," "more examples = better."

**Afternoon hands-on (90 min)**:
- Use ChatGPT or Claude (free tier is fine).
- Exercise 1: Write a bad prompt ("fix the bug"). Then write a good prompt using the four-part structure. Compare results.
- Exercise 2: Try caveman prompting on a simple task. Then try chain-of-thought on a reasoning task. Compare.
- Exercise 3: Paste a short piece of code (10-20 lines) and ask the AI to explain it. Then paste a whole file (200+ lines) and ask the same. Notice how the longer one is worse.
- Exercise 4: Read the [Why Three narrative](../narrative/Why%20Three.md) — a real example of AI-assisted writing about complex ideas. Discuss: how much do you think was AI vs. human?

**Reflection (30 min)**:
- "When did the AI surprise you?" "When did it confuse you?" "When did you have to check its work?"

**Reference material**: The [Science of Approximation narrative](../narrative/Science%20of%20Approximation.md) by Ben Koo et al. — a real example of writing that mixes human reasoning with AI assistance.

---

### Day 3 (Wednesday): Plugging Things In

**Goal**: Students understand MCP (Model Context Protocol) and skills — the two things that turn a chatbot into a professional tool.

**Chapters covered**: [Ch 7](handbook/07_mcp.md), [Ch 8](handbook/08_agent_skills.md), [Ch 14](handbook/14_concrete_examples.md)

**Morning lecture (45 min)**:
- What is MCP? "USB-C for AI tools."
- The four concepts: server, client, tools, resources.
- Example MCP servers: filesystem, GitHub, Postgres, PalmierPro (video editor), Slack.
- What is a skill? A packaged workflow the AI loads on demand.
- Skills vs. tools: a tool is a verb; a skill is a recipe.
- Example skills: codebase exploration, video analysis, code review.
- Why skills reduce tokens (the four mechanisms).

**Afternoon hands-on (90 min)**:
- Browse https://mcp.so together. Find 3 servers you did not expect.
- Browse https://skills.sh together. Find 3 skills for tasks you recognize.
- Read 2 real `SKILL.md` files from this project's `.agents/skills/` folder.
- Read the [MVP Cards Design Rationale](../narrative/MVP%20Cards%20Design%20Rationale.md) — the project's own design for MCard (data), PCard (logic), VCard (verification). This is a real example of how professionals design tools.
- Discuss: "If you could plug AI into any system, what would it be?"

**Reflection (30 min)**:
- "What MCP server or skill did you find most interesting?" "What would you build a skill for?"

---

### Day 4 (Thursday): Letting AI Run

**Goal**: Students understand agentic workflows — when to let AI run on its own, and the patterns people use.

**Chapters covered**: [Ch 9](handbook/09_agentic_workflows.md), [Ch 10](handbook/10_the_tools_people_use.md)

**Morning lecture (45 min)**:
- What is an agentic workflow? (Letting AI plan, act, verify, repeat.)
- When to use it: multi-step, verifiable, bounded.
- When NOT to use it: single-shot, unverifiable, unbounded.
- The five patterns: direct edit, plan-then-execute, subagent delegation, explore-then-edit, verify-and-loop.
- The tools people use: opencode, Cursor, Claude Code, Aider.
- The rhythm of a professional session: scope, plan, execute, verify, commit.

**Afternoon hands-on (90 min)**:
- If machines allow: install opencode or Cursor. Give the AI a small task: "Find all the markdown files in this project with broken links. Report what you find."
- If machines do not allow: walk through the git log of this project together. Show how the June 25 commit ("repo hygiene pass + AI coding workflow handbook") was done — scope, plan, execute, verify, commit. It is a real example of the agentic workflow.
- Read the [Agentic Trinitarianism narrative](../prologue_of_spacetime_improvement/Agentic%20Trinitarianism.md) — the project's own framework for understanding AI agents (Miner, Coder, Trader).
- Discuss: "When would you use an agent? When would you drive yourself?"

**Reflection (30 min)**:
- "What is the difference between a chatbot and an agent?" "When would you trust an agent? When would you not?"

---

### Day 5 (Friday): Being Responsible

**Goal**: Students understand the code of conduct — verification, security, IP, honesty — and present what they learned.

**Chapters covered**: [Ch 11](handbook/11_code_of_conduct.md), [Ch 12](handbook/12_words_youll_hear.md), [Ch 13](handbook/13_where_to_learn_more.md)

**Morning lecture (45 min)**:
- The first rule: you are responsible. A bug the AI introduced is still your bug.
- Verification discipline: read the diff, run the tests, check edge cases.
- Security: prompt injection, secrets in prompts, least privilege.
- IP and licensing: AI can reproduce licensed code without warning.
- When NOT to use AI: critical paths, regulated code, code you do not understand.
- The glossary: 35 terms you will hear.

**Afternoon hands-on (90 min)**:
- Exercise: Take a piece of AI-generated text (use ChatGPT to write a paragraph about any topic). Fact-check it. Find at least one thing that is wrong or unverified.
- Read the [Sovereign Truth and Sustainable Swarms narrative](../narrative/Sovereign%20Truth%20and%20Sustainable%20Swarms.md) — the project's framework for truth in AI systems. Discuss: "What does 'sovereign truth' mean when AI can lie confidently?"
- Read the [Code of Conduct chapter](handbook/11_code_of_conduct.md) together. Discuss each rule.

**Reflection and presentations (30 min)**:
- Each student presents: "One thing I learned this week that changed how I think about AI."
- The teacher summarizes: the three big ideas (tools > prompts, verify before you trust, you are responsible).

---

## How to Present This to the Head of School

### The 10-Minute Pitch

**Minute 0-2: The problem.**
"Students are already using ChatGPT. They are using it badly — copying without understanding, not checking answers, not knowing when the AI is wrong. We cannot ban it. We can only teach them to use it well."

**Minute 2-4: The opportunity.**
"AI coding tools are a new literacy — like word processing in 1990 or the web in 2000. Students who learn this now will be dramatically more capable. This is not about replacing teachers; it is about giving students a skill they will use for the rest of their lives."

**Minute 4-6: The course.**
"A one-week course, 3 hours a day, based on a 14-chapter handbook we have already written. It covers what AI tools are, how they work, how to prompt them, how to plug things in (MCP and skills), how to let them run on their own (agentic workflows), and — most importantly — how to use them responsibly. The handbook is written so a 14-year-old can understand it."

**Minute 6-8: The proof.**
"This is not a hypothetical course. It is built from a real project — *Prologue of Spacetime* — that has been built using exactly these tools. The git log shows 36 commits by Ben Koo and 147 by Henry Koo, all using AI-assisted workflow. The students will see real work, not toy examples."

**Minute 8-10: The ask.**
"We need one week, a computer lab with internet access, and a free ChatGPT or Claude account per student. No software installation required — the course is designed to work with browser-based tools. The handbook is open source and will stay available to students after the course ends."

### What to Bring to the Meeting

1. **The handbook README**: `docs/teaching/handbook/README.md` — show the 14-chapter structure.
2. **Chapter 1**: `docs/teaching/handbook/01_what_is_ai_coding.md` — read the first few paragraphs aloud to show the tone.
3. **The git log**: `git log --oneline -20` — show that the work is real and recent.
4. **One narrative doc**: `docs/narrative/TAME.md` — show that the project produces real intellectual content, not just code.
5. **This plan**: `docs/teaching/presentation_plan.md` — the week-by-week breakdown.

### Anticipated Questions and Answers

**"Is this just teaching students to cheat with AI?"**
No. The opposite. The course teaches students to verify AI output, to check its work, to know when it is wrong. A student who copies ChatGPT answers without understanding is cheating. A student who uses AI to learn, checks the output, and takes responsibility for the result is using a tool professionally. This course teaches the difference.

**"Do we need to install software?"**
No. The course is designed to work with browser-based tools (ChatGPT, Claude, skills.sh, mcp.so). Day 4 has an optional installation of opencode or Cursor if the school allows it, but it is not required.

**"Is the material appropriate for 14-year-olds?"**
Yes. The handbook was specifically written so a 14-year-old can understand it. Each chapter has a "Simple Version" at the top and a "Big Picture" at the bottom. The tone is plain professional — no jargon without explaining it.

**"What if the AI produces something inappropriate?"**
The course addresses this directly in the Code of Conduct chapter. Students learn about prompt injection, security, and when NOT to use AI. The hands-on exercises use school-appropriate tasks.

**"How do we know it works?"**
The proof is in the git log. The handbook itself was written using the workflow it teaches — 10 parallel agents researched and expanded the chapters in a single session. That is not a toy example; that is the professional workflow in action.

---

## Materials Checklist

- [ ] The handbook (14 chapters + README) at `docs/teaching/handbook/`
- [ ] This presentation plan at `docs/teaching/presentation_plan.md`
- [ ] The weekly changelog at `docs/changelog/weekly-2026-06-25.md`
- [ ] Internet access for browsing skills.sh, mcp.so, opencode.ai, modelcontextprotocol.io
- [ ] One free ChatGPT or Claude account per student (for Day 2 and Day 5 exercises)
- [ ] A projector for the lecture portions
- [ ] (Optional) opencode or Cursor installed on lab machines for Day 4

---

## The Bigger Picture

This project — *Prologue of Spacetime* — is itself the teaching example. Ben Koo's narrative docs (TAME, Why Three, Science of Approximation, Sovereign Truth) are real examples of AI-assisted intellectual work. The git log is a real example of professional AI workflow. The handbook is a real example of documentation written with AI assistance.

The students are not learning from a textbook. They are learning from a **living project** that does what it teaches. That is the pitch.

---

## Appendix: The Narrative Docs as Teaching Examples

Ben Koo's narrative docs in `docs/narrative/` are the secret weapon of this course. They are real examples of AI-assisted intellectual writing — deep, structured, and citable. Each one teaches a different lesson. Here is what each one is, and what it teaches.

### Why Three? (`docs/narrative/Why Three.md`)

**What it is**: A 305-line essay arguing that "three" is the minimum number required for reality to exist — geometrically (a triangle is the simplest closed shape), logically (a proof needs a witness), and computationally (the Lambda Cube has three dimensions).

**What it teaches**:
- How to structure a long argument (Part I: Vertical/Time, Part II: Horizontal/Space, Part III: Structural Integrity, Part IV: Operational Proof).
- How to use diagrams (mermaid graphs, tables) alongside prose.
- How to cite real thinkers (Robert Harper, Homotopy Type Theory, Curry-Howard-Lambek).
- The "triadic closure" idea: A judges B and C, B judges A and C, C judges A and B — no infinite regress. This is the same structure as the handbook's Spec/Implement/Verify loop.

**When to use it**: Day 2 (How AI Thinks) — show students how a professional writes a long, structured argument with AI assistance. Read Part I together (lines 38-85). Ask: "How much of this do you think was AI? How much was human? How can you tell?"

---

### TAME (`docs/narrative/TAME.md`)

**What it is**: A 151-line essay on Michael Levin's "Technological Approach to Mind Everywhere" — the idea that cognition is a continuous, scale-free phenomenon from single cells to societies.

**What it teaches**:
- How to explain a complex scientific idea in plain language (Levin's tadpoles with scrambled faces that fix themselves — a great hook for students).
- How to use analogies (DNA as hardware specification, bioelectric networks as software).
- How to connect biology to computation (Abstract Interpretation, Galois Connections).
- The concept of a "Cognitive Light Cone" — the boundary of what an agent can care about. This connects directly to the handbook's "context window" idea.

**When to use it**: Day 1 (What Is AI Coding) — read the first 30 lines together as an example of AI-assisted writing. It shows students that AI can help with deep intellectual work, not just code.

---

### MVP Cards Design Rationale (`docs/narrative/MVP Cards Design Rationale.md`)

**What it is**: A 485-line design document for a triadic system: MCard (data), PCard (logic), VCard (verification). It argues that these three "cards" are sufficient to represent any knowledge.

**What it teaches**:
- How to write a design rationale (not just what the system does, but *why* it is shaped that way).
- How to connect a software architecture to a mathematical foundation (Cubical Type Theory, polynomial functors).
- The "One Object Mandate" — the idea that complexity should be collapsed into a single primitive, not spread across many. This is the same principle as the handbook's "context engineering": load one good thing, not many bad things.
- How to cite inspiration (Apple's HyperCard from 1987 — "cards + links = knowledge navigation").

**When to use it**: Day 3 (Plugging Things In) — show students how a real system design connects to the ideas they just learned (tools, skills, verification). Read the first 25 lines (the table mapping Magnitude/Direction/Vector to MCard/PCard/VCard).

---

### Science of Approximation (`docs/narrative/Science of Approximation.md`)

**What it is**: A 321-line essay on how we make infinite reality computable by approximating it — from program analysis (Abstract Interpretation) to quantum mechanics (measurement collapse).

**What it teaches**:
- How to write across disciplines (computer science, quantum physics, biology) without losing rigor.
- The Galois Connection: the formal relationship between a concrete system and an abstract model of it. This is the same relationship as "the AI's context window" vs. "the whole codebase."
- The Unix story (lines 46-51): how a disk scheduling algorithm accidentally became an operating system. A great example of bottom-up emergence — the opposite of over-planning.
- "Making illegal states unrepresentable" (Yaron Minsky's principle): a type system is a way to make certain errors impossible. This is a deep idea about design.

**When to use it**: Day 2 (How AI Thinks) — the connection between "approximation" and "the AI's context window" is exact. The AI does not see the whole codebase; it sees an approximation (the files you loaded). Read lines 19-36 together.

---

### Sovereign Truth and Sustainable Swarms (`docs/narrative/Sovereign Truth and Sustainable Swarms.md`)

**What it is**: A 154-line essay on how to build a sustainable, decentralized AI system — one that does not collapse into chaos or centralization.

**What it teaches**:
- How to write a design argument grounded in physics and math (thermodynamics, Shannon entropy, the Tinbergen Rule).
- The concept of "sovereign nodes" — each part of the system owns its own decisions. This connects to the handbook's "you are responsible" rule.
- The "Software Lagrangian" (line 51-56): maximizing verified information ($S_T$) while minimizing noise ($H_T$). This is the same as the handbook's "verify before you trust."
- How to use diagrams to show a feedback loop (line 64-75: the cybernetic loop of the PKC Mesh).

**When to use it**: Day 5 (Being Responsible) — the idea of "sovereign truth" is the perfect frame for the code of conduct. The AI can lie confidently; the human must own the verification. Read lines 15-24 together.

---

### Function-Number Duality (`docs/narrative/Function-Number Duality.md`)

**What it is**: An 884-line essay on the foundational duality of computation: Numbers (static, what IS) and Functions (dynamic, what DOES) are two views of the same thing.

**What it teaches**:
- How to write a very long, structured argument with clear parts (Part I: Philosophical Foundations, Part II: Algebraic Structure, etc.).
- How to connect philosophy (Heidegger's Being vs. Becoming), mathematics (complex numbers, category theory), and computer science (lambda calculus, monads).
- The Pythagorean roots (Real vs. Lateral axes mapped to Number vs. Function). This is a great example of how a modern technical essay can draw on ancient ideas.
- The executive summary table at the top (lines 33-42) — a model of how to summarize a long argument in a table.

**When to use it**: Day 2 or Day 4 — as an example of how deep AI-assisted writing can go. Students do not need to understand the math; they need to see that a human and an AI together can produce work of this depth.

---

### Symmetry (`docs/narrative/Symmetry.md`)

**What it is**: A 130-line essay on symmetry as "the absence of history" (after Michael Leyton). A blank hard drive is symmetrical because no bits have been written.

**What it teaches**:
- How to take an intuitive idea (symmetry) and redefine it rigorously (symmetry = no causal history).
- How to connect a mathematical concept to a software architecture (MCards as "shapes" with maximum symmetry; VCards as "causal histories" that break symmetry).
- The Invariance-Variance duality (line 46-53) — a clean table mapping two poles of a duality. Students can use this pattern in their own writing.
- "Decision is Symmetry-Breaking" (line 78) — a coin flip is symmetric; the landing is not. A powerful, simple idea.

**When to use it**: Day 3 or Day 5 — as an example of how to write a short, focused essay. The 130-line length is approachable for students. Read it together and discuss the structure.

---

### Judgment (`docs/narrative/Judgment.md`)

**What it is**: A 165-line essay on what a "judgment" is in formal logic and typed lambda calculus (Γ ⊢ t : T).

**What it teaches**:
- How to explain a technical notation (the turnstile ⊢) in plain language.
- How to connect logic to typed programming (a judgment is a type assertion; type checking is proof verification).
- The reference to Ray Dougherty's lecture (line 44) — a real example of how to cite a talk.
- The structure: start with a definition, give examples, connect to a broader theory (Martin-Löf Type Theory).

**When to use it**: Day 2 — as an example of how to write a clear technical explainer. Short, focused, with concrete examples.

---

### How to Use These Docs in Class

**Do not try to teach the content.** The math and philosophy in these docs is graduate-level. The students do not need to understand Curry-Howard-Lambek or Galois Connections.

**Do teach the structure.** These docs are models of how to write with AI:
1. Start with a thesis (the boxed equation or the "Core Thesis" quote at the top).
2. Break the argument into parts (Part I, Part II, Part III).
3. Use tables to summarize (see the executive summary tables).
4. Use diagrams to show relationships (the mermaid graphs).
5. Cite real sources (named thinkers, real papers).
6. End with an operational proof (how the idea works in practice).

**The exercise**: Pick one narrative doc. Read the first 20-30 lines together. Ask:
1. "What is the thesis?" (Find the boxed equation or the Core Thesis quote.)
2. "How is it structured?" (Find the Parts.)
3. "What sources does it cite?" (Find the named thinkers.)
4. "Where do you think the AI helped? Where is the human?" (This is a judgment call — there is no answer key. The point is to think about it.)

**The takeaway for students**: AI-assisted writing is not "the AI writes it for you." It is a collaboration. The human provides the thesis, the structure, the sources, and the judgment. The AI helps with the prose, the examples, and the bulk. These docs are what that collaboration looks like when it goes well.

---

*Last updated: 2026-06-25. Based on the [AI Coding Handbook](handbook/README.md) and the *Prologue of Spacetime* project.*

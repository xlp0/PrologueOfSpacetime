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

*Last updated: 2026-06-25. Based on the [AI Coding Handbook](handbook/README.md) and the *Prologue of Spacetime* project.*

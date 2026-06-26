# The 10-Minute Pitch (Revised: Core = Ask the Right Question)

> **Core idea**: AI can do surprising things — but the real skill is **asking the right question**. The 3 surprises, the tools, the 5-day sprint — all serve that one point. The questions matter more than the answers.

---

## Minute 0-2: The Core Idea + The Three Surprises

**Open with the core**:

> "AI can do surprising things. But the skill that matters most is not *using* AI — it is *asking it the right question*. I want to show you three things AI did on a real project, then I'll show you what happens when you ask the right question — and what happens when you don't."

**Then the six surprises** (15 seconds each — just name them, don't explain):

1. **AI designed a PCB** — a real four-legged robot, with a bill of materials, 3D-printed parts, and code. In this repo.
2. **AI edited a video** — placed clips, trimmed them, generated captions from spoken audio, generated music, exported the cut.
3. **AI ran a Kubernetes cluster** — production infrastructure with B200 GPUs, Mac Studio workers, Grafana monitoring, and a real incident it helped debug.
4. **AI agents that learn and run 24/7** — OpenClaw (this project's own runtime) and Hermes Agent (Nous Research, 203K stars) are AI agents that create their own skills, improve them during use, and migrate between each other.
5. **AI edited 3D models** — 9 OpenSCAD files and 11 STL files in this repo: drone chassis, telescope assembly, oscilloscope case, VR lens holder, turbine generator, Digital Sundial. Real parametric CAD, not toys.
6. **AI builds beautiful websites and web apps** — tools like Lovable and v0.dev (by Vercel) take a plain-English prompt and produce a full, **beautiful**, production-ready website: frontend, styling, sometimes a backend. The most important thing about Lovable and v0 is not that they generate code — it is that the output looks professionally designed. Landing pages, dashboards, portfolios, e-commerce stores — beautiful, deployable in one click, used by millions of builders. On top of that, companies like Anthropic and Vercel publish "agent skills" (frontend-design, vercel-react-best-practices) that teach an AI the conventions of modern web development. This is not a code snippet — it is a beautiful working application.

**The pivot**:

> "Each of these looks like AI doing something impressive. But that is not what happened. What happened is: a human asked the right question, the AI helped, and the human verified the result. The skill is the question."

---

## Minute 2-4: Surprise 3 in Detail (Kubernetes)

Spend 2 minutes on the Kubernetes example because it is the most relatable to a Head of School — it shows AI helping with *real professional infrastructure*, not toys.

> "The third surprise is this. We have a production Kubernetes cluster — that's the system Google uses to run its servers. We have B200 GPU nodes, Mac Studio workers, a Grafana dashboard showing live metrics.

>
> One day, a node called `minipc` started flapping — going up and down, up and down, visible as a barcode pattern in our dashboard. This is a real problem in a production system.

>
> We used an AI agent to debug this. But the AI did not just tell us the answer. It helped us **ask the right questions**:
> - 'Is the node hardware failing?' (No — uptime was 13 hours.)
> - 'Is it the network?' (Yes — but *which* part?)
> - 'Is it ZeroTier, the VPN?' (Partly — two networks were sharing the same subnet.)
> - 'After fixing that, why does Prometheus still fail to scrape?' (Because of Path MTU Discovery failure — the packets were too big and being silently dropped.)

>
> Two separate root causes. The AI helped us find them by walking through the questions, one at a time. Each answer led to the next question. That is the workflow: **ask, verify, ask again.**

>
> The AI also helped us design the migration strategy — Argo CD for deployment, ARC for self-hosted runners, comparing three alternatives and picking one. That document is in this repo. It is real production work."

**The point**: The AI did not replace the engineer. It helped the engineer ask the right questions, faster. The verification — the SSH, the `kubectl`, the Grafana dashboard — was human.

---

## Minute 3-4: Surprises 4 & 5 Listed (Agents + 3D Models)

After the Kubernetes deep-dive, list the last two surprises quickly — no deep explanation, just name them so the Head of School knows the scope:

> "I won't go deep on the last three, but I want you to see the range:

>
> **Fourth: AI agents that learn.** OpenClaw — the agent runtime this project uses — and Hermes Agent, an open-source tool by Nous Research with 203,000 stars on GitHub, are AI agents that create their own skills, improve them during use, and even migrate between each other. Hermes has a command `hermes claw migrate` — it literally imports settings, memories, and skills from OpenClaw. These are not chatbots. They are agents that persist, learn, and work 24/7.

>
> **Fifth: AI edited 3D models.** In this repo there are 9 OpenSCAD files and 11 STL files — real parametric 3D CAD. A drone chassis. A telescope assembly. An oscilloscope case. VR lens holders. A turbine generator. A Digital Sundial. These were produced or edited with AI assistance. Not rendered images — actual 3D-printable mechanical parts.

>
> **Sixth: AI builds beautiful websites.** This is the most relatable one for students — and honestly, the most surprising. Tools like **Lovable** and **v0.dev** (by Vercel) take a plain-English prompt — 'a portfolio site for a photographer' or 'a SaaS landing page' — and produce a full, beautiful, production-ready website. The most important thing about these tools is not that they generate code. It is that the output is **beautiful** — professionally designed, deployable in one click, used by millions of builders. On top of that, companies like Anthropic and Vercel publish 'agent skills' — packages that teach an AI the conventions of modern web development. The AI is not writing one line of code — it is building a beautiful working application."

**The point**: The range matters. From software infrastructure to creative video to physical hardware to self-improving agents to 3D mechanical design to beautiful web applications — the same skill (asking the right question) applies to all of them.

---

## Minute 4-6: Why "Ask the Right Question" Is the Core Skill

> "Here is why the question matters more than the answer. AI is confident even when it is wrong. If you ask it 'fix this bug,' it will give you something that looks right. If you ask it 'why is this node flapping,' it might guess. The difference between a professional and a student is not knowing the answer — it is knowing **what to ask next**.

>
> Our project documents three professional patterns for asking the right question:

1. **The Four-Part Prompt** (from the handbook): Goal, Context, Constraints, Done. Before you ask the AI anything, you state what you want, what you have, what you can't do, and what 'done' looks like.
2. **The Agentic Loop** (from the project's narrative docs): Observe, reason, act, verify, repeat. The AI does not just answer — it loops. Each loop asks a new question based on what it learned.
3. **The Miner-Coder-Trader Triad** (from the project): The Miner asks 'what is the evidence?' The Coder asks 'what is the implementation?' The Trader asks 'is this verified?' Three questions, three agents, one workflow.

>
> This is not theory. This is how the work in this repo actually happens."

---

## Minute 6-8: The One-Week Sprint

> "I am proposing a one-week course, 3 hours a day, built around this one idea: **teach students to ask the right question**.

>
> The structure:

- **Day 1 (Monday)**: Show the three surprises. Let students generate their own questions. The questions they ask become their personal research track for the week.
- **Day 2 (Tuesday)**: How AI thinks — tokens, context window, why 'more is not better.' Students learn that a good question is bounded, not big.
- **Day 3 (Wednesday)**: Finding the right tools. Students research what MCP servers and skills exist for their chosen surprise — PCB, video, or Kubernetes. They write a one-page tool report: what they'd try first, and what they'd need to install.
- **Day 4 (Thursday)**: Letting AI run — agentic workflows. Walk through the git log. Show how the June 25 commits were made: scope, plan, execute, verify, commit. The Kubernetes migration strategy is one of these.
- **Day 5 (Friday)**: Being responsible — code of conduct, verification, security. Students present: the task they chose, the tools they found, the questions they still have.

>
> The deliverable is not a project. It is a set of questions — and a toolbox. Students leave with the questions they need to keep asking."

---

## Minute 8-10: The Ask + The Proof

**The proof**:

> "This is not a hypothetical course. It is built from a real project. The *Prologue of Spacetime* repository has 36 commits by Ben Koo and 147 by Henry Koo, all using AI-assisted workflow. The Kubernetes migration strategy, the minipc incident resolution, the PCB robot, the video editing MCP server — they are all in the repo. The handbook was written by 10 parallel AI agents in a single session. The git log is the proof."

**The ask**:

> "I need one week, a computer lab with internet access, and a free ChatGPT or Claude account per student. No software installation required — the course is designed to work with browser-based tools. The handbook and all materials are open source and will stay available to students after the course ends.

>
> The outcome is not 'students who know how to use AI.' It is **students who know how to ask the right question** — and who have a real toolbox to find the answer.

>
> That is the skill that will still matter in 10 years, no matter how the tools change."

---

## Anticipated Questions

**"Is this just teaching students to cheat with AI?"**
No. The opposite. The course teaches students to ask the right question, verify the AI's answer, and take responsibility for the result. A student who copies ChatGPT answers without understanding is cheating. A student who uses AI to learn, checks the output, and asks the next question — that is a professional.

**"The Kubernetes example is too advanced for 14-year-olds."**
They do not need to understand Kubernetes. They need to see that AI helped a human debug a real production system by asking the right questions, one at a time. The *structure* is what they learn: observe → ask → verify → ask again. The same structure works for any problem, from a math homework to a broken robot.

**"Do we need to install software?"**
No. The course is designed to work with browser-based tools (ChatGPT, Claude, skills.sh, mcp.so). Day 4 has an optional installation of opencode or Cursor if the school allows it, but it is not required.

**"How do we know it works?"**
The proof is in the git log. The handbook itself was written using the workflow it teaches — 10 parallel agents researched and expanded the chapters in a single session. The Kubernetes docs in the repo were produced by an AI agent walking through the questions, one at a time. That is not a toy example; that is the professional workflow in action.

**"What about the math and philosophy in the narrative docs?"**
Students do not need to understand the math. They need to see the *structure* — how a professional writes with AI: thesis, parts, tables, diagrams, citations, operational proof. We teach the structure, not the content.

---

## What to Bring to the Meeting

1. **The git log**: `git log --oneline -20` — show the work is real and recent.
2. **The Kubernetes incident**: `docs/kubernetes/troubleshooting/minipc_network_flapping_resolution.md` — the strongest single example of "ask the right question."
3. **The Kubernetes migration strategy**: `docs/kubernetes/github_actions_migration_strategy.md` — shows AI helping design production architecture.
4. **The handbook README**: `docs/teaching/handbook/README.md` — the 14-chapter structure.
5. **The sprint outline**: `docs/teaching/sprint_outline.md` — the 5-day plan with the 3 surprises.
6. **One narrative doc**: `docs/narrative/TAME.md` — shows the project produces real intellectual content, not just code.

---

*Revised 2026-06-26. Core: ask the right question. Added Kubernetes as the 3rd surprise (replacing the Digital Scope as the primary example — the Digital Scope remains in the sprint outline as a secondary example).*

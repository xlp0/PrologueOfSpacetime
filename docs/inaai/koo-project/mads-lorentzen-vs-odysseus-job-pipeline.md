---
concept: Mads Lorentzen vs Odysseus for job-application automation
tags: [koo-project, job-search, ai-tools, claude-code, odysseus]
source: ChatGPT convs
---

# Mads Lorentzen vs Odysseus for Job Applications

## Insight
Two open-source approaches to AI-assisted job applications, compared 2026-06-10. **Mads Lorentzen's** pipeline runs on Claude Code: fork the repo, fill in your background once, and it runs a 5-step pipeline for every role you apply to — (1) reads the job posting and scores your fit before you waste a single hour; (2) drafts a tailored CV in LaTeX, selecting only the experience that actually matches; (3) writes a cover letter framed around what you bring to that specific role; (4) a second AI agent reviews the first one's work, flags weaknesses, and the first agent revises (peer review for job applications); (5) both documents compile into clean PDFs ready to send. The whole system is a folder of markdown files — plain text, readable, changeable. No subscription, no premium tier, no giving your CV to a startup you've never heard of. Built because Mads needed it for himself, then shared.

**Odysseus** (PewDiePie's) is the more polished self-hosted AI workspace via Docker; larger community.

**Recommendation: start with Odysseus** (more polished, larger community); only move to Mads' 5-step pipeline if you hit limits. A mediocre workflow targeting the right jobs beats a sophisticated workflow spraying applications. The bottleneck is deal flow and targeting, not tool sophistication.

Key insight from this convo: people jump straight to "how do I automate 500 applications?" when the real bottleneck is "is the underlying resume even good?" Garbage in, garbage out — if your master resume is weak, AI will simply generate 500 tailored weak resumes. The correct order: (Phase 1) build the master resume (database, not the document you send; captures everything valuable, quantified achievements, strong accomplishment bullets, ATS-friendly, no fluff); (Phase 2) resume audit (recruiter review / hiring manager review / ATS review / industry-specific review — ask "what makes me look weak?", "what accomplishments are undersold?", "what would cause rejection in 10 seconds?"); (Phase 3) application workflow (JD → AI extracts requirements → AI compares against master resume → AI selects relevant achievements → AI rewrites bullets → AI generates tailored resume → AI generates cover letter → AI prepares interview talking points); (Phase 4) advanced agent workflow (scrape jobs, score fit, rank opportunities, generate tailored materials, track applications, schedule follow-ups, maintain CRM) — only if applying at scale.

## Context
Came up 2026-06-10 (Job Application AI Tools). Ilham had seen Mads' viral LinkedIn post about a Claude Code job-application pipeline. Same convo dove into Odysseus architecture and walked through resume fundamentals.

## Related
- [[odysseus-pewdiepie-self-hosted-workspace]]
- [[chatgpt-vs-claude-vs-local-ai-verdict]]
- [[resume-gpt-custom-instructions-workflow]]
- [[agency-of-one-job-search-reframe]]
- [[koo-project-highlights]]

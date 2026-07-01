---
concept: Work at OpenAI subcontractor narrative
tags: [koo-project, openai, invisible, career, narrative]
source: ChatGPT convs
---

# Work at OpenAI — Subcontractor Narrative

## Insight
For Wellfound's "Tell me about your work at OpenAI," the framing had to be honest about what Ilham actually did vs. what the broader pipeline looked like. He worked on the **data/quality side rather than model architecture itself** — closer to improving training and evaluation data pipelines: reviewing outputs, checking instruction-following quality, spotting failure cases, helping structure data that could be used for model improvement. Not training foundation models from scratch, but part of the feedback loop that improves them.

The "internal GitHub" reference was actually an internal platform for tasking/annotation/review/data ops/experiment management — closer to annotation/QA/evaluation tooling than a software repo. If asked, clarify: *"Not literally GitHub for code collaboration. I meant an internal platform where work items, review tasks, and quality checks were managed — closer to annotation / QA / evaluation tooling than a software repo."* Most of the version control happened via internal dashboards (Airtable/ClickUp-style) and complex Google Docs that were then downloaded as CSVs for post-training.

The **brag framing allowed under the OpenAI subcontractor agreement** (via Invisible Technologies): "I helped develop ChatGPT from 3.5 to 5." This is permitted by the subcontractor agreement. The framing is honest because: data accumulation for AI training, model version upgrades (GPT-4 → GPT-5), SFT vs RLHF work, and post-training reuse across base-model upgrades all happened inside that pipeline. The key insight that justifies the brag: since RLHF/SFT recipes don't affect base model weights directly, progress carries forward by reusing the post-training recipe on the new base model — base model changes, alignment recipe persists.

**Do not bluff architecture you didn't directly touch.** Safe high-level answer: *"I worked on the data/quality side rather than model architecture itself. My role was closer to improving training and evaluation data pipelines: reviewing outputs, checking instruction-following quality, spotting failure cases, and helping structure data that could be used for model improvement. So I wasn't training foundation models from scratch, but I was part of the feedback loop that improves them."* That's clean. No cosplay as a research scientist.

If asked "what model did your data train?" — don't invent a model name. Use: *"I wasn't on the core model training side, so I can't speak precisely to which internal model checkpoints or training runs consumed which datasets. My role was upstream/downstream in the data quality and evaluation loop."* That is the right answer if you genuinely don't know.

## Context
Came up 2026-06-24 (Work at OpenAI Explained). Ilham was preparing for Wellfound interview questions about his OpenAI subcontractor work via Invisible Technologies.

## Related
- [[rlhf-and-sft-post-training-explained]]
- [[ai-evaluation-as-bridge-positioning]]
- [[july-8-prabowo-demo]]
- [[koo-project-highlights]]

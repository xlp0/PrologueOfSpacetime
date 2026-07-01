---
concept: RLHF and SFT post-training explained
tags: [koo-project, llm, training, sft, rlhf, ai-ops]
source: ChatGPT convs
---

# RLHF and SFT — Post-Training Pipeline

## Insight
**Three layers** mixed together in most LLM conversations: (1) the base model, (2) post-training of that same model, (3) the surrounding product system (memory, tools, dashboards, JSON, browsing). Separate them and the whole thing stops looking like black magic.

**Stage A — Base model / pretraining.** Train a transformer on huge text/code corpora to do one task: predict the next token. This buys grammar, facts/associations, style imitation, reasoning patterns, code syntax, world knowledge priors, coherent text continuation. What it does NOT reliably buy: good assistant behavior. A raw base model is rambling, sycophantic, not instruction-following, not concise, not safe, not good at saying "I don't know."

**Stage B — SFT (supervised fine-tuning).** Take the same base model's weights and continue training on curated `prompt → ideal answer` examples. The objective is still next-token prediction, but the data is assistant-shaped. Teaches: chat behavior, instruction following, formatting, concise answers, chain-of-thought patterns, safety behavior, structured output, sometimes tool-calling patterns.

**Stage C — RLHF / preference tuning.** Compare multiple answers; humans choose the better one; use those preferences to push the model toward preferred behavior. SFT = learning from demonstrations ("here is what a good answer looks like — copy this pattern"). RLHF = learning from preferences/rankings/feedback ("between these two answers, humans prefer this one — move your behavior toward what humans prefer"). Concrete data shape: SFT = one prompt + one target answer; RLHF = one prompt + multiple candidate answers + human preference.

**Common misconception corrected:** SFT is not a "filter" on top of a base model. SFT directly changes the model's weights. Think: base model → edited into assistant model, not base model + filter. Not two separate brains. Same brain, trained further. Boxer analogy: pretraining = years of roadwork/sparring/pad work/strength; SFT = coach says "when opponent jabs, counter like this; in amateur rules, score like this"; RLHF = sparring and coaching feedback ("that was the better move, do more of that"). Same fighter, different conditioning and behavioral shaping.

**Carryover across model versions:** since RLHF/SFT don't affect base model weights directly, progress carries forward by reusing the post-training *recipe* on the new base model — base model changes, alignment recipe persists. GPT-5 is not GPT-4 + more SFT; it's a new base model trained from scratch with improved ingredients. What carries from GPT-4 → GPT-5: SFT datasets, preference data, eval sets, tool-use examples, memory/browsing schemas, lessons learned, synthetic data pipelines, better rubrics and QA process. Not "GPT-4 assistant weights pasted onto GPT-5."

**QA ≠ prompt engineering.** Prompt engineering = changing instructions to get better behavior without retraining. QA = checking outputs, testing model behavior, spotting failures, validating labels/data, evaluating whether prompts/tasks are working. They overlap but are distinct.

## Context
Came up 2026-06-24 (Work at OpenAI Explained) and 2026-06-25 (OpenCode vs Pi Agent, where it spilled into an SFT/RLHF discussion). Ilham was preparing "Tell me about your work at OpenAI" for Wellfound and needed to separate what he actually did from what the broader pipeline looked like.

## Related
- [[work-at-openai-subcontractor-narrative]]
- [[ai-evaluation-as-bridge-positioning]]
- [[rlhf-calibration-70-to-90-across-26-qas]]
- [[koo-project-highlights]]
- **Karpathy LLM Wiki**

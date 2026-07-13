<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Automated Design of Agentic Systems
authors: [Shengran Hu, Cong Lu, Jeff Clune]
year: 2024
source_url: https://arxiv.org/abs/2408.08435
drive_file_id: 18x8R3LvzFOoJo1uSJ7GjRycbPvZKJhYB
text_source: paperclip
ingested_by: agent
---

# Automated Design of Agentic Systems

**Authors:** Shengran Hu, Cong Lu, Jeff Clune  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.08435

## One-line
Proposes Automated Design of Agentic Systems (ADAS) and demonstrates Meta Agent Search, where a meta-LLM iteratively programs new agents in code, growing an archive that compounds discoveries across iterations.

## Key claim
A meta-agent that writes agents as Python code (Turing-complete search space) discovers agentic systems that beat hand-designed baselines (CoT, CoT-SC, Self-Refine, LLM-Debate, Quality-Diversity, Step-back, Role-Assignment) by +13.6 F1 on DROP, +14.4% on MGSM, and transfers to held-out domains/models (+25.9% GSM8K, +13.2% GSM-Hard).

## Method
A meta-agent (GPT-4o) is prompted with an ever-growing archive of past agents (code + scores) and asked to produce an "interestingly new" agent: free-text rationale, then a `forward(taskInfo)` function over a ~100-LOC framework exposing FM-query primitives. Two self-reflection passes enforce novelty + correctness; up to 5 refine-on-error iterations. Evaluation is validation accuracy / F1 on the target task; survivors are appended to the archive. Open-endedness via interestingness pressure, analogous to Quality-Diversity / Intelligent Go-Explore.

## Result
Across ARC (easy subset), DROP, MGSM, MMLU, GPQA-diamond, Meta Agent Search beats every hand-designed baseline. Best discovered agents combine recurring "stepping stones" — multi-CoT sampling, expert-role critics (Efficiency / Readability / Simplicity), structured-feedback refinement loops, ensemble over top-k. Discovered agents transfer across domains (math→reading) and models (GPT-3.5→others) with retained gains. Empty-archive initialization still outperforms baselines; on math it even surpasses warm-start (more diverse reasoning exploration). Run cost: ~$300–500 / domain.

## Key terms
ADAS, Meta Agent Search, agentic systems, code-space search, archive-based open-endedness, stepping stones, self-reflection, Chain-of-Thought, CoT-SC, Self-Refine, LLM-Debate, Quality-Diversity, FunSearch, Intelligent Go-Explore, AI-GAs, meta-agent, foundation model, ARC, DROP, MGSM, MMLU, GPQA, transferability, crossover-via-LLM, Clune, Hu

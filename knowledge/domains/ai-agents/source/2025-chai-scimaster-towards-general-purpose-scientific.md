<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "SciMaster: Towards General-Purpose Scientific AI Agents, Part I. X-Master as Foundation: Can We Lead on Humanity's Last Exam?"
authors: [Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xinyu Zhu, Meng Zhou, Yanfeng Wang, E. Weinan, Yuzhi Zhang, Linfeng Zhang, Siheng Chen]
year: 2025
source_url: https://arxiv.org/abs/2507.05241
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SciMaster: Towards General-Purpose Scientific AI Agents, Part I. X-Master as Foundation: Can We Lead on Humanity's Last Exam?

**Authors:** Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xinyu Zhu, Meng Zhou, Yanfeng Wang, E. Weinan, Yuzhi Zhang, Linfeng Zhang, Siheng Chen  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.05241

## One-line
A tool-augmented open-source reasoning agent (X-Master) plus a scattered-and-stacked multi-role workflow (X-Masters) that sets a new SOTA of 32.1% on Humanity's Last Exam, beating OpenAI/Google Deep Research.

## Key claim
Open-source reasoning models (DeepSeek-R1-0528) wrapped with (a) code-as-interaction-language tool use and (b) a 4-stage Solver→Critic→Rewriter→Selector workflow exceed the 30% threshold on HLE for the first time, reaching 32.1% (vs OpenAI Deep Research 26.6%, Gemini Deep Research 26.9%); also 67.4% on biology benchmark TRQA-lit, beating multi-agent OriGene with only 2 web tools vs OriGene's 500+.

## Method
X-Master treats Python code emitted between `<code>...</code>` tokens as a universal interaction language: during the `<think>` trace the model can write code that calls NumPy/SciPy, custom `web_search` (Google + knowledge graph + related queries), and `web_parse` (HTML via ar5iv with PDF fallback for arxiv), with execution results spliced back into context. Agentic behavior is bootstrapped via "Initial Reasoning Guidance" — first-person self-statements inserted after `<think>` that make a non-agentic R1 act agentic without finetuning. X-Masters scales this at inference: 5 parallel Solvers (temperature 0.6, 64k tokens) → 5 parallel Critics → 5 parallel Rewriters each synthesizing all 5 prior solutions → 1 Selector — a structured exploration/exploitation analog to RL rollouts.

## Result
Ablation across stages: R1 alone 17.7% → +Solver tools 21.1% → +Critic 25.0% → +Rewriter 30.6% → +Selector 32.1%. Removing scattering drops to 25.5%; removing stacking drops to 25.0% — both are required. Rewriting markedly shifts the distribution of correct-answer-counts among the 5 solutions toward all-5-correct. Category gains over base R1 are broad (math, humanities, biology, chemistry, physics, engineering, CS/AI).

## Key terms
tool-augmented reasoning, code as interaction language, DeepSeek-R1, agentic workflow, scattered-and-stacked, Solver-Critic-Rewriter-Selector, Humanity's Last Exam, inference-time scaling, Initial Reasoning Guidance, multi-agent rollouts, web_search, web_parse

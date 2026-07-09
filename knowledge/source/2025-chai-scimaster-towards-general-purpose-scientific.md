---
type: source
kind: paper
title: "SciMaster: Towards General-Purpose Scientific AI Agents, Part I. X-Master as Foundation: Can We Lead on Humanity's Last Exam?"
authors: Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xinyu Zhu, Meng Zhou, Yanfeng Wang, E. Weinan, Yuzhi Zhang, Linfeng Zhang, Siheng Chen
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.05241
source_local: ../raw/2025-chai-scimaster-towards-general-purpose-scientific.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. The relevance is *agent architecture*, not math: the scattered-and-stacked (5 Solvers → Critics → Rewriters → Selector) pattern, code-as-interaction-language, and Initial Reasoning Guidance are templates the autonomous-loop agent could borrow for council dispatch and gap-detect synthesis — particularly the empirical finding that rewriter-synthesis-over-N-solutions is where most of the gain lives (5.6-pt jump vs 3.9 for critic).

## Open questions / connections
- Does the scattered-and-stacked workflow improve quantitative math optimization (continuous score), not just multiple-choice/short-answer accuracy? HLE judges with o3-mini; arena problems are exact numerical.
- The Critic→Rewriter rewrite gain (5.6 pts) dominates the Critic's own gain (3.9 pts) — what's the analog for a numerical optimizer council? Maybe "rewrite five strategy.md drafts after seeing all five" rather than per-persona critique.
- Initial Reasoning Guidance (first-person self-statements injected post-`<think>`) is a cheap alternative to finetuning for agent behavior — could be useful for persona dispatch where personas currently re-derive their stance each call.
- Open question: does code-as-interaction generalize to long-running compute jobs (Modal) rather than sub-second tool calls? Paper only shows sub-second `web_search`/`web_parse`.

## Key terms
tool-augmented reasoning, code as interaction language, DeepSeek-R1, agentic workflow, scattered-and-stacked, Solver-Critic-Rewriter-Selector, Humanity's Last Exam, inference-time scaling, Initial Reasoning Guidance, multi-agent rollouts, web_search, web_parse

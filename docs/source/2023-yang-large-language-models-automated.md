---
type: source
kind: paper
title: Large Language Models for Automated Open-domain Scientific Hypotheses Discovery
authors: Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, E. Cambria
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2309.02726
source_local: ../raw/2023-yang-large-language-models-automated.pdf
topic: general-knowledge
cites:
---

# Large Language Models for Automated Open-domain Scientific Hypotheses Discovery

**Authors:** Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, E. Cambria  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.02726

## One-line
Introduces the TOMATO task — generating novel, valid social-science research hypotheses from raw web corpus — and the MOOSE multi-module LLM framework with three feedback mechanisms (present, past, future) to solve it.

## Key claim
LLMs, when scaffolded with iterative multi-aspect feedback (clarity / reality / novelty checkers plus past- and future-feedback), can produce hypotheses that social-science PhD experts rate as both novel ("not in literature") and valid ("reflecting reality"); MOOSE beats a plain GPT-4 baseline on both GPT-4 and expert evaluation, with progressive gains as each feedback type is added. Expert/GPT-4 soft consistency >0.75 across Validness/Novelty/Helpfulness.

## Method
A pipeline of LLM-prompted modules — Background_Finder → Inspiration_Title_Finder → Inspiration_Finder → Hypothesis_Suggestor → Hypothesis_Proposer — wrapped in two nested loops: an inner present-feedback loop (clarity/reality/novelty critics refine the hypothesis), and an outer past-feedback loop (inspiration selection updated by a heuristic "less-related inspirations → more novel hypotheses"). Future-feedback has earlier modules emit suggestions/justifications that downstream modules build on. Evaluated on a 50-paper post-Jan-2023 social-science dataset with three Marketing PhD raters scoring 400 hypotheses on a 5-point scale.

## Result
Three feedback mechanisms each give monotonic gains over MOOSE-base, which beats the GPT-4 baseline. Qualitative example: baseline hypothesis scores (Validness 4, Novelty 1.5, Helpfulness 2) versus full MOOSE (4.5 / 4 / 4). Expert↔GPT-4 hard-consistency 0.32–0.49, soft-consistency 0.77–0.85, supporting GPT-4 as a proxy evaluator. Counter-intuitive hypotheses (~20% of top-journal output) trade validness for novelty.

## Why it matters here
General background; no direct arena tie. The interesting transferable pattern is the **multi-aspect iterative critic loop** (clarity / reality / novelty + past/future-feedback) as a template for the einstein self-improvement loop — analogous to council-dispatch + gap-detect + failure-finding, but with the critic explicitly separated per-axis and looped. Reinforces that LLM hypothesis-generation needs explicit novelty-vs-validity tension management, mirroring the wiki's reality-check vs cross-pollination filter.

## Open questions / connections
- Does the present/past/future-feedback decomposition transfer to math hypothesis generation (conjecture-style claims about bounds, structure), or is it specific to soft-science narrative hypotheses?
- The "less-related inspirations → more novel" past-feedback heuristic — is there a math analogue (e.g., dispatching personas from distant problem categories to seed P-X)?
- Extends prior self-refine work (Madaan et al., 2023) by adding non-instant feedback channels; future work flags transfer to natural-science domains.

## Key terms
hypothetical induction, open-domain hypothesis generation, MOOSE framework, present-feedback, past-feedback, future-feedback, self-refine, LLM critic loop, novelty-validity tradeoff, multi-aspect filtering, GPT-4 evaluation, inspiration retrieval

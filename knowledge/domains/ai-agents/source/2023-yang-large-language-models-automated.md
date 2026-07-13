<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Large Language Models for Automated Open-domain Scientific Hypotheses Discovery
authors: [Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, E. Cambria]
year: 2023
source_url: https://arxiv.org/abs/2309.02726
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
hypothetical induction, open-domain hypothesis generation, MOOSE framework, present-feedback, past-feedback, future-feedback, self-refine, LLM critic loop, novelty-validity tradeoff, multi-aspect filtering, GPT-4 evaluation, inspiration retrieval

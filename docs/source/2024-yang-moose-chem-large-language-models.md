---
type: source
kind: paper
title: "MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses"
authors: Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, Dongzhan Zhou
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.07076
source_local: ../raw/2024-yang-moose-chem-large-language-models.pdf
topic: general-knowledge
cites:
---

# MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses

**Authors:** Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, Dongzhan Zhou  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.07076

## One-line
A multi-agent LLM framework that rediscovers Nature/Science-level chemistry hypotheses from only a research background, by decomposing $P(h\mid b)$ into inspiration retrieval + hypothesis composition + ranking.

## Key claim
Under the assumption that a hypothesis decomposes as $h = f(b, i_1, \ldots, i_k)$ with $k \in [1,3]$ inspirations, $P(h\mid b)$ factors as $\prod_{j=1}^k P(i_j \mid b, h_{j-1}, I)\cdot P(h_j \mid b, h_{j-1}, i_j)$, defining an MDP over (state, action) = (intermediate hypothesis, chosen inspiration); on a 51-paper post-Jan-2024 benchmark, GPT-4o retrieves >75% of ground-truth inspirations within the top-4% of a 3000-paper corpus and rediscovers core innovations with no data contamination.

## Method
Three-stage agentic pipeline directly implementing the factorization: (1) sliding-window LLM screening of a literature corpus $I$ to pick inspirations $i_j$ unrelated-but-useful to $b$ (not RAG-style semantic neighbors); (2) an "evolutionary unit" that generates multiple hypothesis mutations from $(b, i_j)$, refines each via feedback on validness/novelty/clarity/significance, then recombines survivors; (3) a rating function $R(h)$ scoring validness/novelty/significance/potential for beam-search ranking (default beam = 15, 3 rounds). Evaluated by "Matched Score" (0–5) against expert-annotated ground-truth hypotheses.

## Result
Inspiration-retrieval Hit Ratio: 95.8% at top-20%, 86.9% at top-4%, 70.6% at top-0.8%, 52.0% at top-0.016% (corpus = 3000). MOOSE-Chem reaches Top MS = 4.471 / Avg MS = 3.697 vs SciMON 3.824/3.529 and MOOSE 3.902/3.559; ablations (w/o multi-step: 4.216; w/o multi-step & EU: 3.941) confirm both components contribute. Expert↔GPT-4o evaluation soft-consistency 0.542; expert↔expert 0.854.

## Why it matters here
General background; no direct arena tie — this is about scientific-hypothesis generation in chemistry, not numerical optimization for Einstein Arena. The most transferable idea is the **inspiration-retrieval-vs-semantic-RAG distinction**: a wiki-first agent should sometimes retrieve *non-obvious* pairings (e.g. a technique from a distant problem class) rather than the semantically nearest finding — relevant to council dispatch and cross-pollination gap-detection.

## Open questions / connections
- Does the $h = f(b, i_1, \ldots, i_k)$ decomposition transfer to mathematical-optimization hypotheses (e.g., "compose a new sphere-packing approach from background + two inspirations")?
- The "LLMs encode unrecognized knowledge pairs" claim is testable on the arena's cross-problem findings — could MOOSE-style retrieval surface dead-end findings as inspirations for new problems?
- Evolutionary-unit (mutate → feedback-refine → recombine) is an alternative to the council-dispatch pattern; worth comparing on a single arena problem.

## Key terms
LLM scientific discovery, hypothesis generation, inspiration retrieval, agentic framework, evolutionary algorithm, beam search, Markov decision process, hypothesis ranking, MOOSE-Chem, TOMATO-Chem benchmark, multi-agent LLM, hallucination, chemistry hypothesis decomposition

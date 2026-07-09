---
type: source
kind: paper
title: "Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas"
authors: Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lili Pan, Zhenzhong Lan
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2410.14255
source_local: ../raw/2024-hu-nova-iterative-planning-search.pdf
topic: general-knowledge
cites:
---

# Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas

**Authors:** Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lili Pan, Zhenzhong Lan  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.14255

## One-line
An LLM agent ("Nova") that iteratively plans which external papers to retrieve in order to generate more novel and diverse research ideas than prior RAG-based idea generators.

## Key claim
Nova produces $3.4\times$ more unique novel ideas than a no-planning baseline and at least $2.5\times$ more top-rated (Swiss-tournament score 5) ideas than three SOTA baselines (AI-Researcher, AI-Scientist, Research-Agent) across 170 seed papers.

## Method
Three-stage pipeline: (1) seed-idea generation using the input paper, its references, recent-publication tracking, and 10 Kuhn-style scientific-discovery heuristics, plus self-check/self-critique/reflection; (2) $T{=}3$ iterations of LLM-authored *search plans* — the model identifies which fields to retrieve from, fetches papers, and rewrites each seed into 10 new candidates (pruned to 3 by self-reflection); (3) k-means cluster (405 → 100) then expand each cluster centroid into a full proposal via method-decomposition prompting. Evaluation uses Swiss-tournament pairwise ranking with Claude-3.5-Sonnet plus 10 PhD-level human raters.

## Result
On 170 LLM-related papers from ACL/ICLR/CVPR 2024, Nova yields 619 ideas at score 4 and 2521 at score 5 (vs. far smaller counts for baselines); >80% of generated ideas are non-duplicates (cosine threshold 0.8 on all-MiniLM-L6-v2). Ablation: removing planning flattens unique-idea growth at iteration 3 (42.4 → 44.1); removing both planning and retrieval stagnates at ~31. Human and LLM rankings agree on the method ordering: Nova > AI-Scientist > Research-Agent > AI-Researcher. Gains plateau after 3 iterations.

## Why it matters here
General background; no direct arena tie. The "plan-which-knowledge-to-retrieve before retrieving" pattern is structurally similar to the einstein agent's wiki-first + council-dispatch + self-improvement loop, and the Swiss-tournament pairwise ranking is a candidate template for ranking competing optimizer ideas when no analytical ground truth exists.

## Open questions / connections
- No reward model on the planning step — authors flag this as a limitation; analogous to council dispatch lacking an explicit utility for "which question to ask next".
- Iteration plateau at $T{=}3$: why does novelty saturate? Maps to the einstein loop's "same gap re-learned next cycle" failure mode.
- Pairwise Swiss-tournament ranking (5 rounds × Claude-3.5-Sonnet) reported as more reliable than direct scoring — potentially reusable for ranking dead-end findings or candidate techniques in `docs/agent/skill-library.md`.

## Key terms
LLM idea generation, iterative planning, retrieval-augmented generation, Swiss-system tournament, pairwise ranking, novelty evaluation, diversity evaluation, self-critique, self-reflection, Kuhn paradigm, scientific discovery heuristics, knowledge-graph retrieval

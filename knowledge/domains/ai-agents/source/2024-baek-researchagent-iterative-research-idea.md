<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval]
title: "ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models"
authors: [Jinheon Baek, S. Jauhar, Silviu Cucerzan, Sung Ju Hwang]
year: 2024
source_url: https://arxiv.org/abs/2404.07738
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models

**Authors:** Jinheon Baek, S. Jauhar, Silviu Cucerzan, Sung Ju Hwang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.07738

## One-line
An LLM-powered system that generates novel research ideas (problem + method + experiment design) from a seed paper, augmented with a citation graph and an entity co-occurrence knowledge store, then iteratively refined by LLM "reviewer" agents aligned to human judgment criteria.

## Key claim
Augmenting an LLM with (1) citation-graph–retrieved related papers and (2) an entity-centric knowledge store of cross-paper concept co-occurrences, plus iterative critique from human-preference-aligned ReviewingAgents, produces research ideas judged clearer, more relevant, and especially more novel than ablated LLM baselines on a 300-paper multidisciplinary benchmark, per both GPT-4 and human evaluation.

## Method
Pipeline $o = [p, m, d]$ generated as $p = \text{LLM}(T_p(L))$, $m = \text{LLM}(T_m(p,L))$, $d = \text{LLM}(T_e(p,m,L))$ over a literature subset $L$ chosen by citation-graph proximity to a high-impact core paper. Augmentation: a sparse entity co-occurrence matrix $K \in \mathbb{R}^{m \times m}$ built by off-the-shelf entity linking over post-2023 papers, with top-$k$ retrieval $\arg\max_I \sum_{e_j} P(e_j|e_i)P(e_i)$ surfacing concepts *outside* the seed context to force cross-domain pollination. Refinement: five-criterion ReviewingAgents (clarity, validity, novelty, feasibility, reproducibility, etc.) whose rubrics are induced by prompting GPT-4 on ~10 human-scored Likert pairs per criterion.

## Result
On 300 sampled core papers (avg 87 references, 2.17 entities/abstract), the full ResearchAgent beats two ablations (naive single-paper; references-only without entity store) on all criteria in both GPT-4 and human pairwise judgments. The entity store and iterative refinement each independently contribute gains; humans rated induced criteria as "strongly" (2/5) or "moderately" (3/5) aligned with their own judgments. No quantitative theorem — empirical NLP system paper.

## Key terms
research idea generation, large language models, knowledge-augmented LLM, citation graph retrieval, entity co-occurrence, cross-domain pollination, iterative refinement, ReviewingAgent, human-preference alignment, Likert criteria induction, literature-based discovery, hypothesis generation

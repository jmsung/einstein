---
type: source
kind: paper
title: "SciMON: Scientific Inspiration Machines Optimized for Novelty"
authors: Qingyun Wang, Doug Downey, Heng Ji, Tom Hope
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.14259
source_local: ../raw/2023-wang-scimon-scientific-inspiration-machines.pdf
topic: general-knowledge
cites:
---

# SciMON: Scientific Inspiration Machines Optimized for Novelty

**Authors:** Qingyun Wang, Doug Downey, Heng Ji, Tom Hope  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.14259

## One-line
A framework for LLMs to generate novel scientific research ideas from a background-context input, by retrieving "inspirations" from prior literature and iteratively boosting novelty against retrieved similar work.

## Key claim
LLMs (including GPT-4) by default produce ideas of low technical depth and novelty; combining (a) inspiration retrieval from semantic neighbors, KG neighbors, and citation neighbors, with (b) an iterative retrieve–compare–update novelty-boosting loop and (c) an in-context contrastive fine-tuning objective, substantially raises human-judged helpfulness — but generated ideas still fall far short of real-paper novelty/depth/utility.

## Method
Pipeline over an ACL Anthology corpus (67,408 papers) processed by scientific IE (PL-Marker, SciCo, ScispaCy, sentence classifier) to extract $(B, T)$ pairs — background context $B$ (problem/motivation + seed term $v$) and target ideas $T$. Idea generation runs through (i) retrieval of inspirations from three graphs — semantic-similarity graph $G_S$ over SentenceBERT (all-mpnet-base-v2) embeddings, background KG $G_B$ of used-for relations, and citation graph $G_c$; (ii) generation by GPT-3.5 / GPT-4 (in-context) or T5 (fine-tuned with an InfoNCE in-context contrastive loss $L_{cl}$ using in-text negatives); (iii) an iterative novelty loop that re-retrieves the top-$k{=}20$ most-similar prior ideas to the current draft $I_t$ and re-prompts the model to differ from any whose cosine similarity exceeds $\mu = 0.6$, terminating when all similarities fall below threshold.

## Result
On a 194-instance hand-curated gold test set, GPT4-FS and GPT4-FS+KG dominate (73% and 66% "helpful" votes respectively), with fine-tuned T5+SN+CL the strongest non-GPT-4 baseline at 48%. KG-augmented variant trades a slight overall-helpfulness drop for higher technical depth. Automated BERTScore/ROUGE-L favors fine-tuned T5 variants (R-L ≈ 0.25, BERT ≈ 0.69) over GPT-4 (R-L ≈ 0.15) because of surface-form mismatch. IE preprocessing precision is 91–100% per stage except relation extraction (65%), with 79.7% overall pass rate.

## Why it matters here
General background; no direct arena tie. The retrieve–compare–update loop is structurally analogous to the einstein self-improvement loop (gap → search → ingest → distill → page) and to council-dispatch question-generation — specifically the idea of using cosine-similarity thresholds against a literature corpus to force outputs to differ from prior work could inform how the agent gates novelty of proposed approaches or wiki findings.

## Open questions / connections
- Can the iterative similarity-threshold novelty gate ($\mu = 0.6$ against top-$k$ retrieved priors) be adapted to filter agent-proposed optimization approaches against prior dead-end findings?
- The "questions, not answers" council-dispatch rule echoes SciMON's finding that LLMs generate plausible-but-shallow ideas — does seeding with extracted seed-term + context (vs free generation) generalize to math problem framing?
- Extends prior literature-based discovery (Swanson ABC model, knowledge-graph link prediction) to open-ended natural-language hypothesis generation; leaves open how to evaluate idea quality without expensive human raters.

## Key terms
literature-based discovery, hypothesis generation, retrieval-augmented generation, novelty optimization, in-context contrastive learning, InfoNCE, SentenceBERT, scientific knowledge graph, citation neighbors, GPT-4, T5 fine-tuning, iterative refinement

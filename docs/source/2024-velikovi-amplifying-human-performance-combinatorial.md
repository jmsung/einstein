---
type: source
kind: paper
title: Amplifying human performance in combinatorial competitive programming
authors: Petar Veličković, Alex Vitvitskyi, L. Markeeva, Borja Ibarz, L. Buesing, Matej Balog, Alexander Novikov
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2411.19744
source_local: ../raw/2024-velikovi-amplifying-human-performance-combinatorial.pdf
topic: general-knowledge
cites:
---

# Amplifying human performance in combinatorial competitive programming

**Authors:** Petar Veličković, Alex Vitvitskyi, L. Markeeva, Borja Ibarz, L. Buesing, Matej Balog, Alexander Novikov  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2411.19744

## One-line
Humans write a greedy-heuristic backbone for an NP-hard problem; FunSearch (LLM + evolutionary search) evolves only the scoring function inside it, amplifying scores into the top percentile.

## Key claim
On all eight Hash Code online qualification rounds (2015–2022), human-designed backbone + FunSearch-evolved score function reaches the top percentile, surpasses the finals-qualification cutoff in every year, and beats the rank-1 human team in 5/8 contests (2015, 2018, 2020, 2021, 2022); also achieves ~9th–17th place (95% CI) on held-out AtCoder Heuristic Contest 039.

## Method
Hybrid human-AI workflow: human writes (i) input parser, (ii) greedy-algorithm backbone, (iii) systematic evaluator, plus a trivial initial scoring function `score_greedy(...)`. FunSearch (Gemini 1.5 Flash 002 + island-based evolutionary search with best-shot prompting) mutates *only* the scoring function over ~10,500 program evaluations per backbone in 2h, using the contest's own score as fitness. A boolean "switching variable" lets one evolved function score multiple choice points (e.g., `rate_project` vs role; `give_pos` vs duration). Limits: 10 GB RAM, 1800 s wall-clock per program.

## Result
Evolved scoring functions are interpretable algebraic expressions with hard-threshold gates (e.g., `if server.size > 125: return -100`) and emergent structure not in the seed: subgrid weighted averages, center bias, contiguity bonuses (AHC 039), or $\lfloor N_{cars} N_{str}/1000 + 0.1) \ln(N_{cars}+1) + 1 \rfloor$ for green-light durations (HC2021, score $1{,}019{,}868 \to 1{,}465{,}888$). Solutions typically require 10–30 LLM mutation chains; not retrieval — backbones are unseen in training. HC2015 evolved fn: 348 → 405 pts (rank 2).

## Why it matters here
General background; no direct arena tie — but methodologically *very* relevant to the JSAgent loop. Einstein Arena problems are *exactly* the same regime: NP-hard, partial-credit, public testcases, intractable optima. The "human backbone + LLM-evolved scoring function" pattern is a candidate template for the autonomous-loop agent itself (scoring/heuristic functions inside L-BFGS / basin-hopping / CMA-ES warm-starts). FunSearch + program-space evolution is a possible alternative/complement to council-dispatch on problems where the bottleneck is heuristic search rather than analytical insight.

## Open questions / connections
- Could FunSearch-style evolution evolve *parameterization choices* (Polya step 7 specialize) or *initialization heuristics* for arena problems P1/P11/P15 rather than full solutions?
- Switching-variable trick (one fn, branched choice points) — can it scale to >2 choice points (multi-stage pipelines)?
- Extends Romera-Paredes et al. (2024) FunSearch (cap-set, bin-packing) — same machinery, new domain (combinatorial competitive programming).
- Fitness-evaluator mismatch (AHC 039: hill-climbing set vs held-out testcases) — directly parallels local-evaluator-vs-arena-verifier drift (triple-verify rule).

## Key terms
FunSearch, evolutionary program search, LLM-guided code evolution, greedy heuristic, scoring function, Hash Code, AtCoder Heuristic Contest, combinatorial optimization, NP-hard, human-AI collaboration, island-based evolution, best-shot prompting, Gemini, Romera-Paredes, Veličković, hill-climbing, switching variable

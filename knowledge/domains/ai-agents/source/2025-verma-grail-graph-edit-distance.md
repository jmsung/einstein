<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, sci-math]
title: "GRAIL: Graph Edit Distance and Node Alignment Using LLM-Generated Code"
authors: [S. Verma, Arushi Goyal, Ananya Mathur, Ankit Anand, Sayan Ranu]
year: 2025
source_url: https://arxiv.org/abs/2505.02124
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# GRAIL: Graph Edit Distance and Node Alignment Using LLM-Generated Code

**Authors:** S. Verma, Arushi Goyal, Ananya Mathur, Ankit Anand, Sayan Ranu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.02124

## One-line
Uses an LLM in a FunSearch-style evolutionary loop to discover interpretable Python programs that compute bipartite-matching weights for approximating NP-hard Graph Edit Distance — without any ground-truth GED supervision.

## Key claim
By reformulating GED approximation as "learn a program that emits bipartite edge weights" and exploiting that any such program yields an *upper bound* on true GED, the method discovers heuristics that beat SOTA neural baselines (GREED, GEDGNN, GRAPHEDX, ERIC, H2MN) on 6 datasets in RMSE and Exact Match Ratio, while also generalizing across domains/sizes (avg rank 2 vs ≥3.5 for neural).

## Method
LLM (Gemini 1.5 Pro) is prompted to write a function $P(G_1,G_2) \to W \in \mathbb{R}^{|V_1|\times|V_2|}$; the weight matrix feeds maximum-weight bipartite matching (Hungarian / neighbor-biased mapper) to produce a node mapping $\pi$, scored by $\text{GED}_\pi$. Candidate programs are evolved via the FunSearch islands model (Romera-Paredes et al. 2024) — 5 islands, periodic culling of bottom half, softmax-sampled top-$k$ programs re-inserted into the prompt. A budget-$b{=}15$ subset of programs is chosen by **greedy submodular maximization** of $J(A)=\sum_{\langle G,G'\rangle}\min_{P\in A}\text{GED}_{\pi(P)}$, proven monotone + submodular; subset-selection itself is shown NP-hard by reduction from Set Cover.

## Result
GRAIL/GRAIL-MIX achieve lowest or near-lowest RMSE on AIDS (0.57), Linux (0.13), IMDB (0.55 vs neural ≥1.5), ogbg-molhiv (2.96), ogbg-code2 (4.22), ogbg-molpcba (3.18). GRAIL-MIX (one model trained on a mixture, 166 pairs/dataset) transfers across all six and beats top-3 non-neural baselines by 30–45% tighter upper bounds on the large ogbg-ppa (avg 243 nodes), where neural methods can't even be trained because ground-truth is infeasible. Submodular selection avoids the overfitting seen in naive top-$b$ selection by individual score.

## Key terms
graph edit distance, GED, bipartite matching, Hungarian algorithm, FunSearch, LLM-guided program synthesis, evolutionary program search, islands model, submodular optimization, greedy hill-climbing, upper-bound minimization, self-supervised heuristic discovery, Romera-Paredes, interpretable heuristics, cross-domain generalization

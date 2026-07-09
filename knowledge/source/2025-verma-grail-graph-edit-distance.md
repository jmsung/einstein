---
type: source
kind: paper
title: "GRAIL: Graph Edit Distance and Node Alignment Using LLM-Generated Code"
authors: S. Verma, Arushi Goyal, Ananya Mathur, Ankit Anand, Sayan Ranu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.02124
source_local: ../raw/2025-verma-grail-graph-edit-distance.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. Closest relevance is *methodological*: this is a concrete, recent template for **LLM-driven program search as combinatorial-optimization heuristic discovery** — the same FunSearch substrate the einstein autonomous-loop agent's design implicitly inherits, and a worked example of "evolve a *bounded* objective so you don't need ground truth", which mirrors the project's triple-verify upper-bound-as-loss stance for hard problems.

## Open questions / connections
- Extends FunSearch (Romera-Paredes et al. 2024 *Nature*) from cap-sets/bin-packing to a labeled-graph matching problem — does the same recipe transfer to sphere-packing / kissing / autocorrelation arena problems where an admissible upper bound exists?
- The submodularity proof for "min over a pool of upper-bound heuristics" is reusable: any arena problem where each candidate solution is a verified upper bound (or lower bound) could plug into the same greedy program-portfolio framework.
- Open: how to discover programs when no closed-form upper bound is available, and how to add human-in-the-loop refinement of LLM-emitted code (raised in the conclusion).

## Key terms
graph edit distance, GED, bipartite matching, Hungarian algorithm, FunSearch, LLM-guided program synthesis, evolutionary program search, islands model, submodular optimization, greedy hill-climbing, upper-bound minimization, self-supervised heuristic discovery, Romera-Paredes, interpretable heuristics, cross-domain generalization

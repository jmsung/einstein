---
type: source
kind: paper
title: "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution"
authors: R. Lange, Yuki Imajuku, Edoardo Cetin
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2509.19349
source_local: ../raw/2025-lange-shinkaevolve-towards-open-ended-sample-efficient.pdf
topic: general-knowledge
cites:
---

# ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution

**Authors:** R. Lange, Yuki Imajuku, Edoardo Cetin  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2509.19349

## One-line
An open-source LLM-driven evolutionary program-search framework that discovers high-performing code (including a new SOTA 26-circle packing) using ~150 samples instead of the thousands required by AlphaEvolve.

## Key claim
ShinkaEvolve matches or beats AlphaEvolve on circle packing ($n=26$ unit-square, maximize $\sum r_i$) within **150 program evaluations** — orders of magnitude more sample-efficient — and generalizes to AIME agent-scaffold design, ALE-Bench heuristic contests (+~2.3% mean, 5th→2nd on ahc039), and novel MoE load-balancing losses.

## Method
Evolutionary code search with three coupled innovations: (i) **parent-sampling** that interpolates uniform / power-law-rank ($p_i \propto r_i^{-\alpha}$) / weighted ($w_i = \sigma(\lambda(F_i-\text{median})) \cdot 1/(1+N(P_i))$) / hill-climbing strategies over island sub-populations; (ii) **novelty rejection-sampling** via code-embedding cosine similarity (threshold $\eta=0.95$) plus an LLM-as-novelty-judge; (iii) **UCB1-based LLM ensemble selection** using a relative reward $r_i^u = \exp(\max(r_i - r_i^b, 0)) - 1$ vs the parent/initial-program baseline, plus a periodic "meta-scratchpad" that distils prior wins into prompt-appended heuristics.

## Result
On the AlphaEvolve circle-packing benchmark ($n=26$), ShinkaEvolve discovers a configuration that **exceeds AlphaEvolve's sum-of-radii** using 150 LLM proposals; the discovered program combines a golden-angle spiral init with corner/edge anchors, SLSQP gradient polish, simulated annealing with reheating, and alternating local-circle / global-ring-rotation perturbations. AIME-2024 agent scaffold rises from baseline ~20% to ~34% accuracy (3 experts + skeptical reviewer + editor-in-chief synthesis under a 10-call budget) and generalizes across years and base LLMs. ALE-Bench LITE: +2.3% mean over ALE-Agent across 10 AtCoder heuristic contests.

## Why it matters here
Directly relevant to the einstein autonomous-loop: this is the closest published analogue to JSAgent's cycle (LLM-guided code mutation + archive + fitness + look-back), with a working recipe for orders-of-magnitude sample reduction on a packing problem in the same family as Einstein Arena. Informs council-dispatch (LLM-ensemble selection), self-improvement-loop (meta-scratchpad ≈ wiki findings), parent sampling (power-law vs weighted), and the SLSQP+SA+reheat hybrid pattern already familiar from P11/P15.

## Open questions / connections
- Can the UCB1 LLM-bandit and novelty-rejection be ported to JSAgent's cycle runner to cut compute per problem?
- Meta-scratchpad ↔ docs/wiki/findings: is periodic LLM-summary of recent findings a viable wiki-distillation augmentation?
- The discovered circle-packing program (golden-angle spiral + corner/edge anchors + SLSQP + SA-reheat) is a concrete recipe to ablate against current P1/P11/P15 baselines.
- Island migration with best-program-pinning (Tanese 1989, Romera-Paredes 2024) — does this map to per-problem branch separation in mb/?
- Extends AlphaEvolve (Novikov 2025), OpenEvolve (Sharma 2025), LLM4AD (Liu 2024); contrast with FunSearch (Romera-Paredes 2024) and ADAS (Hu 2024).

## Key terms
ShinkaEvolve, AlphaEvolve, FunSearch, evolutionary code search, LLM mutation operator, circle packing, sample efficiency, UCB1 bandit, novelty rejection sampling, island model, meta-scratchpad, agent scaffold design, ALE-Bench, mixture-of-experts load balancing, SLSQP simulated annealing hybrid, golden-angle spiral packing

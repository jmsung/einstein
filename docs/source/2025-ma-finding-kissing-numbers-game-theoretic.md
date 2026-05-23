---
type: source
kind: paper
title: Finding Kissing Numbers with Game-theoretic Reinforcement Learning
authors: Chengdong Ma, Th'eo Tao Zhaowei, Pengyu Li, Minghao Liu, Haojun Chen, Zihao Mao, Yuan Cheng, Yuan Qi, Yaodong Yang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2511.13391
source_local: ../raw/2025-ma-finding-kissing-numbers-game-theoretic.pdf
topic: general-knowledge
cites:
---

# Finding Kissing Numbers with Game-theoretic Reinforcement Learning

**Authors:** Chengdong Ma, Th'eo Tao Zhaowei, Pengyu Li, Minghao Liu, Haojun Chen, Zihao Mao, Yuan Cheng, Yuan Qi, Yaodong Yang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2511.13391

## One-line
A multi-agent RL system (PackingStar) reformulates the Kissing Number Problem as a two-player Gram-matrix completion game and discovers new lower bounds in dimensions 13 and 25–31.

## Key claim
PackingStar improves every known lower bound for $K(n)$ in dimensions 25–31 (gains of 8, 38, 68, 152, 1224, 456, 5476 spheres), achieves the first rational-structure advance in 13D since 1971 ($K_r(13)=1146$ vs. 1130), and sets new records for generalized kissing numbers $K(n,\alpha)$ at $\alpha \in \{1/3, 1/4, 1/5\}$ in dimensions 12, 14, 17, 20, 21, 22.

## Method
Two cooperating agents play a Markov game on the Gram matrix $G$ of pairwise cosines (not coordinates): Player 1 (Filler) samples new rows/columns from a discrete cosine set $C_1$ (extracted via Step-1 MCTS simulation solving $Ax=b, \|x\|_2=1$ for tangent candidates) under PSD + rank constraints; Player 2 (Corrector, a neural policy trained by policy gradient) deletes suboptimal entries to free up room. After each round, $G$ is decomposed into representative submatrices that seed parallel subsequent games — turning unbounded combinatorial search into guided construction. Shared reward $R_{\text{team}} = \|\text{diag}\,G^{(M)}\|_F^2$ (= matrix size). GPU-parallelized via cuBLAS.

## Result
New construction template $K(n) = K(n-24) + K(24) + 2\sum |S_i|$ with $|S_i|=496$ (vs. prior 488), where $S_i$ decomposes into 28 cross-polytope $X_8$ frames + one Conway–Curtis Cross $X_{24}$ — strong evidence the 25D bound 197056 is optimal along this pathway. 31D uses a novel 84-fold weighted $S_i$ via partitioning 7D kissing config into 42 disjoint unit equilateral triangles. 13D: rational $K_r(13)=1146$ with cosine sets $\{\pm 1/4, \pm 1/2\}$ or $\{-3/4, \pm 1/4, \pm 1/2\}$; one variant splits as 1008+138 with a non-antipodal 1008-piece (98 neighbors each). $K_{\text{new}}(17, 1/3)=578 = 288\times 2 + 2$ (two copies of optimal 16D 288-config). $K_{\text{new}}(12, 1/4)=81$ realized as Schläfli code $\otimes$ equilateral triangle, symmetry group order 311040, no antipodal pairs. Human follow-up inspired by patterns pushed 22D under $\alpha=1/5$ to 352.

## Why it matters here
Direct evidence for **Gram-matrix / cosine-set parameterization** as a superior search space vs. coordinate optimization for kissing/spherical-code problems — relevant to any Einstein Arena problem involving sphere packing, kissing numbers, or spherical codes (P-family kissing problems, and likely cross-cutting to autocorrelation/extremal-geometry problems). Concretely contradicts AlphaEvolve's coordinate-space approach (the wiki's only prior AI-kissing reference) and adds: discrete cosine sets are extractable a priori, MCTS over Gram entries scales, asymmetric/non-antipodal configs are competitive.

## Open questions / connections
- No optimality proofs — RL produces constructions but not matching upper bounds; pairing with LP/SDP duality (Cohn–Elkies–style) is the obvious next step.
- Are the discovered non-antipodal high-regularity configs (12D-81, 13D-1008) related to specific finite simple groups, as the authors hint? Concrete correspondence not stated.
- Can the cosine-set Step-1 simulation extract useful priors for problems beyond kissing — e.g., autocorrelation inequalities or Sidon-set–like extremal configurations?
- Extends Kallal–Kan–Wang 2017 (prior 25–31D bounds via Leech subsets) and Cohn–Jiao–Kumar–Torquato 2011 (rigidity); supersedes Leech–Sloane 1971 rational 13D.

## Key terms
kissing number, K(n), spherical code, Gram matrix completion, two-player reinforcement learning, MCTS, cosine set, Leech lattice, Conway-Curtis Cross, cross-polytope frame, antipodal pairs, rational configuration, generalized kissing number K(n,alpha), Schlafli code, AlphaEvolve, Cohn, Viazovska, dimensions 25-31

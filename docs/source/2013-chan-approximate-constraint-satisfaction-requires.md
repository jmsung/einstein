---
type: source
kind: paper
title: Approximate Constraint Satisfaction Requires Large LP Relaxations
authors: S. Chan, James R. Lee, P. Raghavendra, David Steurer
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.0563
source_local: ../raw/2013-chan-approximate-constraint-satisfaction-requires.pdf
topic: general-knowledge
cites:
---

# Approximate Constraint Satisfaction Requires Large LP Relaxations

**Authors:** S. Chan, James R. Lee, P. Raghavendra, David Steurer  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.0563

## One-line
Proves that any polynomial-sized linear program for approximating boolean Max-CSPs (Max Cut, Max 3-Sat, Max 2-Sat) is no more powerful than a constant number of rounds of the Sherali–Adams hierarchy.

## Key claim
Every polynomial-sized LP for Max Cut has integrality gap $1/2$; for Max 3-Sat $7/8$; for Max 2-Sat $3/4$. These gaps persist for LPs of size up to $n^{o(\log n / \log \log n)}$.

## Method
Reduction from general LP relaxations to Sherali–Adams via a Farkas-lemma slack-function representation $c - \Im = \lambda_0 + \sum \lambda_i q_i$ with $q_i \geq 0$. A truncation + Fourier-junta approximation argument shows each smooth slack function $q_i$ is weakly approximated by a $d$-junta on a small subset $S$; a random-restriction (planting) argument then shows that planting an $m$-vertex SA-gap instance $\Im_0$ inside an $n$-vertex instance forces $L(\Im) \geq SA_d(\Im_0)$, leveraging $R \leq n^{\alpha d}$ functions.

## Result
**Theorem 3.1:** any LP of size $\leq n^{d/2}$ for Max-$\Pi_n$ matches at best the $d$-round SA value. Plugging in known SA gaps (Charikar–Makarychev–Makarychev '09, Schoenebeck '08) yields the integrality-gap corollaries above. **Section 4:** for *symmetric* LPs, the connection is much tighter — any symmetric LP of size $n^d$ is dominated by $d$-round SA (via a group-theoretic orbit/stabilizer argument extending Yannakakis). **Section 3.4:** strong separation between nonnegative rank and $\varepsilon$-smooth (or additive-approximate) nonnegative rank — the Max Cut slack matrix has superpolynomial nonnegative rank but only polynomial smooth/approximate nonnegative rank.

## Why it matters here
General background; no direct arena tie. Relevant only as theoretical context for the [compute-router](.claude/rules/compute-router.md) decision matrix entry on "LP / IPM (HiGHS)" — reminds the agent that LP relaxations have provable approximation limits for combinatorial problems, so when an arena problem reduces to a Max-CSP-shaped formulation, polynomial-size LPs cannot beat constant-round SA. Not directly applicable to any of the 23 current arena problems (sphere packing / autocorrelation / kissing / discrete geometry don't reduce to boolean CSPs).

## Open questions / connections
- Quantitative gap: can the $n^{o(\log n / \log \log n)}$ size lower bound be pushed to $n^{\Omega(\varepsilon)}$, matching the SA round-count? Bottleneck is the $m^d$ factor in the Fourier estimate (3.7).
- SDP analog (Question 5.2): does an analogous "general SDP ↔ Sum-of-Squares" theorem hold? Partially resolved in [LRS15].
- Extension beyond product-structured CSPs to TSP, perfect matching, vertex cover — first steps in [Rot14, BPZ15].

## Key terms
linear programming, extended formulation, Sherali–Adams hierarchy, integrality gap, Max Cut, Max 3-Sat, constraint satisfaction problem, nonnegative rank, smooth nonnegative rank, Yannakakis, slack matrix, Sum-of-Squares, Fourier junta approximation, Farkas lemma

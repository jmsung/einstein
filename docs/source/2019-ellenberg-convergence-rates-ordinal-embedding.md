---
type: source
kind: paper
title: Convergence rates for ordinal embedding
authors: J. Ellenberg, Lalit Jain
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.12994
source_local: ../raw/2019-ellenberg-convergence-rates-ordinal-embedding.pdf
topic: general-knowledge
cites:
---

# Convergence rates for ordinal embedding

**Authors:** J. Ellenberg, Lalit Jain  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.12994

## One-line
Proves near-optimal convergence rates for 1D ordinal (non-metric) embedding by linking the reconstruction error to additive-combinatorics bounds on 3-AP-free sets.

## Key claim
For weakly isotonic subsets $x,y \subset [0,1]$ with $\delta_H(x,[0,1]) \leq \alpha$, there is a similarity $A$ with $d_\infty(x,Ay) = O_\epsilon(\alpha^{1-\epsilon})$; matching lower bound $\Omega_\epsilon(\alpha^{1+\epsilon})$ via Behrend/Graham-style 3-AP-free constructions.

## Method
Upper bound: dyadic bisection argument — locating $x_{m/2^k}$ via "betweenness" comparisons gives a recurrence $a_k = (a_{k-1}+a_{k-2})/2 + 2$ controlling drift, yielding error $\leq 2\alpha(\log_2(1/\alpha)+3/2)$. Lower bound: scale a Graham-type $\{1,\ldots,M\}$ subset $S$ with no 3-APs and gaps $\leq k$ into $[0,1]$; the AP-free condition guarantees $|2x_k-x_i-x_j| \geq 1/M$, so any perturbation $<1/(2M)$ preserves all triplet comparisons, and $1/M$ grows like $\alpha^{1+\epsilon}$.

## Result
Proposition 1/5: explicit $O(\alpha \log(1/\alpha))$ upper bound on $\min_A d_\infty(x,Ay)$ in 1D, improving Kleindessner–von Luxburg's $O(\alpha^{1/2})$. Proposition 3: matching $\Omega(\alpha^{1+\epsilon})$ lower bound. Proposition 4: random $\beta$-perturbation with $\beta > n^{-1}$ violates weak isotonicity with probability $\geq 1 - \exp(-cn)$. Experiments in $d \in \{1,\ldots,5\}$ suggest $d_\infty \sim n^{-2}$ independent of $d$, contradicting Arias-Castro's $O(\alpha^{1/2})$ as tight.

## Why it matters here
Direct precedent for the "ordinal/comparison-only information → metric reconstruction" question; the 3-AP-free → ordinal-ambiguity bridge is a transferable trick for any Einstein problem where discrete-geometry rigidity meets additive combinatorics (kissing, packing, autocorrelation extremal configurations). Problem 6 (β-isosceles-free dense subsets of $[0,1]^d$) is a clean open combinatorial-geometry question that aligns with several arena problem families.

## Open questions / connections
- Problem 6: minimum Hausdorff distance for $\beta$-isosceles-free subsets of $[0,1]^d$; would yield $d$-dim lower bounds.
- Does the optimal rate in $\mathbb{R}^d$ improve with $d$ (experimental hint: $n^{-2}$ independent of $d$) or match Arias-Castro's $O(\alpha^{1/2})$?
- Geometry of the "isotonic region" $P_x \subset ([0,1]^d)^n$: round vs pointy, connected?
- Connection to Behrend/Elkin 3-AP-free constructions and to rigidity theory ([JN11], [JJN15]).

## Key terms
ordinal embedding, non-metric multidimensional scaling, triplet comparison, weak isotonicity, Hausdorff distance, 3-term arithmetic progression, Behrend construction, Graham, isosceles-triangle-free, Procrustes, rigidity, additive combinatorics

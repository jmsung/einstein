---
type: source
kind: paper
title: Simpler and Stronger Approaches for Non-Uniform Hypergraph Matching and the Füredi, Kahn, and Seymour Conjecture
authors: Georg Anegg, Haris Angelidakis, R. Zenklusen
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2009.00697
source_local: ../raw/2020-anegg-simpler-stronger-approaches-non-uniform.pdf
topic: general-knowledge
cites:
---

# Simpler and Stronger Approaches for Non-Uniform Hypergraph Matching and the Füredi, Kahn, and Seymour Conjecture

**Authors:** Georg Anegg, Haris Angelidakis, R. Zenklusen  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2009.00697

## One-line
Two simple algorithms (exponential-clocks rounding and greedy) give the currently best LP-relative guarantee $g(e) = |e| - (|e|-1)x(e)$ for non-uniform hypergraph matching, partially attacking the Füredi–Kahn–Seymour conjecture.

## Key claim
For any hypergraph $H=(V,E)$, weights $w \in \mathbb{R}_{\geq 0}^E$, and fractional matching $x \in [0,1]^E$: (i) an exponential-clocks sampler returns a matching $M$ with $\Pr[e \in M] \geq x(e)/(|e| - (|e|-1)x(e))$; (ii) a natural greedy algorithm gives the same factor even for the more general hypergraph $b$-matching problem. This improves Brubach et al.'s $g(e) = |e| + O(|e|e^{-|e|})$.

## Method
Algorithm 1 assigns each edge $e \in \mathrm{supp}(x)$ an independent exponential clock $Z_e \sim \mathrm{Exp}(x(e))$ and selects $e$ iff $z_e < z_f$ for all overlapping $f \in N(e)$; analysis uses the two standard facts about exponentials ($\min$ is $\mathrm{Exp}(\sum \lambda_i)$; $\Pr[X_1<X_2]=\lambda_1/(\lambda_1+\lambda_2)$) plus a union bound $x(N(e)) \leq |e|(1-x(e))$. Algorithm 2 is plain weight-decreasing greedy; analysis uses a charging scheme that routes LP-weight of blocked edges through saturated vertices to chosen edges. Appendix A uses Carr–Vempala LP-duality + ellipsoid to lift Theorem 2 into a sampling result for $b$-matchings.

## Result
The factor $g(e) = |e| - (|e|-1)x(e)$ matches the FKS conjectured $|e|-1+1/|e|$ whenever $x(e) \geq 1/|e|$, and is strictly better than $|e|$ everywhere; equals $|e|$ only when $x(e)=0$. At extreme points of the fractional matching polytope the average load $|e|x(e) \geq 1$ via the sparsity argument $|\mathrm{supp}(x)| \leq |Q|$ with $Q=\{v : x(\delta(v))=1\}$, suggesting the gap to FKS lives in below-average-load edges.

## Why it matters here
General background — combinatorial-optimization LP-relative rounding, not directly tied to the 23 Einstein Arena problems. Closest relevance is to discrete-geometry / packing problems where an LP relaxation gives a fractional solution and one needs an integer matching/packing back (set-packing-shaped subproblems, contention-resolution-style arguments).

## Open questions / connections
- Can the exponential-clocks rounding be extended to $b$-matchings to give a direct (non-ellipsoid) efficient sampler?
- Does a careful pre-alteration of $x$ before rounding close the residual gap to $g(e)=|e|-1+1/|e|$ on edges with $x(e)<1/|e|$?
- Extends Bansal–Gupta–Li–Mestre–Nagarajan–Rudra (2012) and Brubach–Sankararaman–Srinivasan–Xu (2020); generalizes Bruggmann–Zenklusen exponential-clocks use from graph matchings to hypergraphs; the FKS conjecture itself remains open.

## Key terms
hypergraph matching, set packing, b-matching, Füredi-Kahn-Seymour conjecture, fractional matching LP, integrality gap, exponential clocks, randomized rounding, contention resolution scheme, Carr-Vempala metarounding, LP duality, ellipsoid method, charging scheme

---
type: source
kind: paper
title: An optimal monotone contention resolution scheme for bipartite matchings via a polyhedral viewpoint
authors: Simon Bruggmann, R. Zenklusen
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.08658
source_local: ../raw/2019-bruggmann-optimal-monotone-contention-resolution.pdf
topic: general-knowledge
cites:
---

# An optimal monotone contention resolution scheme for bipartite matchings via a polyhedral viewpoint

**Authors:** Simon Bruggmann, R. Zenklusen  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.08658

## One-line
Introduces a polyhedral viewpoint on contention resolution schemes (CR schemes) for rounding fractional solutions in constrained submodular maximization, yielding an optimal monotone CR scheme for the bipartite matching polytope and an improved one for general matchings.

## Key claim
A monotone $(b,\beta(b))$-balanced CR scheme for the bipartite matching polytope, where $\beta(b) = \mathbb{E}\!\left[\frac{1}{1+\max\{\mathrm{Pois}_1(b),\mathrm{Pois}_2(b)\}}\right]$, is constructed and proven optimal — improving the correlation gap lower bound for bipartite matchings, and beating prior monotone CR schemes for general matchings (which used $e^{-2b}$ or $\tfrac12(1-be^{-b})^2$).

## Method
Reframes CR schemes via the marginals of the dropping procedure rather than the explicit (randomized) drop, turning scheme design into a polyhedral feasibility problem over marginal vectors. A "splitting into siblings" reduction (Lemmas 22-23) shows it suffices to design schemes for vectors with arbitrarily small components, where Poisson approximations of the rounding distribution become exact and tractable. Optimality follows by exhibiting matching upper-bound instances on the bipartite matching polytope.

## Result
For bipartite matchings, the optimal balancedness $\beta(b)$ beats the previous best $(1-be^{-b})^2/b$ achievable by intersecting two partition-matroid schemes; at $b=1$ this also raises the correlation-gap lower bound above the $1-\tfrac{2}{5}e + \tfrac{1}{e} \ge 0.4481$ from Guruganesh–Lee. For general matchings, a new monotone scheme improves over the prior $e^{-2}\approx 0.1353$ and $\tfrac12(1-e^{-1})^2 \approx 0.1997$ bounds, and shows the existing $1-2e^{-2}\ge 0.4323$ correlation-gap lower bound is not tight. Improved approximation factors follow for any CSFM combining matching constraints with others.

## Why it matters here
General background; no direct arena tie. Relevant only as a methodological reference for marginal-based polyhedral analysis of randomized rounding — adjacent to LP-duality / correlation-gap techniques the wiki already touches (Cohn–Elkies LP, matroid CR schemes) but no current Einstein Arena problem is a constrained submodular maximization over matchings.

## Open questions / connections
- Exact correlation gap for general (non-bipartite) matchings remains open — gap between new lower bound and Karp–Sipser's $0.544$ upper bound.
- Can the marginal-polyhedral viewpoint give optimal monotone CR schemes for matroid intersection, knapsack-intersect-matroid, or column-restricted packing?
- The "splitting into siblings" reduction is existential (exponential blowup) — efficient realizations for other constraint families?
- Extends Chekuri–Vondrák–Zenklusen [12] CR-scheme framework and Feldman–Naor–Schwartz [21] continuous-greedy bounds.

## Key terms
contention resolution scheme, monotone CR scheme, bipartite matching polytope, correlation gap, multilinear extension, submodular maximization, matroid polytope, Poisson rounding, balancedness, polyhedral rounding, Chekuri-Vondrák-Zenklusen, splitting into siblings

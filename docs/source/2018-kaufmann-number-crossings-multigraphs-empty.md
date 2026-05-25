---
type: source
kind: paper
title: The number of crossings in multigraphs with no empty lens
authors: M. Kaufmann, J. Pach, G. Tóth, T. Ueckerdt
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.10480
source_local: ../raw/2018-kaufmann-number-crossings-multigraphs-empty.pdf
topic: general-knowledge
cites:
---

# The number of crossings in multigraphs with no empty lens

**Authors:** M. Kaufmann, J. Pach, G. Tóth, T. Ueckerdt  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.10480

## One-line
Extends the Crossing Lemma to topological multigraphs whose parallel edges enclose no empty lens, establishing tight lower bounds on the crossing number under two regimes (with/without the locally-starlike condition).

## Key claim
For an $n$-vertex $e$-edge separated topological multigraph $G$ with $e > 4n$: (i) if $G$ is also locally starlike, $\operatorname{cr}(G) \geq \alpha e^3/n^2$; (ii) in general (parallel edges still no empty lens, but nonparallel edges may cross arbitrarily often), $\operatorname{cr}(G) \geq \alpha e^{2.5}/n^{1.5}$. Both bounds are tight up to the constant $\alpha$.

## Method
Generalized Crossing Lemma framework: any monotone, split-compatible drawing style $\mathcal{D}$ satisfying (P1) crossing-free edge count $\leq k_1 n$, (P2) $\mathcal{D}$-bisection-width bound $b_\mathcal{D}(G) \leq k_2\sqrt{\operatorname{cr}(G) + \Delta(G)\cdot e + n}$, and (P3) edge count $\leq k_3 n^b$, yields $\operatorname{cr}(G) \geq \alpha e^{x(b)+2}/n^{x(b)+1}$ where $x(b) = 1/(b-1)$. Proof is a recursive bisection-decomposition argument à la Pach-Tóth, splitting into parts of $\leq 4/5$ size until parts violate (P3), with Cauchy-Schwarz amortizing the bisection cost. Specializations: locally-starlike separated multigraphs have $e = O(n^2)$ giving exponent $3$; general separated multigraphs have $e = O(n^3)$ giving exponent $2.5$.

## Result
Theorem 1 establishes the two bounds above and shows tightness via constructions: locally-starlike separated multigraphs achieving $\Theta(n^2)$ edges with $\leq 1$ crossing per pair, and general separated multigraphs achieving $\Theta(n^3)$ edges with $\leq 2$ crossings per pair (drawn as circular arcs between $n$ points in general position). The framework also re-derives Székely's bound $\operatorname{cr}(G) \geq \alpha e^3/(mn^2)$ for multiplicity-$\leq m$ multigraphs (slightly improving the edge threshold from $5mn$ to $(3m+1)n$) and the Pach-Spencer-Tóth high-girth bound $\operatorname{cr}(G) \geq \alpha_r e^{r+2}/n^{r+1}$ for girth $> 2r$.

## Why it matters here
General background; no direct arena tie — the Einstein Arena problems are continuous optimization (sphere packing, autocorrelation, kissing numbers), not topological graph drawing or extremal combinatorics on multigraph crossings.

## Open questions / connections
- Best-possible Crossing Lemma for separated *and* single-crossing multigraphs: reduces to finding the smallest $b$ with $e = O(n^b)$; authors conjecture $b = 2$, since verified up to a log factor (Fox-Pach-Suk 2021).
- The bisection-decomposition meta-template (P1)+(P2)+(P3) $\Rightarrow$ crossing bound is a reusable engine: any drawing style with edge-count growth exponent $b$ and a $\sqrt{\operatorname{cr}}$-type bisection bound automatically gets a crossing lemma with exponent $1 + 1/(b-1) + 1$.
- Extends Pach-Tóth (branching multigraphs, 2020), Pach-Tardos-Tóth (non-homotopic, 2020); Felsner et al. (2020) studied a related no-empty-lens setting on $K_n$.

## Key terms
Crossing Lemma, topological multigraph, empty lens, separated drawing, locally starlike, branching multigraph, bisection width, edge multiplicity, Ajtai-Chvátal-Newborn-Szemerédi, Leighton, Pach-Tóth, Székely, extremal graph theory, girth

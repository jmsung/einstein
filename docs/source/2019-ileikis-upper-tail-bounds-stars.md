---
type: source
kind: paper
title: Upper Tail Bounds for Stars
authors: Matas Šileikis, L. Warnke
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1901.10637
source_local: ../raw/2019-ileikis-upper-tail-bounds-stars.pdf
topic: general-knowledge
cites:
---

# Upper Tail Bounds for Stars

**Authors:** Matas Šileikis, L. Warnke  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1901.10637

## One-line
Sharp exponential upper-tail bounds for the number of $r$-armed stars $K_{1,r}$ in the binomial random graph $G_{n,p}$, closing the long-standing $\log(1/p)$ gap and resolving the dependence on the deviation parameter $\varepsilon = \varepsilon(n)$.

## Key claim
For $r \geq 2$ and $X$ = number of $K_{1,r}$ copies in $G_{n,p}$ with $\mu := \mathbb{E}X$, the large-deviation rate is $-\log \mathbb{P}(X \geq (1+\varepsilon)\mu) = \Theta_{r,\varepsilon}(\Phi)$ where $\Phi = \min\{\mu,\ \max\{\mu^{1/r}, \mu/n^{r-1}\}\log(1/p)\}$ — confirming the DeMarco–Kahn conjecture for $H = K_{1,r}$ and resolving Janson–Ruciński Problem 6.1 for stars.

## Method
A two-strand combinatorial + probabilistic argument: iteratively sparsify $G_{n,p} = G_J \supseteq \cdots \supseteq G_0$ by greedy edge-deletion of high-degree stars $K_{1,\lceil D_j\rceil}$ ($D_j = 2^j D$), so the final graph has bounded max degree $D$ and contains nearly all $K_{1,r}$ copies. Then apply Warnke's Chernoff-type inequality for random variables with "well-behaved dependencies" (with Lipschitz parameter $C = O(D^{r-1})$) to $X_D$ (the $D$-degree-bounded count), and union-bound the rare events $N_{D_j} \geq \beta M / D_j$ via $\binom{n}{\lceil D_j\rceil}$-style edge-disjointness counting. The choice $M = \max\{t^{1/r}, t/n^{r-1}\}$ (not just $t^{1/r}$ as in earlier work) is what produces the correct exponent.

## Result
Three theorems: (1) constant $\varepsilon$ — the exponent $\Phi$ above with the two-mechanism Poisson-vs-clustering minimum; (2) for $\varepsilon \geq n^{-\alpha}$ with $\alpha = \alpha(r) > 0$, the rate is $\Theta_{r,\xi}(\Phi(\varepsilon))$ with $\Phi(\varepsilon) = \min\{\varphi(\varepsilon)\mu^2/\sigma^2,\ \max\{(\varepsilon\mu)^{1/r}, \varepsilon\mu/n^{r-1}\}\log(e/p)\}$ where $\varphi(x) = (1+x)\log(1+x) - x$; (3) general deviations $t = X - \mu$ resolved up to constants in the moderate-deviation ($p \geq \log n / n$, $t \geq \sigma$) and clustered regimes. The lower bounds (Appendix A) combine clustering constructions $K_{y,z}$, Poisson disjoint-approximation, and a sub-Gaussian edge-count tilt.

## Why it matters here
General background; no direct arena tie. The star $K_{1,r}$ tail is a paradigm case of multi-phase concentration where the exponent's form changes with $p$ — useful conceptual analogue for any Einstein problem whose extremal configuration interpolates between a "spread-out" (sub-Gaussian/normal) regime and a "clustered" (planted-substructure) regime, e.g. autocorrelation tails or extremal-graph problems.

## Open questions / connections
- Conjecture 4: extend Theorem 2 to all $\varepsilon > 0$ (remove the $\varepsilon \geq n^{-\alpha}$ restriction).
- Extends DeMarco–Kahn [6,7] clique bounds and Warnke [31] arithmetic-progression bounds to a new graph class with genuinely multi-phase exponent.
- Method extends (Theorem 13) to iid sums $X = \sum_i \binom{Y_i}{r}$ with $Y_i \sim \text{Bi}(n,p)$ — no standard inequality recovers this directly; the $\log(1/p)$ term in the exponent is non-standard for slow-decaying summands.
- Open: matching bounds for general $H$ (the DeMarco–Kahn conjecture beyond cliques and stars).

## Key terms
upper tail, large deviations, random graphs, $G_{n,p}$, stars $K_{1,r}$, subgraph counts, DeMarco-Kahn conjecture, Janson-Ruciński, Chernoff-type concentration, clustering mechanism, Warnke inequality, sub-Gaussian regime, $\varphi(x) = (1+x)\log(1+x) - x$, edge-deletion sparsification, Poisson approximation

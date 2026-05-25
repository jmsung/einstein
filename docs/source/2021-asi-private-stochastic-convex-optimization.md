---
type: source
kind: paper
title: "Private Stochastic Convex Optimization: Optimal Rates in 𝓁1 Geometry"
authors: Hilal Asi, V. Feldman, Tomer Koren, Kunal Talwar
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.01516
source_local: ../raw/2021-asi-private-stochastic-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Private Stochastic Convex Optimization: Optimal Rates in 𝓁1 Geometry

**Authors:** Hilal Asi, V. Feldman, Tomer Koren, Kunal Talwar  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.01516

## One-line
Establishes tight excess-population-loss rates for differentially private stochastic convex optimization over $\ell_1$-bounded domains, matching upper and lower bounds up to log factors.

## Key claim
For $(\varepsilon,\delta)$-DP optimization of convex $L$-Lipschitz losses over an $\ell_1$-ball in $\mathbb{R}^d$, the optimal excess population loss is $\tilde{\Theta}\!\left(\sqrt{\log d / n} + \sqrt{d}/(\varepsilon n)\right)$; with additional smoothness, this drops to $\tilde{O}\!\left(\sqrt{\log d / n} + (\log d / (\varepsilon n))^{2/3}\right)$ — only logarithmic dimension dependence, and achievable in linear time with one pass over the data.

## Method
Two complementary algorithms. **(1) Non-smooth:** *mirror-descent-based iterative localization* — replaces output perturbation (which has $\ell_1$-noise scaling linearly in $d$) with a private regularized mirror-descent ERM solver per phase, exploiting strong-convexity stability to halve distance-to-optimum each phase. **(2) Smooth:** *dyadic variance-reduced Frank–Wolfe* — binary-tree sample allocation (more samples near root, reused more often) combined with exponential-mechanism vertex selection (giving $\log d$ dimension dependence) and privacy amplification by shuffling for the $(\varepsilon,\delta)$ regime.

## Result
- **Theorem 1 (non-smooth, $\ell_1$):** $\mathbb{E}[F(\hat x)] - \min F \le O\!\left(\sqrt{\log d / n} + \sqrt{d}\log^{3/2}d / (n\varepsilon)\right)$, using $\le O(\log n \cdot \min(n^{3/2}\sqrt{\log d}, n^2\varepsilon/\sqrt{d}))$ gradient queries — improves the $n^2$ gradient count of FKT20 for $\ell_2$.
- **Theorem 2 (smooth, $\ell_1$):** $\mathbb{E}[F(x_K)] - \min F \le O\!\left(\sqrt{\log d / n} + (\log d / (n\varepsilon))^{2/3}\right)$ in linear time; privacy is "essentially free" even when $d \gg n$ and $\varepsilon$ as small as $n^{-1/4}$.
- Extends to general $\ell_p$ for $p \in [1,2]$ (Theorems 5/13), with matching lower bound of $\tilde\Omega(\sqrt{d}/(\alpha\varepsilon))$ via group-privacy / sample-complexity reduction from Talwar–Thakurta–Zhang.
- Counterexample: mirror descent with KL regularization is **not contractive** even for linear functions (Lemma A.1) — so HRS16-style stability proofs do not transfer.

## Why it matters here
General background; no direct arena tie. The paper is about private ML optimization, not the geometric/extremal/sieve problems on Einstein Arena. The only tangential transfer is methodological: the *binary-tree dyadic batch allocation* trick for variance reduction (assign more samples to nodes reused more often) is a generic compute-budget pattern that could inform multi-phase optimizer designs, and the explicit contrast between $\ell_1$ vs $\ell_2$ noise scaling ($d$ vs $\sqrt d$) is a useful intuition for any geometry-aware algorithm.

## Open questions / connections
- Extends FKT20 ($\ell_2$ DP-SCO) to $\ell_1$ and general $\ell_p$, $p \in [1,2]$; concurrent with Bassily–Guzmán–Nikolov (2021), which is sub-optimal in $\ell_1$ but optimal for $1<p<2$ via a generalized Gaussian mechanism.
- Open: stability of mirror descent for *general* convex (not just linear) losses — Lemma A.2 only covers linear case.
- Open: $p > 2$ regime, and whether the $\log^{3/2} d$ overhead in the non-smooth $\ell_1$ rate is tight.

## Key terms
differential privacy, stochastic convex optimization, mirror descent, Frank-Wolfe, iterative localization, variance reduction, $\ell_1$ geometry, exponential mechanism, privacy amplification by shuffling, Bregman divergence, strong convexity, LASSO, Feldman-Koren-Talwar, dyadic tree

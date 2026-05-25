---
type: source
kind: paper
title: The p-Airy distribution
authors: S. Caracciolo, Vittorio Erba, A. Sportiello
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.14468
source_local: ../raw/2020-caracciolo-p-airy-distribution.pdf
topic: general-knowledge
cites:
---

# The p-Airy distribution

**Authors:** S. Caracciolo, Vittorio Erba, A. Sportiello  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.14468

## One-line
Introduces and characterizes a one-parameter family of universal limit distributions (the $p$-Airy distributions) generalizing the area-Airy distribution to deformed-area observables $A^{(\omega_p)}(w) = \sum_{e \in w} \omega_p(\ell_w(e))$ on Dyck paths/bridges, where $\omega_p(k) \sim k^p$.

## Key claim
For $p > \tfrac{1}{2}$ and $p \in (0,\tfrac{1}{2})$, the deformed area satisfies $A^{(\omega_p)} \stackrel{d}{=} \alpha(\omega_p) N + x_p N^{p+1/2}(1 + O(N^{-\min(p,\eta,1/2)}))$, with $x_p$ a universal random variable whose integer moments obey a quadratic Takács-type recursion: $\mu_s(p) = \mu_{s-1}(p)\frac{\Gamma(s(p+1/2)-1)}{2\Gamma(s(p+1/2)-1-p)} + \sum_{k=1}^{s-1}\mu_k(p)\mu_{s-k}(p)$, with $\mu_0(p) = -\tfrac{1}{2}$. At $p=1$ this recovers Takács' recursion for the area-Airy distribution.

## Method
Generating-function singularity analysis on Dyck paths/bridges: encode moments via formal power series $E_s(z), B_s(z)$, derive a quadratic recursion (Proposition 1) using the standard $w = (+,w_1,-,w_2)$ excursion decomposition, then extract leading singular behavior at $z=1$ using a linear operator $\hat{L}_{(\omega_p,\epsilon)}[f](z) = \sum (\omega_p(N)-\epsilon) f_N z^N$ acting via Hadamard product. Uniqueness of the limit distribution follows from Carleman's condition on moment growth (bounded by $|\mu_s| \le R A^s \Gamma(ps+1) C_{s-1}$).

## Result
Establishes existence of two distribution families $\rho^{(E)}(x;p)$ (excursions, $p > 1/2$: support $\mathbb{R}_+$; $p < 1/2$: support $\mathbb{R}$) and $\rho^{(B)}(x;p)$ (bridges) characterized by moments via the recursion above. Singular limits: at $p = 1/2$, $A^{(\omega_{1/2})} \stackrel{d}{=} t_* N \log N + (\alpha_0 + t_0)N + \tilde{x}_{1/2}N + o(N)$ with $t_* = 1/(2\sqrt{\pi})$; at $p \to 0^+$ with $\omega_0(k) \sim \log k$, Gaussian fluctuations $A^{(\omega_0)} \stackrel{d}{=} \alpha(\omega_0)N + \sqrt{\gamma_E N \log N}\, z + O(\sqrt{N})$. Universality: depends only on exponent $p$, not on microscopic details of $\omega_p$ (provided $\omega_p(k) = k^p(1 + O(k^{-\eta}))$).

## Why it matters here
General background; no direct arena tie. Closest relevance is to the **1D Euclidean Random Assignment Problem** (Section 1.1) — the Dyck-cost upper bound for concave costs $0 < p < 1$ — and to **tree hook formulas** (Section 1.2). Neither is currently an Einstein Arena problem, but the universality machinery (Takács-style moment recursions, singularity analysis on lattice-path generating functions) is a transferable technique if any arena problem reduces to area-statistics of constrained walks.

## Open questions / connections
- Rigorous treatment of the singular $p = 1/2$ limit (companion paper promised) — how to choose the "canonical" regularization $t(p)$ uniquely.
- Extension to multi-dimensional / higher-codimension Brownian processes — what is the $p$-Airy analog for Bessel excursions?
- Whether the combinatorial tree-sum interpretation of moments (Section 3) yields closed forms beyond $p=1$.
- Connection to the optimal cost of the concave ERAP for $0 < p < 1$ — the Dyck cost is only an upper bound; how loose is it?

## Key terms
Airy distribution, p-Airy distribution, Dyck paths, Dyck bridges, Brownian excursion, Takács recursion, area statistics, singularity analysis, generating functions, Euclidean random assignment, hook formula, Catalan numbers, Carleman condition, universality

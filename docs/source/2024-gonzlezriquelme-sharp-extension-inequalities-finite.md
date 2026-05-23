---
type: source
kind: paper
title: Sharp extension inequalities on finite fields
authors: Cristian González-Riquelme, Diogo Oliveira e Silva
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.16647v2
source_local: ../raw/2024-gonzlezriquelme-sharp-extension-inequalities-finite.pdf
topic: general-knowledge
cites: 
---

# Sharp extension inequalities on finite fields

**Authors:** Cristian González-Riquelme, Diogo Oliveira e Silva  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2405.16647v2

## One-line
Initiates sharp restriction theory over finite fields, proving constants maximize Fourier extension inequalities from paraboloids and (some) cones at the Stein–Tomas endpoint.

## Key claim
Constant functions maximize the $L^2 \to L^4$ extension inequality from $P_2 \subset \mathbb{F}_q^{3*}$ with sharp constant $R^*_{P_2}(2 \to 4) = (1 + q^{-1} - q^{-2})^{1/4}$; analogous sharp results hold for $P_1$ ($L^2 \to L^6$, $p>3$), the hyperbolic paraboloid $H^2$, and the cone $\Gamma^3$ when $q \equiv 3 \pmod 4$. For $q \equiv 1 \pmod 4$, maximizers on $P_2$ are exactly $\lambda \exp(2\pi i \operatorname{Tr}_n(a\eta + b\zeta + c\eta\zeta)/p)$. Surprisingly, constants fail to be critical points on $\Gamma^3 \cup \{0\}$ and $\Upsilon^3 \cup \{0\}$ over $\mathbb{F}_p^4$.

## Method
Reformulate even-exponent extension inequalities as multilinear convolution/counting inequalities via Plancherel (Proposition 2.1). Compute $k$-fold convolutions of normalized surface measures explicitly using Gauss sums and Legendre/Jacobi symbols, identifying a "critical set" $\mathcal{C}$ where the convolution spikes. Bound generic-set contributions by Cauchy–Schwarz; on $\mathcal{C}$, exploit the geometry of $\Sigma^k_{P_d}(\xi,\tau)$ (singletons or line-decompositions of $\Gamma^3$ into disjoint punctured lines) plus case-splits modulo $p$. Characterize maximizers via equality-case chasing through every intermediate inequality.

## Result
Sharp constants: $R^*_{P_2}(2\to 4) = (1+q^{-1}-q^{-2})^{1/4}$, $R^*_{P_1}(2\to 6) = (1+q^{-1}-q^{-2})^{1/6}$ ($p>3$), $R^*_{H^2}(2\to 4) = (1+q^{-1}-q^{-2})^{1/4}$, $R^*_{\Gamma^3}(2\to 4) = (1-2q^{-1}+2q^{-2}-3q^{-4}+3q^{-5})^{1/4}(1-q^{-1})^{-3/4}(1+q^{-2})^{-3/4}$ when $q\equiv 3\pmod 4$. Maximizers have constant modulus throughout; for $P_2$ ($q\equiv 1 \pmod 4$) and $H^2$, full classification as exponentials of quadratic trace-forms. For full cones including the origin, $\Phi'_p(0) > 0$ ($\Upsilon^3_0$) and $\Psi'_p(0) < 0$ ($\Gamma^3_0$, $p\equiv 3\pmod 4$) — perturbing constants by adding mass at $0$ strictly increases the functional.

## Why it matters here
General background for the agent — the sharp-restriction / Fourier-extension toolkit (Cauchy–Schwarz on convolution support, equality-case chasing, Plancherel reduction to counting) is the same machinery underlying Cohn–Elkies-style LP bounds and autocorrelation extremals; the finite-field setting offers clean "toy problems" where exact best constants are known. No direct Einstein Arena problem tie, but informs technique pages on extension inequalities, Gauss sums, and the maximizer-characterization workflow.

## Open questions / connections
- Euclidean hyperbolic paraboloid $L^2 \to L^4$ extension remains open (Carneiro–Oliveira–Sousa 2022); finite-field analogue is now resolved — does the FF proof suggest a euclidean route?
- What replaces "constants" as critical points on $\Gamma^3_0, \Upsilon^3_0$? The failure of constants is a new phenomenon absent from the euclidean setting.
- Extends Mockenhaupt–Tao (2004) restriction property $R^*_S(2\to 4)$ from boundedness to sharp form; opens analogous sharp questions for spheres (Iosevich–Koh 2010) and other quadratic varieties.

## Key terms
Fourier extension, finite field restriction, Stein–Tomas endpoint, paraboloid, hyperbolic paraboloid, cone, Gauss sum, Legendre symbol, sharp constant, Strichartz inequality, Mockenhaupt–Tao, Foschi maximizer, Plancherel convolution reduction

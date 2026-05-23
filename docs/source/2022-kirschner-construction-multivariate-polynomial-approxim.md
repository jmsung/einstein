---
type: source
kind: paper
title: Construction of multivariate polynomial approximation kernels via semidefinite programming
authors: Felix Kirschner, Etienne de Klerk
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2203.05892v3
source_local: ../raw/2022-kirschner-construction-multivariate-polynomial-approxim.pdf
topic: general-knowledge
cites: 
---

# Construction of multivariate polynomial approximation kernels via semidefinite programming

**Authors:** Felix Kirschner, Etienne de Klerk  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2203.05892v3

## One-line
Constructs a hierarchy of non-negative multivariate polynomial kernels on $[-1,1]^n$ with minimal "resolution" $\sigma_r$ via SDP, generalizing the univariate Jackson/KPM kernel to several variables with symmetry reduction under $S_n$.

## Key claim
For fixed $n$ and $r \geq n$, the optimal resolution satisfies $\sigma_r^2 \leq n(1 - \cos(\pi/(\lfloor r/n\rfloor + 2))) \sim n^3\pi^2/(2(r+n)^2)$, so $\sigma_r = O(1/r)$, and any continuous $f$ on $K = [-1,1]^n$ obeys $\|K^{(r)}(f) - f\|_\infty \leq 2(1 + \pi/\sqrt{2})\,\omega_f(\sigma_r)$ — the best possible rate for non-differentiable $f$ by Bernstein's theorem.

## Method
Express the desired kernel $K_r(x,y) = \sum_{\alpha \in \mathbb{N}^n_r} g_\alpha T_\alpha(x) T_\alpha(y)$ in the multivariate Chebyshev basis; nonnegativity is enforced via a Fejér-type Positivstellensatz that writes the corresponding even trigonometric polynomial as $\exp(i\alpha^T\phi)^* M \exp(i\alpha^T\phi)$ with $M \succeq 0$. Minimizing the resolution $\sigma_r^2 = \sum_i (1 - g_{e_i})$ gives an SDP whose coefficient matching uses the identity $\prod_i \cos(x_i) = 2^{-H(\alpha)} \sum_{I \subseteq [n]} \cos(\sum_i \omega_I(x)_i)$. Symmetry reduction under $S_n$ via a symmetry-adapted basis decomposes $M$ into $k(n,r)$ smaller psd blocks, dramatically shrinking the SDP for large $n$.

## Result
Tabulated $\sigma_r^2$ for $n \in \{2,3,4\}$ up to $r=50$ ($n=2$), $r=22$ ($n=3$), $r=13$ ($n=4$) using CSDP. Proposition 2 establishes $\sigma_r^2 \leq n(1-\cos(\pi/(\lfloor r/n\rfloor+2)))$, beating the trivial product-of-univariate-Jackson-kernel bound $\sigma_{nr,\text{KPM}}^2 \approx n\pi^2/(2(r+2)^2)$. Numerical comparisons (Figs. 2–3) show the SDP kernels yield smaller uniform errors than products of univariate Jackson kernels on test functions $x_2 \sin(2\pi x_1)$ and a 2D peaks function.

## Why it matters here
Directly relevant to Cohn–Elkies / LP-bound style problems where one needs non-negative auxiliary functions on $[-1,1]^n$ with controlled tails — closes the multivariate-Jackson-kernel gap that may be useful for any arena problem requiring tight $L^\infty$ approximation of non-smooth objective surrogates (autocorrelation, density-of-states, kernel-polynomial-method physics applications). Adds an SDP-constructive route + symmetry-reduction recipe absent from the wiki's current SDP/LP toolkit.

## Open questions / connections
- Closed-form expressions for the SDP-optimal coefficients $g_\alpha$ (univariate Jackson form (12) exists; multivariate form unknown).
- Sparsity exploitation (TSSOS-style, [Wang–Magron–Lasserre]) for large $r$ — symmetry reduction handles large $n$ but not large $r$.
- Connection to Laurent–Slot's effective Schmüdgen Positivstellensatz on the hypercube and Lasserre-type upper-bound hierarchies for polynomial optimization on $[-1,1]^n$.
- Empirical "stabilization" of $\sigma_{r,r'}^2$ at $r' \geq r + \lfloor (r-1)/2 \rfloor$ for $n=2$ — does not hold for $n \geq 3$; structural reason unclear.

## Key terms
Jackson kernel, kernel polynomial method, Chebyshev polynomials, resolution $\sigma_r$, multivariate approximation, semidefinite programming, Positivstellensatz, Fejér theorem, symmetry reduction, $S_n$-invariance, symmetry-adapted basis, Christoffel-Darboux kernel, modulus of continuity, Bernstein theorem, hypercube optimization, Lasserre hierarchy, sum-of-squares, trigonometric polynomials

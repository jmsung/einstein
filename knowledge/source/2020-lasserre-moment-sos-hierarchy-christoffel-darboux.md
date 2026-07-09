---
type: source
kind: paper
title: The moment-SOS hierarchy and the Christoffel–Darboux kernel
authors: J. Lasserre
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.08566
source_local: ../raw/2020-lasserre-moment-sos-hierarchy-christoffel-darboux.pdf
topic: general-knowledge
cites:
---

# The moment-SOS hierarchy and the Christoffel–Darboux kernel

**Authors:** J. Lasserre  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.08566

## One-line
Reinterprets each step of the Moment-SOS lower-bound hierarchy for polynomial optimization as computing a signed polynomial density (with respect to a reference measure $\mu$ on the feasible set $B$) whose coefficients in an orthonormal basis equal moments of a probability measure on $B$, with the optimal density given by the Christoffel–Darboux kernel evaluated at a global minimizer.

## Key claim
For POP $f^* = \min\{f(x) : x \in B\}$ with $B$ compact basic semi-algebraic, the dual of the step-$t$ SOS relaxation (1.2) is equivalent to minimizing $\int_B f \, \sigma \, d\mu$ over signed polynomial densities $\sigma(x) = \sum_{|\alpha| \le 2t} \sigma_\alpha T_\alpha(x)$ whose coefficients are moments $\sigma_\alpha = \int T_\alpha \, d\phi$ of some $\phi \in P(B)$. When the relaxation is exact, $\sigma^*(x) = K_{2t}(\xi, x)$ (the CD kernel anchored at a global minimizer $\xi$), and $\sigma^*(\xi)^{-1}$ equals the Christoffel function at $\xi$.

## Method
Algebraic reinterpretation, not a new algorithm. Uses Fubini interchange plus the reproducing property of the CD kernel $K_t(x,y) = \sum_{|\alpha| \le t} T_\alpha(x) T_\alpha(y)$ on the RKHS $R[x]_t \subset L^2(B,\mu)$. Change of basis matrix $D_t$ between monomial basis $v_{2t}(x)$ and orthonormal basis $(T_\alpha)$ converts the standard moment relaxation $\inf \langle f, y \rangle$ s.t. $y_0 = 1, M_{t-d_j}(g_j\,y) \succeq 0$ (Putinar) into the polynomial-density form $\sigma = D_t \cdot y$.

## Result
Lemma 2.2: $f^* = \inf_\sigma \int_B f\sigma\,d\mu$ over polynomials $\sigma \in R[x]_t$ with coefficients $\sigma_\alpha = \int T_\alpha d\phi$ for some $\phi \in P(B)$. Lemma 2.3: the SDP relaxation (2.8) of this is exactly the dual (1.2) of the standard Moment-SOS hierarchy. Corollary 2.4: at exact relaxation with representing measure $\phi^*$, $\sigma^*(\xi) = K_{2t}(\xi,\xi)$ for every $\xi \in \mathrm{supp}(\phi^*)$, so $\sigma^*(\xi)^{-1}$ is the Christoffel function value. Key contrast with upper-bound hierarchy (1.3): signed density can mimic Dirac on finite moments via reproducing kernel, so exactness is achievable in finitely many steps (generically [Nie 2014]); SOS positive density of (1.3) cannot, giving only asymptotic convergence.

## Why it matters here
Provides a unifying lens connecting the Moment-SOS / Lasserre hierarchy to the Christoffel–Darboux kernel and Christoffel function, both relevant tooling for SDP-based bounds on Einstein Arena problems with polynomial / semi-algebraic structure (e.g., sphere packing relaxations, autocorrelation, LP-bound duals where CD-like extremal kernels appear). Mainly conceptual scaffolding rather than a directly-usable computational recipe.

## Open questions / connections
- Does the CD-kernel-as-optimal-density interpretation suggest a constructive extraction of global minimizers from $K_{2t}(\xi,\cdot)$ that is more numerically stable than current moment-matrix flat-extension methods?
- Connection to [Slot–Laurent 2020] convergence rates on $\{0,1\}^n$ and sphere — does the CD-kernel framing tighten these via Christoffel-asymptotic estimates?
- Extends [Lasserre 2020 "spectral analysis of tri-diagonal matrices"] linking polynomial optimization with orthogonal polynomial theory — open whether the link informs problem-specific hierarchies on Einstein Arena semi-algebraic sets.

## Key terms
Moment-SOS hierarchy, Lasserre hierarchy, Christoffel-Darboux kernel, Christoffel function, semidefinite programming, polynomial optimization, orthonormal polynomials, Putinar positivstellensatz, reproducing kernel Hilbert space, signed polynomial density, moment matrix, flat extension

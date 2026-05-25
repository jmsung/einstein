---
type: source
kind: paper
title: Determining projection constants of univariate polynomial spaces
authors: S. Foucart, J. Lasserre
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.04205
source_local: ../raw/2018-foucart-determining-projection-constants-univariate.pdf
topic: general-knowledge
cites:
---

# Determining projection constants of univariate polynomial spaces

**Authors:** S. Foucart, J. Lasserre  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.04205

## One-line
Computes tight numerical bounds on projection constants $\lambda(U)$ of univariate polynomial subspaces of $C[-1,1]$ by sandwiching them between a linear-programming upper bound and a moment-method semidefinite-programming lower bound.

## Key claim
A discretization-plus-moments approach pins down $\lambda(\mathcal{P}_d)$ to 4–5 digits for low $d$: $\lambda(\mathcal{P}_2)\approx 1.2201$ (recovers Chalmers–Metcalf), $\lambda(\mathcal{P}_3)\approx 1.365$, $\lambda(\mathcal{P}_4)\approx 1.459$, $\lambda(\mathcal{P}_5)\approx 1.538$, with state-of-the-art bounds through $d=12$; also exhibits $\lambda(\mathrm{span}\{1,x^2,x^3\})=1$.

## Method
Upper bound: restrict the signed measures $\mu_m$ defining a projection $P(f)=\sum_m \eta_m(f)u_m$ to atomic measures at points $v_k$, replace the continuous max-norm by a max over Chebyshev zeros $w_\ell$ (using the Ehlich–Zeller bound $\|p\|_\infty \le \cos(\pi d/(2L))^{-1} \max_\ell |p(w_\ell)|$), giving an LP. Lower bound: change variables to $\theta=\arccos x$, Jordan-decompose into nonnegative measures, replace measures by their truncated trigonometric-moment sequences, and impose Toeplitz $\succeq 0$ constraints — yielding an SDP via Lasserre's moment hierarchy. Symmetry $u(-\cdot)\in U$ is exploited by splitting into even/odd bases, halving the problem.

## Result
Upper and lower bounds match to 4–5 digits for $d \le 5$ and tighten the best previously known intervals (Helzel–Petras 1997) for $d=6,\dots,10$, e.g. $1.60271\le\lambda(\mathcal{P}_6)\le 1.60383$; new bounds at $d=11,12$ where none existed. The computed near-minimal projection onto $\mathcal{P}_2$ differs from the Chalmers–Metcalf one (same support but different shape) — suggesting non-uniqueness — and for $\mathcal{P}_3$ a small LP shows the candidate minimal projection fails the $d$-convexity preservation conjecture of Prophet–Chalmers–Metcalf.

## Why it matters here
General background; no direct arena tie. Technique-level relevance: the LP-upper / SDP-lower "sandwich" with Lasserre moments and Chebyshev-zero discretization is the same dual pattern used in Cohn–Elkies / LP-bound work on sphere packing and kissing numbers, and the equioscillation / Chebyshev-zero machinery overlaps with Remez-style extremal problems (P15/P16 family).

## Open questions / connections
- Extends Chalmers–Metcalf (1990) analytic minimal projection for $\mathcal{P}_2$; computationally suggests non-uniqueness — open whether multiple exact minimal projections exist.
- Disproves (numerically) the Prophet–Chalmers–Metcalf 1997 conjecture that minimal projections preserve $d$-convexity for $d \ge 3$.
- Multivariate polynomial projection constants remain essentially open (only Shekhtman–Skrzypek 2006 known); same LP/SDP framework applies but hits numerical limits.

## Key terms
projection constant, minimal projection, Lasserre moment hierarchy, semidefinite programming, linear programming, Toeplitz matrix, trigonometric moment problem, Chebyshev zeros, Ehlich–Zeller inequality, equioscillation, shape preservation, Chalmers–Metcalf

---
type: source
kind: paper
title: Fast conformal bootstrap and constraints on 3d gravity
authors: N. Afkhami-Jeddi, Thomas Hartman, Amirhossein Tajdini
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.06272
source_local: ../raw/2019-afkhamijeddi-fast-conformal-bootstrap-constraints.pdf
topic: general-knowledge
cites:
---

# Fast conformal bootstrap and constraints on 3d gravity

**Authors:** N. Afkhami-Jeddi, Thomas Hartman, Amirhossein Tajdini  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.06272

## One-line
A fast Newton-based algorithm for the (spinless) modular bootstrap that solves truncated crossing equations directly, extending reach from $P \sim 100$ to $P \sim 2500$ and yielding new spectral-gap bounds on 3d gravity duals.

## Key claim
The truncated primal crossing equations (a closed system of $P$ polynomial equations in $P$ unknowns) are Lagrange dual to the extremal-functional method, so their solutions yield rigorous bounds on all unitary CFTs; applied to modular bootstrap, the asymptotic spinless bound at large central charge is $\Delta_1 \lesssim c/9.1$ (best fit $c/9.08 + 0.439\log c - 0.896$).

## Method
Reformulate the dual problem by parameterizing the extremal functional via its roots (single zeros at $\Delta=0,\Delta_1$ and $P/2-1$ double zeros), giving a closed polynomial system. Solve via Newton's method, ramping $P$ upward and using a self-similarity-based guess generator (Hermite-interpolated spectra fit with $a_1 + a_2 y + a_3 \log y + a_4 \log^2 y + a_5 \log^3 y$) to seed each step. Derivative basis uses odd-index Laguerre polynomials $L_{2k-1}$; computations in Mathematica with adaptive precision (16–500 digits).

## Result
At $c=1800, P=2310$, strict bound $\Delta_1^{\max} = c/8.956$; extrapolated asymptotic $c/9.1$ (vs. Hellerman's analytic $c/6$ and BTZ threshold $c/12$). Algorithm is ~$10^6$× faster than SDPB at large $P$ (estimated $10^9$ s for SDPB at $P=2000$ vs CPU-hours here). For $c=12$, recovers $j(\tau)-744$ with $\Delta_1 < 2 + 10^{-30}$. Recovers spectra of $\sim 1000$ operators per problem.

## Why it matters here
Demonstrates that truncating an LP/SDP bootstrap to a closed polynomial system + Newton's method with smart guess-generation can achieve orders-of-magnitude speedup over semidefinite programming — directly relevant for arena problems using LP/SDP duality bounds (Cohn-Elkies sphere packing P1, autocorrelation P15/P16, kissing-number-style problems). The root-parameterization trick and self-similarity guess generator are transferable optimizer techniques.

## Open questions / connections
- Extension to bootstrap problems *with* spin fails because the extremal functional's zero-pattern is no longer the simple "single + double roots" structure — open: how to characterize the spin zero-pattern and generate guesses for it.
- Connection to total positivity (Arkani-Hamed et al. 2018) suggested as the structural reason single+double zeros appear; could give analytic handle.
- Whether spinning modular bootstrap can saturate the BTZ threshold $c/12$ and thereby rule in/out pure 3d quantum gravity remains open.
- "Hot starting" with analytic spectra (lightcone, large-$N$, short-distance) as a way to leverage analytics inside numerics.

## Key terms
conformal bootstrap, modular bootstrap, extremal functional, truncated crossing equations, semidefinite programming, SDPB, Newton's method, Laguerre polynomials, Lagrange duality, 3d gravity, BTZ black holes, central charge, spectral gap, Hellerman bound, j-function, total positivity, root parameterization, self-similar spectrum

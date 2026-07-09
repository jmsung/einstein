---
type: source
kind: paper
title: The Number of Optimal Matchings for Euclidean Assignment on the Line
authors: S. Caracciolo, Vittorio Erba, A. Sportiello
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.04926
source_local: ../raw/2021-caracciolo-number-optimal-matchings-euclidean.pdf
topic: general-knowledge
cites:
---

# The Number of Optimal Matchings for Euclidean Assignment on the Line

**Authors:** S. Caracciolo, Vittorio Erba, A. Sportiello  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.04926

## One-line
Counts and characterizes the (exponentially many) optimal matchings of the 1D Euclidean assignment problem at $p=1$, and studies the limiting distribution of its zero-temperature entropy.

## Key claim
For $N$ white and $N$ black points on a line with cost $c(x)=|x|$, a matching $\pi$ is optimal iff $k_\pi(z)=k_{LB}(z)$ for all $z$ (equivalently, all stacks are monochromatic), giving the product formula $Z_J=\prod_{i:\,h_i\sigma_i<0}\bar h_i(\sigma)$ over descending steps of the associated Dyck bridge, with entropy $S_N \stackrel{d}{=} \tfrac12 N\log N + N s + O(\log N)$.

## Method
Bijection between bi-colored point orderings and lattice paths (Dyck bridges / excursions); combinatorial decomposition around "closing steps" yields a product formula for $|Z_J|$. The limiting rescaled entropy $s=\int_0^1 \log|\sigma(t)|\,dt$ on Brownian bridges/excursions is analyzed via Wiener-process correlation integrals (using the reflection principle, hyperbolic-sine expansions, Gaussian moment formulas) and, in parallel, via singularity analysis of generating functions $M_k^{(T)}(z)$ over the scale $(1-x)^{-\alpha}L(x)^\beta$ with $x(z)=zC(z)^2$.

## Result
Closed forms for first two moments of $s$: for bridges $\langle s\rangle_B=-(\gamma_E+2)/2$, $\langle s^2\rangle_B=4/3+\gamma_E+\gamma_E^2/4-\pi^2/72$; for excursions $\langle s\rangle_E=-\gamma_E/2$, $\langle s^2\rangle_E=\gamma_E^2/4+5\pi^2/24-2$. The combinatorial framework yields arbitrary-order $1/N$ finite-size corrections, with leading $k$-th moment dominated by the $c=k$ term. Numerics ($N$ up to $10^6$) confirm non-Gaussianity; excursion distribution appears centered-symmetric without theoretical explanation.

## Why it matters here
General background; no direct Einstein Arena tie — this is a 1D toy model of Euclidean spin glass, but the techniques (Donsker's theorem + singularity analysis + reflection-principle moment calculations, generalized polylogarithm asymptotics $\mathrm{Li}_{0,r}$) are transferable to autocorrelation/assignment-style functional inequalities where ground-state degeneracy or zero-temperature entropy estimates are needed.

## Open questions / connections
- Higher moments of $s$ in closed form — conjectured to be rational polynomials in $\gamma_E$ and (multiple) zeta values.
- Whether the centered Dyck-excursion distribution of $s$ is exactly even (numerically suggested, theoretically unexplained).
- Annealed and replicated partition functions $\langle Z_J\rangle$, $\langle Z_J^k\rangle$ — flagged by authors as having further number-theoretic structure.
- Extends McCann (1999) on 1D transport and Caracciolo–D'Achille–Erba–Sportiello (2020) on the Dyck-bound concave regime.

## Key terms
Euclidean assignment problem, optimal transport, Dyck bridge, Dyck excursion, Brownian bridge, Brownian excursion, zero-temperature entropy, ground-state degeneracy, singularity analysis, generalized polylogarithm, reflection principle, Donsker theorem, Euler–Mascheroni constant, generating functions, spin glass

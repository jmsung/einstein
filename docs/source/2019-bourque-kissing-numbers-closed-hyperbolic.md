---
type: source
kind: paper
title: Kissing numbers of closed hyperbolic manifolds
authors: Maxime Fortier Bourque, Bram Petri
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.11083
source_local: ../raw/2019-bourque-kissing-numbers-closed-hyperbolic.pdf
topic: general-knowledge
cites:
---

# Kissing numbers of closed hyperbolic manifolds

**Authors:** Maxime Fortier Bourque, Bram Petri  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.11083

## One-line
Upper bounds the kissing number (count of shortest closed geodesics) of any closed hyperbolic $n$-manifold in terms of its volume and systole, generalizing Parlier's surface result to all dimensions via the Selberg trace formula.

## Key claim
For every $n \geq 2$ there exists $A_n > 0$ such that $\mathrm{Kiss}(M) \leq A_n \cdot \mathrm{vol}(M) \cdot e^{(n-1)\mathrm{sys}(M)/2}/\mathrm{sys}(M)$ for every closed hyperbolic $n$-manifold $M$; in dimension 2 this recovers Parlier's bound with improved constant $U \approx 63.71$ (vs prior $200$). Corollary: $\mathrm{Kiss}(M) \leq A''_n \cdot \mathrm{vol}(M)^2/\log(1+\mathrm{vol}(M))$ — sub-quadratic in volume.

## Method
Selberg trace formula as the hyperbolic analogue of Poisson summation: choose an admissible Fourier pair $(g,h)$ where $g \leq 0$ outside $[-\mathrm{sys}(M), \mathrm{sys}(M)]$ and $h \geq 0$ on the spectral strip $\mathbb{R} \cup i[-(n-1)/2, (n-1)/2]$, then the geodesic side dominates the shortest-geodesic contribution while the spectral side is bounded by $\mathrm{vol}(M) \int h \Phi_n$. Explicit test pair built from iterated self-convolutions of indicator functions $\chi_{[-\varepsilon/(n+2), \varepsilon/(n+2)]}^{*(n+2)}$ (or $*(n+1)$ for odd $n$), ensuring $h$ is a non-negative even power of $\sin(a\xi)/\xi$ with the required decay. Inspired directly by the Cohn–Elkies sphere-packing magic-function strategy.

## Result
Three quantitative results: (1) the systole-volume kissing bound above; (2) for $\mathrm{sys}(M) \geq 2\delta$, two-sided uniform bounds $C_{n,\delta} e^{(n-1)L}/L - D_{n,\delta} \mathrm{vol}(M) e^{(n-1)L/2}/L \leq \#P_{[L-\delta,L+\delta]}(M) \leq B_{n,\delta} \mathrm{vol}(M) e^{(n-1)L}/L$ on primitive closed geodesics in a length window (uniform analogue of the prime geodesic theorem, with explicit volume dependence); (3) integrated version giving matching upper/lower bounds on $\#P_{[0,L]}(M)$. Lower bound functions as a Bertrand-postulate analogue: in any thick manifold, every window $[N, e^{2\delta}N]$ contains a primitive geodesic norm.

## Why it matters here
Direct methodological transplant of the Cohn–Elkies linear-programming bound from sphere packing into hyperbolic geometry — the same "find a function whose Fourier transform has a sign condition" recipe used in Viazovska's $E_8$ and Leech-lattice optimality proofs (which underlie Cohn–Elkies LP-bound techniques the agent uses on sphere-packing-family arena problems). Reinforces that LP/trace-formula duality is the *universal* tool for extremal counting bounds — relevant for kissing-number, sphere-packing, and autocorrelation problem families where one needs a sign-controlled Fourier pair.

## Open questions / connections
- Can the constants $A_n, B_{n,\delta}$ be made sharp? The paper notes they are "effectively computable" but does not pursue this beyond $n=2$.
- Maximal-kissing-number manifolds in higher dimensions remain unknown (analogous to lattice kissing numbers being unsolved except in dims 1–9, 24).
- Lower-bound construction analogous to Vlăduț's exponentially-large lattice kissing numbers — what hyperbolic-manifold families maximize $\mathrm{Kiss}/\mathrm{vol}$?
- Extends Parlier (2013), Fanoni–Parlier (2015) surface bounds; relates to Buser's small-eigenvalue counting and Margulis tube volume estimates.

## Key terms
Selberg trace formula, kissing number, hyperbolic manifold, systole, primitive closed geodesic, length spectrum, Laplace spectrum, Cohn-Elkies, magic function, Fourier pair, prime geodesic theorem, Margulis tube, Parlier, Viazovska, admissible transform pair

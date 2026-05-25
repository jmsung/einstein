---
type: source
kind: paper
title: First passage percolation on random graphs with infinite variance degrees
authors: E. Baroni, R. Hofstad, J. Komjáthy
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.01255
source_local: ../raw/2015-baroni-first-passage-percolation-random.pdf
topic: general-knowledge
cites:
---

# First passage percolation on random graphs with infinite variance degrees

**Authors:** E. Baroni, R. Hofstad, J. Komjáthy  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.01255

## One-line
Proves non-universality of first-passage percolation on the configuration model with power-law degrees of exponent $\tau \in (2,3)$: weight asymptotics depend qualitatively on the edge-weight distribution.

## Key claim
Two distinct universality classes emerge depending on whether the approximating age-dependent branching process $(h_B, F_Y)$ is explosive: (i) if explosive, $W_n(u,v) \to_d V^{(1)} + V^{(2)}$ (sum of two i.i.d. explosion times, bounded); (ii) if edge weights satisfy $Y = 1 + X$ with $\inf\mathrm{supp}(X) = 0$, then $W_n(u,v)/\log\log n \to_d 2/|\log(\tau-2)|$.

## Method
Couple the local neighborhood growth of shortest-weight graphs $\mathrm{SWG}^u_{n^\rho}, \mathrm{SWG}^v_{n^\rho}$ to a two-stage age-dependent branching process with size-biased offspring $B = D^\star - 1$ (infinite mean since $\tau \in (2,3)$). For the explosive class, use disjointness of the two SWGs plus a short bridging path. For the $\inf\mathrm{supp}(X)=0$ class, combine bond percolation on the configuration model (Janson) with a layered decomposition through high-degree "core" vertices $\Gamma_i^p = \{v : D_v^p > u_i\}$ with doubly-exponentially growing thresholds $u_{i+1} = (u_i / C\log n)^{1/(\tau-2)}$.

## Result
Theorem 1.6: For explosive $(h_B,F_Y)$, $W_n(u,v) \to_d V^{(1)} + V^{(2)}$ where $V^{(i)}$ are i.i.d. explosion times. Theorem 1.8: For $Y = 1 + X$ with $\inf\mathrm{supp}(X)=0$, both $W_n(u,v)/\log\log n$ and the hopcount $H_n(u,v)/\log\log n$ converge in distribution to $2/|\log(\tau-2)|$ — matching the graph-distance scaling. This is sharply contrasted with finite-variance degrees, where a single universality class with $W_n - \gamma\log n$ convergence holds.

## Why it matters here
General background; no direct arena tie. Relates to extremal/random-graph asymptotics and branching-process explosion criteria — peripheral to the current 23 Einstein Arena problems unless a future problem touches random-graph distances or sieve-type configuration models.

## Open questions / connections
- Behavior of hopcount $H_n(u,v)$ in the explosive class (not characterized here).
- Behavior of $W_n(u,v)$ for general edge weights outside the two classes treated.
- Whether competition / coexistence results (Deijfen–Hofstad, Komjáthy–Hofstad) extend to the explosive passage-time regime.
- Extends Bhamidi–Hofstad–Hooghiemstra finite-variance universality (2012) and the exponential-weight case (BHH 2010).

## Key terms
first-passage percolation, configuration model, power-law degrees, infinite variance, age-dependent branching process, explosion time, size-biased distribution, bond percolation, hopcount, universality class, ultra-small world, Janson percolation, Molloy-Reed, $\tau \in (2,3)$

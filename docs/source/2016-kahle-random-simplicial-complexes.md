---
type: source
kind: paper
title: Random simplicial complexes
authors: M. Kahle
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1607.07069
source_local: ../raw/2016-kahle-random-simplicial-complexes.pdf
topic: general-knowledge
cites:
---

# Random simplicial complexes

**Authors:** M. Kahle  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1607.07069

## One-line
Survey chapter mapping the topological and geometric structure of random simplicial complexes — thresholds, phase transitions, Betti numbers, and persistent homology — across Erdős–Rényi-style, clique, and geometric models.

## Key claim
The Linial–Meshulam–Wallach threshold $p = d\log n / n$ is the sharp cohomology-vanishing threshold for $H_{d-1}(Y_d(n,p), G)$ over any finite abelian $G$; the top-homology birth threshold is the Aronshtam–Linial constant $c^*_d/n$ with $c^*_d = -\log x / (1-x)^d$ where $x \in (0,1)$ solves $(d+1)(1-x) + (1+dx)\log x = 0$; and the simple-connectivity threshold for $Y(n,p)$ lies near $1/\sqrt{n}$ (conjecturally sharp at $C/\sqrt{n}$).

## Method
Co-isoperimetric inequalities on the simplex combined with cocycle counting (Linial–Meshulam, Meshulam–Wallach); Garland's spectral method via $\lambda_2$ of link Laplacians (Ballmann–Świątkowski form: $\lambda_2[\mathrm{lk}(\sigma)] > 1 - 1/d$ forces $H_{d-1} = 0$); local-to-global hyperbolicity (Gromov) for fundamental-group results; Poisson approximation for boundary-of-simplex subcomplexes near $c/n$.

## Result
Tabulated sharp/coarse thresholds for $G(n,p)$, $Y_d(n,p)$, clique complex $X(n,p)$, Čech $C(n,r)$, and Vietoris–Rips $VR(n,r)$: e.g. $H_k(X(n,p), \mathbb{R}) = 0$ sharply at $p = ((k/2+1)\log n / n)^{1/(k+1)}$; $\beta_k$ in subcritical $VR$ scales as $n^{2k+2} r^{d(2k+1)}$; Bobrowski–Weinberger sharp Čech homology-vanishing at $nr^d = \log n + k\log\log n$; maximal persistence in random geometric complexes is $\Theta((\log n / \log\log n)^{1/i})$ (Bobrowski–Kahle–Skraba).

## Why it matters here
General background; no direct arena tie. Useful peripheral context for any Arena problem framed via clique-complex / simplicial-complex topology, expander-style bounds, or coboundary expansion (e.g. high-dimensional analogues of extremal graph problems); informs the wiki's coverage of expander/spectral-gap techniques and Garland's method as potential cross-pollination tools.

## Open questions / connections
- Conjecture 23.3.11: is $d\log n/n$ also the sharp threshold for $H_{d-1}(Y_d, \mathbb{Z})$ (integer coefficients)?
- Conjecture 23.3.9 (bouquet-of-spheres): is $X(n,p)$ homotopy equivalent (not just rationally) to a wedge of $k$-spheres in the appropriate $p$-window — equivalently, is $H_k(X, \mathbb{Z})$ torsion free?
- Conjecture 23.3.21: sharp $\pi_1$-vanishing threshold at $C/\sqrt{n}$ for $Y(n,p)$; constant $C$ open (current bounds: $C = 1/2$ suffices, Korándi–Peled–Sudakov).
- Conjecture 23.4.4: law-of-large-numbers for maximal persistence; constant $C_{d,i}$ unknown.
- Embedding-density folklore conjecture (Kalai/Dey): a $d$-complex on $n$ vertices embeddable in $\mathbb{R}^{2d}$ has $O(n^d)$ faces — open for all $d \geq 2$; Theorem 23.3.18 shows it holds generically.

## Key terms
random simplicial complex, Linial–Meshulam, Meshulam–Wallach, Garland's method, clique complex, Vietoris–Rips, Čech complex, coboundary expander, spectral gap, Cheeger number, Betti number, persistent homology, Aronshtam–Linial constant, Erdős–Rényi threshold, Kazhdan property (T), hyperbolic group, cohomological dimension, random geometric complex, Bobrowski–Weinberger, bouquet of spheres

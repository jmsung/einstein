---
type: source
kind: paper
title: Melonic CFTs
authors: D. Benedetti
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.08616
source_local: ../raw/2020-benedetti-melonic-cfts.pdf
topic: general-knowledge
cites:
---

# Melonic CFTs

**Authors:** D. Benedetti  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.08616

## One-line
Review of tensor field theories in $d \geq 2$ Euclidean dimensions whose large-$N$ limit is dominated by melonic Feynman diagrams, yielding solvable non-trivial CFT fixed points.

## Key claim
In rank-$r$ tensor field theories with $O(N)^r$ or $U(N)^r$ symmetry and 't Hooft scalings $\rho_b = (F(I_b)-3)/2$, the $1/N$ expansion exists with leading vacuum graphs of degree $\omega(G)=0$ scaling as $N^{3-\omega}$; this melonic dominance allows the full two-point Schwinger–Dyson equation to be solved in closed form and the four-point kernel spectrum to be computed, producing genuine higher-dimensional CFTs (Wilson–Fisher-style in short-range models, lines of fixed points parameterized by an exactly marginal MST coupling in long-range models with $\zeta = d/4$).

## Method
Two-particle-irreducible (2PI) effective action $\Gamma[G] = \tfrac{1}{2}\mathrm{Tr}\, C^{-1}G + \tfrac{1}{2}\mathrm{Tr}\ln G^{-1} + \Gamma_2[G]$, truncated to leading order in $1/N$ via melon-tadpole bubbles (tetrahedron + pillow + double-trace + mass). Schwinger–Dyson then reduces to $G(p)^{-1} = p^{2\zeta} - \lambda_t^2 \!\int\! G^3$ which for $\zeta = d/4$ is solved by $G(p)^{-1}=Z p^{2\zeta}$ with $Z^4 - Z^3 = \lambda_t^2 (4\pi)^{-d}\Gamma(1-d/4)/(d/4\,\Gamma(3d/4))$. Bilinear operator dimensions come from diagonalizing the ladder four-point kernel $K$ on conformal three-point structures.

## Result
For long-range bosonic $O(N)^3$ with $0<\zeta<1$ and quartic action, the tetrahedron coupling $g$ is exactly marginal at large $N$, generating a line of IR-attractive fixed points in the $(\lambda_p,\lambda_d)$ plane parametrized by $g \in i\mathbb{R}$; in finite windows of $g$ all computed scaling dimensions are real and respect unitarity bounds. Tensorial Gross–Neveu in $d=2-\varepsilon$ with chiral-symmetric tetrahedron has $\beta_\lambda = -\varepsilon\lambda + (3/\pi^2)\lambda^3$, giving an IR fixed point at $\lambda_* \sim \sqrt{\varepsilon}$ — sign reversed vs vector GN because here the two-loop term is leading-$N$. The $U(N)^3$ complex-fermion model in $d=3$ exhibits a new spontaneous-$U(N)$-breaking phase forbidden by Coleman–Mermin–Wagner in $d=2$.

## Why it matters here
General background; no direct arena tie. Melonic CFT machinery (2PI effective action, ladder-kernel diagonalization, exactly-marginal-coupling lines) is the QFT analog of the LP-bound / four-point-bootstrap toolkit but does not bear on the 23 Einstein Arena packing / autocorrelation / extremal-graph problems.

## Open questions / connections
- Do $1/N$ corrections lift the exact marginality of the tetrahedron coupling and select a discrete fixed point inside the unitary window?
- Fermionic long-range tensor models — does the $d=2-\varepsilon$ IR fixed point continue smoothly to $d=1$ and recover conformal SYK?
- Connection to fishnet CFTs (Kazakov–Olivucci): both have ladder-renormalized double-trace lines driven by a complex marginal coupling — is the apparent non-unitarity structurally the same?

## Key terms
melonic limit, tensor field theory, large-N expansion, 2PI effective action, Schwinger-Dyson equation, four-point kernel, tetrahedron invariant, SYK model, Gross-Neveu, long-range Ising, conformal field theory, Wilson-Fisher fixed point

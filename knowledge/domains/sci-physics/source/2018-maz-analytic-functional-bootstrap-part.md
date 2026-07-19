---
type: source
kind: paper
title: The analytic functional bootstrap. Part II. Natural bases for the crossing equation
authors: D. Mazáč, M. Paulos
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.10646
source_local: ../raw/2018-maz-analytic-functional-bootstrap-part.pdf
topic: general-knowledge
cites:
---

# The analytic functional bootstrap. Part II. Natural bases for the crossing equation

**Authors:** D. Mazáč, M. Paulos  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.10646

## One-line
Constructs two complete bases of extremal linear functionals (labeled by generalized free boson/fermion double-traces) that act on the 1D ($z=\bar z$) conformal crossing equation and yield non-perturbative OPE sum rules incorporating Regge boundedness.

## Key claim
For each $n\in\mathbb{N}_{\ge 0}$ there exist functionals $\alpha_n,\beta_n$ (contour integrals in $z$) satisfying $\alpha_n(\Delta_m)=\delta_{nm}$, $\alpha_n'(\Delta_m)=0$, $\beta_n(\Delta_m)=0$, $\beta_n'(\Delta_m)=\delta_{nm}$ on double-trace dimensions $\Delta_n=2\Delta_\phi+2n$ (bosonic) or $+1$ (fermionic); applying them to crossing gives sum rules equivalent to the full crossing equation and proving large-$\Delta$ OPE bounds, e.g. every $\phi\times\phi$ OPE must contain at least one primary in $[2\Delta_\phi+2n,\,2\Delta_\phi+2n+4]$ for all sufficiently large $n$.

## Method
Functionals are realized as holomorphic contour integrals against kernels built from Legendre polynomials $P_{h-1}$ and $\partial_h$-derivatives, evaluated on $\mathcal{F}_\Delta(z)=z^{-2\Delta_\phi}G_\Delta(z)-(1-z)^{-2\Delta_\phi}G_\Delta(1-z)$ with $G_\Delta(z)=z^\Delta {}_2F_1(\Delta,\Delta;2\Delta;z)$. The dual-basis conditions are imposed using the generalized-free-field (mean-field) spectrum as the saturating extremal solution. Regge boundedness as $z\to i\infty$ is what allows the functionals to swap with the infinite OPE sum.

## Result
Established a rigorous derivation of the SL(2) Polyakov–Mellin bootstrap (fixing the contact-term ambiguity by identifying $\alpha_n(\Delta),\beta_n(\Delta)$ with OPE coefficients of crossing-symmetrized AdS$_2$ Witten exchange in the conformal-block basis). Proved two-sided large-$\Delta$ bounds: $\limsup_{n\to\infty}\sum_{|\Delta_O-\Delta_n|\le 1}\frac{4\sin^2\frac{\pi}{2}(\Delta_O-\Delta_n)}{\pi^2(\Delta_O-\Delta_n)^2}\frac{a_O}{a^{\text{free}}_{\Delta_O}}\le 1$ and a matching $\liminf\ge 1$ lower bound over $[\Delta_{n-1},\Delta_{n+1}]$, both saturated by the generalized free field. Used the basis to bootstrap one- and two-loop AdS$_2$ $\phi^4$ Witten diagrams (explicit closed forms at $\Delta_\phi=1$ involving $\zeta(3),\zeta(5),\pi^k$).

## Why it matters here
Direct methodological cousin of the Cohn–Elkies / Viazovska sphere-packing magic functions: the $\sin^2\frac{\pi}{2}(\Delta-\Delta_n)$ double-zero prefactor is the same "interpolation basis with prescribed zeros" mechanism that Viazovska uses for $E_8$/Leech (the authors explicitly cite Viazovska and note an upcoming "Modular Bootstrap and Sphere-Packing" connection). Relevant to LP-duality / extremal-functional problems (sphere packing P-class, autocorrelation/uncertainty problems, modular-form-based LP bounds).

## Open questions / connections
- Generalization to $D>1$ crossing (full conformal group, not just SL(2)) and to multi-correlator / non-identical-operator systems.
- Direct bridge to modular bootstrap and the Cohn–Elkies / Viazovska sphere-packing program (announced sequel: Mazáč–Rastelli, "Modular Bootstrap and Sphere-Packing").
- Whether an analogous extremal-functional basis exists for every CFT that saturates some bootstrap bound, beyond perturbations of mean field theory.
- Connection to Caron-Huot's Lorentzian inversion formula (the $\sin^2$ prefactor mirrors the double discontinuity); promised in companion arXiv:1812.02254.

## Key terms
conformal bootstrap, extremal functional, Polyakov–Mellin bootstrap, generalized free field, double-trace operator, Regge boundedness, crossing equation, SL(2) conformal blocks, Witten diagrams AdS2, mean field theory, Viazovska magic function, sphere packing LP bound, Mazáč, Paulos, dual basis, contour-integral functionals

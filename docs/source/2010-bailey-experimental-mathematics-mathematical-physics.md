---
type: source
kind: paper
title: Experimental Mathematics and Mathematical Physics
authors: David H. Bailey, Jonathan M. Borwein, David Broadhurst, Wadim Zudilin
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1005.0414v1
source_local: ../raw/2010-bailey-experimental-mathematics-mathematical-physics.pdf
topic: general-knowledge
cites: 
---

# Experimental Mathematics and Mathematical Physics

**Authors:** David H. Bailey, Jonathan M. Borwein, David Broadhurst, Wadim Zudilin  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1005.0414v1

## One-line
A survey of the "compute-to-high-precision, then PSLQ-recognize" methodology applied to integrals and sums arising in Ising theory, quantum field theory, lattice spin chains, box geometry, hyperbolic 3-manifolds, and multiple zeta values.

## Key claim
High-precision quadrature (tanh-sinh, Ooura-Mori, Gaussian) coupled with PSLQ integer-relation detection can identify closed forms for multi-dimensional physics integrals that resist symbolic attack — yielding e.g. $\lim_{n\to\infty} C_n = 2e^{-2\gamma}$ for the Ising $C_n$ family, a conjectural closed form for $E_5$ verified to 240 digits, and an empirical depth-7→5 "pushdown" $\zeta(6,2,3,3,5,1,1) \stackrel{?}{=} -\tfrac{326}{81}\zeta(3,\bar 6,3,\bar 6,3) + \text{(depth-5 products)}$ at MZV weight 21.

## Method
Two-stage pipeline: (1) compute the target constant to hundreds or thousands of digits via tanh-sinh quadrature (exponential convergence under the change of variable $x=\tanh(\tfrac{\pi}{2}\sinh t)$, handles endpoint singularities), Ooura-Mori for oscillatory integrands, or Gaussian quadrature; (2) feed the value plus candidate basis terms (zeta values, $\log 2$, $\pi^k$, $\mathrm{Cl}_2$, $\mathrm{Ti}_2$, $L_{-D}(2)$) to PSLQ to discover an integer linear relation. Parallelized over up to 1024 cores; ARPREC for arbitrary precision; LLL via Pari-GP as a fallback for harder MZV cases.

## Result
Closed forms for $C_3, C_4, D_2, D_3, D_4, E_2, E_3, E_4$ (proved) and conjecturally $E_5$; linear recurrences across rows of $C_{n,k}$ (e.g. $0 = C_{3,0} - 84 C_{3,2} + 216 C_{3,4}$); hypergeometric forms for Bessel-moment constants $c_{3,0}, c_{3,2}, c_{4,0}, c_{4,2}$; Heisenberg spin-chain emptiness probabilities $P(n)$ for $n\le 5$ in terms of $\zeta$ products; explicit box-integral evaluations $B_n(s), \Delta_n(s)$ for $n\le 5$ involving Catalan's $G$, Clausen $\mathrm{Cl}_2$, Lewin $\mathrm{Ti}_2$; a proof of $3\mathrm{Cl}_2(\alpha) - 3\mathrm{Cl}_2(2\alpha) + \mathrm{Cl}_2(3\alpha) = \tfrac{7\sqrt 7}{4} L_{-7}(2)$ at $\alpha=2\arctan\sqrt 7$; five open conjectural Clausen identities for $D=-8,-11,-15,-20,-24$ relating $\mathrm{Cl}_2$ sums to Dedekind zeta values $\zeta_K(2)$.

## Why it matters here
Direct relevance to autocorrelation, uncertainty, and functional-inequality problems where the optimal constant is a high-precision number begging closed-form recognition: PSLQ + tanh-sinh is the canonical "is this number $\zeta(3)$, $G$, $L_{-D}(2)$, or something nameable?" pipeline, and tanh-sinh's robustness to endpoint singularities matches arena evaluators that blow up at boundaries. Box-integral closed forms (random distance, electrostatic potential in $[0,1]^n$) are reference values for any discrete-geometry / sphere-packing problem testing Monte-Carlo evaluators.

## Open questions / connections
- Closed form for $D_5$ (500-digit value computed; no relation found in standard basis).
- The five Clausen-function/Dedekind-zeta identities for $D \in \{-8,-11,-15,-20,-24\}$ remain conjectural — testbed for new dilogarithm machinery beyond Zagier's 1986 theorems.
- The depth-7 → depth-5 MZV pushdown at weight 21 is empirically validated but algebraically out of reach; connects to Broadhurst–Kreimer dimension conjectures and Feynman-diagram cohomology.
- Sparse-grid quadrature (Smolyak) is flagged as the next frontier for $\geq 4$-D high-precision integrals — currently the wall is $\sim 60$ digits at $n=5$, $\sim 6$ digits at $n=6$.
- Challenge integral $\int_{[0,1/2]^3} f^{-2} = 1.1871875\ldots$ left open to 32 digits.

## Key terms
PSLQ, tanh-sinh quadrature, Ooura-Mori oscillatory quadrature, Ising integrals, Bessel moments, box integrals, multiple zeta values, Euler sums, Clausen function, Dedekind zeta, hyperbolic 3-manifold volumes, Broadhurst-Kreimer conjecture, integer relation detection, high-precision arithmetic, ARPREC, Catalan constant, polylogarithm, Heisenberg spin chain, Zagier, experimental mathematics

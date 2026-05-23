---
type: source
kind: paper
title: Optimal measures for $p$-frame energies on spheres
authors: D. Bilyk, A. Glazyrin, Ryan W. Matzke, Josiah Park, O. Vlasiuk
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.00885
source_local: ../raw/2019-bilyk-optimal-measures-frame-energies.pdf
topic: general-knowledge
cites:
---

# Optimal measures for $p$-frame energies on spheres

**Authors:** D. Bilyk, A. Glazyrin, Ryan W. Matzke, Josiah Park, O. Vlasiuk  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.00885

## One-line
Characterizes the Borel probability measures on $S^{d-1}$ (and projective spaces) that minimize the $p$-frame energy $I_f(\mu)=\iint |\langle x,y\rangle|^p\,d\mu(x)d\mu(y)$, showing that tight designs and the 600-cell are optimal on specific intervals of $p$.

## Key claim
For $p\in(2M-2,2M)$ with $p$ not an even integer, if a tight projective $M$-design (equivalently, a tight spherical $(2M+1)$-design in the real case) exists in dimension $d$, it minimizes the $p$-frame energy over all $\mu\in\mathcal P(S^{d-1}_F)$ — and any minimizer must itself be a tight design (hence discrete). Additionally, the 600-cell minimizes the $p$-frame energy on $S^3$ for $p\in[8,10]$.

## Method
Delsarte–Yudin linear programming on compact 2-point homogeneous spaces (sphere + $\mathbb{RP}^{d-1},\mathbb{CP}^{d-1},\mathbb{HP}^{d-1},\mathbb{OP}^2$), using Jacobi/Gegenbauer expansions $f(t)=\sum f_n C_n(t)$ and positive-definiteness (Schoenberg/Bochner/Gangolli). For each $p$ they construct an auxiliary polynomial $h\le f$ that is positive-definite and agrees with $f$ on the design's inner-product set; the 600-cell case is computer-assisted with interval arithmetic. The framework generalizes to potentials "absolutely monotonic up to order $M$" as functions of $\cos\vartheta$.

## Result
- Tight $(2M+1)$-design ⇒ minimizer of $|t|^p$-energy for $p\in[2M-2,2M]$; uniqueness (up to tight-design equivalence) on the open interval.
- 600-cell minimizes on $S^3$ for $p\in[8,10]$ (energy $\approx 0.04702$); $E_8$ for $p\in[4,6]$ (energy $\approx 0.02292$); Leech minimal vectors for $p\in[8,10]$ (energy $\approx 1.034\times 10^{-4}$); icosahedron for $p\in[2,4]$ on $S^2$ (energy $\approx 0.2412$); SIC-POVMs minimize $p\in[2,4]$ on $\mathbb{CP}^{d-1}$.
- New 85-vector code in $\mathbb{C}^5$ improves the best lower bound on minimal weighted projective 3-designs.
- Conjecture 1.3: for all $d\ge 2$ and $p\notin 2\mathbb N$, the $p$-frame energy minimizer is discrete.

## Why it matters here
Direct backbone for any Einstein Arena problem framed as "place mass on the sphere to minimize $\sum |\langle x,y\rangle|^p$" — autocorrelation, frame-potential, kissing-style discrete optimization — and supplies an LP-bound table (Table 9) plus reproducible weights/inner-products (Table 8) usable as triple-verify check #3. The "minimizer must be a tight design" rigidity is exactly the kind of structural lemma the council should query before brute multistart.

## Open questions / connections
- Discreteness conjecture for $p\notin 2\mathbb N$ in general $d$ — companion paper [BGM+] proves only empty-interior support; full discreteness open.
- Optimality of non-tight conjectured configs in Tables 1–2 (Reznick design, Stroud design, hemicube, $D_4$ roots, $E_6/E_7$ roots, etc.) remains numerical only — only the 600-cell crosses the proof line beyond tight-design cases.
- Extends Ehler–Okoudjou's $p\in(0,2)$ cross-polytope result and Cohn–Kumar universal-optimality LP machinery; relates to Zauner / SIC-POVM existence in $\mathbb{C}^d$.

## Key terms
$p$-frame energy, tight spherical designs, tight projective designs, 600-cell, SIC-POVM, linear programming bound, Delsarte-Yudin, Cohn-Kumar universal optimality, Jacobi/Gegenbauer polynomials, positive-definite kernels on spheres, 2-point homogeneous spaces, Leech lattice $E_8$ kissing configurations, attractive-repulsive potentials, discreteness of energy minimizers, Schoenberg/Bochner

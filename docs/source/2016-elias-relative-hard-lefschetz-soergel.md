---
type: source
kind: paper
title: Relative hard Lefschetz for Soergel bimodules
authors: Ben Elias, G. Williamson
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1607.03271
source_local: ../raw/2016-elias-relative-hard-lefschetz-soergel.pdf
topic: general-knowledge
cites:
---

# Relative hard Lefschetz for Soergel bimodules

**Authors:** Ben Elias, G. Williamson  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1607.03271

## One-line
Proves a relative hard Lefschetz theorem for Soergel bimodules, yielding unimodality of Kazhdan–Lusztig structure constants for all Coxeter groups and rigidity/pivotality of Lusztig's $J$-ring categorifications.

## Key claim
For $x,y\in W$ and dominant regular $\rho\in\mathfrak{h}^*$, the operator $\eta:B_x\otimes_R B_y\to B_x\otimes_R B_y[2]$, $b\otimes b'\mapsto b\otimes\rho b'$, induces isomorphisms $\eta^i:\mathcal{H}^{-i}(B_xB_y)\xrightarrow{\sim}\mathcal{H}^i(B_xB_y)$ on perverse cohomology for all $i\geq 0$. Consequently every Kazhdan–Lusztig structure constant $\mu_{x,y}^z$ is a non-negative $\mathbb{Z}$-linear combination of quantum numbers $[m]$ (unimodality).

## Method
Algebraic/Hodge-theoretic induction in the category of Soergel bimodules: prove the stronger Hodge–Riemann bilinear relations (HR) on multiplicity spaces of $\mathcal{H}^i(B_xB_y)$, then deduce hard Lefschetz (HL). Inductive engine combines (i) "HR in lower dimension $\Rightarrow$ HL" via Rouquier-complex / weak-Lefschetz arguments using positively polarized bimodules and adjoint maps $d_x^*\circ d_x=B_x\rho-(x\rho)B_x$, and (ii) signature propagation along continuous one-parameter families of Lefschetz operators $L_{a,b}$ (de Cataldo–Migliorini's "conservation of signs").

## Result
Theorem 1.2 (relative HL) and the stronger Theorem 3.3 (relative HR on multiplicity spaces) hold for any Coxeter system. Corollary 1.4: $\mu_{x,y}^z=\sum_{m\geq 1}a_m[m]$ with $a_m\geq 0$, i.e. each structure constant is the character of a finite-dimensional $\mathfrak{sl}_2(\mathbb{C})$-representation. Theorem 5.2: Lusztig's monoidal category $\mathcal{J}$ attached to any two-sided cell $\mathbf{c}\subset W$ is rigid and pivotal (the pivotal structure depends on the choice of $\rho$), so its Drinfeld center is a modular tensor category.

## Why it matters here
General background; no direct arena tie. Hodge-theoretic / hard-Lefschetz machinery is conceptually adjacent to LP-bound and SDP positivity arguments (sphere packing, kissing), but this paper's content is representation-theoretic and does not bear on any current Einstein Arena problem.

## Open questions / connections
- Conjecture 3.4: extend relative HR to iterated tensor products $B_{x_1}\cdots B_{x_m}$ of arbitrary length (still open even for Bott–Samelson bimodules).
- Whether the $\rho$-dependence of the pivotal structure on $\mathcal{J}$ yields a unitary structure via HR — flagged for future work.
- Cells in non-crystallographic Coxeter groups conjecturally give new modular tensor categories (Drinfeld centers of $\mathcal{J}$); the $H_4$ $a=6$ cell is a concrete test case (Ostrik).
- Extends Elias–Williamson's algebraic proof of Soergel's conjecture / KL positivity [EW14]; replaces geometric BBD relative HL in non-crystallographic settings where no variety is available.

## Key terms
Soergel bimodules, Kazhdan–Lusztig polynomials, relative hard Lefschetz, Hodge–Riemann bilinear relations, perverse cohomology, Hecke algebra, Coxeter group, structure constants unimodality, Lusztig $J$-ring, rigid pivotal monoidal category, Rouquier complex, Bott–Samelson, de Cataldo–Migliorini conservation of signs, Elias, Williamson

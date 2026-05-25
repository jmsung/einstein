---
type: source
kind: paper
title: The Hodge theory of Soergel bimodules
authors: Ben Elias, G. Williamson
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1212.0791
source_local: ../raw/2012-elias-hodge-theory-soergel-bimodules.pdf
topic: general-knowledge
cites:
---

# The Hodge theory of Soergel bimodules

**Authors:** Ben Elias, G. Williamson  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1212.0791

## One-line
Proves Soergel's conjecture on characters of indecomposable Soergel bimodules for arbitrary Coxeter systems, yielding positivity of Kazhdan–Lusztig polynomials and an algebraic proof of the Kazhdan–Lusztig conjecture.

## Key claim
For any Coxeter system $(W,S)$ and reflection-faithful representation over $\mathbb{R}$, the indecomposable Soergel bimodule $B_x$ has character $\mathrm{ch}(B_x) = \underline{H}_x$ (the Kazhdan–Lusztig basis), and $B_x$ satisfies hard Lefschetz and the Hodge–Riemann bilinear relations with respect to left multiplication by any $\rho \in h^*$ strictly positive on simple coroots — even when no underlying flag variety exists (e.g., $H_3$, $H_4$, non-crystallographic dihedral groups).

## Method
Adapts de Cataldo–Migliorini's Hodge-theoretic proof of the decomposition theorem to a purely algebraic setting. Inductive scheme on Bruhat order linking four statements — Soergel's conjecture $S(x)$, hard Lefschetz $hL(x)$, Hodge–Riemann $HR(x)$, and a "global" form variant $\overline{HR}(x)$ — and embeds local intersection forms $\mathrm{Hom}(B_y, B_xB_s)$ isometrically into primitive subspaces of $(B_xB_s)_{-\ell(y)}$. A one-parameter deformation $L_\zeta = \rho \otimes \mathrm{id} + \zeta\,\mathrm{id} \otimes \rho$ replaces hyperplane sections / weak Lefschetz, with Rouquier complexes ("linear" / "Hodge–Riemann") providing the inductive engine; signature-invariance in families converts $hL$ for all $\zeta \ge 0$ plus $HR$ at one $\zeta$ into $HR$ at $\zeta = 0$.

## Result
Soergel's conjecture (Theorem 1.1) holds for all Coxeter systems. Consequences: (i) Kazhdan–Lusztig polynomials $h_{y,x} \in \mathbb{Z}_{\ge 0}[v]$ (Corollary 1.2(1)); (ii) structure constants $\mu^z_{x,y} \in \mathbb{Z}_{\ge 0}[v^{\pm 1}]$ (Corollary 1.2(2)); (iii) hard Lefschetz and Hodge–Riemann for $\overline{B}_x$ (Theorems 1.3–1.4); (iv) algebraic proof of the Kazhdan–Lusztig character formula via Soergel/AJS/Fiebig machinery, extending to affine Lie algebras (non-critical level), quantum groups at roots of unity, and Lusztig's modular conjecture for $p \gg 0$.

## Why it matters here
General background; no direct arena tie. Distant relevance to extremal-combinatorics positivity arguments and to the broader pattern "objects behave like IH of projective varieties even when no variety exists" — analogous to how Cohn–Elkies / SDP bounds yield extremal structure without a geometric model. Nothing in current wiki on Hodge-theoretic methods.

## Open questions / connections
- Does Dyer's conjectural framework [D1, D2] unifying this theory with intersection cohomology of non-rational polytopes [BL, Ka, BBFK] admit a common proof technique?
- Can the Rouquier-complex substitute for weak Lefschetz transfer to other settings lacking hyperplane sections (e.g., combinatorial / matroid Hodge theory à la Adiprasito–Huh–Katz)?
- The proof requires characteristic 0; positivity / Lusztig conjectures in characteristic $p$ small remain a separate question.

## Key terms
Soergel bimodules, Kazhdan–Lusztig polynomials, Coxeter system, Hecke algebra, hard Lefschetz theorem, Hodge–Riemann bilinear relations, intersection cohomology, decomposition theorem, Rouquier complex, Bott–Samelson, de Cataldo–Migliorini, signature deformation argument

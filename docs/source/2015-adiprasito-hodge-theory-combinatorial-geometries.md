---
type: source
kind: paper
title: Hodge theory for combinatorial geometries
authors: Karim A. Adiprasito, June Huh, Eric Katz
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.02888
source_local: ../raw/2015-adiprasito-hodge-theory-combinatorial-geometries.pdf
topic: general-knowledge
cites:
---

# Hodge theory for combinatorial geometries

**Authors:** Karim A. Adiprasito, June Huh, Eric Katz  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.02888

## One-line
Proves the long-standing log-concavity conjectures for matroids by building a Hodge-theoretic structure (hard Lefschetz + Hodge-Riemann relations) on the Chow ring of an arbitrary matroid, not just realizable ones.

## Key claim
For any loopless matroid $M$ of rank $r+1$, the Chow ring $A^*(M)_{\mathbb{R}}$ (Feichtner-Yuzvinsky) satisfies Poincaré duality, the hard Lefschetz theorem, and the Hodge-Riemann relations with respect to any strictly convex piecewise linear function $\ell$ on the Bergman fan $\Sigma_M$. Consequence: the coefficients $w_k(M)$ of the characteristic polynomial $\chi_M(\lambda)$ are log-concave ($w_{k-1}w_{k+1} \le w_k^2$), as are the independent-set counts $f_k(M)$ — settling the Rota–Heron–Welsh, Mason–Welsh, and Read–Hoggar conjectures.

## Method
Builds a "combinatorial Chow ring" $A^*(M) = S_M/(I_M + J_M)$ on the Bergman fan of $M$, then runs an inductive proof modeled on McMullen's proof of the $g$-theorem for simple polytopes: induct on rank and on the size of an order filter $\mathcal{P}$, using "matroidal flips" (stellar subdivisions of $\Sigma_{M,\mathcal{P}}$) to transport the Hodge-Riemann property between adjacent fans. Local Hodge-Riemann at every ray (via the product structure of stars of rays in a combinatorial geometry — Prop 3.5) plus a continuous deformation $Q^q_t$ of the bilinear form lifts local HR to global HL, then global HR. The log-concavity is then extracted as a Khovanskii-Teissier-type inequality $\deg(\ell_1^2 \ell_2^{r-2}) \deg(\ell_2^2 \ell_2^{r-2}) \le \deg(\ell_1 \ell_2 \ell_2^{r-2})^2$ applied to nef classes $\alpha_M, \beta_M$, identified with reduced-characteristic-polynomial coefficients via $\mu_k(M) = \deg(\alpha_M^{r-k} \beta_M^k)$.

## Result
- Theorem 1.4 / 8.8: hard Lefschetz and Hodge-Riemann for $A^*(M)_{\mathbb{R}}$ at every strictly submodular $\ell$, for all matroids.
- Theorem 9.9: log-concavity of (a) reduced characteristic polynomial coefficients $\mu_k(M)$, (b) full characteristic polynomial coefficients $w_k(M)$, (c) independent-set numbers $f_k(M)$, (d) chromatic polynomial coefficients of any graph $G$.
- Theorem 8.9: the stronger mixed hard Lefschetz and mixed Hodge-Riemann relations also hold.

## Why it matters here
General background; no direct arena tie. Closest contact is methodological: log-concavity-via-Hodge-Riemann is the same template used for Alexandrov-Fenchel mixed-volume inequalities on convex bodies, which is the family of tools relevant to Cohn-Elkies / LP-bound style problems and sphere/kissing extremal problems in the wiki. Informs `concepts/` entries on log-concave sequences, Lefschetz/Hodge-Riemann transfer arguments, and the matroid → tropical-fan → Chow-ring pipeline.

## Open questions / connections
- Relationship to Hrushovski-Zilber intersection theory for finitary combinatorial geometries (authors flag this as unclear).
- Tropical Hodge conjecture: Babaee-Huh counterexample shows Poincaré + HL can hold without HR — what extra structure on a tropical variety forces HR?
- Extending the McMullen-style "flip" induction beyond Bergman fans (e.g. to general balanced tropical varieties, IKMZ tropical homology).
- Mixed HL/HR (Theorem 8.9) suggests Alexandrov-Fenchel-style inequalities in a purely combinatorial setting — what other matroid invariants does this constrain?

## Key terms
matroid, Chow ring, Bergman fan, hard Lefschetz theorem, Hodge-Riemann relations, log-concavity, characteristic polynomial, chromatic polynomial, Mason conjecture, Rota-Heron-Welsh conjecture, Feichtner-Yuzvinsky, McMullen, tropical geometry, mixed volumes, Khovanskii-Teissier, simple polytope, order filter, matroidal flip, combinatorial geometry, Möbius function

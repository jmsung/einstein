---
type: source
kind: paper
title: Three-point bounds for energy minimization
authors: Henry Cohn, Jeechul Woo
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1103.0485
source_local: ../raw/2011-cohn-three-point-bounds-energy-minimization.pdf
topic: general-knowledge
cites:
---

# Three-point bounds for energy minimization

**Authors:** Henry Cohn, Jeechul Woo  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1103.0485

## One-line
Extends semidefinite programming (three-point) bounds from coding theory to potential energy minimization and uses them to prove universal optimality of the 7-line rhombic dodecahedron code in $\mathbb{RP}^2$.

## Key claim
The seven lines through opposite vertices of a rhombic dodecahedron (equivalently, cube ∪ dual octahedron diagonals) form a universally optimal code in $\mathbb{RP}^2$ — they minimize $E_f(C) = \tfrac{1}{2}\sum_{x\neq y} f(d(x,y)^2)$ for every completely monotonic $f$ of squared chordal distance, uniquely so unless $f$ is linear, and they are the unique optimal 7-point projective code. This is also the **last** universal optimum in $\mathbb{RP}^2$ (Theorem 2 completeness, via Leech's classification of balanced configurations on $S^2$).

## Method
A new derivation of Bachoc–Vallentin three-point SDP bounds via matrix-valued positive-definite kernels: starting from a Bochner-type characterization (Theorems 3–4), they exhibit explicit $H$-invariant matrix kernels on $S^{n-1}$ built from Gegenbauer polynomials $P_k^{n-1}$ evaluated at $(t-u_1 u_2)/\sqrt{(1-u_1^2)(1-u_2^2)}$ (Theorem 5) — no special-function machinery beyond what two-point bounds already require. Sharpness for the rhombic dodecahedron is verified by an exact sum-of-squares certificate (PARI/GP computer-algebra check via characteristic-polynomial positivity, all in rational arithmetic).

## Result
$(3,14,1/\sqrt{3})$ antipodal code = 7 lines in $\mathbb{RP}^2$ is universally optimal; uniqueness holds for all non-linear completely monotonic $f$. Complete $\mathbb{RP}^2$ list: $\le 3$ orthogonal lines, cube (4), icosahedron (6), rhombic dodecahedron (7). First example where LP/SDP bounds are sharp for a code that is **not distance-regular** — a regularity barrier broken.

## Why it matters here
Direct relevance to **P11 (kissing/projective packing on $S^2$ / $\mathbb{RP}^2$)** and any line-packing / Grassmannian problem; extends the Cohn–Kumar universal-optimality toolkit and is the precedent that three-point SDP can settle cases two-point LP cannot. Complements existing wiki entries on Cohn–Elkies LP, equioscillation, and SDP flag algebra by giving an energy-not-just-distance template plus a concrete sum-of-squares certification workflow.

## Open questions / connections
- Conjecture 12: analogous 16-line configuration in $\mathbb{R}^5$ universally optimal? Three-point bounds insufficient — needs four-point (cf. Gijswijt–Mittelmann–Schrijver 2010).
- Conjectures 13–15: three-point bounds may stay sharp *through phase transitions* (Petersen ↔ orthogonal pentagons in $S^3$; one-parameter antiprism family in $S^2$; 24-cell in $S^3$ vs its competitors). Would be unprecedented.
- No known generalization of Levenshtein's design-based sharpness criterion to three-point bounds — conceptual organizing principle missing.

## Key terms
three-point bounds, semidefinite programming, Bachoc-Vallentin, universal optimality, rhombic dodecahedron, projective code, Gegenbauer polynomial, Cohn-Kumar, completely monotonic potential, orthoplex bound, positive-definite kernel, matrix-valued kernel, antipodal code, RP2, Schoenberg

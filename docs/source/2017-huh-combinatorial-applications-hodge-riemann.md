---
type: source
kind: paper
title: COMBINATORIAL APPLICATIONS OF THE HODGE–RIEMANN RELATIONS
authors: June Huh
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.11176
source_local: ../raw/2017-huh-combinatorial-applications-hodge-riemann.pdf
topic: general-knowledge
cites:
---

# COMBINATORIAL APPLICATIONS OF THE HODGE–RIEMANN RELATIONS

**Authors:** June Huh  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.11176

## One-line
Survey explaining how Poincaré duality, hard Lefschetz, and Hodge–Riemann (PD/HL/HR) on a graded algebra $A(X)$ furnish a unified mechanism for proving log-concavity of combinatorial sequences.

## Key claim
For a graded $A(X)=\bigoplus_q A^q(X)$ of "dimension" $d$ with a Kähler-type cone $K(X)$, the HR property in degrees $q\le 1$ forces any matrix $M_{ij}=P(\eta_i,(\prod_{k=1}^{d-2}L_k)\eta_j)$ on $A^1(X)$ to have exactly one positive eigenvalue, which yields Alexandrov–Fenchel-type inequalities $\deg(L\xi_1\xi_2)^2\ge \deg(L\xi_1^2)\deg(L\xi_2^2)$ and hence log-concavity of the associated combinatorial sequences.

## Method
Constructs (or cites the construction of) a graded $\mathbb{R}$-algebra $A(X)$ from the combinatorial object $X$ (polytope, matroid, vector configuration), defines a Kähler-type cone $K(X)\subset A^1(X)$, and verifies the PD/HL/HR triple — for matroids via the Chow ring $A(M)=\mathbb{R}[x_F]/(\text{linear}+\text{incomparability})$ of Feichtner–Yuzvinsky with strictly submodular elements $L_c=\sum c_F x_F$. The degree-$\le 1$ HR is then reduced to a $2\times 2$ determinant inequality by Cauchy interlacing on a 3-dimensional restriction.

## Result
Unified proofs / consequences: (a) Aleksandrov's mixed-discriminant inequality and van der Waerden's permanent bound; (b) Alexandrov–Fenchel for mixed volumes and Stanley's $3/11<\Pr(x_1<x_2)<8/11$ for poset linear extensions; (c) Heron–Rota–Welsh conjecture — coefficients of $\chi_M(q)/(q-1)$ are log-concave for every matroid $M$, via $e_i(M)=\deg(\alpha^i\beta^{d-i})$; (d) Mason/Welsh log-concavity of $f_i(M)$ (independent-set counts); (e) Dowling–Wilson top-heavy $w_i(E)\le w_{d-i}(E)$; (f) correlation-constant bound $\frac{b\,b_{ij}}{b_i b_j}\le 2-2(\dim V)^{-1}\le 2$ for any matroid/field.

## Why it matters here
General background for any Einstein Arena problem framed as "prove a combinatorial sequence is log-concave / unimodal" (extremal graph theory, matroid-coefficient questions, counting independent configurations): supplies the Chow-ring / submodular-cone template plus the $2\times 2$-determinant inequality that turns one-positive-eigenvalue into Alexandrov–Fenchel; complements existing wiki content on LP duality and equioscillation by adding a *positivity-of-quadratic-forms* tool kit.

## Open questions / connections
- Dawson/Colbourn conjecture: $h_i(M)^2\ge h_{i-1}(M)h_{i+1}(M)$ for general (non-realizable) matroids — combinatorial HR not yet formulated; expected to be *strictly stronger* than the matroid Chow-ring HR of Adiprasito–Huh–Katz.
- Rota's unimodality / Welsh log-concavity for whole-flat counts $w_k(M)$ across all ranks; Fox's trapezoidal conjecture for Alexander polynomials of alternating knots; Kazhdan–Lusztig polynomials of matroids conjectured non-negative log-concave.
- Whether the correlation constant $\sup b\,b_{ij}/(b_i b_j)$ depends on the field (Seymour–Welsh char-2 example gives $35/36$; upper bound $2$ universal); applications of HR in degrees $q>1$ outside Grothendieck's standard-conjectures $\Rightarrow$ Weil-conjectures route.

## Key terms
Hodge–Riemann relations, hard Lefschetz, Poincaré duality, log-concavity, unimodality, Alexandrov–Fenchel inequality, mixed discriminants, mixed volumes, Chow ring of a matroid, Heron–Rota–Welsh conjecture, characteristic polynomial, Kähler cone, submodular function, McMullen polytope algebra, Dowling–Wilson, Mason conjecture, Huh–Katz, Adiprasito, permanent inequality, van der Waerden

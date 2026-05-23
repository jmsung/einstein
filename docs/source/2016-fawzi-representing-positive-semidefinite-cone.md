---
type: source
kind: paper
title: On representing the positive semidefinite cone using the second-order cone
authors: Hamza Fawzi
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1610.04901
source_local: ../raw/2016-fawzi-representing-positive-semidefinite-cone.pdf
topic: general-knowledge
cites:
---

# On representing the positive semidefinite cone using the second-order cone

**Authors:** Hamza Fawzi  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1610.04901

## One-line
Proves that the $3\times 3$ PSD cone $\mathcal{S}^3_+$ cannot be expressed as a projection of any finite Cartesian power of the Lorentz (second-order) cone.

## Key claim
**Theorem 1:** $\mathcal{S}^3_+$ admits no $\mathcal{Q}^k$-lift for any finite $k$ — and consequently neither does $\mathcal{S}^n_+$ for any $n\geq 3$, nor can higher-dimensional second-order cones help (they reduce to 3D ones).

## Method
Uses the slack-matrix / cone-factorization framework of Gouveia–Parrilo–Thomas: a proper cone has a $\mathcal{Q}^k$-lift iff its slack matrix has a $\mathcal{Q}^k$-factorization. Exhibits an explicit sequence of submatrices $A_n$ of the slack matrix (indexed by 2-subsets and singletons of $[n]$, with entries $\det(v_{i_1},v_{i_2},v_j)^2$ for $v_i=(1,i,i^2)$) and bounds its "soc-covering number" using a combinatorial argument: the orthogonality geometry of $\mathcal{Q}$ (Fact 1: nonzero $a,b_1,b_2\in\mathcal{Q}$ with $\langle a,b_i\rangle=0$ forces $b_1\parallel b_2$) plus **Turán's theorem** to extract a large all-zero clique submatrix, giving the recursion $\mathrm{cov}_{\mathrm{soc}}(A_{3n_0^2})\geq \mathrm{cov}_{\mathrm{soc}}(A_{n_0})+1$.

## Result
$\mathrm{rank}_{\mathrm{soc}}(A_n)\to\infty$ as $n\to\infty$, hence $\mathcal{S}^3_+$ has no finite SOC lift. Section 4 extends the obstruction: the slice $C=\{X\in\mathcal{S}^3_+ : X_{11}=X_{22}+X_{33}\}$ admits no SOC-representable set sandwiched between $C$ and $\mathcal{S}^3_+$. Contrast: the slice $\{X_{11}=X_{22}\}$ *does* have an explicit SOC representation via a chordal arrow-pattern decomposition.

## Why it matters here
General background for the project's earlier finding that SDP relaxations are useless on P1 — this paper rules out a tempting alternative ("just rewrite the SDP as an SOCP") at the cone-representability level, so for any arena problem reaching for $\mathcal{S}^3_+$ structure (sphere packing duals, autocorrelation LP/SDP hierarchies, Cohn–Elkies-style positivity), SOC reformulation is provably not a free shortcut. Reinforces compute-router intuition: SDP solvers (or chordal slice exploitation) are required when $3\times 3$ PSD blocks appear; one cannot escape to cheaper SOCP.

## Open questions / connections
- Which *specific* slices of $\mathcal{S}^n_+$ admit SOC lifts? The arrow/chordal-sparsity case is known; a full characterization is open.
- Quantitative version: how fast does $\mathrm{rank}_{\mathrm{soc}}(A_n)$ actually grow? Paper only proves $\to\infty$.
- Extends Gouveia–Parrilo–Thomas (cone factorizations) and FGPRT (PSD rank) framework to SOC rank; analogous lower bounds for other cone families (exponential cone, power cone) remain open.

## Key terms
positive semidefinite cone, second-order cone, Lorentz cone, SOC lift, cone factorization, slack matrix, extended formulation, soc-rank, Turán theorem, chordal sparsity, Gouveia-Parrilo-Thomas, Fawzi, SDP vs SOCP, lift complexity

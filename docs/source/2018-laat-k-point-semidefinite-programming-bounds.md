---
type: source
kind: paper
title: k-Point semidefinite programming bounds for equiangular lines
authors: David de Laat, Fabrício Caluza Machado, F. M. D. O. Filho, F. Vallentin
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1812.06045
source_local: ../raw/2018-laat-k-point-semidefinite-programming-bounds.pdf
topic: general-knowledge
cites:
---

# k-Point semidefinite programming bounds for equiangular lines

**Authors:** David de Laat, Fabrício Caluza Machado, F. M. D. O. Filho, F. Vallentin  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1812.06045

## One-line
Builds a hierarchy of $k$-point SDP bounds extending Delsarte-Goethals-Seidel LP (k=2) and Bachoc-Vallentin SDP (k=3), and computes 4-, 5-, 6-point bounds for equiangular lines in $\mathbb{R}^n$ with fixed common angle.

## Key claim
For $a \in \{1/5, 1/7, 1/9, 1/11\}$, $\Delta_k(G)^*$ with $k=4,5,6$ substantially improves the best known SDP upper bounds on $M_a(n)$ (equiangular lines with $\cos\alpha = a$) for $n > 3/a^2 - 16$, and extends the stable plateau range where Gerzon's bound $(1/a^2-2)(1/a^2-1)/2$ holds (e.g. for $a=1/11$, plateau extends to $n=448$ vs 347 for $\Delta_3$).

## Method
Derives a weaker but cheaper hierarchy from de Laat-Vallentin's extension of Lasserre's hierarchy to compact topological packing graphs, by replacing the full Lasserre matrix $M(\nu)$ with principal submatrices $M_Q(\nu)$ indexed by independent sets $Q \in I_{k-2}$. Symmetry reduction under the orthogonal group $O(n)$ uses Musin's multivariate Gegenbauer polynomials $P_l^{n,m}(t,u,v)$ to parameterize $\text{Stab}_{O(n)}(R)$-invariant positive kernels, yielding finite SDPs whenever $D \subseteq [-1,1)$ is finite (so $I_{k-2}/O(n)$ is finite). Solved with SDPA-GMP at degree $d=5$, rigorously verified with Arb interval arithmetic.

## Result
For $a=1/5$: $\Delta_6(G)^* = 70$ at $n=65$ vs 326 for $\Delta_3$; for $a=1/7$: 169 at $n=125$ vs 1128 plateau extended to $n=130$; for $a=1/9$: 300 vs 3160 plateau extended to $n=240$. Proves $\Delta_2 = $ LP bound and $\Delta_3 \equiv$ Bachoc-Vallentin (modulo an ad hoc $2\times 2$ block); for $k\geq 4$ on infinite $D$ (spherical codes), $I_{k-2}/O(n)$ is infinite, so generalization beyond finite-distance sets remains open. Computation of $\Delta_6$ takes ~5 days on a single i7-8650U core per instance.

## Why it matters here
Directly informs P11 (equiangular lines / two-distance sets) and the kissing number family (P-class sphere_packing/kissing) — the same SDP hierarchy machinery is the SOTA upper-bound tool. Adds: (a) a concrete way to push past 3-point SDP on finite-$D$ problems, (b) the explicit symmetry-reduction recipe (Musin multivariate Gegenbauer + stabilizer parameterization) needed to implement $k>3$ bounds.

## Open questions / connections
- Does $\Delta_k(G)^* \to \alpha(G)$ as $k\to\infty$? (Open; the parent Lasserre hierarchy converges, but this weakened version's convergence is unknown.)
- How to extend $k$-point bounds to infinite $D$ (general spherical codes / kissing number) given $I_{k-2}/O(n)$ becomes infinite — what's the right finite-orbit truncation?
- Bound on smallest $n$ where $M_a(n) > (1/a^2-2)(1/a^2-1)/2$ — Conjecture 5.9 (Lemmens-Seidel) says $n=185$ for $a=1/5$, far beyond the $n=3/a^2-16$ of Theorem 5.6; $\Delta_k$ cannot prove this via $A(n,\{1/13,-5/13\})$ since $A \geq 3n/2-3$ (Lin-Yu).
- Extends Bachoc-Vallentin 3-point SDP and Lasserre hierarchy; complements Glazyrin-Yu polynomial-method bound (Thm 5.11) which dominates asymptotically.

## Key terms
k-point SDP bound, equiangular lines, spherical two-distance set, Lasserre hierarchy, Bachoc-Vallentin, Delsarte-Goethals-Seidel LP bound, Lovász theta, multivariate Gegenbauer polynomial, Musin, Schoenberg theorem, topological packing graph, symmetry reduction, Gerzon bound, $M_a(n)$, SDPA-GMP, Arb interval arithmetic

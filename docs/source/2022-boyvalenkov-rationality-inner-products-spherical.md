---
type: source
kind: paper
title: Rationality of the inner products of spherical $s$-distance $t$-designs for $t \geq 2s-2$, $s \geq 3$
authors: Peter Boyvalenkov, Hiroshi Nozaki, Navid Safaei
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2204.00261v1
source_local: ../raw/2022-boyvalenkov-rationality-inner-products-spherical.pdf
topic: general-knowledge
cites: 
---

# Rationality of the inner products of spherical $s$-distance $t$-designs for $t \geq 2s-2$, $s \geq 3$

**Authors:** Peter Boyvalenkov, Hiroshi Nozaki, Navid Safaei  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2204.00261v1

## One-line
Proves that all spherical $s$-distance $t$-designs with $t \geq 2s-2$ and $s \geq 3$ have rational inner products, with the icosahedron as the sole exception.

## Key claim
For every spherical $s$-distance $t$-design $C \subset S^{n-1}$ with $s \geq 3$ and $t \geq 2s-2$, all pairwise inner products $\langle x,y\rangle$ are rational, except for the icosahedron (where they involve $\pm 1/\sqrt{5}$). Equivalently: all sharp configurations and all non-icosahedron Levenshtein-bound-attaining codes have rational inner products.

## Method
For $s \geq 6$: leverage the $Q$-polynomial association scheme structure (Delsarte–Goethals–Seidel, Theorem 2.2) and act on primitive idempotents via Galois automorphisms of the splitting field; Suzuki's classification of multiple $Q$-polynomial orderings rules out any nontrivial reordering, forcing rational entries in $E_1$. For $s=4,5$: rationality of $Q_k$ on inner products forces all irrationals to be $\pm\sqrt{3/(n+2)}$, then design equations (2) on the distance distribution give contradictions. For $s=3$: use Besicovitch's theorem on linear independence of $\sqrt{n_i}$ to reduce to antipodal case and derive $|C| = n^2+n$ (tight), recovering the icosahedron exception.

## Result
Theorem 2.6 settles $s \geq 6$; Theorems 3.1 and 3.2 settle $s = 4, 5$ and $s = 3$ respectively. Corollary 4.3: all codes attaining $L_t(n,u)$ for $t \geq 3$ have rational inner products except the icosahedron. Corollary 4.5: all sharp configurations except the icosahedron have rational inner products. The splitting field of such a $Q$-polynomial scheme has degree at most 2 over $\mathbb{Q}$ (Remark 3.3).

## Why it matters here
Sharp configurations and Levenshtein-bound codes are exactly the universally-optimal point sets relevant to Einstein Arena's kissing-number, sphere-packing, and energy-minimization problems — rationality of inner products is a strong arithmetic constraint that narrows the search space for candidate optimal configurations and supports exact (mpmath) verification rather than float-precision optimization on these problems.

## Open questions / connections
- Extends Bannai–Damerell's rationality results for tight spherical designs to the broader class $t \geq 2s-2$.
- The case $t = 2s-2$ in Bannai's alternative proof (Remark 4.6) remains open because $b^*_{s-1}$ depends on the undetermined $a^*_{s-1}$.
- Connects to the still-unresolved classification of sharp configurations (Cohn–Kumar) and to the list of known $s$-distance $t$-designs unchanged since 1987 (Levenshtein).

## Key terms
spherical designs, s-distance sets, sharp configurations, Levenshtein bound, Delsarte-Goethals-Seidel, Q-polynomial association scheme, Bose-Mesner algebra, Gegenbauer polynomials, splitting field, Galois automorphism, icosahedron, kissing number, tight designs, Besicovitch theorem, Bannai-Damerell, Suzuki multiple Q-polynomial, universally optimal codes

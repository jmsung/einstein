---
type: source
kind: paper
title: Improved stability for the size and structure of sumsets
authors: Andrew Granville, Jack Smith, Aled Walker
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2406.03275v1
source_local: ../raw/2024-granville-improved-stability-size-structure.pdf
topic: general-knowledge
cites: 
---

# Improved stability for the size and structure of sumsets

**Authors:** Andrew Granville, Jack Smith, Aled Walker  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2406.03275v1

## One-line
Sharper effective thresholds for when the $N$-fold sumset $NA \subset \mathbb{Z}^d$ becomes polynomial in size and rigid in structure.

## Key claim
For finite $A \subset \mathbb{Z}^d$ with $\Lambda_{A-A}$ full-dimensional, the Khovanskii threshold satisfies $N_{Kh}(A) \le |A|^2 \mathrm{Vol}^{\dagger,\max}(H(A)) - |A| + 1$, and the structural threshold satisfies $N_{Str}(A) \le (d+1)\kappa(A)(|A|-d-1)\mathrm{Vol}^{\dagger,\max}(H(A))$ — exponential improvements over the prior $(2|A| \cdot \mathrm{width}(A))^{(d+4)|A|}$ and $(d|A| \cdot \mathrm{width}(A))^{13d^6}$ bounds.

## Method
Returns to Khovanskii's original Hilbert-polynomial framing and adapts Gröbner-basis / toric-ideal techniques from Sturmfels (Ch. 4 of *Gröbner bases and convex polytopes*), but recast in elementary linear-algebra language. Core machinery: control the lattice $Z(A) = \{z \in \mathbb{Z}^\ell : \mathrm{wt}(z)=0,\ A_{\mathrm{mat}} z = 0\}$ via "primitive" elements $Z^\dagger$ whose $\ell_\infty$ norm is bounded by $\mathrm{Vol}^{\dagger,\max}(H(A))$ (Cramer's rule), then bound the Mann–Dickson minimal set $M(U)$ in the Nathanson–Ruzsa inclusion-exclusion. For the structural bound, a "regular representation" lemma decomposes $v \in P(A)$ as $u+w$ where $u \in MA$ and $w$ lives in a single facet, combined with a convex-geometric quantity $\kappa(A)$ measuring facet-volume anisotropy.

## Result
Theorem 1.5: $N_{Kh}(A) \le |A|^2 \mathrm{Vol}^{\dagger,\max}(H(A)) - |A| + 1 \le |A|^2 d^{d/2} \mathrm{width}(A)^d - |A| + 1$. Theorem 1.8: $N_{Str}(A) \le (d+1)\kappa(A)\bigl(d!\mathrm{Vol}(H(A)) + |\mathrm{ex}(H(A))| - d - 1\bigr)\mathrm{Vol}^{\dagger,\max}(H(A))$, with the cleaner corollary $N_{Str}(A) \le (d+1)(d!)^2(|\mathrm{ex}(H(A))|-d)\mathrm{Vol}(H(A))^2$. When $|A|=d+2$ with full lattice, the Khovanskii bound is optimal up to the $|A|^2$ factor; for simplices $\kappa(A)=1$ and the structural bound essentially recovers the prior best $(d+1)!\mathrm{Vol}(H(A))$.

## Why it matters here
General background on additive combinatorics / sumset growth — no direct arena tie to the 23 problems, but the polytope-volume and lattice-relation machinery (Mann–Dickson, $Z^\dagger$ primitive null vectors, Cramer/Hadamard determinant bounds) is the kind of discrete-geometry toolkit that could inform lattice-point counting or extremal-configuration arguments in kissing-number / sphere-packing settings.

## Open questions / connections
- Eisenbud–Goto regularity conjecture restricted to projective toric varieties would imply the essentially optimal $N_{Kh}(A) \le d!\mathrm{Vol}(H(A)) - |A| + O_d(1)$ — still open.
- Conjectured general bound $N_{Str}(A) \lesssim d!\mathrm{Vol}(H(A))$ remains; current $(1.9)$ is roughly its square.
- Extends Khovanskii (1992), Nathanson–Ruzsa (2002), Curran–Goldmakher (2021), Granville–Shakan–Walker (2023), Lev (2022); leaves open whether the $|A|^2$ factor in the Khovanskii bound can be reduced to $|A|$ or $O(1)$.

## Key terms
sumset, Khovanskii threshold, Ehrhart polynomial, convex polytope, lattice points, Mann–Dickson lemma, Gröbner basis, toric ideal, Eisenbud–Goto conjecture, Hilbert polynomial, additive combinatorics, Granville, Sturmfels, Khovanskii

---
type: source
kind: paper
title: The generalized Makeev problem revisited
authors: Andres Mejia, S. Simon, Jialin Zhang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.03818
source_local: ../raw/2023-mejia-generalized-makeev-problem-revisited.pdf
topic: general-knowledge
cites:
---

# The generalized Makeev problem revisited

**Authors:** Andres Mejia, S. Simon, Jialin Zhang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.03818

## One-line
Improved upper bounds on the minimum dimension $\Delta(m;\ell/k)$ needed so that $m$ masses in $\mathbb{R}^d$ admit $k$ hyperplanes any $\ell$ of which equipartition each mass, for $\ell=2$ (any $k$) and $(\ell,k)=(3,4)$, including pairwise-orthogonal and transversal (piercing) extensions.

## Key claim
For $m = 2^{q+1}-t$ with $1 \le t \le 2^q$: (a) $\Delta(m;2/k) \le 2^q(k+1)-t$ and (b) $\Delta(m;3/4) \le 7\cdot 2^q - 2t$, exponentially better than the prior $\Delta(m;k)$ bound $2^q(2^{k-1}+1)-t$ when $\ell=k-1$; nearly tight at $m+1$ a power of two (e.g. $11 \le \Delta(3;3/4) \le 12$ vs $12 \le \Delta(3;4) \le 17$).

## Method
Configuration-space/test-map paradigm: identify hyperplane arrangements with $(S^d)^k$ under the $\mathbb{Z}_2^k$-action, expand mass-region indicators in the $\chi_h$ Fourier basis on $\mathbb{Z}_2^k$, and reduce equipartition to zeros of a $\mathbb{Z}_2^k$-equivariant map into $U_{\ell,k}^{\oplus m} = \bigoplus_{h:1\le |h|\le \ell} V_h^{\oplus m}$. Apply Fadell–Husseini ideal-valued cohomological index (Proposition 2.4): if the polynomial $p_U = \prod_i (a_{i,1}t_1+\cdots+a_{i,k}t_k)$ equals $t_1^d\cdots t_k^d$ modulo $(t_j^{d+1})$, the map has a zero. The improvement comes from careful term-by-term exponent bookkeeping in $p_{\ell,k}^m$ (using identities like $p_{3,4} = t_1t_2t_3t_4 r_{2,4}r_{3,4}$ and degree-forcing arguments to collapse Vandermonde products to $t_1^d\cdots t_k^d$).

## Result
Pairwise-orthogonal analogues $\Delta^\perp$ match the same bounds for $t \ge 2$ (Theorem 1.5), giving e.g. $\Delta^\perp(2;2/3) \le 6$ and $\Delta^\perp(2;3/4) \le 10$. Appendix: $5 \le \Delta^\perp(1;3/4) \le 7$ and $7 \le \Delta^\perp(1;3/5) \le 9$. Transversal Theorem 1.7: if $m$ families of compact convex sets in $\mathbb{R}^d$ have no $2\ell$ pairwise-disjoint members per family, then $k$ hyperplanes exist whose any $\ell$ pierce each family — proved via a Radon-type intersection theorem on the deleted join $\Sigma_n = (\Delta_n)^{*2}_\Delta$ with the same equivariant cohomology computation.

## Why it matters here
General background; no direct Einstein Arena tie. The arena problems index does not include hyperplane mass-partition / Grünbaum–Hadwiger–Ramos problems, and this paper's $\mathbb{Z}_2^k$ Fourier/equivariant-cohomology machinery is orthogonal to the LP/SDP/sphere-packing/autocorrelation toolkit used here. Possibly distant relevance to any future discrete-geometry partition problem (Radon-type combinatorial divisions of point sets) but not to current optimizer pipeline.

## Open questions / connections
- Ramos lower bound $\Delta(m;k) \ge m(2^k-1)/k$ conjectured tight; ℓ=k case open except small $(m,k)$ — gap remains exponential in $k$ and $q$.
- Bounds at general $(\ell,k)$ with $4 \le \ell \le k-1$ (and $k \ge 5$) are not addressed; method requires per-case polynomial analysis.
- Whether the transversal Theorem 1.7 has an $\ell=k$ analog matching $\Delta(1;4) \le 5$ is explicitly noted as unknown.
- Extends Blagojević–Karasev 2012 polynomial criteria and Frick–Murray–Simon–Stemmler 2022 transversal framework.

## Key terms
hyperplane mass equipartition, Grünbaum–Hadwiger–Ramos problem, Makeev problem, ham sandwich theorem, Borsuk–Ulam, Fadell–Husseini index, equivariant cohomology, $\mathbb{Z}_2^k$ Fourier analysis, Radon-type intersection, deleted join, Kneser hypergraph chromatic number, Dolnikov transversal, Vandermonde determinant, configuration-space/test-map

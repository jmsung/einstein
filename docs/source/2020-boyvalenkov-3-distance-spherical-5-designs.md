---
type: source
kind: paper
title: On 3-distance spherical 5-designs
authors: P. Boyvalenkov, Navid Safaei
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.01895
source_local: ../raw/2020-boyvalenkov-3-distance-spherical-5-designs.pdf
topic: general-knowledge
cites:
---

# On 3-distance spherical 5-designs

**Authors:** P. Boyvalenkov, Navid Safaei  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.01895

## One-line
New proof that spherical 3-distance 5-designs are maximal codes, plus a divisibility condition ($n \mid 2M$) that prunes the search space for the Bannai et al. classification conjecture.

## Key claim
For any spherical 3-distance 5-design $C \subset S^{n-1}$ with $|C| = M$: (i) the three inner products are exactly the roots $\alpha_0 < \alpha_1 < \alpha_2$ of the Levenshtein polynomial $P_3(t)P_2(s) - P_3(s)P_2(t) = 0$, and (ii) $n \mid 2M$. Conjecture 1.1 (Bannai et al.) is verified computationally for all $n \le 1000$.

## Method
Levenshtein quadrature formula (4) applied to monomials $t^i$ ($i=0,\dots,5$) yields a linear system (6) for the distance distribution $(X,Y,Z) = (A_a, A_b, A_c)$. Combining with Vieta on the cubic (7) gives the symmetric product $XYZ$ as a rational function of $(n, M)$; integrality of $XYZ$ together with $p$-adic valuation analysis ($v_p$) forces $n \mid 2M$. Remaining exceptional $(n,T)$ pairs are killed by computing distance distributions of derived codes $C_a, C_b, C_c$ (sections on $S^{n-2}$) via the Cosine Law.

## Result
Two main theorems: Theorem 2.1 (inner products = Levenshtein zeros, generalized in Thm 2.3 to $k$-distance $(2k-1)$-designs) and Theorem 4.1 ($n \mid 2M$). Computer search over $n \le 1000$ leaves only two candidate exceptions $(n,T) = (341, 3744)$ with $(a,b,c) = (-1/7, -1/35, 1/14)$ and $(638, 7011)$ with $(a,b,c) = (-1/8, -1/40, 1/20)$, both ruled out by derived-code distance-distribution non-integrality (Theorem 6.1). The conjectured family is $n = 3m^2 - 5$, $M = m^4(3m^2-5)/2$, with examples known only for $m = 2, 3$.

## Why it matters here
General background on extremal coding theory / spherical design theory; informs the Levenshtein-bound machinery and Jacobi-polynomial framework used in sphere-packing / kissing-number LP bounds. No direct Einstein Arena problem maps to 3-distance 5-designs, but the Levenshtein quadrature and distance-distribution integrality arguments are reusable techniques for arena problems involving spherical codes or few-distance sets.

## Open questions / connections
- Full proof of Bannai et al. Conjecture 1.1 (only $n \le 1000$ verified; the failed "$n+5 \mid 9T$" route shows the easy strengthening is wrong).
- Existence of tight spherical 5-designs beyond $m = 3, 5$ (folklore conjecture: none exist).
- Existence of derived-from-tight-7-design codes beyond $m = 2, 3$.
- Extends Delsarte–Goethals–Seidel [8], Levenshtein [12, 13], Boyvalenkov–Nikova [7]; connects to few-distance-set upper bounds [1, 2, 10, 11, 14].

## Key terms
spherical design, 5-design, 3-distance set, Levenshtein bound, Levenshtein quadrature, Jacobi polynomial, Gegenbauer polynomial, Delsarte-Goethals-Seidel, distance distribution, tight design, derived code, Bannai conjecture, maximal code, $p$-adic valuation

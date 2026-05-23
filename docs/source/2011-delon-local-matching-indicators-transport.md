---
type: source
kind: paper
title: Local Matching Indicators for Transport Problems with Concave Costs
authors: J. Delon, J. Salomon, A. Sobolevski
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.1795
source_local: ../raw/2011-delon-local-matching-indicators-transport.pdf
topic: general-knowledge
cites:
---

# Local Matching Indicators for Transport Problems with Concave Costs

**Authors:** J. Delon, J. Salomon, A. Sobolevski  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.1795

## One-line
Introduces local "matching indicators" that detect which neighbor-pairs are matched in the 1D optimal transport plan when the cost is a strictly concave function of distance, yielding an $O(N^2)$-worst-case algorithm (often near-linear in practice) for the assignment problem on the line.

## Key claim
For supplies and demands alternating along a line (a "chain"), the optimal assignment under strictly concave $c(x,y)=g(|x-y|)$ can be built greedily: a *negative* local indicator $I_k^p(i)$ or $I_k^q(i)$ of order $k$, computed from only $2k+2$ consecutive points, certifies $k$ matched pairs of the optimal plan independently of all other points (Theorem 3.2).

## Method
Define order-$k$ indicators as signed sums of $O(k)$ cost evaluations over $2k+2$ consecutive alternating points (Def. 3.1). Combined with the non-crossing rule (Lemma 2.2) and a "rule of three" (Lemma 3.4) — both consequences of strict concavity + monotonicity of $g$ — negativity of an indicator forces the inner $k$ pairs to be matched in *every* optimal plan. Algorithm 1 sweeps $k=1,2,\dots$ in lexicographic order, peels off matched pairs whenever an indicator goes negative, and resets. Real-valued (non-unitary) histograms are reduced to unitary chains via a stratification of the cumulative distribution (Lemma 5.2) computed in $O(M+N)$ via stack-based Algorithms 2–3.

## Result
- Worst-case additions $C^+(N) \le 3N^2 - 6N$ (Theorem 6.2); cost-function evaluations bounded by $N(N+1)/2$.
- If all visited orders are bounded by $K$, $C^+(N) \le 3N(K^2+2K+2)$ — i.e., linear in $N$ when local structure is shallow.
- Empirically for $c(x,y)=|x-y|^\alpha$ on $[0,1]$, the empirical exponent $\alpha_\text{emp}$ drops from $\approx 1.88$ ($\alpha=1$) toward $\approx 1.22$ ($\alpha=10^{-3}$): the more concave $g$ is, the more often low-order indicators fire, approaching linear time.
- Side lemma: for four consecutive points with $b=1-a-c$, the order-1 indicator $f(\alpha)=b^\alpha+1-a^\alpha-c^\alpha$ is monotone in $\alpha$ — if negative for some $\alpha$, negative for all smaller $\alpha$ (a refined rule-of-three).

## Why it matters here
General background; no direct arena tie. The concave 1D transport setting doesn't map onto current Einstein problems (sphere packing, autocorrelation, kissing) — those use convex / spectral / LP-duality machinery, not concave-cost matching. Closest tangent: the non-crossing rule is the discrete analogue of monotone-rearrangement intuition that appears in 1D extremal problems, and the stratification trick is a useful template for any "lift unitary algorithm to weighted case" reduction.

## Open questions / connections
- Extends Aggarwal–Bar-Noy–Khuller–Kravets–Schieber [1] (quadrangle-inequality / Monge-matrix matching) from $c=|x-y|$ to general strictly concave $g$; complements McCann's analytic treatment [15].
- Conjecture (unproven in paper): negativity-monotonicity in $\alpha$ holds for indicators of *all* orders, not just order 1 — would explain the observed near-linear empirical scaling for small $\alpha$.
- Open: chain decomposition across strata treats strata independently; exploiting identical indicators across strata could push real-valued complexity below $O(N^3)$.
- Does not extend to the circle (where the cut point becomes cost-dependent for concave $g$); concave transport on $S^1$ remains open.

## Key terms
optimal transport, concave cost, assignment problem, Monge matrix, non-crossing rule, rule of three, local matching indicator, monotone rearrangement, McCann, Kantorovich, stratification, 1D transport, quadrangle inequality, Aggarwal

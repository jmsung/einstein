---
type: source
kind: paper
title: "The geometry of differential privacy: the sparse and approximate cases"
authors: Aleksandar Nikolov, Kunal Talwar, Li Zhang
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1212.0297
source_local: ../raw/2012-nikolov-geometry-differential-privacy-sparse.pdf
topic: general-knowledge
cites:
---

# The geometry of differential privacy: the sparse and approximate cases

**Authors:** Aleksandar Nikolov, Kunal Talwar, Li Zhang  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1212.0297

## One-line
Gives near-optimal (polylog-approximation) differentially private mechanisms for any set of linear queries, in both dense and sparse-database regimes, via convex-geometric tools tied to hereditary discrepancy.

## Key claim
For any $d \times N$ query matrix $A$, an efficient $(\varepsilon,\delta)$-DP mechanism achieves mean-squared error within $O(\log^2 d \cdot \log 1/\delta)$ of the optimum (dense case); sparse-case bounds match within $\mathrm{polylog}(d,N)$; as a byproduct, $\mathrm{herdisc}_\infty(A)$ is approximated to within $O(\log^2 d \cdot \log N \sqrt{\log\log d})$.

## Method
Decompose $A$ via its **minimum-volume enclosing ellipsoid** (Löwner–John) and add correlated Gaussian noise scaled to the ellipsoid's axes, recursing on shorter directions. For sparse $\|x\|_1 \le n$, post-process by **least-squares projection** onto $nAB_1^N$ (statistical-estimation shrinkage). Lower bounds use **restricted invertibility** (Bourgain–Tzafriri, Vershynin) to extract a large nearly-orthogonal simplex from John contact points, yielding a determinant / least-singular-value lower bound matching the mechanism.

## Result
Dense $(\varepsilon,\delta)$-DP: error $\le O(\log^2 d \log 1/\delta) \cdot L_A$ (Thm 1). Sparse $(\varepsilon,\delta)$-DP: error $\le O(\log^{3/2} d \log N \log 1/\delta + \log^2 d \log 1/\delta) \cdot L_{A,n}$ (Thm 3). Pure $\varepsilon$-DP sparse: error $\le O(\mathrm{polylog}(d) \log^{3/2} N) \cdot L_{A,n}$ (Thm 4). For counting queries, gives $\tilde O(\sqrt{dn})$ per-query $\varepsilon$-DP error — improving Blum-Ligett-Roth's $\tilde O(d n^{3/4})$ and matching the Dinur-Nissim lower bound up to logs. Gap between optimal $\varepsilon$-DP and $(\varepsilon,\delta)$-DP is at most $O(\log(N/d) \cdot \mathrm{polylog}\, d)$ for linear queries.

## Why it matters here
General background; no direct arena tie — this is differential-privacy / discrepancy theory. The transferable ideas for the arena agent are (a) the **John/Löwner ellipsoid + restricted invertibility** machinery for producing nearly-orthogonal large simplices inside a convex body (potentially useful in sphere-packing / kissing-number lower-bound constructions), and (b) the **determinant lower bound** $d^{3} \cdot \mathrm{vol}(S)^{2/d}$ as a clean volumetric certificate.

## Open questions / connections
- Can hereditary discrepancy be approximated below the $\mathrm{polylog}$ factor, or is there a superconstant hardness?
- Extends Hardt–Talwar [HT10] (which assumed the slicing/hyperplane conjecture) by replacing the M-ellipsoid with the minimum-volume enclosing ellipsoid — simpler and unconditional.
- Leaves open near-optimal $\ell_\infty$-error mechanisms in the sparse case.
- Connects to Matoušek's tightness of the LSV determinant bound; to Bansal's SDP-based discrepancy minimization; to Vershynin's John-decomposition selection.

## Key terms
differential privacy, hereditary discrepancy, Löwner-John ellipsoid, minimum volume enclosing ellipsoid, restricted invertibility, Bourgain-Tzafriri, Vershynin, Gaussian noise mechanism, K-norm mechanism, determinant lower bound, linear queries, convex geometry, least-squares projection, counting queries

---
type: source
kind: paper
title: The 1 / N Expansion of the Symmetric Traceless and the Antisymmetric Tensor Models in Rank Three
authors: D. Benedetti, Sylvain Carrozza, R. Gurau, Maciej Kolanowski
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1712.00249
source_local: ../raw/2017-benedetti-expansion-symmetric-traceless-antisymmetric.pdf
topic: general-knowledge
cites:
---

# The 1 / N Expansion of the Symmetric Traceless and the Antisymmetric Tensor Models in Rank Three

**Authors:** D. Benedetti, Sylvain Carrozza, R. Gurau, Maciej Kolanowski  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1712.00249

## One-line
Proves rigorously that rank-3 tensor models built on symmetric traceless or antisymmetric tensors with a tetrahedral quartic interaction admit a $1/N$ expansion dominated by melonic diagrams.

## Key claim
For $P \in \{A, S\}$ (antisymmetric or symmetric-traceless projector), the free energy admits $F_P(\lambda) = \sum_{\omega \in \mathbb{N}/2} N^{-\omega} F_P^{(\omega)}(\lambda)$ (Theorem 1), and the leading order $F_P^{(0)}(\lambda)$ is a sum over melonic stranded maps (Theorem 2). This confirms the Klebanov–Tarnopolsky conjecture (arXiv:1706.00839), previously checked only numerically up to 8th order.

## Method
Combinatorial / stranded-graph analysis of the perturbative expansion, with a degree $\omega(S) = 3 + \tfrac{3}{2}V(S) + B(S) - F(S)$ controlling the $N$-scaling. The central technical step is a partial resummation of "bad tadpoles" via a Wick-ordering trick: the original theory is rewritten as a Wick-ordered interaction with a renormalized covariance $K(\lambda, N)$, which is shown to itself admit a $1/N^{1/2}$ expansion. Bounds are then proved by induction using dipole, triangle, and H-graph contractions (Lemmas 3, 6, 7, 11, 12).

## Result
Both the symmetric traceless and antisymmetric rank-3 tensor models with tetrahedral interaction $\tfrac{\lambda}{4N^{3/2}} T_{a_1a_2a_3} T_{a_3a_4a_5} T_{a_5a_2a_6} T_{a_6a_4a_1}$ have a well-defined large-$N$ limit dominated by melons. The symmetric (non-traceless) model fails: trace modes develop an instability — the would-be renormalized covariance is a divergent series in $\lambda N^{1/2}$ — and saving it requires a rescaling that strictly suppresses melons (Appendix B). Schur's Lemma applied to the irreducible representation explains why tracelessness is essential.

## Why it matters here
General background; no direct arena tie. This is hep-th/quantum-gravity combinatorics (SYK-model holography), not extremal geometry or analytic number theory; none of the 23 Einstein Arena problems are tensor-model partition functions. The melonic-dominance / large-$N$ techniques are conceptually adjacent to flag-algebra SDP and graph-limit arguments used in extremal combinatorics, but the bridge is loose.

## Open questions / connections
- Extension to mixed-symmetry irreducible components of $O(N)^{\otimes 3}$, and to hybrid models with traces (cf. [38] Halmagyi–Mondal).
- Builds on the two-symmetric-tensor result of Gurau (arXiv:1706.05328 [34]); generalizes the tadpole-resummation method to settings where individual graphs violate the naive scaling bound.
- Relation between melonic dominance and the matrix-tensor large-$D$ limit of Ferrari et al. ([39, 40, 41]) — when do the two expansions coincide?

## Key terms
1/N expansion, tensor models, melonic diagrams, SYK model, symmetric traceless tensor, antisymmetric tensor, tetrahedral interaction, Wick ordering, stranded graphs, large-N limit, Klebanov-Tarnopolsky conjecture, Gurau, Schur's lemma, orthogonal group O(N), tadpole resummation

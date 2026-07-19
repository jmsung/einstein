---
type: source
kind: paper
title: Freeness for tensors
authors: Remi Bonnin, Charles Bordenave
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2407.18881
source_local: ../raw/2024-bonnin-freeness-tensors.pdf
topic: general-knowledge
cites:
---

# Freeness for tensors

**Authors:** Remi Bonnin, Charles Bordenave  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.18881

## One-line
Extends Voiculescu's free probability from matrices to tensors of arbitrary order, defining tensor freeness via a poset on combinatorial maps and proving asymptotic freeness for the basic random tensor models.

## Key claim
Independent Wigner tensors (of possibly different orders) and Haar-orthogonal-conjugated tensor families are asymptotically free in probability as $N \to \infty$, with the joint distribution characterized by Schwinger-Dyson loop equations on combinatorial maps.

## Method
Tensors of order $p$ are represented as vertices of combinatorial maps; trace invariants $m((T_v)_{v\in V}) = N^{-\gamma}\sum_i \prod_v (T_v)_{i_{\partial v}}$ generalize matrix traces. Freeness is defined via a "non-crossing" poset on maps where switches alter connected-component counts, with conditions (P1)-(P2) replacing the non-crossing-partition structure of classical free probability. Proofs use Schwinger-Dyson loop equations derived by integration-by-parts (Gaussian case) or Weingarten calculus on $O(N)$ (Haar case), plus a moment-comparison argument extending to non-Gaussian Wigner tensors.

## Result
Theorems 1-2: deterministic family $A_0^N$ and normalized Wigner tensor $W_N = X/N^{(p-1)/2}$ are asymptotically free in probability (Gaussian under (A1); general bounded moments under (A2)). Theorem 3: $A_0^N$ and Haar $\{U_N, U_N^*\}$ are asymptotically free. Theorem 4: two deterministic families $A_1^N$ and $A_2^N \cdot U_N^{\#}$ (conjugating each leg by Haar $U_N$) are asymptotically free. Corollary 1: independent Wigner tensors of arbitrary orders are jointly asymptotically free. Recovers the Wigner-Gurau limit law for $p\geq 3$ as a special case.

## Why it matters here
General background; no direct arena tie. The 23 Einstein Arena problems are low-dimensional discrete-geometry / extremal / analytic optimization questions — none are random-tensor or large-$N$ free-probability problems. Potentially adjacent only via tensor-PCA-style spectral methods if any future problem demanded them.

## Open questions / connections
- Non-Gaussian (A1)-only case: conjectured asymptotically free without the stronger hyper-map assumption (A2); proof open.
- Unitary-invariant case for even-order Hermitian tensors mentioned but deferred (cf. Collins-Gurau-Lionni in preparation).
- Connection to Male's traffic distributions [22] and operad formalism [23] noted but not developed; could unify multiple "independence" notions.
- Tensor analogs of Voiculescu free entropy / free Fisher information [34] not addressed.

## Key terms
free probability, asymptotic freeness, random tensors, Wigner tensor, GOTE, Haar orthogonal, Schwinger-Dyson equations, Weingarten calculus, combinatorial maps, trace invariants, non-crossing poset, free cumulants, Voiculescu, Gurau

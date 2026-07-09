---
type: source
kind: paper
title: Melonic Large N Limit of 5-Index Irreducible Random Tensors
authors: Sylvain Carrozza, Sabine Harribey
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2104.03665
source_local: ../raw/2021-carrozza-melonic-large-limit-5-index.pdf
topic: general-knowledge
cites:
---

# Melonic Large N Limit of 5-Index Irreducible Random Tensors

**Authors:** Sylvain Carrozza, Sabine Harribey  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2104.03665

## One-line
Proves that rank-5 irreducible $O(N)$ tensor models with sextic 5-simplex interaction admit a melonic large $N$ expansion, extending the rank-3 program to rank 5.

## Key claim
For any of the seven inequivalent irreducible rank-5 representations of $O(N)$ (symmetric traceless, antisymmetric, and five mixed-symmetry Young tableaux), the free energy admits a $1/N$ expansion $F_P(\lambda) = \sum_{\omega \in \mathbb{N}} N^{-\omega} F_P^{(\omega)}(\lambda)$ (Theorem 1), and the leading order $F_P^{(0)}$ is a sum over melonic stranded graphs satisfying $1 - X + m_P \lambda^2 X^6 = 0$ with $m_S = m_A = \frac{1}{5!^4}$ (Theorem 2).

## Method
Feynman expansion in rooted connected combinatorial maps, refined to stranded graphs where each of the $945$ propagator tensor structures induces a strand pairing classified as unbroken / broken / doubly-broken. The degree $\omega(G) = 5 + 5V(G) + B_1(G) + 2B_2(G) - F(G)$ is bounded by (i) subtracting melon and double-tadpole subgraphs via a closed Schwinger–Dyson equation (using irreducibility + Schur's lemma to bound their amplitudes), then (ii) recursively deleting tadpoles, dipoles, dipole-tadpoles, and quartic rungs with face-count bounds and Cauchy–Schwarz inequalities to force $\omega \geq 0$.

## Result
The $1/N$ expansion exists (Theorem 1) and the leading sector is melonic (Theorem 2), with the leading two-point function solving an algebraic sextic equation. Unlike rank 3, triangle subgraphs play no role, but the analysis requires bounding eight-point functions (Lemma 8 enumerates 13 special two-point subgraph cases $H_0$–$H_{12}$). The colorable 5-simplex contraction (Eq. 13) gives $m_P > 0$ for any irreducible $P$.

## Why it matters here
General background; no direct arena tie. The 23 Einstein Arena problems include sphere packing, autocorrelation, and discrete combinatorics — none currently mapped to tensor large-$N$ techniques — but melonic/tensor-model machinery is a candidate framework for any future arena problem involving high-rank symmetric tensor decompositions or random-tensor eigenvalue statistics (cf. refs [66, 67] on Wigner semicircle generalizations and largest eigenvalues of random tensors).

## Open questions / connections
- Extending the proof to rank-4 with 4-simplex interaction (expected to reintroduce triangle-submap difficulties as in rank 3).
- Generalizing to arbitrary rank $r \geq 6$ — would need a systematic method to bound two-point stranded subgraphs without ad-hoc inductive moves.
- Generalizing to $Sp(N)$ fermionic tensor fields by analogy with the rank-3 construction of Carrozza–Pozsgay [21]; identifying effective $n$-point interactions (e.g., $n \leq 6$) at leading order for QFT applications.

## Key terms
melonic large N limit, irreducible tensor representation, 5-simplex interaction, stranded graph, Feynman map, Schwinger-Dyson equation, O(N) symmetry, Young tableau, Cauchy-Schwarz bound, double-tadpole subtraction, SYK model, Carrozza, Harribey, Gurau

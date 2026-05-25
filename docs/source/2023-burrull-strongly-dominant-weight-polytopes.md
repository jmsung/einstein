---
type: source
kind: paper
title: Strongly dominant weight polytopes are cubes
authors: Gastón Burrull, Tao Gui, Hongsheng Hu
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2311.16022
source_local: ../raw/2023-burrull-strongly-dominant-weight-polytopes.pdf
topic: general-knowledge
cites:
---

# Strongly dominant weight polytopes are cubes

**Authors:** Gastón Burrull, Tao Gui, Hongsheng Hu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.16022

## One-line
For any root system of rank $r$, the dominant weight polytope $P_\lambda$ associated with a strongly dominant weight $\lambda$ is combinatorially equivalent to the $r$-dimensional cube.

## Key claim
**Theorem 2.9:** If $\lambda \in C^+$ (strongly dominant, interior of dominant Weyl chamber), then $P_\lambda := \mathrm{Conv}(W_f \lambda) \cap \overline{C^+}$ has the face lattice of $[0,1]^r$. Its $2^r$ vertices $\{p_J^\lambda \mid J \subseteq [r]\}$ are computable explicitly from the Cartan matrix: $p_J^\lambda = \lambda - \sum_{j \in J} c_j^\lambda \alpha_j^\vee$ with $(c_j^\lambda)_{j \in J} = M_J^{-1} \cdot ((\alpha_i \mid \lambda))_{i \in J}$.

## Method
Express $P_\lambda$ as the intersection of two closed simplicial cones $\overline{C^+} \cap \overline{Q_\lambda}$ (Proposition 2.1). Decompose into pieces $F_{I,J} = C_I \cap Q_J^\lambda$ indexed by pairs of subsets $I, J \subseteq [r]$; show $F_{I,J} \neq \emptyset \iff I \cup J = [r]$ (Lemma 2.6), using that inverses of Cartan matrices have non-negative entries. Match faces to cube faces via the bijection $\theta: H(I_0, I_1, I_{01}) \mapsto F_{I_0 \cup I_{01}, I_1 \cup I_{01}}$ and verify the partial order is preserved.

## Result
Face structure of $P_\lambda$ depends only on rank $r$, not on the root system or specific $\lambda$ (as long as $\lambda$ is strongly dominant). Faces $F_{I,J}$ have dimension $|I| + |J| - r$. Minkowski additivity: $P_{\lambda+\mu} = P_\lambda + P_\mu$ (Proposition 2.13). Generalization (Theorem 3.1) to any basis $\{v_1, \dots, v_r\}$ with $(v_i \mid v_j) \leq 0$ for $i \neq j$. Application (Theorem 4.1): Poincaré polynomial of the Peterson variety in classical Lie types is $h_Y(q) = (1+q)^r$, so $b_{2i} = \binom{r}{i}$, $b_{2i+1} = 0$.

## Why it matters here
General background; no direct arena tie. The combinatorics of root-system polytopes (Cartan-matrix-driven vertex enumeration, cube face lattices, Minkowski additivity of dominant weight polytopes) sits adjacent to lattice/representation-theoretic methods but doesn't bear on the current arena problems (sphere packing, autocorrelation, kissing, Sidon, discrete geometry) in any direct way I can see.

## Open questions / connections
- Face structure of $P_\lambda$ for $\lambda \in \overline{C^+} \setminus C^+$ (boundary case) — strictly fewer vertices than the cube; structure depends nontrivially on $\Phi$ (Question 1.1).
- Rietsch's conjecture: is the totally non-negative part $Y_{\geq 0}$ of the Peterson variety cell-decomposed-homeomorphic to $[0,1]^{\dim_\mathbb{C} Y}$ in all Lie types? (Question 4.2)
- Extends Besson–Jeralds–Kiers work on Kostka cones / intersection polytopes; complements Horiguchi–Masuda–Shareshian–Song's results connecting partitioned weight polytopes to Peterson cohomology.

## Key terms
dominant weight polytope, root system, Weyl group, Cartan matrix, strongly dominant weight, simplicial cone intersection, face lattice, combinatorial cube, Peterson variety, Betti numbers, toric orbifold, Minkowski sum, fundamental coweights, classical Lie types

---
type: source
kind: paper
title: Asymptotic Log-concavity of Dominant Lower Bruhat Intervals via Brunn--Minkowski Inequality
authors: Gaston Burrull, Tao Gui, Hongsheng Hu
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.17980v3
source_local: ../raw/2023-burrull-asymptotic-log-concavity-dominant-lower.pdf
topic: general-knowledge
cites: 
---

# Asymptotic Log-concavity of Dominant Lower Bruhat Intervals via Brunn--Minkowski Inequality

**Authors:** Gaston Burrull, Tao Gui, Hongsheng Hu  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2311.17980v3

## One-line
Proves that the Betti-number sequences of spherical Schubert varieties in affine Grassmannians become asymptotically log-concave under dilation, by realizing them as hyperplane-section volumes of a convex polytope $P_\lambda$.

## Key claim
For an affine Weyl group $W = \mathbb{Z}\Phi^\vee \rtimes W_f$ and dominant coroot $\lambda$, the length-counting sequence $({}^fb^{t_\lambda}_i)_i$ of the dominant lower Bruhat interval ${}^f[e,t_\lambda]$, suitably dilated and rescaled, converges (weak + uniform) to the density $g(z) = \tfrac{1}{\|2\rho\|}\mathrm{Vol}_{r-1}(\mathrm{ht}^{-1}(z))$ of the height pushforward of Lebesgue measure on $P_\lambda := \mathrm{Conv}\{w\lambda \mid w \in W_f\} \cap C^+$, and Brunn--Minkowski forces $\log g$ concave.

## Method
Combinatorial-to-geometric reduction: a "dominant lattice formula" expresses the Poincaré polynomial $\pi_{t_\lambda}(q) = \sum_{\mu \in P_\lambda \cap \mathbb{Z}\Phi^\vee} q^{(2\rho|\mu)} \cdot {}^\mu\pi_f(q^{-1})$ as a lattice-point sum over $P_\lambda$. Hyperplane slices $P^z_\lambda = P_\lambda \cap H_{2\rho,z}$ are approximated by fundamental parallelotopes $B_k$ (lattice tiling at scale $1/k$); $\epsilon$-tube volume bounds via Proposition 6.5 control boundary error, yielding uniform convergence. Brunn--Minkowski (Theorem 1.5) applied to the linear height map $\mathrm{ht}: P_\lambda \to \mathbb{R}$ gives concavity of $\mathrm{Vol}_{r-1}(\mathrm{ht}^{-1}(z))^{1/(r-1)}$, hence log-concavity of $g$.

## Result
Theorem 1.3: $m_k \rightharpoonup \tfrac{1}{\mathrm{Vol}_r(A^+)} \mathrm{ht}_*\mathrm{Vol}_r$ weakly, and step functions $S_k \to g/\mathrm{Vol}_r(A^+)$ uniformly. Corollary 1.6: $\log g$ is concave on $[0, \ell(t_\lambda)]$. Worked C₃ example with $\lambda = 3\alpha_1^\vee+6\alpha_2^\vee+7\alpha_3^\vee$: estimate $\widehat{{}^fb^{t_{8\lambda}}_{196}} \approx 829.87$ vs exact $863$ (3.84% error). Sequence itself can fail log-concavity (e.g. consecutive $4,4,5$) — only the limit is log-concave. Conjecture 1.8: unimodality of $({}^fb^{t_\lambda}_i)_i$ verified by SageMath up to rank 5.

## Why it matters here
General background; no direct arena tie — but methodologically relevant as a clean template for asymptotic log-concavity proofs (lattice-point sum → polytope slice → Brunn--Minkowski), the same machinery family invoked by Cohn--Elkies sphere-packing and Heckman/Okounkov multiplicity work that the wiki already touches.

## Open questions / connections
- Question 1.10/1.11: is $\mathrm{Card}({}^f[e,t_{k\lambda}])$ a quasi-polynomial in $k$ of degree $r$ with leading coefficient $\mathrm{Vol}_r(P_\lambda)/\mathrm{Vol}_r(A^+)$? Refinement: is ${}^fb^{t_{k\lambda}}_{ki}$ quasi-polynomial of degree $r-1$ with leading coefficient $\mathrm{Vol}_{r-1}(\mathrm{ht}^{-1}(i))/(\mathrm{Vol}_r(A^+)\cdot\|2\rho\|)$?
- Brenti's Conjecture 1.2 (log-concavity of generic Bruhat intervals in Weyl groups) and Rota's unimodality conjecture for matroids remain open — this paper handles only the *asymptotic* affine-Grassmannian case.
- Extends Heckman (1982) / Okounkov (1996) Brunn--Minkowski-multiplicity framework to a setting with no underlying symplectic manifold (the module $U \subset V_\lambda$ from Ginzburg's theorem); Theorem 1.3(2) (uniform convergence) is strictly stronger than the weak-convergence analogues in that lineage.

## Key terms
affine Weyl group, Bruhat interval, Schubert variety, affine Grassmannian, Betti numbers, log-concavity, unimodality, Brunn--Minkowski inequality, Duistermaat--Heckman measure, geometric Satake, Ehrhart polynomial, Newton--Okounkov body, Kazhdan--Lusztig, dominant lattice formula

---
type: source
kind: paper
title: Solving clustered low-rank semidefinite programs arising from polynomial optimization
authors: Nando Leijenhorst, David de Laat
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2202.12077
source_local: ../raw/2022-leijenhorst-solving-clustered-low-rank-semidefinite.pdf
topic: general-knowledge
cites:
---

# Solving clustered low-rank semidefinite programs arising from polynomial optimization

**Authors:** Nando Leijenhorst, David de Laat  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2202.12077

## One-line
A high-precision primal-dual interior-point SDP solver (ClusteredLowRankSolver.jl) that exploits clustered low-rank constraint structure from sampled sums-of-squares, delivering large speedups on kissing-number and binary sphere packing computations.

## Key claim
For the Bachoc–Vallentin three-point kissing-number SDP at degree $d=16$, the solver beats SDPA-GMP by $28\times$ (8 cores) / $9.6\times$ (1 core), enabling degree-$20$ computations that improve upper bounds on the kissing number in dimensions $11$–$23$.

## Method
Generalizes SDPB to handle (i) constraint matrices of the form $A_t^{j,l}(r,s) = \sum_i \lambda_i v_i w_i^T$ with **nonsymmetric** rank-1 factors (a strict generalization over [38, 43, 2]), (ii) clusters linked only by free variables, and (iii) multivariate invariant polynomial constraints via combined symmetry reduction (Gatermann–Parrilo symmetry-adapted bases $E^\pi(x) = \Pi^\pi(x) \otimes w(x)w(x)^T$ for reflection groups) and sampling at unisolvent point sets. Schur complement blocks $S_{ab}^j = \langle A_a^j, (X^j)^{-1} A_b^j Y^j \rangle$ are computed via precomputed bilinear pairings $(W^{j,l})^T (X^{j,l})^{-1} V^{j,l}$, exploiting Arb's subcubic high-precision matrix multiplication. Good sample sets / orthogonal bases are chosen by a greedy pivoted-QR (approximate Fekete points, Sommariva–Vianello) on the Vandermonde matrix.

## Result
Empirical scaling: SDPA-GMP $\sim d^{10.1}$ vs the new solver $\sim d^{8.55}$ (theory predicts $d^{12}$ vs $d^9$). At $d=20$, projected speedup is $40\times$. New kissing-number records (Table 6.1, rounded down): $n=11$ at $869$, $n=12$ at $1355$, ..., $n=23$ at $122351$, improving prior bests in dims $11$–$23$. For binary sphere packing: the bound (formulated as a univariate matrix polynomial program with Laguerre-polynomial basis) is **not convex** in radius ratio $r$; in dim 2 it beats Florian's bound for small $r$; in dim 24 it appears to converge to the conjectured optimal limiting density $\Delta + (1-\Delta)\Delta$ as $r \to 0$; generally seems to approach $\delta + \delta(1-\delta)$ where $\delta$ is the Cohn–Elkies LP bound.

## Why it matters here
Direct tooling for arena problems involving multivariate SOS over symmetric semialgebraic sets — the three-point kissing bound (P-kissing family) and Cohn–Elkies-style packing bounds (P1, binary/multi-radius variants). ClusteredLowRankSolver.jl is the production-grade replacement for SDPA-GMP that should be the default high-precision SDP backend whenever the arena problem reduces to a clustered SOS program; nonsymmetric rank-1 decomposition is essential for the $S_3$-symmetric three-point matrices $\bar Y_k^n$.

## Open questions / connections
- Can direct non-symmetric-cone interior-point methods (Skajaa–Ye, Papp–Yıldız) be extended to SDP+polynomial constraints at high precision, and how would they compare?
- Invariant minimal unisolvent sets do not always exist (Appendix B, $D_4$ example) — when can sampling be made fully orbit-respecting without losing unisolvence?
- Cohn–Elkies LP-bound saturation in dims 8 and 24 explains why the kissing table omits those dimensions; the binary packing limit $\Delta + (1-\Delta)\Delta$ suggests a sharp limit theorem analogous to [10, 8].
- Verification of new kissing bounds via interval arithmetic was not done; rigorous certification of the basis-transformed solutions is open follow-up work.

## Key terms
clustered low-rank SDP, primal-dual interior-point method, sums-of-squares, sampling vs coefficient matching, symmetry reduction, Gatermann-Parrilo, three-point bound, Bachoc-Vallentin, kissing number, Cohn-Elkies bound, binary sphere packing, ClusteredLowRankSolver.jl, SDPB, SDPA-GMP, Putinar Positivstellensatz, Hol-Scherer matrix SOS, Gegenbauer polynomials, Laguerre polynomials, approximate Fekete points, Sommariva-Vianello, unisolvent set, Arb arbitrary precision, Schur complement, nonsymmetric rank-1 decomposition

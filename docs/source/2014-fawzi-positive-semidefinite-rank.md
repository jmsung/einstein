---
type: source
kind: paper
title: Positive semidefinite rank
authors: Hamza Fawzi, J. Gouveia, P. Parrilo, Richard Z. Robinson, Rekha R. Thomas
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.4095
source_local: ../raw/2014-fawzi-positive-semidefinite-rank.pdf
topic: general-knowledge
cites:
---

# Positive semidefinite rank

**Authors:** Hamza Fawzi, J. Gouveia, P. Parrilo, Richard Z. Robinson, Rekha R. Thomas  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.4095

## One-line
A survey establishing the theory of positive semidefinite (psd) rank of nonnegative matrices — the smallest $k$ such that $M_{ij} = \langle A_i, B_j \rangle$ for $k \times k$ psd factors — and its role as the exact complexity measure for semidefinite lifts of polytopes.

## Key claim
For a polytope $P \subseteq Q$ with slack matrix $S_{P,Q}$, $\operatorname{rank}_{\text{psd}}(S_{P,Q})$ equals the smallest $k$ such that there exists an affine slice of $S^k_+$ projecting to a convex body sandwiched between $P$ and $Q$ (Theorem 3.3 / Yannakakis-style extension). Basic sandwich: $\tfrac{1}{2}(\sqrt{1+8\operatorname{rank}(M)} - 1) \le \operatorname{rank}_{\text{psd}}(M) \le \operatorname{rank}_+(M) \le \min(p,q)$.

## Method
Algebraic-geometric survey: psd factorizations $M_{ij} = \operatorname{trace}(A_i B_j)$ with $A_i, B_j \in S^k_+$, analyzed via cone duality, self-duality of $S^k_+$, and Farkas-type lemmas. Lower semicontinuity is shown by bounding factor traces and extracting convergent subsequences. Block-triangular and Kronecker structure yield rank inequalities; symmetric ("completely psd") variant connects to doubly nonnegative and completely positive cones.

## Result
Establishes: (i) psd rank is lower semicontinuous; (ii) $\operatorname{rank}_{\text{psd}}\!\begin{pmatrix}P&0\\Q&R\end{pmatrix} \ge \operatorname{rank}_{\text{psd}}(P)+\operatorname{rank}_{\text{psd}}(R)$ with equality when $Q=0$; (iii) $\operatorname{rank}_{\text{psd}}(M \circ M) \le \operatorname{rank}(M)$; (iv) for rank-3 matrices with psd rank 2, the space of factorization orbits $\mathrm{SF}(M)/GL(2)$ is connected (Prop. 7.9); (v) field dependence — $\operatorname{rank}^{\mathbb C}_{\text{psd}} \le \operatorname{rank}_{\text{psd}} \le 2\operatorname{rank}^{\mathbb C}_{\text{psd}}$, gap can be $\sqrt{2}$ asymptotically; (vi) $\operatorname{rank}_{\text{psd}}=2$ decidable by SDP.

## Why it matters here
Direct background for any arena problem framed as a lift / extended formulation question (extremal polytopes, packing LP/SDP relaxations, Lovász-theta-style stable-set bounds); supplies the slack-matrix dictionary tying combinatorial polytopes to SDP-representability. Relevant for techniques wiki on `SDP-relaxation`, `LP-vs-SDP-gap`, and findings around SDP relaxations being slack vs tight on geometric problems (e.g. `sdp-relaxation-uselessness` for P1).

## Open questions / connections
- Is $\operatorname{rank}_{\text{psd}}(M) \le k$ NP-hard to decide for fixed $k \ge 3$? (Problem 9.5 — open; analogous nonneg-rank is poly-time via Moitra/AGKM.)
- Find explicit 0/1-polytopes with exponential psd rank, and find families with exponential gap between psd and nonnegative rank (Problems 9.8, 9.9 — would prove SDP $>$ LP for combinatorial optimization).
- Is $\mathrm{CP}^n_{\text{psd}}$ (completely-psd cone) closed; is the cpsd-rank bounded by $f(n)$? (Problem 9.11.)

## Key terms
positive semidefinite rank, psd factorization, slack matrix, extended formulation, semidefinite lift, Yannakakis theorem, nonnegative rank, completely positive semidefinite, doubly nonnegative cone, spectrahedron, square root rank, cone factorization, convex algebraic geometry

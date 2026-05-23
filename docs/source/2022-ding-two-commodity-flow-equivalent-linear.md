---
type: source
kind: paper
title: Two-Commodity Flow is Equivalent to Linear Programming under Nearly-Linear Time Reductions
authors: M. Ding, Rasmus Kyng, Peng Zhang
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2201.11587
source_local: ../raw/2022-ding-two-commodity-flow-equivalent-linear.pdf
topic: general-knowledge
cites:
---

# Two-Commodity Flow is Equivalent to Linear Programming under Nearly-Linear Time Reductions

**Authors:** M. Ding, Rasmus Kyng, Peng Zhang  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2201.11587

## One-line
Any polynomially-bounded integer linear program can be encoded as a directed 2-commodity max-flow instance in nearly-linear time with only polylog blow-up, proving 2CF and LP are equivalent under nearly-linear-time reductions.

## Key claim
For any polynomially-bounded LP $\max\{c^\top x : Ax \le b, x \ge 0\}$ with $N$ nonzeros, integer entries in $[-X,X]$, and feasible-polytope radius $R$, there is an $\tilde O(N \log X)$-time reduction to a 2CF instance with $O(N \log X)$ edges, polynomially-bounded integer capacities, and additive-error blow-up only $\mathrm{poly}(N)$ — so any $\tilde O(|E|^a)$ high-accuracy 2CF solver yields an $\tilde O(N^a)$ high-accuracy LP solver.

## Method
Refines Itai's 1978 polynomial-time LP→2CF reduction into a chain LP → LEN → 2-LEN → 1-LEN → FHF → FPHF → SFF → 2CFF → 2CFR → 2CF, with new gadgets that (a) shrink the edge-count blow-up from $\Theta(N^2 \log^2 X)$ to $O(N \log X)$, (b) keep capacities polynomially bounded by exploiting the polytope-radius bound, and (c) carry an additive-error analysis through every step so accumulated error is only polynomial. A simplifying "fixed flow network" abstraction (edges with equal lower/upper capacity) replaces Itai's general $(l,u)$-networks.

## Result
Theorem 5.1: the chain produces a 2CF instance with $|V^{2cf}|, |E^{2cf}| \le 10^6 \cdot \mathrm{nnz}(A)(3+\log X)$, capacities $\le 10^8 \cdot \mathrm{nnz}^3(A) R X^2 (2+\log X)^2$, and error tolerance $\varepsilon_{2cf} \ge \varepsilon_{lp} / (1024\, \mathrm{nnz}^7(A) R X^3 (3+\log X)^6)$. Exact-feasibility is preserved both directions; approximate 2CF solutions map back to approximate LP solutions in linear time. Open: whether the equivalence holds in strongly polynomial time, and whether dense LPs reduce to dense 2CF instances.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems route through LP/SDP/IPM solvers (HiGHS LP, SDP flag algebra) where this paper's framing — that LP solvers are no faster than 2CF solvers up to polylog factors — sets a *lower-bound floor* on hopes of replacing LP with cheaper specialized flow solvers for arena-style relaxations.

## Open questions / connections
- Strongly polynomial equivalence of 2CF and LP remains open — would tighten the hardness story.
- Density-preserving reduction (dense LP → dense 2CF with $O(n)$ edges, $O(m)$ vertices) is open.
- Extends the Kyng–Zhang [KZ20] line ruling out IPM+special-solver speedups for multi-commodity flow; complements [KWZ20] hardness for packing/covering LPs.
- Connects to the Cohen–Lee–Song [CLS21] LP-in-matmul-time frontier as the upper-bound counterpart.

## Key terms
2-commodity flow, linear programming, nearly-linear-time reduction, Itai reduction, interior point method, fixed flow network, multi-commodity flow, fine-grained complexity, Renegar condition number, polytope radius, edge capacity gadget, Cohen-Lee-Song

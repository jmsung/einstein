---
type: source
kind: paper
title: Intrinsic Sparsity of Kantorovich solutions
authors: Bamdad Hosseini, S. Steinerberger
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.03213
source_local: ../raw/2022-hosseini-intrinsic-sparsity-kantorovich-solutions.pdf
topic: general-knowledge
cites:
---

# Intrinsic Sparsity of Kantorovich solutions

**Authors:** Bamdad Hosseini, S. Steinerberger  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.03213

## One-line
Shows that when transporting between two uniform discrete measures of different cardinalities $m \neq n$, there always exists a Kantorovich-optimal coupling that is sparse: each source point splits to at most $n/\gcd(m,n)$ targets and each target receives from at most $m/\gcd(m,n)$ sources.

## Key claim
For $\mu = (1/m)\sum_{i=1}^m \delta_{x_i}$ and $\nu = (1/n)\sum_{i=1}^n \delta_{y_i}$, there is an optimal Kantorovich plan in which the support degree at each $x_i$ is $\leq n/\gcd(m,n)$ and at each $y_j$ is $\leq m/\gcd(m,n)$. The bound is independent of the cost $c(x,y)$.

## Method
Reduction to Birkhoff/König/von Neumann: duplicate each $x_i$ into $n/\gcd(m,n)$ identical copies and each $y_j$ into $m/\gcd(m,n)$ copies, so both sides become uniform measures on $mn/\gcd(m,n)$ points. Apply the classical bijection result (extremal points of bistochastic polytope = permutation matrices) to get a bijective optimal transport on the lifted sets, then project back to obtain the sparsity bound. Extends to rationally-weighted Dirac measures via $\mathrm{lcm}$ of denominators.

## Result
**Theorem:** an optimal plan exists with per-point sparsity $n/\gcd(m,n)$ (rows) and $m/\gcd(m,n)$ (columns). **Corollary** for rationally weighted measures with denominator-lcms $B, D$: bounds become $D/\gcd(B,D)$ and $B/\gcd(B,D)$, though these can exceed $n, m$ trivially when denominators are coprime. Example: $m=20, n=30$ gives at most 3 targets per source, 2 sources per target.

## Why it matters here
General background; no direct arena tie. Relevant if any arena problem reduces to discrete optimal transport / assignment LP — the sparsity guarantee bounds the support of extremal LP solutions, which can shrink search spaces for combinatorial optimizers (e.g., reformulating discrete-geometry packing as transport).

## Open questions / connections
- Does sparsity extend to non-uniform real-weighted measures (irrational weights) via limits, and with what quantitative degradation?
- Can this be combined with structured cost functions (e.g., $c(x,y)=\|x-y\|^p$) to yield better-than-generic sparsity?
- Relation to entropic-regularized OT (Sinkhorn) — does the sparse extremal plan survive small-$\varepsilon$ regularization?

## Key terms
Kantorovich problem, Monge problem, optimal transport, Birkhoff theorem, bistochastic matrices, permutation matrices, discrete measures, sparse coupling, linear programming, extremal points, assignment problem, Steinerberger

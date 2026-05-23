---
type: source
kind: paper
title: Faster High Accuracy Multi-Commodity Flow from Single-Commodity Techniques
authors: Jan van den Brand, Daniel Zhang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2304.12992
source_local: ../raw/2023-brand-faster-high-accuracy-multi-commodity.pdf
topic: general-knowledge
cites:
---

# Faster High Accuracy Multi-Commodity Flow from Single-Commodity Techniques

**Authors:** Jan van den Brand, Daniel Zhang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2304.12992

## One-line
First high-accuracy multi-commodity flow algorithm faster than general LP solvers by importing single-commodity graph techniques (expander decomposition) into the IPM machinery.

## Key claim
2-commodity flow on $n$-vertex, $m$-edge graphs solved in $\tilde O(\sqrt{m}\,n^{\omega-1/2})$ time (currently $\omega \approx 2.373$), and $k$-commodity flow in $\tilde O(k^{2.5}\sqrt{m}\,n^{\omega-1/2})$, beating previous bests $\tilde O((km)^\omega)$ [CLS21] and $\tilde O(k^{2.5}\sqrt{m}\,n^2)$ [KV96] on non-sparse graphs.

## Method
Robust interior point method with $\sqrt{km}$ iterations (log-barrier-style), combined with two graph-aware ingredients: (1) inverse/projection maintenance applied to the *reduced* $kn \times kn$ system $M^\top M x = b$ where $M$ is a "$k$-commodity incidence matrix" (Def 1.3), exploiting the sparse per-iteration change of the LP and the capacity-constraint block structure used earlier by [KV96]; (2) a "heavy hitter" data structure for $Ah$ on multi-commodity incidence matrices, reduced to the classical edge-vertex incidence heavy hitter of [BLN+20] which uses dynamic expander decomposition [SW19, HKGW22].

## Result
Theorem 1.1 (max-throughput) and Theorem 1.2 (min-cost) give deterministic $\tilde O(k^{2.5}\sqrt{m}(n^{\omega-1/2} + n^{\omega(1,1,\mu)-\mu/2} + n^{1+\mu} + n\log(U/\epsilon)))$ runtime, with additive demand error $\|B^\top f_i - d_i\|_1 \le \epsilon$. Conceptually: multi-commodity flow is "more combinatorial" than the [Ita78, DKZ22, KZ20] sparse-graph hardness reductions suggested — those impossibility results only constrain sparse instances. Heavy hitter on multi-commodity incidence matrices is shown strictly easier than on general sparse matrices (no near-linear time consequence for general LP follows).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are multi-commodity flow LPs, but the IPM + inverse-maintenance + expander-decomposition stack is the modern toolkit behind fast LP/SDP solvers that *could* underlie HiGHS-class solvers used for P1 Cohn–Elkies-style LP bounds — relevant only if we ever hit RAM-bound LP/SDP instances (see [compute-router](../wiki/techniques/compute-router.md) for that regime).

## Open questions / connections
- Can [DKZ22]'s LP→2-commodity-flow reduction be tightened to preserve LP "shape" ($n$ rows, $m \le n^2$ cols → $O(m)$ edges, $O(n)$ vertices)? If yes, this paper would beat state-of-the-art LP solvers when $m \le n^{1.254}$.
- Heavy-hitter on general sparse matrices with $k$ nonzeros/row in $\tilde O(km)$ total time remains open and would yield near-linear sparse LP solvers.
- Extending expander-decomposition single-commodity speedups to dense $k$-commodity instances — does the $k^{2.5}$ factor admit improvement?

## Key terms
multi-commodity flow, interior point method, expander decomposition, inverse maintenance, heavy hitter, Laplacian paradigm, k-commodity incidence matrix, projection maintenance, fast matrix multiplication, linear programming, max flow, min-cost flow

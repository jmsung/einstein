---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P13, P15]
related_techniques: [sdp-flag-algebra.md]
related_findings: []
cites: []
related_personas: [razborov.md, szemeredi.md, turan.md]
cites:
  - ../personas/razborov.md
  - ../personas/szemeredi.md
  - ../personas/turan.md
---

# Turán Density

## TL;DR

Turán's theorem states that the maximum edge density of an `H`-free graph on `n` vertices is asymptotically `1 − 1/(χ(H) − 1)` where `χ(H)` is the chromatic number of `H`. The Turán density `π(H)` is the foundational extremal-graph constant. Razborov's edge-triangle density curve (P13) is the explicit version for `H = K_3`; the kinks at `e = 1 − 1/k` are exactly the Turán density transitions.

## What it is

For a graph `H`, the **Turán number** `ex(n, H) = max{ |E(G)| : G has n vertices, H ⊄ G }`. The **Turán density** is

```
π(H) = lim_{n → ∞} ex(n, H) / C(n, 2).
```

**Erdős–Stone–Simonovits theorem**: `π(H) = 1 − 1 / (χ(H) − 1)`.

For `H = K_r` (complete graph on `r` vertices), `χ(K_r) = r` so `π(K_r) = 1 − 1/(r − 1)`. The extremal graph is the **Turán graph `T_{n, r-1}`** — the balanced `(r-1)`-partite graph on `n` vertices.

For more general `H`, the asymptotic is determined by chromatic number, but **lower-order behavior** is highly non-trivial — the exact extremal structure depends on the *colour critical edges* of `H`.

The **edge-triangle density curve** (Razborov 2007, refining Bollobás 1976): for fixed edge density `e ∈ [0, 1]`, the minimum triangle density `t(e)` is piecewise:

```
t(e) = (k − 2)/k · (k(e − 1) + 1)·(...)   for e ∈ [1 − 1/k, 1 − 1/(k+1)],   k = 2, 3, ...
```

with kinks at `e = 1 − 1/k`. At each kink the extremal graph transitions from `(k−1)`-partite-with-extras to `k`-partite-with-extras.

## When it applies

- **Extremal graph theory** problems where the question is "max density of `G` while avoiding/bounding subgraph `H`" — Turán's theorem and its descendants.
- **Density curves** parameterized by edge density `e`: the kinks at `1 − 1/k` are universal for `K_r`-density problems.
- **Computer-assisted Turán bounds**: flag-algebra SDPs (see [flag-algebra](flag-algebra.md)) yield numerical Turán-density bounds that match the asymptotic in special cases.

## Why it works

Two structural reasons:

1. **Chromatic number determines density asymptotically**. If `χ(H) = r`, the complete `(r−1)`-partite graph contains no `H` but has edge density `1 − 1/(r − 1)`. So `π(H) ≥ 1 − 1/(r−1)`. Erdős–Stone shows this is also the upper bound. The chromatic number is the only `H`-statistic that matters at first order.
2. **The piecewise structure for triangle density** comes from the iteratively-refined Turán construction: at edge density `e ∈ [1 − 1/k, 1 − 1/(k+1)]`, the extremal graph is a `k`-partite graph (so `K_{k+1}`-free) with certain inhomogeneous part sizes. The transition at `e = 1 − 1/k` is when adding one more part becomes optimal.

The kinks are the **Turán construction transitions**. They are not artifacts; they are real first-order discontinuities in the extremal-density function. This is why P13's optimization requires kink-aware techniques (boundary-snap, per-region sigmoid) — smooth optimizers cannot navigate the kinks.

## Classic examples

1. **P13 Edges vs Triangles** — minimize area of the Razborov edge-triangle envelope. The kinks at `e = 1 − 1/k` for `k = 3, ..., 19` are the Turán-graph transitions; samples must hit them exactly. JSAgent rank #1 locally (`−0.711709188`) via per-region sigmoid + boundary-snap.
2. **Turán's theorem (1941)** — `π(K_3) = 1/2` (max edges in triangle-free graph), achieved by the complete bipartite graph `K_{n/2, n/2}` (Mantel 1907 special case).
3. **Bollobás 1976** — established the exact edge-triangle density curve up to the asymptotic. Razborov 2007 refined to closed-form via flag algebras.

## Related

- Concepts: [flag-algebra](flag-algebra.md), [lp-duality](lp-duality.md), [equioscillation](equioscillation.md).
- Techniques: [sdp-flag-algebra](../techniques/sdp-flag-algebra.md).
- Findings: P13 strategy and optimizer-recipes lessons on per-region sigmoid + boundary-snap.
- Sources: Erdős–Stone (1946), Bollobás (1976), Razborov 2007 — not yet ingested into `source/papers/` (gap for future wiki-ingest).

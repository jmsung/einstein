---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P13]
related_techniques: [sdp-flag-algebra.md, bounded-lbfgs-per-region-sigmoid.md, boundary-snap-for-kinks.md]
related_findings: []
cites: []
---

# Flag Algebra (Razborov)

## TL;DR

Razborov's flag algebra (2007) is a calculus for extremal graph theory that turns asymptotic density questions into semidefinite programs. Subgraph densities form the algebra elements; positivity constraints from random sampling yield SDP feasibility conditions; the SDP dual is a *certificate* that no graph achieves a higher density. Arena P13 (edges vs triangles) is the canonical instance: minimize the area of the Razborov edge-triangle density curve plus a max-gap penalty.

## What it is

Notation: for finite graphs `H` and `G`, let `p(H; G)` be the density of `H` as an induced subgraph of `G` (probability that a random `|H|`-vertex subset induces `H`). For an infinite graphon limit `Γ`, `p(H; Γ)` is well-defined.

The **flag algebra** `A` is the formal vector space spanned by graph types (small graphs with labeled vertices) modulo a chain-rule identity. Multiplication: `(H₁ · H₂)` corresponds to drawing both `H₁` and `H₂` from disjoint vertex subsets. **Positivity**: `p(H; Γ) ≥ 0` for all `H` and the squared element `(σ − E σ)² ≥ 0` for every `σ` in `A`.

For **edge density `e` and triangle density `t`**, Razborov's main theorem (2007) gives the exact achievable region in the `(e, t)`-plane: a piecewise curve parameterized as `t(e) = (k − 1)(k − 2)·... / k³` on each scallop `[1 − 1/k, 1 − 1/(k+1)]` for `k = 2, 3, ...`. The curve has kinks at every scallop boundary `e = 1 − 1/k`.

The **arena objective** for P13: minimize `∫ t(e) de + 10 · max_gap` where `max_gap` measures discretization deviation from the exact Razborov envelope. The objective is a *piecewise-linear interpolation* of the envelope at sample points `(e_i, t_i)`; sample-point placement determines the area.

## When it applies

- Extremal graph theory: density problems for `H`-free graphs (Turán-type) or `H`-density-bounded graphs.
- Coloring-density questions, hypergraph density (with appropriate flag generalizations).
- **Computer-assisted proofs** of extremal bounds: Razborov's framework + SDP solvers prove tight bounds for `K_4`-free, triangle-free, etc.

For Einstein Arena, P13 is the only flag-algebra problem so far. Recognition: any objective involving "density of induced subgraph `H` in a graph of edge density `e`" falls into this family.

## Why it works

Three pillars:

1. **The chain rule** in flag algebra makes graph-density limits algebraically tractable. Densities of small graphs satisfy polynomial identities; truncating the algebra at small flag size gives a finite-dimensional projection.
2. **SDP positivity = density positivity**. The constraint `Σ c_i · σ_i ≥ 0 in A` is equivalent to a positivity-of-quadratic-forms condition that becomes a semidefinite program when truncated. Solving the SDP gives a numerical bound; rounding the dual gives a *proof*.
3. **Razborov's edge-triangle curve is exact**. Unlike most flag-algebra applications which give numerical bounds with small gaps, the edge-triangle curve is *closed-form*: `(k − 1)(k − 2) / k²` is the triangle density at edge density `e = 1 − 1/k`. Between kinks the curve is determined by `k`-partite Turán-style constructions; at kinks the construction transitions.

For P13 the "flag-algebra" content is in the *envelope formula*; the arena problem is then *interpolating the envelope by sample points*. The hard mathematical work (Razborov 2007) gives the closed form; the optimization work is sample-point placement.

## Classic examples

1. **P13 Edges vs Triangles** — minimize the area of the slope-`N` interpolation of the Razborov envelope. JSAgent rank #1 locally (`−0.711709188`) via per-region sigmoid + boundary-snap. The kinks at `e = 1 − 1/k` for `k = 3, ..., 19` require a sample point exactly on each kink — see [boundary-snap-for-kinks](../techniques/boundary-snap-for-kinks.md). Submission BLOCKED by minImprovement guard (10+ rejections).
2. **Razborov 2007** — the foundational paper introducing flag algebras. Used to prove the asymptotic edge-triangle and edge-`K_4` density curves.
3. **Razborov 2008 (followup)** — extends flag algebras to compute the minimum `K_4`-density given edge density via SDP. Numerical results closed the long-open problem in the `t = 0.5` case.

## Related

- Concepts: [turan-density](turan-density.md), [lp-duality](lp-duality.md).
- Techniques: [sdp-flag-algebra](../techniques/sdp-flag-algebra.md), [bounded-lbfgs-per-region-sigmoid](../techniques/bounded-lbfgs-per-region-sigmoid.md), [boundary-snap-for-kinks](../techniques/boundary-snap-for-kinks.md), [greedy-insert-cd-redistribute](../techniques/greedy-insert-cd-redistribute.md).
- Findings: P13 strategy and `findings/optimizer-recipes.md` lessons #31, #32, #67–#71 (per-region sigmoid, boundary-snap, slope-N interpolation).
- Sources: Razborov 2007 "Flag algebras" (foundational; not yet ingested into `source/papers/`).

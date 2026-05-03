---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P5, P15, P16]
related_techniques: [basin-hopping-multistart.md, multistart-with-rotation-lottery.md, slsqp-active-pair-polish.md]
related_findings: [basin-rigidity.md, equioscillation-escape.md, frozen-problem-triage.md, dead-end-p19-imperfect-5mark-sidon.md]
related_personas: [archimedes.md, polya.md, hadamard.md]
cites:
  - basin-rigidity.md
  - contact-graph-rigidity.md
  - provable-floor-and-frozen-problems.md
  - symmetry-and-fundamental-domain.md
  - ../source/papers/2025-novikov-alphaevolve.md
---

# Heilbronn-type extremal problems (and the over-determined active-constraint pattern)

## TL;DR

The **Heilbronn family** of arena problems (P15 triangles n=11, P16 convex regions n=14) is a class of *discrete-geometry extremal problems with affine-invariant objectives*. They share a structural feature with P5 (min-distance ratio): the optimum sits at a configuration where the **number of active constraints exceeds the degrees of freedom** — making the basin rigid via KKT counting. **Multistart and basin-hopping cannot improve a Heilbronn-type basin; the only paths to improvement are (a) finding a structurally different basin via diverse-seed search, or (b) waiting for a new published construction.** Heilbronn-type problems with n in published tables are therefore **Tier C / D for arena play** — match SOTA, take rank-2/3 if minImprovement permits, move on.

## What it is

A Heilbronn-type problem has the structure:

> Given `n` points in some affine-invariant 2D region (triangle, square, disk, convex hull), maximize the minimum-area `m`-tuple over all `m`-subsets, normalized by an affine-invariant.

Examples in the arena:

- **P15 Heilbronn Triangles, n=11**: place 11 points in unit equilateral triangle, maximize `min_{i<j<k} area(△p_i p_j p_k) / (√3/4)`.
- **P16 Heilbronn Convex, n=14**: place 14 points in plane, maximize `min(triangle area) / convex_hull_area`.
- (broader family) **Heilbronn small-n triangles**, n ∈ [3, 30]: similar formulation; classical computer-search records.

The objective is affine-invariant (rotation, scale, translation, sometimes shear), so the search space is a *quotient* of the configuration space by the affine group. For 2D, `dim(quotient) = 2n − 4` (subtracting 4 affine gauge dimensions: 2 translation, 1 rotation, 1 scale). For Heilbronn convex it's `2n − 6` (also subtracting affine shear).

## When it applies

Recognize a Heilbronn-type problem by:

1. **Affine-invariant ratio** in the objective.
2. **Min-of-many-triples (or min-of-pairs)** as the inner extremal.
3. **Optimum at over-determined active-constraint configuration**: the number of equality-active constraints exceeds the DOF after gauge quotient.

The third feature is the *key signal* that you're dealing with a Heilbronn-family rigid basin.

For arena problems, this includes P15 and P16 directly. For other 2D discrete-geometry extremals (Erdős-Szekeres-style problems, small-n distance-ratio problems), the same machinery applies.

## Why the optimum is rigid

The KKT structure: for the optimum `x*` at active set `I(x*) = {(i,j,k) : area(△p_i p_j p_k) = m*}`, the Lagrangian system with multipliers `λ_t ≥ 0` for each active triple gives:

```
∇L = ∇(m) + Σ_{t ∈ I} λ_t · ∇(area_t − m) = 0
```

If `|I| ≥ DOF` (after affine gauges), the system is over-determined: the multipliers are uniquely determined (modulo positivity) and **no infinitesimal motion improves `m` while keeping all active constraints satisfied**.

For P15 (n=11):

- `dim(config) = 22` (11 points × 2 coords).
- `dim(affine quotient) = 22 − 4 = 18` (3-point gauge fix).
- Empirical active count: **20 active triples** at AlphaEvolve §6.48's basin.
- `|I| − DOF = 20 − 18 = 2` over-determined.
- Reduced Hessian has 2 zero eigenvalues — *rigid*.

For P16 (n=14, convex):

- `dim(config) = 28`.
- `dim(affine quotient) = 28 − 6 = 22` (additional shear gauge).
- Empirical active count: 20 active (capybara's basin) or 21 (alternate sub-basin).
- `|I| − DOF = 20 − 22 = −2` (slightly under-determined!) for the 20-active basin; capybara's basin has 2 free directions, but the score difference between configurations along these directions is below `minImprovement` precision.

Two distinct outcomes:

- **Over-determined (P15)** → rigid basin, single configuration up to gauge, multistart finds nothing.
- **Slightly under-determined (P16, capybara)** → continuous family of configurations, minimum-distinguishability set by `minImprovement`. Practical effect: also frozen, but for arithmetical rather than geometric reasons.

## Why this matters for arena play

Heilbronn-type problems with n in published tables (Yang's table for triangles; AlphaEvolve §6.48 for n=11; Goldberg's for convex regions) are typically at the constructive optimum. The arena's role is then:

1. **Match SOTA** — get the published configuration via warm-start, polish to float64 ceiling, submit.
2. **Don't pursue rank #1** unless you have a NEW construction. Multistart from random init produces worse-than-published basins; multistart from SOTA produces the same basin (rigid, no escape).
3. **Use the rigidity proof itself as a deliverable**: the over-determined KKT analysis is publishable, even if the score isn't.

This explains the inventory's Tier-C classification of P15 and the Tier-A classification of P16 (P16 has a sub-basin at 21-active triples, distinct from capybara's 20-active — that's the +9e-9 rank-2 grab JSAgent achieved).

## Classic examples

| Problem | n | DOF | Active | Status | JSAgent rank |
|---|---|---|---|---|---|
| P15 Heilbronn triangles | 11 | 18 | 20 (over-determined) | rigid; AlphaEvolve §6.48 | not submitted (rank #5 = 0 pts) |
| P16 Heilbronn convex (capybara) | 14 | 22 | 20 (under-determined by 2) | basin family; minImprovement-locked | rank #2 (alt 21-active basin) |
| P5 min-distance ratio (D. Cantrell) | 16 | 28 | 30 (over-determined by 2) | rigid; (22, 8) Cantrell config | rank #4 (proven global, frozen) |

All three are Tier C/B/A in the inventory because the optima are mathematical certainties (proven or empirically verified across 1000s of multistart trials).

## How the agent should approach a Heilbronn-type problem

When the council dispatches with category `discrete_geometry_extremal` or affine-invariant 2D ratio:

1. **First action**: count active constraints versus DOF after affine gauge. If `|I| ≥ DOF`, the basin is rigid. Don't run optimizers; document.
2. **If `|I| < DOF`**: there's a free family. Look for a *different* basin (different active set) via multi-seed BH from averaged leader solutions — this is the P16 rank-2 grab pattern.
3. **Polish to float64 ceiling**: SLSQP active-pair polish at wide tolerance + mpmath at 60-80 dps for verification.
4. **Submit if minImprovement allows AND rank #2/#3 is achievable**.
5. **Do NOT waste compute on multistart from random init**: random initial configurations are far from the SOTA basin and converge to worse local optima.

This protocol follows the [`provable-floor-and-frozen-problems.md`](provable-floor-and-frozen-problems.md) framework specialized to the affine-invariant 2D family.

## Limits

- Doesn't generalize to **higher-dimensional** discrete-geometry extremals directly. For 3D analogs (e.g., minimum tetrahedron volume of n points in unit cube), the active-constraint counting changes: tuples are quadruples not triples, and DOF scales as `3n − {gauges}`.
- Doesn't apply to **kissing-number** problems — those have a different rigidity mechanism (first-order link-tangent test, see `techniques/first-order-link-tangent-test.md`).
- The "minimum distance ratio" family (P5) is a *boundary case* — the minimum is over pairs (not triples), and the active-constraint structure differs in detail. P5 is Heilbronn-adjacent, not strictly Heilbronn.

## Related

- [`concepts/basin-rigidity.md`](basin-rigidity.md) — broader concept; over-determined active-constraint case is one specialization
- [`concepts/contact-graph-rigidity.md`](contact-graph-rigidity.md) — analogous for sphere-packing
- [`concepts/provable-floor-and-frozen-problems.md`](provable-floor-and-frozen-problems.md) — when to declare a problem frozen
- [`concepts/symmetry-and-fundamental-domain.md`](symmetry-and-fundamental-domain.md) — affine quotient construction
- [`findings/basin-rigidity.md`](../findings/basin-rigidity.md) — empirical lessons (Lessons #29, #84, #85, #88, #96)
- [`findings/equioscillation-active-triple-diagnostic`](../findings/equioscillation-escape.md) (sister finding)
- [`source/papers/2025-novikov-alphaevolve.md`](../../source/papers/2025-novikov-alphaevolve.md) — AlphaEvolve §6.48 figure, P15 SOTA construction

*Last updated: 2026-05-02*

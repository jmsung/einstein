---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P5, P6, P11, P14, P15, P16]
related_techniques: [slsqp-active-pair-polish.md, mpmath-ulp-polish.md, basin-hopping-multistart.md]
related_findings: [basin-rigidity.md, float64-ceiling.md, equioscillation-escape.md]
cites:
  - ../findings/basin-rigidity.md
  - ../findings/float64-ceiling.md
---

# Basin Rigidity

## TL;DR

A constrained optimum is **rigid** when active constraints over-determine the variables: `|active| ≥ DOF` (with proper symmetry-gauge accounting), so the reduced Hessian has no zero eigenvalues and no infinitesimal motion improves the objective while staying feasible. Rigidity is provable in seconds with constraint counting + a KKT solve; once proven, no local method will ever improve the score.

## What it is

For a constrained optimization

```
minimize f(x)   subject to   g_i(x) ≤ 0,  h_j(x) = 0,
```

let the active set at a candidate `x*` be `I(x*) = {i : g_i(x*) = 0}`, and let `DOF = dim(x) − |gauges| − |h|` be the effective degrees of freedom after symmetry quotients (rotation, translation, scale; affine gauges; Möbius). The candidate is **rigid** if

```
|I(x*)| + |h| ≥ DOF,
```

with the additional analytic condition that the **reduced Hessian** of the Lagrangian on the active manifold has no zero eigenvalues — i.e. the system is genuinely over-determined, not coincidentally tight.

Equivalent formulations:

- **First-order LP test** (Sierpinski / KKT): solve `min δ s.t. ∇g_i(x*)·δ ≤ 0 for all i ∈ I, ∇f(x*)·δ < 0`. If infeasible (returns `δ_min = 0`), no first-order descent exists.
- **mpmath KKT solve** (P18 lesson #88): with `|I| = DOF`, solve the active-constraint system at high precision. Solution is unique; no nearby alternative.
- **Reduced Hessian** (P5 lesson #85): project the Lagrangian Hessian onto the tangent of the active manifold. Zero eigenvalues mean a zero-cost direction exists; positive definiteness means rigid.

## When it applies

Constrained geometric problems and over-determined extremal problems:

- Sphere/disk packings (active = touching pairs; DOF = positions modulo rigid motion).
- Heilbronn-type max-min problems (active = minimum-area triplets).
- Tammes/kissing-type max-min angle problems (active = nearest-neighbor edges).
- Equioscillation minimax (active = extremal points; see [equioscillation](equioscillation.md)).

Diagnostic tells:

- All top agents converge to the same configuration up to rigid motion + ulps.
- Multistart with > 1000 trials produces zero alternatives strictly above the candidate score.
- Remove-and-readd / 1-swap / micro-perturbation produces no improvement after exhaustive sampling.

## Why it works

A candidate at the boundary of the feasible polytope locally looks like the vertex of a polyhedral cone. With `|active| = DOF`, the cone is a single point — there is no infinitesimal direction that respects all constraints; the only "moves" available leave the active manifold (worsen the objective). With `|active| > DOF`, the system is **over**-determined: even non-strict relaxations of one constraint leave fewer than `DOF` directions, and second-order reduced Hessian rules them out as ascent.

This is the analytical strengthening of "44K multistart found nothing": rigidity is an a-priori proof, not an empirical absence. P5's `30 active − 28 DOF = +2` over-determination is **stronger** than 44 018 multistart trials returning the same basin (lesson #84): the count is constant-time, the search was 205 seconds.

The practical inversion: **count active constraints vs DOF before launching multistart**. If the count is over-determined, multistart is wasted compute — pivot to a different basin (cold start with structurally different initialization) or accept the ceiling.

## Classic examples

1. **P5 Min Distance Ratio (n=16)** — (22, 8) configuration: 22 min-edge equality + 8 max-edge equality = 30 active on 28 DOF (32 coords − 4 affine gauges). Over-constrained by 2. Reduced Hessian has no zero eigenvalues. 44 018 random multistart returned 11 distinct basins, **none below 12.889228** — the global optimum is provably the (22,8) Cantrell configuration. See [findings/basin-rigidity.md](../findings/basin-rigidity.md) lessons #84, #85.
2. **P11 Tammes (n=50)** — `|I| = 95+` near-contact pairs at `tol = 1e-3` for ~50 vectors with 3 DOF each (after rotation gauge): basin float64-ceiling. Wide active-pair tolerance (1e-3) is required because 1e-7 tolerance misses 95+ near-contact pairs and stalls below the ceiling. Technique: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md).
3. **P15 Heilbronn Triangles (n=11)** — 17 active triples on 8 effective DOF after D1 symmetry. SierpinskiAgent2083's first-order LP returned `δ_min = 0`; CHRONOS's KKT obstruction theorem classifies it as a rigid local max. mpmath 60-digit Newton confirms the basin's true-math ceiling is `+6.245e-17` above the float64 score — `1.6 × 10⁸` times below `minImprovement`.

## Related

- Concepts: [contact-graph-rigidity](contact-graph-rigidity.md), [equioscillation](equioscillation.md), [float64-ceiling](float64-ceiling.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [symmetry-and-fundamental-domain](symmetry-and-fundamental-domain.md).
- Techniques: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md), [basin-hopping-multistart](../techniques/basin-hopping-multistart.md).
- Findings: [basin-rigidity](../findings/basin-rigidity.md), [float64-ceiling](../findings/float64-ceiling.md), [equioscillation-escape](../findings/equioscillation-escape.md).

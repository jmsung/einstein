---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P13, P15, P16]
related_techniques: [boundary-snap-for-kinks.md, bounded-lbfgs-per-region-sigmoid.md, greedy-insert-cd-redistribute.md]
related_findings: [equioscillation-escape.md]
related_personas: [razborov.md, turan.md, riemann.md]
cites:
  - flag-algebra.md
  - turan-density.md
  - parameterization-selection.md
  - equioscillation.md
---

# Piecewise-linear interpolation with kink singularities

## TL;DR

Many extremal-graph and density-curve problems (P13 edges-triangles is the canonical instance) optimize over **continuous piecewise-linear curves on a discrete index set** — where the curve must pass through specified `(x_i, y_i)` knot points and the *kinks* (slope discontinuities at each `x_i`) are the actual decision variables. Standard smooth optimizers (L-BFGS, gradient methods) fail at kinks because the gradient is undefined there; the optimum *sits exactly at the kinks*. Two techniques handle this — boundary-snap and per-region sigmoid — and together they reveal a general principle: **when the optimum is structurally at non-smooth singularities, the optimizer must be told about the kinks explicitly, not asked to find them via smoothing.**

## What it is

Formal setup: optimize over functions `g : [a, b] → ℝ` of the form

```
g(x) = y_i + (y_{i+1} - y_i) · (x - x_i) / (x_{i+1} - x_i)   for x ∈ [x_i, x_{i+1}]
```

i.e., piecewise-linear with knots `(x_1, y_1), ..., (x_N, y_N)` at *fixed* `x_i` (the discrete index) and *variable* `y_i`. The decision is the vector `y ∈ ℝ^N`. The objective `F(y)` typically combines:

- A smooth integral term `∫ f(g(x)) dx`
- A non-smooth maximum term `max_i (y_{i+1} - y_i)` (gap penalty) or `max_i |y_i - y*_i|` (envelope penalty)

The optimum almost always has many `y_i = y*_i` (active constraints) creating *kinks*. The smooth integral pulls the curve into smooth regions; the non-smooth max forces it to touch specific knots; the optimum is where these forces balance — at a configuration with O(N) active kinks.

## When it applies

- **P13 Edges vs Triangles** (Razborov flag-algebra) — the edge/triangle density curve is piecewise-linear in the rational density values; kinks are at the *integer-index transitions* of Razborov's chunk decomposition. The arena objective is `area + 10·max_gap`, which combines smooth and non-smooth terms.
- **P15 Heilbronn Triangles** — the active-triple structure (20 active out of all triples for n=11) creates kinks in the dual Lagrangian.
- **P16 Heilbronn Convex** — same story; 20 vs 21 active triples = different basin = different kink pattern.
- **General extremal-graph density problems** — anywhere flag algebra produces a piecewise-linear lower-bound curve.

The signal that you're in this regime:

- Objective written as `area + λ · max_gap` or similar smooth + max combination.
- Optimum has O(N) "active" knots (constraints satisfied with equality).
- L-BFGS / Adam from random init produces a smooth result that's strictly worse than a known kink-saturated solution.

## Why it's hard for standard optimizers

Smooth optimizers assume `∇F` exists everywhere. At a kink, `∇F` is undefined (left and right derivatives differ); the optimizer either (a) reports `nan`, (b) bounces between subgradients, (c) settles into a smooth interior result that's strictly worse.

Three failure modes you'll see in tracking logs:

1. **L-BFGS convergence to smooth interior**: optimizer reports converged at a `y` with no active kinks; score is 5-30% worse than known kink-saturated solution.
2. **Adam oscillation around a kink**: at a kink, the gradient flips sign across the discontinuity; Adam's exponential moving averages produce an oscillating step that never settles.
3. **CMA-ES gets the right basin but wrong precision**: population search finds the kink-active region but float64 polish to the kink can't be done by population-mean updates.

## How the two P13 techniques solve it

**[boundary-snap-for-kinks](../techniques/boundary-snap-for-kinks.md)** — explicitly snap each `y_i` to its kink value when the optimizer's continuous step crosses it. Like a "discrete barrier method": after each L-BFGS step, project each variable onto its nearest kink and re-evaluate. If the snap improves the objective, accept; else reject the snap and continue. Works because the kink is *known a priori* (it's an active constraint at a knot).

**[bounded-lbfgs-per-region-sigmoid](../techniques/bounded-lbfgs-per-region-sigmoid.md)** — re-parameterize each `y_i` as `y_i = a_i + (b_i - a_i) · σ(z_i)` where `σ` is a steep sigmoid and `(a_i, b_i)` is the kink-pair. The original variable `y_i` is now a smooth function of the auxiliary `z_i ∈ ℝ`; the kink at `y_i = a_i` (or `b_i`) becomes an asymptote in `z_i`. L-BFGS works smoothly on `z`; after convergence, the kinks are *implicitly* saturated by `σ(z_i) → 0` or `1`.

The two techniques are *equivalent in optimum* but differ in convergence dynamics. Boundary-snap is faster when the kink structure is known; per-region sigmoid is more robust when you don't know which kinks will be active. P13 used both: per-region sigmoid for the global structure, then boundary-snap for the final ulp polish.

## Connection to parameterization-selection

This is a specific instance of the broader [parameterization-selection](parameterization-selection.md) principle. The choice of *parameterization* (raw `y` vs sigmoid-of-`z`) determines whether the optimization landscape is smooth or has kinks. The same lesson:

- Stuck on a piecewise-linear problem with smooth optimizers → reach for the per-region sigmoid first.
- Once the basin is found, boundary-snap is the precision polisher.
- The kinks are a *feature* of the math, not a numerical defect; the parameterization should respect them.

## Classic examples

1. **P13 Edges vs Triangles** (2026-04-09): the breakthrough that took us from #7 to #1-local was the per-region sigmoid + boundary-snap chain. Per-region sigmoid found the deeper basin (multi-seed BH on seed 11); boundary-snap polished to the kink configuration; total improvement +1.4e-7. Three other techniques (BIPOP-CMA-ES, Snell refraction, cusp-crossing) failed to find this basin.
2. **P15 Heilbronn Triangles** (2026-04-15): 20-active-triple basin is a kink configuration; KKT solve at the kinks proves the basin is rigid (excess of 2 over DOF).
3. **P16 Heilbronn Convex** (2026-04-09): 21-active-triple sub-basin discovered via multistart from averaged leader solutions — a *different* kink configuration than capybara's 20-active. Both basin types coexist; the agent's best play is the rank-2 grab (~9e-9 above tied group, requires kink-saturated atom).

## Limits

- **Requires knowing the kink structure** — boundary-snap needs the `(a_i, b_i)` pairs; per-region sigmoid needs the partition. Neither generalizes to problems where the kinks are *emergent* (e.g., free-boundary problems).
- **Float64 precision matters** — the kink is a *discrete* event in continuous space; polished kink values must be float64-exact for the verifier to accept the active-constraint count.
- **Concept doesn't apply to fully-smooth problems** — autocorrelation family (P2/P3/P4) is fully smooth at the optimum despite having equioscillation; that's a *different* singularity (multiple isolated peaks, not kinks).

## See also

- [`techniques/boundary-snap-for-kinks.md`](../techniques/boundary-snap-for-kinks.md), [`techniques/bounded-lbfgs-per-region-sigmoid.md`](../techniques/bounded-lbfgs-per-region-sigmoid.md) — the two techniques that operationalize this concept
- [`concepts/parameterization-selection.md`](parameterization-selection.md) — broader principle this is an instance of
- [`concepts/flag-algebra.md`](flag-algebra.md), [`concepts/turan-density.md`](turan-density.md) — the math of P13 specifically
- [`personas/razborov.md`](../personas/razborov.md), [`personas/turan.md`](../personas/turan.md) — personas that reach for these concepts
- [`findings/equioscillation-escape.md`](../findings/equioscillation-escape.md) — sister concept for the *smooth* singularity case (autocorrelation family)

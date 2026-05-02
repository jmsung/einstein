---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P22, P23]
related_techniques: [first-order-link-tangent-test.md, parallel-tempering-sa.md, micro-perturbation-multiscale.md]
related_findings: [hinge-overlap-rank3-squeeze.md, sa-parallel-tempering.md, perturbation-landscape.md]
cites:
  - ../findings/hinge-overlap-rank3-squeeze.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
---

# Hinge-Overlap Loss

## TL;DR

The hinge-overlap loss `Σ_{i<j} max(0, T − ‖c_i − c_j‖)` is the canonical kissing-tight loss formulation. Its zero floor encodes a feasibility certificate (a `κ(d)`-kissing configuration exists). Its non-smoothness at active pairs creates a fractal landscape where finite-difference perturbation finds improvements gradient methods miss.

## What it is

For unit vectors `c_1, ..., c_n ∈ S^{d−1}` and threshold `T > 0`, the hinge-overlap is

```
L(c) = Σ_{i < j} max(0, T − ‖c_i − c_j‖).
```

In the kissing context, `T = 2` is the "touching" distance: two unit vectors `v, w ∈ S^{d−1}` give unit spheres at `2v, 2w` whose closest points are at distance `‖2v − 2w‖ − 2 = ‖v − w‖_{2v} − 2`. Equivalently `⟨v, w⟩ ≤ 1/2 ⇔ ‖2v − 2w‖ ≥ 2`. So `L(c) = 0` iff every pair has `‖c_i − c_j‖ ≥ T` — a valid kissing/sphere-packing configuration.

The arena's score uses centers scaled by 2: score = `Σ_{i<j} max(0, T − ‖2c_i − 2c_j‖)` over unit vectors `c`. With `T = 2` this is the hinge-overlap; the score-0 floor proves `κ(d) ≥ n`.

## When it applies

- Kissing-tight problems on `S^{d−1}`: P6 (d=11, n=594), P22 (d=12, n=841), P23 (d=16, n=4321).
- Any "minimum pairwise distance ≥ T" feasibility encoded as a smooth-from-above penalty.
- Sphere-code construction problems where the score is "how much does this configuration violate distance ≥ T."

## Why it works (and where it traps)

Three structural properties:

1. **Zero floor = mathematical certificate**. `L = 0` is achievable iff a valid `T`-distance configuration exists; it is the **provable global minimum** (cannot go lower). When a competitor reaches `L = 0`, the problem is permanently frozen for SOTA — see [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md). Endgame: download-verify-submit for tied #1 (P6 lesson #81).
2. **Non-smooth at active pairs**. The penalty term has a kink at `‖c_i − c_j‖ = T`. Gradient is zero on the inactive side, finite on the active side; the gradient is *not zero* at the optimum — it's *zero in many directions but finite in others* via the support function. This is why **finite-difference / stochastic perturbation finds improvements where Riemannian gradient descent does not** (P6 lesson #20).
3. **Smooth surrogate is a trap**. Replacing `max(0, T − d)` with `softplus(β(T − d))/β` changes the optimum at low β and flattens gradients at high β. P6 lesson #25: tested β ∈ [100, 5 000], all made score worse (0.35–1.5 vs 0.156 SOTA). **Stay on the true hinge.**

The first-order link-tangent test (see [first-order-link-tangent-test](first-order-link-tangent-test.md)) gives a closed-form check for whether the kissing-tight floor + duplicate is a strict local min: `min_u S(u) > 1`. This subsumes "polish-and-see" with a deterministic O(d²·|link|) computation.

## Classic examples

1. **P6 Kissing d=11 (n=594, T=2)** — `L = 0` floor reached by KawaiiCorgi (2026-04-10). All 176 121 pair distances ≥ 2.0 in mpmath-80. Triple-verified across float64, mpmath dps=50/80/120 (lesson #73 — "score = 0.0" is unverified at float64 alone). Endgame: tied #1 via download-verify-submit.
2. **P22 Kissing d=12 (n=841)** — leader at exact `L = 2.0` from κ(12) = 840 perfect kissing core + 1 duplicate. Rank-3 squeeze at `δ = 1e-4` along `u_best` (link-tangent direction with `S(u_best) ≈ 8.02`) lands score in `(silver, bronze)` window for +1 pt. See [findings/hinge-overlap-rank3-squeeze.md](../findings/hinge-overlap-rank3-squeeze.md) lesson #99.
3. **P23 Kissing d=16 (n=4321)** — same pattern: leader at `L = 2.0`, link is denser (|link| = 280 from BW₁₆ structure), `min S(u) ≈ 16.67`. Squeeze at `δ = 1e-7` for sole rank-2.

## Related

- Concepts: [kissing-number](kissing-number.md), [sphere-packing](sphere-packing.md), [first-order-link-tangent-test](first-order-link-tangent-test.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md), [fractal-perturbation-landscape](fractal-perturbation-landscape.md), [smooth-max-approximation](smooth-max-approximation.md).
- Techniques: [first-order-link-tangent-test](../techniques/first-order-link-tangent-test.md), [parallel-tempering-sa](../techniques/parallel-tempering-sa.md), [micro-perturbation-multiscale](../techniques/micro-perturbation-multiscale.md).
- Findings: [hinge-overlap-rank3-squeeze](../findings/hinge-overlap-rank3-squeeze.md), [sa-parallel-tempering](../findings/sa-parallel-tempering.md), [perturbation-landscape](../findings/perturbation-landscape.md), [float64-ceiling](../findings/float64-ceiling.md).
- Sources: `source/papers/2024-cohn-li-kissing.md`, `source/papers/2024-delaat-kissing-sdp.md`.

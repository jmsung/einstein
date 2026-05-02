---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P6, P22, P23]
related_techniques: [first-order-link-tangent-test.md]
related_findings: [hinge-overlap-rank3-squeeze.md]
cites:
  - ../findings/hinge-overlap-rank3-squeeze.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
---

# First-Order Link-Tangent Test (Concept)

## TL;DR

For a hinge-overlap objective `Σ max(0, T − ‖2v − 2v_i‖)` evaluated at a duplicate of a kissing-tight vector `v_0`, the first-order rate of change in the perturbation direction `u ∈ T_{v_0} S^{d−1}` is `2δ · (S(u) − 1)` where `S(u) = Σ_{i ∈ link(v_0)} [⟨u, w_i⟩]_+` over link projections `w_i`. The duplicate is a **strict local minimum** iff `min_u S(u) > 1`. This is the analog of "compute the gradient and check it's zero" for a non-smooth, kink-rich objective.

This page is the **mathematical statement**; the corresponding [technique](../techniques/first-order-link-tangent-test.md) is the procedure for computing it.

## What it is

Setup (kissing-tight hinge-overlap):

- Cutoff `T` (typically `T = 2`); `γ_* = 1 − T²/8` is the touching threshold (`γ_* = 1/2` for `T = 2`).
- `v_0 ∈ S^{d−1}` and a kissing-saturated core `{v_i}` with `⟨v_0, v_i⟩ ∈ [γ_*, 1]`.
- The **link** of `v_0`: `link(v_0) = {v_i : ⟨v_0, v_i⟩ = γ_*}` — vectors at exact touching distance.
- For each `v_i ∈ link(v_0)`, the **link projection**: `w_i = (v_i − γ_* v_0) / ‖v_i − γ_* v_0‖`. These are unit vectors in `T_{v_0} S^{d−1}`.

Perturbation along a unit tangent `u`: `v(δ) = cos(δ) v_0 + sin(δ) u`. The first-order penalty rate is

```
Δscore(δ, u) ≈ 2δ · ( Σ_{i ∈ link(v_0)} [⟨u, w_i⟩]_+  −  1 )
            = 2δ · ( S(u) − 1 ).
```

The "−1" comes from the duplicate's own contribution decreasing as `v` moves away from `v_0`. The criterion:

```
min_{u ∈ S^{d−2}} S(u) > 1   ⇒   v_0-duplicate is a strict local min;
                                   rank-#1 (score below the integer floor) infeasible at this config.
min_{u ∈ S^{d−2}} S(u) < 1   ⇒   strict improvement direction exists; descend along −u_best.
```

## When it applies

- Score has the form `Σ_{i<j} max(0, T − ‖c_i − c_j‖)` with hinge cutoff `T`.
- The leader's score is exactly the small integer floor implied by `n − κ(d)` duplicates of `κ(d)` perfect kissing vectors (P22 d=12: leader at 2.0 for n = 841 = 840 + 1; P23 d=16: leader at 2.0 for n = 4321 = 4320 + 1).
- You are about to invest GPU compute on "find a strict improvement"; this O(d²·|link|) test answers in seconds whether such an improvement can exist at first order.

## Why it works

Geometrically, `S(u)` measures the cumulative *first-order penalty* from link members as `v` moves into the tangent space. The duplicate's own contribution is `−1` (its hinge term decreases as `v` separates from `v_0`). Net rate: `S(u) − 1`. If every direction `u` has `S(u) > 1`, every escape direction makes the score worse.

`S(u)` is **convex on each orthant** of `(⟨u, w_1⟩, ..., ⟨u, w_m⟩)` sign patterns — the positive part is piecewise linear. Optimization over the unit tangent sphere of `T_{v_0}` is a `(d−1)`-dimensional problem solvable by L-BFGS in well under a minute even for d = 16, |link| = 280.

The criterion is **first-order**. Companion check at non-link members: vectors `v_j` with `⟨v_0, v_j⟩ < γ_*` contribute `0` at first order but `O(δ²)` at second order. For very small `δ` they may flip the sign. P22's link contribution dominated by 10:1 so first-order was decisive; for sparser links a δ-sweep at multiple scales is required.

This statement subsumes empirical "polish from SOTA and see if you escape" because it gives the answer in a closed-form O(d²·|link|) test rather than an optimizer-tuning lottery. Run before committing GPU compute on any kissing-tight problem.

## Classic examples

1. **P22 Kissing d=12 (n=841)** — `min S(u) ≈ 8.02` (8× the threshold of 1). Strict first-order local min; rank-#1 infeasible at this duplicate position. Confirms the 8-way structural cap on κ(12) ≤ 840 from CHRONOS arena thread 198. Pivot to rank-3 squeeze (`δ = 1e-4`, `cos(δ)v_0 + sin(δ)u_best` lands in the silver–bronze gap). See [findings/hinge-overlap-rank3-squeeze.md](../findings/hinge-overlap-rank3-squeeze.md) lesson #100.
2. **P23 Kissing d=16 (n=4321)** — `|link| = 280` neighbors at exact 60° to `v_0` (Barnes-Wall lattice neighbor density). `min S(u) ≈ 16.67` (14× threshold). Even more rigid than P22 because the link is denser. Rank-2 squeeze with `δ = 1e-7` produced score `2.0000026872584407` for sole rank-2.
3. **P6 Kissing d=11 (n=594)** — at the conquered score-0 configuration the link analysis is trivially tight (no duplicate to perturb). The 8-way structural argument from P22/P23 generalizes: kissing-tight configurations whose link contribution exceeds 1 in every tangent direction are first-order rigid.

## Related

- Concepts: [kissing-number](kissing-number.md), [hinge-overlap](hinge-overlap.md), [contact-graph-rigidity](contact-graph-rigidity.md), [sphere-packing](sphere-packing.md).
- Techniques: [first-order-link-tangent-test](../techniques/first-order-link-tangent-test.md) (procedure / code).
- Findings: [hinge-overlap-rank3-squeeze](../findings/hinge-overlap-rank3-squeeze.md) (#99, #100), [p22-d12-construction-survey](../findings/p22-d12-construction-survey.md).
- Sources: `source/papers/2024-cohn-li-kissing.md`, `source/papers/2024-delaat-kissing-sdp.md`.

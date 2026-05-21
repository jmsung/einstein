---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P22, P23, P6]
compute_profile: [local-cpu]
cost_estimate: "minutes"
hit_rate: "TBD"
---

# First-Order Link-Tangent Test

## TL;DR

For kissing-tight hinge-overlap problems, parameterize a perturbation of the duplicated vector along a unit tangent of the sphere, sum the positive part of inner products with link projections, and check whether the minimum exceeds 1. If `min S(u) > 1`, the duplicate position is a strict first-order local minimum and rank-#1 (score below the integer floor) is infeasible at that configuration. Decisive in seconds; replaces hours of GPU-tuning roulette.

## When to apply

- Score has the form `Σ_{i<j} max(0, T − ‖c_i − c_j‖)` with hinge cutoff `T` (P22 d=12: T=2; P23 d=16: T=2; P6 d=11: T=2).
- Leader's score is exactly the small integer floor implied by `n − κ(d)` duplicates of `κ(d)` perfect kissing vectors (e.g. P22 leader at 2.0, P23 at 2.0).
- You are about to invest GPU compute on a "find a strict improvement" search; this 1-second test tells you whether such an improvement can exist at first order.

## Procedure

1. Fix the duplicate position `v_0 ∈ S^{d-1}` and the kissing-saturated core `{v_i}`.
2. Compute the link: `link(v_0) = { v_i : ⟨v_0, v_i⟩ = γ_* }` with `γ_* = 1 − T²/8` (γ_* = 0.5 for T=2).
3. For each `v_i ∈ link(v_0)`, compute the link projection `w_i = (v_i − γ_* v_0) / ‖v_i − γ_* v_0‖`.
4. Define `S(u) = Σ_{i ∈ link(v_0)} [⟨u, w_i⟩]_+` over unit tangents `u ∈ T_{v_0} S^{d-1}` (a `(d−1)`-dim sphere).
5. Minimize `S(u)` via L-BFGS or projected gradient on the tangent unit sphere. Convex on each orthant; cheap.
6. Decision:
   - `min S(u) > 1` → duplicate is a strict local min; rank #1 infeasible at this config.
   - `min S(u) < 1` → improvement direction exists; descend along `−sign(...)·u_best`.

```python
# Pseudocode
gamma_star = 1 - T**2 / 8                       # 0.5 for T=2
link = [v for v in core if abs(v @ v0 - gamma_star) < 1e-12]
W = np.array([(v - gamma_star * v0) / np.linalg.norm(v - gamma_star * v0) for v in link])
def S(u): return np.maximum(W @ u, 0).sum()
# minimize S(u) s.t. ||u|| = 1, u ⟂ v0  (tangent space)
```

## Pitfalls

- **Link membership is exact**: use a strict tolerance (`1e-12`) on `⟨v_0, v_i⟩ = γ_*`. Numerical sloppiness can include or exclude link members and corrupt `S`.
- **Second-order companion check**: contributions from non-link members `w_j` with `⟨v_0, v_j⟩ < γ_*` are zero at first order but quadratic in δ — for very small δ they may flip the sign. Confirmed dominant on P22 (10:1) but check explicitly when |link| is small.
- **Tangent-space gauge**: minimize over the unit sphere of `T_{v_0}` (use `u ← u − (u·v_0)v_0` then normalize). Forgetting the projection contaminates the result with radial motion.
- The criterion is **first-order**; a tight `min S(u) ≈ 1` should be re-tested with a finer δ-sweep to catch borderline cases.

## Compute profile

Local CPU. `O(d²·|link|)` per L-BFGS iteration. P22 d=12, |link|≈24 → seconds. P23 d=16, |link|=280 → still under a minute. Do not put this on Modal — sequential L-BFGS, GPU sits idle.

## References

- `wiki/findings/hinge-overlap-rank3-squeeze.md` (lesson #100 — derivation + P22/P23 results).
- `wiki/findings/p22-d12-construction-survey.md` (P12a construction, link structure of v₀).
- `mb/tracking/problem-22-kissing-d12/strategy.md` (attack-ladder step 2).
- `wiki/techniques/parallel-tempering-sa.md` (the heavier alternative this test obsoletes for kissing-tight problems).

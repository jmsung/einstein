---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P13]
compute_profile: [local-cpu]
cost_estimate: "minutes (PyTorch L-BFGS, max_iter ~50)"
hit_rate: "TBD"
---

# Bounded L-BFGS via Per-Region Sigmoid

## TL;DR

When each decision variable must stay inside a per-element fixed region `[lo_i, hi_i]` AND the score function depends on a discrete index per element (Turán scallop, sphere-packing contact-graph hinge, KKT-boundary kink), reparameterize as `x_i = lo_i + (hi_i − lo_i) · sigmoid(raw_i)` and optimize `raw_i ∈ ℝ` with PyTorch autograd + L-BFGS. Unlocked +1.4e-7 on P13 where every other local optimizer (scipy L-BFGS-B with bounds, SLSQP, BIPOP-CMA-ES) returned zero gain.

## When to apply

- Each variable has a per-element region `[lo_i, hi_i]` (different regions per i, NOT the same global box).
- The score function uses a discrete index that depends on the variable's region membership (e.g. `k_vec[i]` mapping `x_i` to its scallop in Turán density).
- Crossing the region boundary silently invalidates the score (the discrete index changes — silent constraint violation).
- scipy L-BFGS-B with `bounds=` either crosses the boundary or stalls against the ordering constraint.

## Procedure

1. **Define per-element region**: arrays `lo[i]`, `hi[i]` from the problem structure (e.g. P13 Turán scallops `[1 − 1/k, 1 − 1/(k+1)]` for k=2..n).
2. **Reparameterize**: `x_i = lo_i + (hi_i − lo_i) · sigmoid(raw_i)`. The sigmoid keeps the gradient nonzero everywhere inside the region.
3. **Optimize `raw_i` in unconstrained ℝ** via PyTorch autograd + L-BFGS:
   ```python
   raw = torch.zeros(n, requires_grad=True)
   opt = torch.optim.LBFGS([raw], max_iter=50, lr=0.1)
   def closure():
       opt.zero_grad()
       x = lo + (hi - lo) * torch.sigmoid(raw)
       loss = score(x)
       loss.backward()
       return loss
   for _ in range(20):
       opt.step(closure)
   ```
4. **Project back**: `x_final = lo + (hi − lo) · sigmoid(raw_final)`. Verify each `x_i ∈ [lo_i, hi_i]` strictly.
5. **Pair with boundary-snap** (`boundary-snap-for-kinks.md`) when kinks are present: snap, polish, snap again.

## Pitfalls

- **scipy L-BFGS-B silent boundary cross**: if the Hessian step pushes `x_i` past `hi_i`, the discrete index `k_vec[i]` changes and the score function's derivative becomes wrong. The optimizer then "improves" along a fake gradient. The sigmoid prevents this by construction.
- **Quadratic penalty is wrong**: a `λ · max(0, lo − x)²` penalty dominates the true objective at the boundary. Sigmoid is gradient-aware everywhere.
- **Hard clamping is wrong**: `x = max(lo, min(hi, x))` makes the gradient zero on the constraint, killing L-BFGS. Sigmoid keeps the gradient continuous.
- **Region must be non-overlapping**: if `[lo_i, hi_i]` and `[lo_j, hi_j]` overlap and share constraints, you need an additional ordering term — sigmoid alone doesn't enforce ordering.
- **sigmoid saturates at extremes**: very large `|raw_i|` produces tiny gradients. Re-initialize from `raw=0` and avoid ultra-aggressive learning rates.

## Compute profile

Local CPU with PyTorch. P13 n=500 Turán scallops: max_iter=50, lr=0.1, ~10 outer steps, ~30s total. GPU offers no benefit — L-BFGS is sequential.

## References

- `wiki/findings/optimizer-recipes.md` (#68 — bounded L-BFGS per-region sigmoid).
- knowledge.yaml pattern `bounded-lbfgs-per-region-sigmoid`.
- `wiki/techniques/boundary-snap-for-kinks.md` (companion technique for kinks).
- `mb/wiki/problem-13-edges-triangles/strategy.md`, `mb/wiki/problem-13-edges-triangles/implementation-recipes.md`.

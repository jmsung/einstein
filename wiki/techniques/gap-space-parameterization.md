---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P9]
compute_profile: [local-cpu]
cost_estimate: "negligible — reparameterization, no extra compute"
hit_rate: "TBD"
---

# Gap-Space Parameterization for Ordered Roots

## TL;DR

When variables are ordered (`z_1 < z_2 < ... < z_k`), reparameterize as gaps `g_i = z_{i+1} − z_i > 0` (with `g_0 = z_1`). Naturally enforces ordering, dramatically reduces the search-space condition number, and lets optimizers explore relative structure. P9 Uncertainty Principle: gap-space Nelder-Mead found `k=14, S=0.31817` that position-space NM completely missed.

## When to apply

- Variables are an ordered tuple of real positions: Laguerre roots, Heilbronn points along an axis, sorted weights, root-gap ordering for polynomial constraints.
- Position-space optimization wastes most evals on configurations that violate the ordering constraint.
- Hessian eigenvalues span many orders of magnitude in position space (correlated absolute positions).

## Procedure

1. **Reparameterize**:
   ```python
   # z = [z_1, z_2, ..., z_k] ordered
   g = [z[0]] + [z[i+1] - z[i] for i in range(k-1)]   # gap-space
   # inverse: z = np.cumsum(g)
   ```
2. **Optimize in gap-space**: variables `g_i` are nearly independent; Hessian is well-conditioned.
3. **Soft repair after each sample** (CMA-ES variant, lesson #67): `g_i ← max(g_i, eps)` with `eps ~ 1e-6`.
4. **Linear penalty for boundary** (NOT clamping, NOT quadratic):
   ```python
   loss += lambda_pen * sum(max(0, eps - g_i) for g_i in g)
   ```
   - Clamping zeros the gradient on the constraint.
   - Quadratic penalty dominates the true objective at the boundary.
5. **Phase-anneal sigma** for CMA-ES: phase 1 `sigma=0.05` (broad), phase 2 `sigma=0.005` (refine). Converges to within 1e-7 of the basin floor.

## Pitfalls

- **Don't clamp** `g_i = max(g_i, 0)`: gradient becomes zero on the constraint; optimizer stalls.
- **Don't use quadratic penalty**: dominates the true objective near the boundary; the wrong basin is found.
- **Linear penalty + soft repair** is the working combination (lesson #67).
- **Higher k = condition number gets worse in position space**: P9 k=13 NM converges; k=14 in position space cannot find the basin gap-space NM finds immediately.
- **Combine with k-climbing** (`k-climbing.md`): when extending dimensionality, add a new gap variable in the far cluster, not a new absolute position.
- **mpmath dps must scale with k** (lesson #65): cond(Laguerre) at k=14 is 9e37. dps=20 underflows; dps=30 minimum for k=15.

## Compute profile

Local CPU. Reparameterization is free; no compute overhead. NM / CMA-ES / L-BFGS all benefit equally. P9 gap-space NM at k=14: minutes to converge.

## References

- `wiki/findings/optimizer-recipes.md` (#26 — gap-space reparameterization improves NM convergence; #67 — CMA-ES gap-space recipe).
- knowledge.yaml pattern `gap-space-reparameterization`.
- `wiki/techniques/k-climbing.md` (companion: increase dimensionality + new gap).
- `mb/wiki/problem-9-uncertainty-principle/strategy.md`.

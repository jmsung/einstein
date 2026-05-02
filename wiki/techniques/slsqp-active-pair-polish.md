---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P5, P11, P14, P17b, P18]
compute_profile: [local-cpu]
cost_estimate: "seconds to minutes"
hit_rate: "TBD"
---

# SLSQP Active-Pair Polish (Wide-Tolerance)

## TL;DR

SLSQP polish on contact-graph-locked geometric problems — sphere packing, Tammes, circles-in-rectangle — converges to the basin's float64 floor in 3–5 iterations, but only if the active-pair tolerance is **wide** (`tol_active = 1e-3`), not tight. Narrow tolerances miss 95+ near-active pairs and stall well below the ceiling.

## When to apply

- Constrained maximin geometric problems (kissing, Tammes, packing, min-distance-ratio).
- A warm-start whose contact graph is already approximately correct.
- Many simultaneous near-active inequality constraints (15+ active triples / pairs).
- Goal: descend to the basin's float64 floor for triple-verify or a rank-#2 grab.

## Procedure

1. **Identify near-active constraints** with a wide tolerance:
   ```python
   active = [(i, j) for i, j in pairs if abs(dist(i, j) - target) < 1e-3]
   ```
   `1e-3`, not `1e-7` — this is the load-bearing parameter.
2. **Set up the SLSQP epigraph** with explicit affine gauge to break invariances:
   - Translation: fix `p_0` at origin.
   - Rotation: fix `p_1` on `+x` axis (2D) or first 3 coords (3D).
   - Scale: appropriate fixing depending on objective.
3. **Run SLSQP** with `ftol=1e-20`, `maxiter=200`. Aggressive ftol because we're below smooth-surrogate noise.
4. **Triple-verify**: arena evaluator + `scipy.spatial.distance.pdist` + mpmath at dps=50 Newton-KKT. If two of three agree, the float64 floor is real.

```python
# P11 Tammes n=50 sketch
from scipy.optimize import minimize
def obj(x): return -min_pairwise_distance_squared(x)  # epigraph variable t
res = minimize(obj, x0, method='SLSQP',
               constraints=active_pair_constraints,
               options={'ftol': 1e-20, 'maxiter': 200})
```

## Pitfalls

- **Narrow active-pair tolerance (1e-7)** misses 95+ near-active pairs; SLSQP terminates at a pseudo-optimum tens of ulps above the basin's true floor. The default scipy tolerance is wrong here.
- **Missing the affine gauge**: invariance dimensions (translation, rotation, scale) cause ill-conditioning; SLSQP wanders or stalls. Always fix the gauge explicitly.
- **Cold start is hopeless**: the contact graph must be approximately correct already. From a random init, SLSQP converges to a different (worse) basin.
- **Smooth surrogates fail at the floor**: softplus(β·hinge)/β has a kernel noise floor ~1e-12 while the residual loss is ~1e-13 (P6). Discrete ulp coordinate descent (`mpmath-ulp-polish.md`) is the workhorse below SLSQP's reach.
- **Symmetric stagnation**: SLSQP can converge with some constraints at slightly non-binding values. Pair with `iterated_slsqp_perturb` (tiny tangent kicks σ≈1e-13 between polishes) to displace into a better float64 minimum.

## Compute profile

Local CPU. Sequential SLSQP — GPU sits idle. Negligible cost: Tammes n=50 polish < 1s, P14 n=26 packing polish < 5s, P17b n=21 circle packing polish < 1s.

## References

- `wiki/findings/optimizer-recipes.md` (SLSQP smooth-NLP min-max-ratio: P5 reproduction recipe).
- `wiki/findings/packing-techniques.md` (lesson #56 P14 generalization; lesson #92 arena-tolerance variant).
- `wiki/findings/float64-polish.md` (lesson #74 float64 screen + mpmath verify).
- knowledge.yaml strategies: `slsqp_active_pair_polish`, `slsqp_smooth_nlp_minmax_ratio`, `slsqp_epigraph_polish`, `iterated_slsqp_perturb`.
- `mb/wiki/problem-11-tammes-n50/strategy.md`.

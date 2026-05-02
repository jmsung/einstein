---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P13]
compute_profile: [local-cpu]
cost_estimate: "minutes per problem"
hit_rate: "TBD"
---

# Greedy-Insert + Coordinate-Descent + Redistribute

## TL;DR

Three-stage optimizer for curve-approximation / sample-point-placement problems: (1) greedy best-insert finds a good initial layout, (2) golden-section coordinate descent refines each point's position, (3) block redistribution re-spaces windows of adjacent points to break collective spacing failures. Each stage addresses a different failure mode; they don't substitute. Champion on P13 Edges-vs-Triangles: uniform −0.7118 → greedy+CD −0.7117111 → +redistribute −0.71170988 (1.4e-4 total).

## When to apply

- Solution is a set of sample points defining a curve, density function, or one-dimensional distribution.
- Score depends on placement of points (not just count or type).
- Local methods at fixed point count converge but have residual structural issues (collective spacing failures, density mismatches).

## Procedure

### Stage 1 — Greedy best-insert

```python
# Start with a small seed; insert one point at a time at the best position
points = [seed_point]
for _ in range(n_target - 1):
    candidate_positions = grid_or_optimizer(domain)
    best_pos = max(candidate_positions, key=lambda x: score(points + [x]))
    points.append(best_pos)
```

Global step: O(n × candidates). Finds a good initial layout but doesn't tune exact positions.

### Stage 2 — Coordinate descent (golden-section)

```python
for sweep in range(n_sweeps):
    for i in range(n):
        points[i] = golden_section_search(lambda x: score(points_with_i_set_to(x)),
                                          bracket=[lo[i], hi[i]])
```

Local step: each point's position is refined holding others fixed. Converges to local optimum within the current arrangement.

### Stage 3 — Block redistribution

```python
# For window sizes k = 5, 10, 20, 50, 100:
for k in [5, 10, 20, 50, 100]:
    for start in range(0, n - k + 1, k):
        window = points[start:start+k]
        # Re-space evenly within the window's bracket
        points[start:start+k] = np.linspace(window[0], window[-1], k)
        # Re-polish via coord descent
```

Meso-scale step: breaks coordination failures that CD misses (groups of points stuck at the wrong spacing).

### Stages 2 + 3 alternation

Run Stage 2 to convergence; run Stage 3; repeat. Each redistribution typically produces a "big jump" after CD has converged.

## Pitfalls

- **Skipping Stage 1**: cold-start CD from random points is much slower; greedy insertion gives 50–80% of the final solution quality before stages 2–3 add the rest.
- **Skipping Stage 3**: CD converges to a local optimum where the SPACING of point clusters is wrong; redistribution breaks this. P13: removing Stage 3 caps at −0.7117111; with it, −0.71170988.
- **Wrong window sizes**: too small → no redistribution effect; too large → destroys local structure. Vary k from 5 to 100.
- **Greedy insertion is NOT optimal** in the global sense: it's a fast warm-start, not a final solution. Always follow with stages 2–3.
- **Pair with boundary-snap for kink-rich problems** (`boundary-snap-for-kinks.md`): if the envelope has discrete kinks (P13 Turán scallops), snap is a separate Stage 4 — neither greedy nor CD nor redistribution will hit boundary samples on their own.

## Compute profile

Local CPU. P13 n=500 points: minutes for the full three-stage cycle. Sequential — GPU sits idle.

## References

- `wiki/findings/optimizer-recipes.md` (#31 — hierarchical optimization for curve-approximation).
- knowledge.yaml strategy `greedy_insert_cd_redistribute`; pattern `greedy-insert-cd-redistribute`.
- `wiki/techniques/bounded-lbfgs-per-region-sigmoid.md` (companion polish for kink-aware problems).
- `wiki/techniques/boundary-snap-for-kinks.md` (companion when envelope has discrete kinks).
- `mb/tracking/problem-13-edges-triangles/strategy.md`, `mb/tracking/problem-13-edges-triangles/implementation-recipes.md`.

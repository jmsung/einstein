---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - reference/2025-jaech-autoconvolution.md
  - reference/2026-sung-jsagent-codebase.md
---

# Optimizer Recipes & Technique Catalog

## Technical Patterns

### Dinkelbach Fractional Programming

Converts ratio optimization (hard) to parametric optimization (easier). Works for any C = N(f)/D(f) problem.

- **Inner**: max_f [N(f) - lambda*D(f)] with smooth L-infinity proxy (LogSumExp)
- **Outer**: lambda <- N(f*)/D(f*)
- **Beta cascade**: low to high to anneal the proxy

The key insight is that the ratio objective is quasiconvex even when neither numerator nor denominator is convex, and the parametric form converts each inner problem into a standard optimization. The beta cascade (starting with low beta for broad search, increasing to high beta for precision) is essential — jumping to high beta immediately gets trapped in the nearest local optimum of the approximation.

### Adam with Peak-Flattening

When L-infinity is in the denominator, Adam's gradient naturally flattens peaks. This discovers sparse block structure without being told to. Use for any problem where "flatness" is rewarded. Adam's per-coordinate adaptive learning rate concentrates gradient updates on the highest-magnitude coordinates, which are exactly the peaks that the L-infinity denominator penalizes. The emergent behavior is that Adam discovers and exploits sparse block structure in the solution without any explicit structural prior.

### Cross-Resolution Basin Transfer

Optimize at high resolution, compress to target resolution, refine. The compressed structure retains "memory" of the higher-resolution basin. Novel technique from Problem 3. Structure found at high resolution is preserved through compression because the dominant features (block positions, relative magnitudes) are low-frequency and survive downsampling. The refinement step at target resolution then polishes within the transferred basin rather than searching from scratch.

### Multi-Scale Upsampling

Optimize at small n (fast, many trials), 4x interpolate, refine at each scale. Proven by Jaech & Joseph (2025). Structure found at small n is preserved by interpolation. This is the reverse direction from cross-resolution basin transfer: start small and grow. The advantage is that small-n optimization is fast enough for massive multi-start search, finding basins that are invisible at large n due to the combinatorial explosion of local optima. The 4x interpolation factor is a sweet spot — larger jumps lose too much structure, smaller jumps are too slow.

## Numbered Lessons

### #26: Gap-space reparameterization improves NM convergence

Instead of optimizing absolute root positions z_i, optimize gaps g_i = z_{i+1} - z_i. This naturally enforces ordering (all gaps > 0), reduces the condition number of the search space, and lets the optimizer explore relative structure. Problem 18: gap-space NM found k=14 solution S=0.31817 that position-space NM missed. The condition number improvement is dramatic — in position space, the Hessian eigenvalues span many orders of magnitude because absolute positions are correlated; in gap space, the variables are nearly independent.

### #31: Hierarchical optimization for curve-approximation

When the solution is a set of sample points defining a curve, use three stages:

1. **Greedy insertion**: place each new point where it maximally improves the objective.
2. **Coordinate descent**: fine-tune each point's position via golden-section search.
3. **Block redistribution**: re-space windows of adjacent points for even coverage.

Problem 13: uniform sampling gave -0.7118, greedy+CD gave -0.7117111, adding redistribution gave -0.71170988 (total improvement 1.4e-4). Each stage has diminishing returns, but redistribution provided a "big jump" after CD had converged. The stages are ordered by scope: greedy insertion is global (where to place), CD is local (exact position), redistribution is meso-scale (relative spacing of neighborhoods).

### #32: Saturated penalty terms can be ignored

When a penalty term in the objective is always at its maximum regardless of the solution (e.g., gap penalty = 10 * max_gap where max_gap >= 0.05 for all feasible solutions), identify this early and focus optimization entirely on the remaining terms. Problem 13: gap penalty is always 0.5, so the problem reduces to pure area minimization. Identifying saturated penalties early prevents wasted optimization effort on terms that cannot improve.

### #67: CMA-ES with smooth penalty + gap repair for ordered-roots

For any problem where the search variables are an ordered tuple of real positions (Laguerre roots, Heilbronn points along an axis, sorted weights), naive CMA-ES in position space wastes most of its evaluations on "rejected" configurations that violate ordering. The working recipe:

1. Reparameterize as gaps `g_i = z_{i+1} - z_i > 0` (gap-space).
2. Apply a soft repair `g_i <- max(g_i, eps)` after each CMA sample with eps ~ 1e-6.
3. Add a linear penalty `lambda * sum(max(0, eps - g_i))` to the loss so the optimizer is gently pushed away from the boundary instead of clamped.

With sigma=0.05, popsize=14, ~4000 fevals per start, this found the k=15 basin where pure position-space NM and unrepaired CMA both failed. Phase 1 (sigma=0.05) -> Phase 2 (sigma=0.005) annealing schedule converges to within 1e-7 of the basin floor. Do NOT clamp hard (gradient becomes zero on the constraint), do NOT use a quadratic penalty (dominates the true objective at the boundary).

### #68: Bounded L-BFGS via per-region sigmoid

Problem 13 Edges vs Triangles: the Turan envelope is a union of K scallops, each `[1 - 1/k, 1 - 1/(k+1)]` for k=2..19, and the slope-N interpolation requires every sample point to stay inside its assigned scallop. Vanilla scipy L-BFGS-B either crosses scallop boundaries or stalls against the ordering bound.

The working recipe is **per-scallop sigmoid bounding**: parameterize each `x_i = scallop_lo[i] + (scallop_hi[i] - scallop_lo[i]) * sigmoid(raw_i)`, optimize raw_i in R via PyTorch autograd + L-BFGS, and let the sigmoid enforce the membership constraint smoothly. This unlocked +1.4e-7 improvement where every other local optimizer returned zero gain.

**Rule**: any optimizer on a problem where decision variables must stay inside per-element fixed regions should use the per-element sigmoid bounding pattern, NOT scipy L-BFGS-B with bounds. The sigmoid keeps the gradient nonzero everywhere inside the region, lets L-BFGS take long unconstrained steps in raw space, and prevents the silent constraint violation that breaks the score function.

### #69: Multi-seed basin-hopping reveals warm-start polish sub-basins

Problem 13 Edges vs Triangles: polishing the rank-1 and rank-2 leaderboard solutions both reach `-0.71170951` — looked like a single attractor. Running 10 independent BH seeds from that polished score found a strictly better basin at `-0.71170936` on seed 11 only — none of the other 9 seeds reached it.

**Rule**: when warm-start polish from multiple competitor solutions yields the same final score, the polished score is the entry to a family of nearby sub-basins, not a single attractor. Run 10+ independent BH seeds from the polished best before declaring the basin saturated. Single-seed BH hides 1-2 orders of magnitude of sub-basin structure. The hit rate (1/10 in our case) means single-seed runs miss the deeper basin ~90% of the time.

### #93: Square parameterization (f=v^2) escapes peak-locking where exp(v) fails

Problem 2 First Autocorrelation (2026-04-15): the exp(v) parameterization was universally peak-locked at delta~5.25e-8 from SOTA across ALL resolutions (30k-300k) and ALL optimizers (L-BFGS, Adam, SGD, CMA-ES). Switching to f=v^2 at n=90000 broke through to delta=1.23e-6 (12.3x minImprovement), reaching #1. Three mechanisms: (1) exact zeros when v_i=0 lets the optimizer change support structure freely, (2) vanishing gradient df/dv=2v near zero encourages sparsity (exp has non-vanishing gradient there, resisting it), (3) different Hessian curvature sends L-BFGS to different stationary points. The critical companion technique is **ultra-aggressive low-beta exploration**: beta=1e6 with max_iter=3000, history_size=300 (~6 min of broad landscape traversal) before tightening to beta=1e14. Most practitioners tighten beta too quickly, committing to the nearest basin. n=90000 (3x block-repeat) is a sweet spot; larger n converges to shallower minima.

**Rule**: when exp(v) parameterization stagnates on ratio-of-autoconvolution objectives, try f=v^2 before declaring the basin locked. The parameterization is the first lever to pull — it defines the optimization landscape more than the optimizer choice.

### #71: Boundary-snap for slope-N interpolation kinks

Problem 13 Edges vs Triangles: the Turan envelope has a kink at every scallop boundary `x = 1 - 1/k` (k = 3..19). Slope-3 linear interpolation between adjacent sample points overshoots the true envelope at every kink not exactly hit by a sample. Snapping the nearest sample point EXACTLY to each kink (and re-polishing the rest with bounded L-BFGS, lesson #68) reduces the cumulative interpolation overshoot by `+1.24e-8`. Iterating snap -> bounded-L-BFGS -> BH -> snap converges in 2-3 rounds.

**Rule**: for any problem where the score is a slope-N interpolation of an envelope with first-order discontinuities (kinks at known points), the interpolation error is dominated by the kinks not coincident with sample points. Always include a boundary-snap pass: for each known kink x_kink, find the nearest sample point and snap it exactly to x_kink, then re-polish neighboring points. This is a one-shot improvement that competitors using purely smooth optimizers will miss — the gradient at x_kink is discontinuous, so gradient-based methods avoid the boundary, while the actual optimum requires a sample on the boundary.

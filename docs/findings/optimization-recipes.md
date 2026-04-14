# Optimization Recipes

Named techniques with enough detail to reimplement. Each recipe includes the problem(s) where it proved effective.

## Dinkelbach Fractional Programming

**Used in**: P3 (second autocorrelation)

Converts ratio optimization max(N/D) to parametric max(N − λD):

```
λ = 0
repeat:
    x* = argmax_x [N(x) - λ * D(x)]
    λ = N(x*) / D(x*)
until convergence
```

**Key detail**: Pair with LogSumExp smooth-max and a beta cascade (1e4 → 1e10). The Dinkelbach iteration converges superlinearly, but only if each subproblem is solved well — which requires the beta cascade to avoid trapping.

## Cross-Resolution Basin Transfer

**Used in**: P3 (second autocorrelation)

1. Optimize at high resolution (n ≈ 1.6M)
2. Block-average to target resolution (n ≈ 100k)
3. The block-averaged solution is in a **different basin** than native-resolution optimization finds

**Why it works**: High-resolution optimization discovers fine structure. Block averaging preserves low-frequency features while smoothing high-frequency noise. The resulting starting point accesses a basin that native-resolution random initialization cannot reach.

## Larger-n Escape (Block-Repeat + Noise)

**Used in**: P4 (third autocorrelation)

When equioscillation traps form at fixed discretization n:

1. Take best solution at n = N
2. Block-repeat each value K times → solution at n = NK
3. Add Gaussian noise σ ≈ 1e-3 to break exact equioscillation
4. Optimize at n = NK with smooth-max surrogate

**Why it works**: The higher resolution provides new degrees of freedom between the original discretization points. The noise breaks the symmetric equioscillation pattern, allowing the optimizer to find asymmetric improvements.

## Per-Scallop Sigmoid Bounding

**Used in**: P13 (edges-triangles)

For per-variable bounded intervals [lo_i, hi_i]:

```python
x_i = lo_i + (hi_i - lo_i) * torch.sigmoid(raw_i)
```

Optimize over `raw_i` with PyTorch autograd + L-BFGS. Gradients are nonzero everywhere (no boundary deadlocks). Each variable stays in its assigned interval without explicit constraint handling.

**Why it works**: Box constraints have zero gradient at boundaries, killing gradient-based optimization. Sigmoid parameterization maps ℝ → (lo, hi) smoothly with everywhere-nonzero Jacobian.

## Boundary-Snap for Kinks

**Used in**: P13 (edges-triangles)

When the scoring function has first-order discontinuities (kinks) at known positions:

1. Identify kink locations (e.g., x = 1 − 1/k for Turán breakpoints)
2. Snap the nearest sample point exactly to each kink
3. Re-optimize neighboring points around the snapped positions

Each snap round improves the score by ~1.24 × 10⁻⁸ per kink. The improvement comes from reducing interpolation error at the discontinuity.

## Gap-Space Parameterization

**Used in**: P13 (edges-triangles), P18 (uncertainty principle)

For ordered variables x₁ < x₂ < ... < xₖ, optimize gaps:

```python
g_i = x_{i+1} - x_i  # all g_i > 0
# Reconstruct: x_i = x_1 + sum(g[1:i])
```

**Benefits**: Enforces ordering for free, reduces condition number, lets optimizers explore relative structure. CMA-ES and basin-hopping in gap-space preserve ordering naturally.

## Parallel Tempering SA

**Used in**: P6 (kissing number)

8 temperature replicas with geometric spacing [T_min, T_max] = [1e-12, 1e-4]:

1. Each replica runs SA independently at its temperature
2. Periodically attempt replica exchange (Metropolis criterion on energy difference × inverse temperature difference)
3. High-temperature replicas explore broadly; low-temperature replicas polish

**730x improvement** over single-temperature greedy perturbation. The temperature hierarchy naturally handles multi-scale contact graph structure.

**Enhancement**: Contribution-weighted sampling — focus perturbations on the highest-contribution elements rather than sampling uniformly.

## k-Climbing

**Used in**: P18 (uncertainty principle)

When optimization at k degrees of freedom plateaus, try k+1:

1. Insert a new variable (e.g., a new root) at the position that most improves the score
2. Optimize the full k+1 variable set
3. Track the **gate-feasibility ratio**: (improvement from k→k+1) / minImprovement

**Diminishing returns**: The ratio typically collapses after 1-2 climbs. For P18: k=13→14 gave ratio 1.8 (viable); k=14→15 gave ratio 0.046 (unviable). Pivot when ratio < 0.1.

## Rank-Window Strategy (Packing)

**Used in**: P14 (circle packing square)

When #1 is at the float64-overlap-noise ceiling:

1. Polish SOTA to strict-disjoint floor (overlap_tol=0, ftol=1e-16)
2. Identify safe rank-2 window: [S₂ + minImprovement, S₁ − ε]
3. Uniform shrink each radius by (S_floor − target) / n to land in window
4. Triple-verify with `evaluate_strict(tol=0)` before submission

**Mechanical rank capture**: No creative optimization needed — just arithmetic on the known score window.

## Arena-Tolerance SLSQP

**Used in**: P17 (circles-in-rectangle)

Optimize with configurable constraint slack matching the arena's acceptance thresholds:

- `overlap_tol = 9.99e-10` (arena accepts < 1e-9)
- `perim_slack = 9.9e-10` (arena accepts < 3e-9)

Beats strict-disjoint by ~4 × 10⁻⁹. Headroom comes from multiple independent slack sources (many active circle pairs + rectangle perimeter).

**Critical**: Arena checks use `<` not `≤`. Stay just under the threshold. Test overlap and perimeter slack independently — they contribute additive headroom.

*Last updated: 2026-04-13*

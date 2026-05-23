---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: [parameterization-selection.md, basin-rigidity.md, piecewise-linear-with-kinks.md]
related_problems: [P9, P17a, P18, P15, P16]
compute_profile: [local-cpu]
cost_estimate: seconds to minutes
hit_rate: 7/13 (champion on P9; reliable on small-DOF non-smooth)
related_findings: [optimizer-recipes.md, k-climbing.md, equioscillation-escape.md]
related_personas: [polya.md, hilbert.md]
cites:
  - ../concepts/parameterization-selection.md
  - ../concepts/basin-rigidity.md
---

# Nelder–Mead simplex method

## TL;DR

Nelder–Mead is the **gradient-free simplex-evolution optimizer** for smooth-or-non-smooth low-dimensional problems. It maintains `n+1` test points (a simplex in `ℝⁿ`), iteratively reflects/expands/contracts toward better values. **Champion technique on P9 Uncertainty Principle** (7 wins out of arena cycles, average rank 1.5) because the gap-space parameterization makes the landscape nearly flat near the optimum, where smooth-gradient methods stall but the simplex finds tiny improvements. Use when (a) gradient is undefined, expensive, or unreliable; (b) DOF ≤ 50; (c) the problem is in a *parameterized* space (gap-space, root-space) where polynomial smoothness arguments fail.

## When to apply

- **Non-smooth or kink-prone landscapes**: Nelder–Mead doesn't need a gradient. Robust at P9-style polynomial root configurations and P17a hexagon symmetry-bounded optimizations.
- **Small to medium DOF**: empirically reliable up to ~50 dimensions; degrades sharply above 100. For high-DOF problems (P19's 360-mark configuration), NM is too slow per iteration.
- **Parameterized search spaces**: when the optimization variable is a parameterization (gap-space, root-space, sigmoid-space) rather than direct coordinates, NM avoids the "gradient is wrong sign" trap that smooth methods hit.
- **Polish phase after CMA-ES / basin-hopping**: NM is a reliable final polish for population-search outputs.

Specific arena fits:

- **P9 Uncertainty Principle (k=14)**: gap-space NM is the *breakthrough technique*; CMA-ES + NM polish drove `k=14` from `S=0.31817` to ulp-level. 7 wins, average rank 1.5.
- **P17a Hexagon Packing (n=12)**: outer-parameters Nelder-Mead + DE for inner is the canonical pipeline.
- **P18 Circles in Rectangle**: NM polish after SLSQP for the 21-circle configuration.
- **P15/P16 Heilbronn**: NM tries the simplex around a candidate; useful as a low-cost first probe before committing to SLSQP.

Don't use for:

- Large-DOF problems (NM scales poorly above ~50 vars).
- Problems with cheap analytical gradient (use L-BFGS instead).
- Highly multimodal problems without good warm-start (NM is local).

## Procedure

```
init  simplex S = {x_0, ..., x_n} ⊂ ℝⁿ        (n+1 points)
for iter = 1, 2, ...:
    sort:        f(x_0) ≤ f(x_1) ≤ ... ≤ f(x_n)
    centroid:    c = (x_0 + ... + x_{n-1}) / n             # excludes worst
    reflect:     x_r = c + α·(c − x_n)                     # α = 1
    if f(x_0) ≤ f(x_r) < f(x_{n-1}):
        x_n ← x_r;  continue
    if f(x_r) < f(x_0):                                    # better than best — expand
        x_e = c + γ·(x_r − c)                              # γ = 2
        x_n ← min(x_e, x_r) by f
        continue
    # Worse than second-worst — contract
    if f(x_r) < f(x_n):
        x_c = c + ρ·(x_r − c)                              # ρ = 0.5 (outer)
    else:
        x_c = c + ρ·(x_n − c)                              # ρ = 0.5 (inner)
    if f(x_c) < f(x_n):
        x_n ← x_c;  continue
    # Shrink
    x_i ← x_0 + σ·(x_i − x_0)  for i = 1..n                # σ = 0.5
```

Standard parameters `(α, γ, ρ, σ) = (1, 2, 0.5, 0.5)` are robust across problem types. Modern implementations (`scipy.optimize.minimize` with `method='Nelder-Mead'`) handle this with minor adaptations.

Convergence diagnostics:

- **`xatol`** (default 1e-4): stop when simplex spread across all dimensions falls below this.
- **`fatol`** (default 1e-4): stop when objective spread across simplex falls below this.
- For high-precision polish, set both to `1e-12` or lower.

## Pitfalls

- **Slow convergence**: on smooth problems with gradient available, L-BFGS / SLSQP is faster. Use NM only when gradient is unavailable / unreliable.
- **Curse of dimensionality**: above ~50 vars, NM gets stuck in degenerate-simplex states. For high-DOF, prefer CMA-ES (which adapts the covariance matrix).
- **Inner contraction trap**: at flat plateaus, NM's contraction step shrinks the simplex without finding improvement; eventually triggers a "shrink" which can lose progress. Combat with random restarts.
- **Initial simplex orientation matters**: a degenerate initial simplex (e.g., all points colinear) can cause the algorithm to silently fail. Use the "implicit pivoting" simplex from scipy for safety.
- **Local minimum only**: NM finds a local optimum near the initial simplex. For multimodal problems, combine with basin-hopping or multistart.

## Compute profile

**Local CPU only**. NM is inherently sequential (each iteration depends on the previous); GPU parallelism doesn't help for vanilla NM. M5 Max single-core handles up to ~10⁵ iterations/second for the P9 polynomial-root setup. Cost: seconds to minutes for typical convergence.

If you need GPU-style parallelism, use **CMA-ES** instead — it maintains a population of `4 + ⌊3 ln n⌋` trial points per generation, naturally parallel.

## Variants worth knowing

- **Subplex (Tom Rowan 1990)**: for higher-DOF problems, decompose into low-DOF subproblems and apply NM to each. Better than vanilla NM at d > 30.
- **Nelder–Mead with restart**: after convergence, perturb the best point and re-initialize the simplex; helps escape local optima.
- **Constrained NM**: for box-bounded problems, project onto the feasible region after each step. Less robust than SLSQP for tight constraints.

## References

- Nelder, J.A. and Mead, R. (1965). "A simplex method for function minimization." *The Computer Journal* 7(4), 308–313.
- Lagarias, J.C., Reeds, J.A., Wright, M.H., Wright, P.E. (1998). "Convergence properties of the Nelder–Mead simplex method in low dimensions." *SIAM J. Optimization* 9(1), 112–147 — convergence proofs for d ≤ 2; failure for d ≥ 5 (McKinnon counterexample).
- Used in: P9 cycles for gap-space + k-climbing breakthrough; documented in `findings/k-climbing.md` and `findings/optimizer-recipes.md`.

*Last updated: 2026-05-02*

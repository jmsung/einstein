# JSAgent Methodology Guide

A cross-problem reference for the optimization techniques, strategies, and lessons learned across all 18 Einstein Arena problems.

## Philosophy

Three principles guide JSAgent's approach:

1. **Literature first**: Reading papers saves weeks. Search arXiv before writing optimizers.
2. **Breadth before depth**: Test 5+ approaches quickly (1 hour each) before committing to GPU-scale compute. Time-box ruthlessly.
3. **Warm-start from SOTA**: The SOTA basin is usually unreachable from scratch. Always download top solutions from `/api/solutions/best` before any optimization.

## Optimizer Taxonomy

### Continuous Optimization

| Technique | Best For | Key Insight |
|-----------|----------|-------------|
| **SLSQP** | Constrained packing, epigraph problems | Tolerance cascade (loose → tight) avoids boundary deadlocks |
| **L-BFGS** | Smooth surrogates, high-dimensional | Pair with LogSumExp smooth-max (beta cascade essential) |
| **Adam** | Ratio objectives, sparse structure | Per-coordinate LR discovers structure automatically |
| **CMA-ES** | Low-dimensional (~10-50 vars), noisy | Gap-space parameterization for ordered variables |
| **Nelder-Mead** | Low-dimensional, non-differentiable | Good for k-climbing in gap-space |

### Discrete Optimization

| Technique | Best For | Key Insight |
|-----------|----------|-------------|
| **Memetic Tabu Search** | Binary sequences (±1) | Short-term memory prevents cycling |
| **SA Parallel Tempering** | Sphere packing, contact graphs | 8 replicas, geometric temps — 730x over greedy |
| **Branch-and-Bound** | Exact combinatorial (small blocks) | Document the invariant your branching enforces |
| **ULP-Step Descent** | Float64 precision floor | ±1/2/4 ulp coordinate sweeps when smooth methods stall |

### Fractional Programming

| Technique | Best For | Key Insight |
|-----------|----------|-------------|
| **Dinkelbach** | Ratio objectives N/D | Convert to parametric N − λD, iterate on λ |
| **Beta Cascade** | LogSumExp smooth-max | Low → high β avoids trapping (1e4 → 1e10) |

## General Techniques (Transfer Across Problems)

### Warm-Start Pipeline

Every problem should start with:
1. Download top-K solutions via `/api/solutions/best?problem_id=N&withData=true&limit=K`
2. Verify each solution reproduces its published score with your evaluator
3. Use the best as the optimization seed

The SOTA basin is almost always unreachable from random initialization.

### Two-Tier Verification

Every candidate score must pass two independent evaluations:

- **Fast evaluator** (FFT, numpy, milliseconds): Drives the inner optimization loop
- **Exact evaluator** (sympy, np.convolve, mpmath): Quality gate before trusting a score

**Never collapse the tiers**. Exact-only cripples search speed. Fast-only lets false positives through. The fast evaluator produces false positives most often at:
- Far-field sign changes (P18 uncertainty principle)
- Float64 → mpmath discrepancies (P6 kissing number)
- Boundary cases in piecewise functions (P13 edges-triangles)

### Entry Gate Analysis

Before investing compute in any problem, run this 3-check test:

1. **Tie-multiplicity**: Count agents at the top score. If ≥ N medal slots, matching SOTA yields 0 points.
2. **Paper-copy detection**: Hash SOTA against published constructions (AlphaEvolve, DeepMind notebooks). If bit-identical, local polish has zero headroom.
3. **mpmath-ceiling check**: High-precision Newton polish on the reduced KKT system. If true-math gap < minImprovement, the basin is mathematically unbeatable.

### Float64 Precision Floor

When all smooth optimizers plateau, the remaining headroom is in the float64 representation:

- **ULP-step descent**: ±1/2/4 ulp single-coordinate sweeps
- **Float-precision lottery**: Random isometries + re-evaluation sample nearby float64 representations
- **Byte-identical consensus**: If 8+ agents submit byte-identical solutions, you're at the float64 ceiling of a known construction

### Basin Rigidity Diagnostic

Count: active_constraints − (coordinates − gauge_freedoms)

- **Positive** → basin is fully rigid, no local improvement possible
- **Zero** → basin is marginal, may have infinitesimal slack
- **Negative** → degrees of freedom remain, optimization may still help

### Equioscillation Escape

For discretized-function problems where equioscillation traps form:

1. **Block-repeat**: Repeat each value 4x to create a higher-resolution solution
2. **Add noise**: Small Gaussian noise breaks the exact equioscillation pattern
3. **Optimize at higher resolution**: New degrees of freedom escape the lock

This is a general technique for any problem where the solution quality is limited by discretization rather than the basin.

### Cross-Resolution Basin Transfer

Different discretization resolutions access different basins. Optimize at high resolution, compress to target via block averaging. The compressed solution is in a different basin than native-resolution optimization finds.

### Gap-Space Parameterization

For ordered variables (roots, breakpoints, positions): optimize gaps g_i = x_{i+1} − x_i instead of absolute positions x_i.

Benefits:
- Enforces ordering without constraints
- Reduces condition number
- Lets optimizers explore relative structure

### Per-Variable Sigmoid Bounding

For variables constrained to intervals [lo_i, hi_i]:

    x_i = lo_i + (hi_i − lo_i) × sigmoid(raw_i)

Benefits over box constraints:
- Nonzero gradients everywhere (no boundary deadlocks)
- Prevents silent constraint violation
- Compatible with PyTorch autograd + L-BFGS

## When to Stop

Knowing when a problem is frozen saves more time than any optimization technique:

- **12+ approaches yield zero improvement** → single-basin landscape, move on
- **Over-constrained Hessian** (active > DOF) → mathematically rigid
- **mpmath ceiling < minImprovement** → provably unbeatable
- **8+ agents byte-identical** → float64 ceiling reached
- **Gate-feasibility ratio < 0.1** → diminishing returns on k-climbing

## Cross-Problem Transfer Lessons

Lessons that applied to 3+ problems:

1. **Warm-start is universal**: Applied to all 18 problems. SOTA basins are unreachable from scratch.
2. **Beta cascade for smooth-max**: Applied to P3, P4, and any LogSumExp surrogate.
3. **Tolerance cascade for SLSQP**: Applied to P5, P14, P17 (circles), P16.
4. **Basin rigidity diagnostic**: Applied to P5, P10, P11, P15, P16.
5. **Two-tier verification**: Applied to P3, P4, P6, P18 — essential wherever the landscape is deceptive.
6. **Domain mismatch detection**: P7 (PNT) was LP, not number theory. Always check arena discussions.
7. **Resolution as hyperparameter**: P2, P3, P4 — different n values access different basins.

*Last updated: 2026-04-13*

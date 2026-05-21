---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P3, P4]
related_techniques: [larger-n-cascade.md, cross-resolution-basin-transfer.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md]
cites:
  - ../findings/equioscillation-escape.md
  - ../source/papers/2025-jaech-autoconvolution.md
  - ../personas/tao.md
related_personas: [tao.md]
---

# Discretization as Structure (`n` is a Hyperparameter)

## TL;DR

For continuous functional inequalities discretized at `n` samples, the optimum **at fixed `n`** is structurally different from the continuous optimum and from optima at other `n`. Resolution is *not* monotonic: `n = 100k` and `n = 200k` give different basins (P3); `n = 30k` and `n = 90k` give different parameterization regimes (P2). Always test multiple `n` before accepting any solution.

## What it is

For a continuous problem `inf_{f ∈ F} C(f)` with `f` defined on an interval, the discretization at `n` samples replaces `F` with `F_n = {f : f sampled at n points, piecewise-constant or interpolated}`. Define `C_n(f) = C(f)|_{F_n}` and the discrete optimum `s_n = inf C_n`.

Three failure modes of "more `n` is always better":

1. **Discretization optimum != continuous optimum**. `s_n → s_∞` as `n → ∞`, but the convergence rate depends on the function class. For piecewise-constant `f` on `[−1/4, 1/4]`, `s_n − s_∞ = O(1/n)` typically, but the *shape* of the optimizer changes with `n` — equioscillation patterns at `n = 400` differ from those at `n = 1600` (P4 lesson #51).
2. **Different `n` give different basins**. For non-convex `C`, different `n` discretize the function space differently and produce structurally distinct local optima. P3 lesson: `n = 100k` and `n = 200k` autocorrelation problems converge to different solutions, neither dominating the other.
3. **Resolution non-monotonicity**. Increasing `n` does not monotonically improve score. P2: best is at `n = 90 000` (3× block-repeat from a base 30k); larger `n` (100k, 300k) converge to *shallower* minima. P3: `n = 1.6M` is worse than transferring its structure to `n = 100k`.

Wisdom hook (P3): high-resolution solutions downsampled to target resolution create structurally novel basins — resolution is not monotonic in optimization.

## When it applies

- Continuous functional inequalities discretized for numerical solution (autocorrelation P2, P3, P4; Erdős overlap P1).
- LP / IPM problems where the variable count `N` is itself the discretization parameter (P7 sieve LP — though P7 has monotone behavior, see [n-extension-monotonicity](n-extension-monotonicity.md)).
- Spectral methods where the basis truncation `K` plays the role of `n`.

## Why it works

Three structural reasons:

1. **Non-convex landscape**: at fixed `n`, the discrete problem `C_n` has many local minima. The mapping "warm-start at `n`, refine to `n'`" lands in a basin determined by the *path* of refinement, not just the endpoint resolution.
2. **Equioscillation traps are `n`-specific**. At `n` samples, the optimum has `≈ n` active constraints (the equioscillation pattern). At `2n` samples, the same configuration has `n` active and `n` slack — opening descent directions invisible at fixed `n`. See [equioscillation](equioscillation.md), [findings/equioscillation-escape.md](../findings/equioscillation-escape.md) lesson #51.
3. **Block-repeat upsample preserves score exactly** (piecewise-constant function): a configuration at `n` mapped to `4n` by block-repeat has the same `C_n`. So the upsample alone does nothing — but adding tiny noise (`σ = 1e-6`) breaks the piecewise-constant constraint and lets gradient descent find new structure at the finer resolution. This is the **larger-n escape recipe**.

The cross-resolution variant (P3): optimize at *higher* `n` than the target, then average-pool down. The compression preserves dominant low-frequency features (block positions, relative magnitudes) but the polished structure transfers as a warm start at lower `n`. This is the inverse of larger-`n` escape — sometimes the *deeper* basin lives at a lower `n`.

## Classic examples

1. **P4 Third Autocorrelation** — `n = 400` Chebyshev equioscillation basin (`400/799` active conv positions) was the floor for 9 top agents (3 byte-identical). Block-repeat to `n = 1600` + 1e-6 noise + L-BFGS smooth-max β-cascade dropped score by `4.7e-4` immediately. Cascading through `n ∈ {3 200, 6 400, 12 800, 25 600, 51 200, 100 000}` totaled `1.52e-3` (15× `minImprovement`). See [findings/equioscillation-escape.md](../findings/equioscillation-escape.md) lesson #51.
2. **P2 First Autocorrelation** — `n = 90 000` (3× block-repeat sweet spot) outperforms larger `n`. Combined with `f = v²` parameterization, achieves rank #1 at delta `1.23e-6`. Larger `n` converges to shallower minima.
3. **P3 Second Autocorrelation** — cross-resolution basin transfer: optimize at `n = 1.6M`, average-pool to `n = 100k`, polish. The compressed structure retains "memory" of the higher-resolution basin and lands in a structurally novel basin at `n = 100k` — better than from-scratch at `n = 100k`.

## Related

- Concepts: [equioscillation](equioscillation.md), [parameterization-selection](parameterization-selection.md), [autocorrelation-inequality](autocorrelation-inequality.md), [n-extension-monotonicity](n-extension-monotonicity.md).
- Techniques: [larger-n-cascade](../techniques/larger-n-cascade.md), [cross-resolution-basin-transfer](../techniques/cross-resolution-basin-transfer.md).
- Findings: [equioscillation-escape](../findings/equioscillation-escape.md), [optimizer-recipes](../findings/optimizer-recipes.md).
- Sources: `source/papers/2025-jaech-autoconvolution.md` (multi-scale upsampling).

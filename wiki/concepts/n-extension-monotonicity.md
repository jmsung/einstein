---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P7]
related_techniques: [larger-n-cascade.md, lp-cutting-plane-warmstart.md]
related_findings: [prime-number-theorem-lp.md, lp-solver-scaling.md]
cites:
  - ../findings/prime-number-theorem-lp.md
  - ../personas/euler.md
related_personas: [euler.md]
---

# N-Extension Monotonicity

## TL;DR

For LP / autocorrelation / sieve problems where the variable set is indexed by `N`, extending the set to `N' > N` can only weakly improve the optimum. The old solution is feasible for the larger problem (set new variables to zero); warm-start cutting plane from the old optimum reaches the new optimum quickly. Distinguish from [discretization-as-structure](discretization-as-structure.md): there `N` changes the *function space*; here `N` changes the *variable count* in a fixed family.

## What it is

Setup: a parametric family of optimization problems `P_N` with feasible set `F_N` and objective `C_N`, satisfying:

- **Variable set extension**: `F_N ⊆ F_{N+1}` (the smaller problem's feasible points embed in the larger). Typically: extra variables in `F_{N+1}` can be set to zero to recover a point in `F_N`.
- **Compatible objective**: `C_{N+1}|_{F_N} = C_N` (the objective's restriction to the smaller feasible set agrees).

Then `s_N = max_{F_N} C_N ≤ s_{N+1}` (or `≥` for minimization). Monotonicity is automatic.

The key arena instance is **Tao's sieve LP for P7**: variables `f(k)` for squarefree `k ∈ [2, N]`. Extending `N → N + 1` adds new variables; setting them to zero recovers any feasible point of the smaller LP. The objective `Σ −f(k) log(k)/k` is compatible. So the LP is monotone in `N`; warm-starting cutting-plane LP at `N + 1` from the `N`-optimum is correct.

For **P2 First Autocorrelation**, the situation is more subtle: at fixed parameterization (e.g. `f = v²`, sample count `n`), the variable set is `n` reals. Extending `n → 2n` via block-repeat gives a feasible point but **does not strictly improve the score** (block-repeat is exact-score-preserving; see [discretization-as-structure](discretization-as-structure.md)). The improvement comes from *re-optimizing at the new resolution after a small noise perturbation*. So P2 is "monotone with re-optimization" rather than "monotone via warm-start alone."

## When it applies

- **LP / IPM problems** with variable-set extension (P7 sieve LP).
- **Sparse-support problems** where extending the support set can only help.
- **Spectral truncation** where higher-`N` is a strict superset (P9-style basis truncation also satisfies this).

Distinguishing signal: the old optimum's objective value is still attainable in the larger problem with no work. If yes, you are in the monotone regime; warm-start is the right tool. If extending requires re-optimizing from scratch (different basin), you are in the discretization-as-structure regime.

## Why it works

Two consequences:

1. **Warm-start cutting plane works** (P7, lesson #14, #57). The `N`-LP solution is a feasible point of the `N + 1`-LP. Cutting-plane iteration from this start converges within ~5 cuts to the `N + 1` optimum. Cold-start LP at `N + 1` is wasteful.
2. **Score monotonicity is a stopping criterion**. Compute `s_N` for `N ∈ {1000, 2000, 4000, 8000, ...}`. When `s_{N+1} − s_N < ε`, declare converged. P7: `s_{1000} = 0.989`, `s_{2000} = 0.993`, `s_{2938} = 0.994`, `s_{3287} = 0.99473`, `s_{3350} = 0.99485` — flattening, near continuous limit.

The trap: confusing N-extension monotonicity with discretization-as-structure. P2's `n` parameter is *not* monotone in this sense — different `n` give different basins, and the best `n` is `90 000` (3× block-repeat sweet spot), not the largest. The distinction:

- **N-extension monotone**: the `N+1` LP includes the `N` LP as a sub-problem; old solution feasible.
- **Discretization-structural**: different `n` discretize the function space differently; old solution at `n` may *not* be a "natural" point at `n'`, and re-optimization at `n'` may find a structurally different optimum.

## Classic examples

1. **P7 Prime Number Theorem** — `s_N` monotone increasing in `N`. JSAgent rank #1 at `N = 3350`, score 0.994847. Beyond `N = 4000`, the LP becomes RAM-bound (constraint matrix ~99.5% dense) and IPM solver wall hits. Submitting *exactly* 2000 keys triggers evaluator timeout — use 1997. See [findings/prime-number-theorem-lp.md](../findings/prime-number-theorem-lp.md).
2. **General LP variable-extension** — IPM warm-start is well-supported in modern LP solvers (HiGHS); extending with cuts is `O(few iterations)` rather than `O(full re-solve)`.
3. **Counter-example: P2 First Autocorrelation** — `n` is *not* this kind of parameter. The `n = 90k` sweet spot is below `n = 300k`; resolution non-monotonic. This is [discretization-as-structure](discretization-as-structure.md), not N-extension monotonicity. Do not conflate.

## Related

- Concepts: [discretization-as-structure](discretization-as-structure.md) (the contrasting case), [sieve-theory-as-lp](sieve-theory-as-lp.md), [lp-duality](lp-duality.md), [warm-start-dynamics](warm-start-dynamics.md).
- Techniques: [larger-n-cascade](../techniques/larger-n-cascade.md), [lp-cutting-plane-warmstart](../techniques/lp-cutting-plane-warmstart.md).
- Findings: [prime-number-theorem-lp](../findings/prime-number-theorem-lp.md), [lp-solver-scaling](../findings/lp-solver-scaling.md).
